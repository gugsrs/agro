from django.conf.urls import url

from safra.views import ProductsView, HarvestView


urlpatterns = [
    url(r'^products/create', ProductsView.create),
    url(r'^products/list', ProductsView.products),
    url(r'^products/delete', ProductsView.delete, name='delete_product'),
    url(r'^products/edit', ProductsView.edit, name='edit_product'),
    url(r'^harvest/create', HarvestView.create),
    url(r'^harvest/delete', HarvestView.delete),
    url(r'^harvest/edit', HarvestView.edit),
    url(r'^harvest/list', HarvestView.harvests),
]
