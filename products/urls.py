from django.urls import path
from django.contrib import admin

from .views import ProductDetailView, ProductListView

app_name = "products"

admin.site.site_title = "1425"


urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="detail"),
    path("category/<slug:slug>/", ProductListView.as_view(), name="list_by_category"),
]