from django.shortcuts import render, redirect


# Create your views here.

def home(r):
    return redirect('user/login')
