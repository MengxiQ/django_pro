from django.urls import path
from mrg.customer import *
urlpatterns = [
    path('listcustomer', dispatcher)
]