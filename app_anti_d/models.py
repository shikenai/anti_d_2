from django.db import models


# Create your models here.

class DisasterName(models.Model):
    title = models.CharField(verbose_name='災害名', max_length=20, null=True, blank=True)
    list_mode = ((0, '訓練'), (1, '本番'), (2, 'その他'))
    mode = models.IntegerField(choices=list_mode, verbose_name='種別', blank=True, null=True)
    start_date = models.DateField(verbose_name='開始日', null=True, blank=True)
    end_date = models.DateField(verbose_name='終了日', null=True, blank=True)

    def mode_name(self):
        return str(self.list_mode[self.mode][1])

    def __str__(self):
        return '【' + str(self.list_mode[self.mode][1]) + '】' + self.title


class LocalGovernments(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
