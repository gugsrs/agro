from django.conf.urls import url

from services.views import ServicesView


urlpatterns = [
    url(r'^create', ServicesView.create),
    url(r'^list', ServicesView.services),
    url(r'^prices', ServicesView.process_prices),
]
