from django.contrib import admin
from .views import send_transaction_email
from .models import Transaction
# Register your models here.

@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display=['account','amount','balance_after_transaction','transaction_type','loan_approve']

    def save_model(self,request,obj,form,change):
        obj.account.balance+=obj.amount
        obj.balance_after_transaction=obj.account.balance
        obj.account.save()

        send_transaction_email(obj.account.user,obj.amount,"Loan Approval","admin_email.html")
        super().save_model(request,obj,form,change)

         