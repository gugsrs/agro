from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404 

from safra.models import Product

class ProductsView:
    '''
    Products View define crud methods.
    '''
    
    def create(request):
        template = 'safra/create_product.html'
        if request.method == 'POST':
            name = request.POST.get('name', '')
            product = Product(name=name)
            product.save()
        return render(request, template, {})


    def products(request):
        template = 'safra/products.html'
        products = Product.objects.all()
        return render(request, template, {'products': products})


    def edit(request):
        template = 'safra/edit_product.html'
        product_id = request.GET.get('product_id', None)
        if not product_id:
            product_id = request.POST.get('product_id', None)
        if product_id is not None:
            product = Product.objects.get(pk=product_id)
        else:
            raise Http404
        if request.method == 'POST':
            name = request.POST.get('name', '')
            price = request.POST.get('price', 0)
            product.name = name
            product.avg_price = price
            product.save()
            return redirect(ProductsView.products)

        if product:
            return render(request, template, {'product': product})
        return render(request, template, {})


    def delete(request):
        product_id = request.GET.get('product_id', None)
        if product_id is not None:
            product = Product.objects.get(pk=product_id)
        if not product:
            raise Http404
        product.delete()
        return redirect(ProductsView.products)
