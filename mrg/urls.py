from django.urls import path

import mrg.medicine
import mrg.customer
from mrg.views import *

urlpatterns = [
    # 界面
    path('customer-list', listcustomer),
    path('customer-add', customer_add),
    path('member-edit', customer_modify),

    path('medicine-list', medicine_list),
    path('medicine-add', medicine_add),



    #服务
    path('customer', mrg.customer.dispatcher),
    path('medicine', mrg.medicine.dispatcher)
]