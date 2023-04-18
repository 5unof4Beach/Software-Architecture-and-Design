# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from product_model.models import product_details


@csrf_exempt
def get_product_data(request):
    data = []
    resp = {}
    # This will fetch the data from the database.
    prodata = product_details.objects.all()
    for tbl_value in prodata.values():
        data.append(tbl_value)
    # If data is available then it returns the data.
    if data:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['data'] = data
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Data is not available.'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def add_product_data(request):
    resp = {}
    id = request.POST.get("id")
    cat = request.POST.get("cat")
    name = request.POST.get("name")
    availability = request.POST.get("availability")
    price = request.POST.get("price")
    respdata = data_insert(id, cat, name, availability, price)
    if respdata:
        resp['status'] = 'Success'
        resp['status_code'] = '200'
        resp['message'] = 'Product added Successfully.'
    # If it is not returning any value then the show will fail.
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Unable to register user, Please try again.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def data_insert(id, cat, name, availability, price):
    user_data = product_details(id, cat, name, availability, price)
    user_data.save()
    return 1