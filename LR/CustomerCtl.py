

from LR.models import Customer
class CustomerController():

    def getCustomers(self,requestUser):
        customer = Customer.objects.filter()
        return customer