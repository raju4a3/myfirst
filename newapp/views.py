from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import empdata
from .serializers import employeeserializer
def home(request):
	return HttpResponse('Home page')

def about(request):
	return HttpResponse('about page')

def index(request):
	return render(request,'accounts/dash.html')

def contact(request):
	return render(request,'accounts/contact.html')

class employees(APIView):
	def get(self,request):
		employee=empdata.objects.all()
		serializer=employeeserializer(employee,many=True)
		print(employee)
		return Response(serializer.data)
