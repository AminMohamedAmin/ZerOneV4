from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver
from Auth.models import User
from datetime import date


class Treasury(models.Model):
    treasury_name = models.CharField(max_length=100, verbose_name="اسم الخزينة")
    treasury_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الاضافة")
    treasury_balance = models.FloatField(default=0.00, verbose_name="رصيد الخزينة")
    treasury_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="اضافة بواسطة")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.treasury_name
    

OPERATION_TYPE = (
    (1, "اضافة رصيد"),
    (2, "سحب رصيد")
)

class TreasuryOperation(models.Model):
    treasury = models.ForeignKey(Treasury, on_delete=models.CASCADE,null=True, blank=True, verbose_name="الخزينة")
    operation_type = models.IntegerField(choices=OPERATION_TYPE, default=0, verbose_name="نوع العملية")
    operation_value = models.FloatField(default=0.0, verbose_name="قيمة العملية")
    operation_description = models.TextField(max_length=200, null=True, blank=True, verbose_name = "وصف العملية")
    operation_notes =  models.TextField(max_length=200, null=True, blank=True, verbose_name = "ملاحظات علي العملية")
    operation_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  verbose_name="انشاء بواسطة")
    operation_date = models.DateField(default=date.today, verbose_name="تاريخ العملية")
    deleted_operation = models.BooleanField(default=False)

    def __str__(self):
        return self.treasury.treasury_name
    

# signals function to create operation when user created new treasury 
@receiver(post_save, sender=Treasury)
def create_treasury_operatoin(sender, instance, created, **kwargs):
    if created:
        TreasuryOperation.objects.create(
            treasury = instance,
            operation_type = 1,
            operation_value = instance.treasury_balance,
            operation_description = "قيمة افتتاحية",
            operation_user = instance.treasury_user
            )
  