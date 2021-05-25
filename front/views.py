from django.shortcuts import render
from django.views.generic import TemplateView

class FrontView(TemplateView):
    template_name = "front/shop_product_col_3.html"

# Create your views here.
