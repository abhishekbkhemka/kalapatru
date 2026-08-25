from LR.models import Customer


class CustomerController:
    def getCustomers(self, requestUser):
        # Active customers only; lighter payload for autocomplete
        return (
            Customer.objects.filter(isActive=True)
            .only(
                'id',
                'label',
                'name',
                'org_id',
                'contactPerson',
                'contactNumber',
                'isActive',
                'addressLine1',
                'addressLine2',
                'area',
                'city',
                'state',
                'country',
            )
            .order_by('name')
        )
