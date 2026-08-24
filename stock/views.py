from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stock.models import Stock, Company, Commodity


@login_required(login_url='/admin/login/')
def stock(request):
    groups = request.user.groups.all()
    groupList = [obj.name for obj in groups]
    usr = request.user
    if usr.is_superuser or 'stock' in groupList:
        companyObj = Company.objects.all()
        commodityObj = Commodity.objects.all()
        context = {
            'companyObj': companyObj,
            'commodityObj': commodityObj,
        }

        if request.method == 'POST':
            stockObj = Stock()
            stockObj.type = request.POST.get('type1', None)
            stockObj.company_id = str(request.POST.get('company_Name', None))
            stockObj.address_id = str(request.POST.get('cmpAddress', None))
            stockObj.bill_No = request.POST.get('bill_No', None)
            bill_Date = request.POST.get('bill_Date', None)
            if bill_Date and len(bill_Date) > 4:
                stockObj.bill_Date = bill_Date
            bill_Rec_Date = request.POST.get('bill_Rec_Date', None)
            if bill_Rec_Date and len(bill_Rec_Date) > 4:
                stockObj.bill_Rec_Date = bill_Rec_Date
            try:
                stockObj.bill_Amount = float(str(request.POST.get('bill_Amount', '')))
            except Exception:
                pass

            stockObj.lr_No = request.POST.get('lr_No', None)
            lr_Date = request.POST.get('lr_Date', None)
            if lr_Date and len(lr_Date) > 4:
                stockObj.lr_Date = lr_Date
            stockObj.cases = request.POST.get('cases', None)
            stockObj.carriers_Name = request.POST.get('carriers_Name', None)
            stockObj.permit_No = request.POST.get('permit_No', None)
            try:
                stockObj.permit_Amt = float(str(request.POST.get('permit_Amt', '')))
            except Exception:
                pass
            stockObj.doc_Month = request.POST.get('doc_Month', None)
            stockObj.F_C_O = request.POST.get('F_C_O', None)
            date = request.POST.get('date', None)
            if date and len(date) > 4:
                stockObj.date = date
            stockObj.qrt = request.POST.get('qrt', None)
            stockObj.remarks = request.POST.get('remarks', None)
            stockObj.commodity_id = str(request.POST.get('commodity', None))
            stockObj.year = request.POST.get('year', None)
            stockObj.save()
            context['message'] = "Stock Added Successfully. Note down Record Id-" + str(stockObj.id)
            return render(request, 'stock.html', context)
        return render(request, 'stock.html', context)

    context = {'errorCode': 404, 'errorMsg': 'You dont have this permissions'}
    return render(request, 'error.html', context)


def upload(request):
    if request.method == 'POST':
        fileName = request.POST.get('myfile', None)
        print(fileName)
    return render(request, 'uploadfile.html')
