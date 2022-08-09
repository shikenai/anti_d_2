from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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


class HearingReportsFromLocalGovernment(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=20, blank=True, null=True)
    reported_at = models.DateTimeField(verbose_name='報告日時', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', blank=True, null=True)
    contents = models.TextField(verbose_name='内容', blank=True, null=True)
    disaster_name = models.ForeignKey(DisasterName, on_delete=models.CASCADE, blank=True, null=True)


class LocalGovernments(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hearing_report = models.ForeignKey(HearingReportsFromLocalGovernment, on_delete=models.CASCADE, blank=True,
                                       null=True)

    def __str__(self):
        return self.name
