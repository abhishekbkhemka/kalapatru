from django.shortcuts import render
import re,json
from constants import BRANCHES
from django.shortcuts import redirect
from django.db.models import Sum
from datetime import datetime
from  django.http import HttpResponse
from LR.models import DailyReport
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from LR.Serializers import DailyReportSerializer
from django.db import connection


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
        start_date=request.GET.get('start_date',datetime.strftime(datetime.today().replace(day=1),"%Y-%m-%d"))
        end_date=request.GET.get('end_date',datetime.strftime(datetime.today(),"%Y-%m-%d"))
        where_clause = "date BETWEEN '%s' and '%s'" %(start_date,end_date)
        if request.GET.get("branch") and not request.GET.get("branch")=="All":
            where_clause += "and branch_name = %s"%(request.GET.get("branch",'').lower())
        sql = """
                select SUM(day_card_sale) as total_card_sale, SUM(day_credit_sale) as total_credit_sale, SUM(day_cash_sale) as total_cash_sale, SUM(day_card_sale+day_credit_sale+day_cash_sale) as total_sale,
                SUM(total_credit_purchase) , SUM(total_cash_purchase) , SUM(total_cash_purchase+ total_credit_purchase) , SUM(bank_deposit),SUM(total_expense),SUM(total_misc_cash_in)
                from kalptaru1.LR_dailyreport where %s
       """ %(where_clause,)
        try:

            with connection.cursor() as cursor:
                cursor.execute(sql)
                data = cursor.fetchone()
            # data.reverse()
                data=list(data)
                context['branches'] = BRANCHES
                chart_data = {'labels':
                                  ['Total Card Sale ('+str(data[0])+')',
                                   'Total Credit Sale ('+str(data[1])+')',
                                   'Total Cash Sale ('+str(data[2])+')',
                                   'Total Sale ('+str(data[3])+')',
                                   'Total Credit Purchase ('+str(data[4])+')',
                                   'Total Cash Purchase ('+str(data[5])+')',
                                   'Total Purchase ('+str(data[6])+')',
                                   'Total Deposit ('+str(data[7])+')',
                                   'Total Expense ('+str(data[8])+')',
                                   'Total Cash In ('+str(data[9])+')'],
                            'datasets': [{'backgroundColor':
                                                ['green','green','green','green','red','orange','red','blue','red','green'],
                            'data':data }]}
                context['chart_data'] = chart_data
        except Exception,e:
            context['chart_data'] = {}
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

        return HttpResponse("Daily Report Created")

    if request.method == "GET":
        #Add branches here
        context['branches']= BRANCHES
    return render(request, 'dailyreport.html', context)
