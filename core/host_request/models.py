# Imports
from django.urls import reverse
from django.db import models


class RequestModel(models.Model):
    cmd = models.CharField('Данные', max_length=255)
    code = models.CharField('Код', max_length=255)

    request_date = models.DateTimeField('Дата запроса', auto_now=True)

    def get_absolute_url(self):
        return reverse('local_request_detail_page', args=[int(self.id)])

    def __str__(self):
        return f'{str(self.request_date)} | {str(self.code)}'

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
