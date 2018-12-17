from django.shortcuts import render
import re,json
from django.shortcuts import redirect
from django.db.models import Sum
from datetime import datetime
from  django.http import HttpResponse
from LR.models import DailyReport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LR.Serializers import DailyReportSerializer

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

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
        data=DailyReport.objects.filter(date__gte=start_date,date__lte=end_date).aggregate(Sum("day_card_sale")
        ,Sum("day_credit_sale"),Sum("day_cash_sale"),
        Sum("total_credit_purchase"),Sum("total_cash_purchase"),
        Sum("bank_deposit"),
        Sum("total_expense"),
        Sum("total_misc_cash_in")
).values()
        data.insert(3,sum(data[0:3]))
        data.insert(6,sum(data[4:6]))
        context['data']=data
    return render(request,"chart.html",context)
def dailyReportView(request):
    context={}
    if request.method=="POST" and request.is_ajax():
        data = request.POST.get("data")
        data=json.loads(data)
        camel={}
        for i in data.keys():
            value=data[i]
            if 'detail' in i.lower():
                value=json.dumps(value)
            camel[to_snake_case(i)]=value if value else 0
        try:
            obj = DailyReport.objects.get(branch_name=data.get("BranchName"), date=data.get("Date"))
            if not obj.is_editable:
                return redirect('/dailyreport/')
        except DailyReport.DoesNotExist:
            pass
        if 'edit' in request.POST:
            obj=DailyReport.objects.get(branch_name=data.get("BranchName"),date=data.get("Date"))
            camel["is_editable"]=False
            serializer=DailyReportSerializer(obj,data=camel)
        else:
            serializer = DailyReportSerializer(data=camel)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data)
        else:
            return HttpResponse(serializer.errors)

            # obj=DailyReport()

        """
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
        """
        return HttpResponse("Daily Report Created")

    if request.method == "GET":
        #Add branches here
        context['branches']=['Raja Bazar']
    return render(request, 'dailyreport.html', context)
