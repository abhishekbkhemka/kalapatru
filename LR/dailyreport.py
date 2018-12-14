from django.shortcuts import render
import re,json
from datetime import datetime
from  django.http import HttpResponse
from LR.models import DailyReport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django import  forms
from django.core.exceptions import MultipleObjectsReturned
from LR.serializers import DailyReportSerializer
class CheckEntryView(APIView):
    def get(self,request):
        data=request.query_params
        branch_name=data.get("branchname")
        date=data.get("date")
        try:
            obj=DailyReport.objects.get(branch_name=branch_name,date=date)
            if obj.is_editable:
                stat = status.HTTP_200_OK
                serializer=DailyReportSerializer(obj)
                return Response(serializer.data, status=stat)

            else:
                stat = status.HTTP_403_FORBIDDEN
        except DailyReport.DoesNotExist:
            stat=status.HTTP_200_OK
        return Response({},status=stat)

def chartView(request):
    context={}
    if request.method=="GET":
        start_date=request.GET.get('start_date',datetime.strftime(datetime.today(),"%Y-%m-%d"))
        end_date=request.GET.get('end_date',datetime.strftime(datetime.today(),"%Y-%m-%d"))
        objs=DailyReport.objects.filter(date__gte=start_date,date__lte=end_date)
        card_sale=0
        credit_sale=0
        cash_sale=0
        total_sale=0
        credit_purchase=0
        cash_purchase=0
        total_purchase=0
        total_deposit=0
        total_expense=0
        total_cash_in=0
        for i in objs:
            card_sale+=i.day_card_sale
            credit_sale+=i.day_credit_sale
            cash_sale+=i.day_cash_sale
            credit_purchase+=i.total_credit_purchase
            cash_purchase+=i.total_cash_purchase
            total_deposit+=i.bank_deposit
            total_expense+=i.total_expense
            total_cash_in+=i.total_misc_cash_in
        total_sale=card_sale+credit_sale+cash_sale
        total_purchase=credit_purchase+cash_purchase
        context['data']=[card_sale,credit_sale,cash_sale,total_sale,credit_purchase,cash_purchase,total_purchase,total_deposit,total_expense,total_cash_in]
    return render(request,"chart.html",context)
from django.shortcuts import redirect
def dailyReportView(request):
    context={}
    if request.method=="POST" and request.is_ajax():
        data = request.POST.get("data")
        data=json.loads(data)
        try:
            obj = DailyReport.objects.get(branch_name=data.get("BranchName"), date=data.get("Date"))
            if not obj.is_editable:
                return redirect('/dailyreport/')
        except DailyReport.DoesNotExist:
            pass
        if 'edit' in request.POST:
            obj=DailyReport.objects.get(branch_name=data.get("BranchName"),date=data.get("Date"))
        else:
            obj=DailyReport()
        obj.misc_cash_in_details = json.dumps(data["miscCashInDetails"])
        obj.purchase_detail = json.dumps(data["purchaseDetail"])
        obj.expenses_detail = json.dumps(data["expensesDetail"])
        obj.day_card_sale=data["dayCardSale"] if data["dayCardSale"] else 0
        obj.bank_deposit = data["bankDeposit"] if data["bankDeposit"] else 0
        obj.day_credit_sale = data["dayCreditSale"] if data["dayCreditSale"] else 0
        obj.total_expense = data["totalExpense"] if data["totalExpense"] else 0
        obj.total_credit_purchase = data["totalCreditPurchase"] if data["totalCreditPurchase"] else 0
        obj.total_cash_purchase = data["totalCashPurchase"] if data["totalCashPurchase"] else 0
        obj.opening_balance = data["openingBalance"] if data["openingBalance"] else 0
        obj.total_misc_cash_in = data["TotalMiscCashIn"] if data["TotalMiscCashIn"] else 0
        obj.cash_inhand = data["cashInhand"] if data["cashInhand"] else 0
        obj.date = data["Date"]
        obj.day_cash_sale = data["dayCashSale"] if data["dayCashSale"] else 0
        obj.branch_name = data["BranchName"]
        obj.day_cash_difference = data["DayCashDifference"] if data["DayCashDifference"] else 0
        obj.is_editable =False
        obj.save()
        return HttpResponse("dw")

    if request.method == "GET":
        #Add branches here
        context['branches']=['Raja Bazar']
    return render(request, 'dailyreport.html', context)
