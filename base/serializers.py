from rest_framework.serializers import ModelSerializer
from .models import Advocate, Company

#Serialize the advocates field to convert into JSON format.
class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'