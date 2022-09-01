from django.shortcuts import render
from django.http import HttpResponse

def user_profiles(request):
    return HttpResponse("This is for User_profile management")