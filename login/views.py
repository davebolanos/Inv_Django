from json import load
from multiprocessing import context
from re import template
import re
from unittest import loader
from urllib import request
from django.shortcuts import render, get_list_or_404
from django.template import loader
from django.http import HttpResponse
from django.views import generic

def login(request):
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')
    