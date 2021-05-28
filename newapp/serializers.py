from rest_framework import serializers
from .models import empdata

class employeeserializer(serializers.ModelSerializer):
	class meta:
		model = empdata
		fields ={'firstname','lastname','address'}