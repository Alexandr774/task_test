from rest_framework import serializers

from core.models import DataSetFile


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSetFile
        fields = '__all__'

class DataSetListSerializer(serializers.Serializer):
    data_set = serializers.CharField(required=True)
    class Meta:
        model = DataSetFile
        fields = ('name')
