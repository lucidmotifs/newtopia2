from django.http import HttpResponse
from django.shortcuts import render

from ntmeta.systems.province import ProvinceSystem

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the newtopia index.")


def province_system(request):
    output = ProvinceSystem.generate_entities('ntgame')
    return HttpResponse(output)
