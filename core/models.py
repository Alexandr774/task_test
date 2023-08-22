from django.db import models

class DataSetFile(models.Model):
    name = models.CharField(max_length=255)
    data_set = models.FileField(upload_to='data_set')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'
