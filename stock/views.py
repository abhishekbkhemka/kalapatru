from django.shortcuts import render
from forms import StockForm
from django.contrib.auth.decorators import login_required
from models import Stock,Company,SupplyPlace
from django.contrib import admin

@login_required(login_url='/admin/login/')
def stock(request):
    groups = request.user.groups.all()
    groupList=[]
    for obj in groups:
        groupList.append(obj.name)
    usr=request.user
    if usr.is_superuser or 'stock' in groupList:
        companyObj=Company.objects.all()
        supplyPlaceObj=SupplyPlace.objects.all()
        context={}
        context['companyObj']=companyObj
        context['supplyPlaceObj']=supplyPlaceObj

        if request.method == 'POST':
            tp= request.POST.get('type1', None)
            stockObj=Stock()
            stockObj.type=request.POST.get('type1',None)
            stockObj.company_Name=request.POST.get('company_Name',None)
            stockObj.supply_Place=request.POST.get('supply_Place',None)
            stockObj.bill_No=request.POST.get('bill_No',None)
            bill_Date = request.POST.get('bill_Date', None)
            if len(bill_Date)>4:
                stockObj.bill_Date=bill_Date
            bill_Rec_Date = request.POST.get('bill_Rec_Date', None)
            if len(bill_Rec_Date) > 4:
                stockObj.bill_Rec_Date=bill_Rec_Date
            try:
                bill_Amount = float(str(request.POST.get('bill_Amount', '')))
                stockObj.bill_Amount=bill_Amount
            except:
                pass

            stockObj.lr_No=request.POST.get('lr_No',None)
            lr_Date = request.POST.get('lr_Date', None)
            if len(lr_Date) > 4:
                stockObj.lr_Date=lr_Date
            stockObj.cases=request.POST.get('cases',None)
            stockObj.carriers_Name=request.POST.get('carriers_Name',None)
            stockObj.permit_No=request.POST.get('permit_No',None)
            stockObj.doc_Month=request.POST.get('doc_Month',None)
            stockObj.F_C_O=request.POST.get('F_C_O',None)
            date = request.POST.get('date', None)
            if len(date) > 4:
                stockObj.date=date
            stockObj.qrt=request.POST.get('qrt',None)
            stockObj.remarks=request.POST.get('remarks',None)
            stockObj.commodity=request.POST.get('commodity',None)
            stockObj.year=request.POST.get('year',None)
            stockObj.save()
            context['message']="Stock Added Successfully"
            return render(request, 'stock.html',context)
        return render(request, 'stock.html',context)
    else:
        context={'errorCode':404,'errorMsg':'You dont have this permissions'}
# admin.site.register_view('somepath', view=stock)