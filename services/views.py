from django.shortcuts import render, redirect
from services.models import Service, UsedProducts
from safra.models import Harvest, Product
from datetime import datetime

class ServicesView:
    '''
    Services View define methods for crud.
    '''

    def create(request):
        template = 'services/create_service.html'
        harvests = Harvest.objects.all()
        products = Product.objects.all()
        if request.method == 'POST':
            name = request.POST.get('name', '')
            cost = request.POST.get('cost', '')
            date_start = request.POST.get('date_start', '')
            date_end = request.POST.get('date_end', '')
            harvest_id = request.POST.get('harvest_id', '')
            service = Service(
                        name=name,
                        cost=cost,
                        date_start=date_start,
                        date_end=date_end,
                        harvest_id=harvest_id,
                    )
            service.save()
            for product in products:
                qtd = int(request.POST.get('{}'.format(product.id), 0))
                if qtd != 0:
                    used_prod = UsedProducts(
                                    product_id=product.id,
                                    service=service,
                                    quantity=qtd,
                                    price=0,
                                )
                    used_prod.save()

        return render(request, template, {'harvests': harvests,
                                          'products': products})

    def services(request):
        template = 'services/services.html'
        services = Service.objects.all()
        return render(request, template, {'services': services})


    def process_prices(request):
        current_month=datetime.now().month
        current_year=datetime.now().year
        if current_month == 1:
            month = 12
            year = current_year - 1
        else:
            month = current_month - 1
            year = current_year
        services = Service.objects.filter(
            date_start__year=year,
            date_start__month=month,
        )
        total_cost = 0
        products={}
        print(services)
        for service in services:
            total_cost += service.cost
            for used_prod in service.usedproducts_set.all():
                qtd = products.get('{}'.format(used_prod.product_id), 0)
                qtd += used_prod.quantity
                products['{}'.format(used_prod.product_id)]=qtd
        qtd_total=0
        for key in products:
            qtd_total += products[key]
        for product_id in products:
            price = (products[product_id]/qtd_total)*total_cost/products[product_id]
            product = Product.objects.get(pk=product_id)
            product.avg_price = price
            data = {'product_id': product_id, 'avg_price': price}
            # send_data(data)
            product.save()

        return redirect(ServicesView.services)

    
    def send_data(data):
        import json
        json_data = json.dumps(data)
        # send json_data to other platforms
