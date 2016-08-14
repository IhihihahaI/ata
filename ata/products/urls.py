from django.conf.urls import url
from . import views

app_name = "products"
urlpatterns = [
    url(r"^$", views.indexView, name = "index"),
    url(r"^(?P<product_name>[^ \t\r\n\v\f]+)/$", views.productDetailView, name = "detail"),
]
