from django.urls import path
from front.views import FrontView

urlpatterns = [
    path('Home', FrontView.as_view()),
]