import csv
import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataSetFile
from .serializers import DataSetSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = DataSetFile.objects.all()
    serializer_class = DataSetSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """ получение списка файлов и название столбцов"""
        respons: dict = {}
        for item in self.queryset:
            try:
                with open(item.data_set.path, 'r') as file:
                    spamreader = csv.reader(file, delimiter=",")
                    for i in spamreader:
                        respons[(item.data_set.path).split('/')[-1]] = i
                        break
            except Exception:
                continue
        return Response(respons)

    def destroy(self, request, *args, **kwargs):
        """ удаление записи из БД, удаление файла из памяти"""
        data = self.get_object()
        os.remove(data.data_set.path)
        return super().destroy(request, *args, **kwargs)


class DataSetView(APIView):
    def get(self, request) -> Response:
        """ получение данных из контректного файла, файл задается по вхождению символов в название файла, параметр называется /?name= """
        req = self.request.query_params.get('name')
        data = DataSetFile.objects.all()
        if req:
            item = data.filter(data_set__icontains=req)
            for i in item:
                respons: list = []
                with open(i.data_set.path, 'r') as file:
                    spamreader = csv.reader(file, delimiter=",")
                    for q in spamreader:
                        respons.append(q)
                return Response(respons)
