from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def result(request):
    user_input_age =request.GET["age"]
    return render(request,'result.html',{'age':user_input_age})