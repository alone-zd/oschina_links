from django.db import models

# Create your models here.


class OsChina(models.Model):

    links = models.CharField(max_length=500, verbose_name='链接')
    title = models.TextField(max_length=500, verbose_name='标题', null=True)

    class Meta:
        db_table = 'urls'
        ordering = ['id']
