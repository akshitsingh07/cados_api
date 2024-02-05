from django.db.models import Q
# from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
# from rest_framework.throttling import UserRateThrottle

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    return Response(data)

# @throttle_classes([UserRateThrottle])
@api_view(['GET','POST'])
def advocate_list(request):
    #Handling GET reuqests
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(username__icontains = query) | Q(bio__icontains = query) )
        serializer = AdvocateSerializer(advocates, many = True)
        return Response(serializer.data)
    
    #Handeling POST requests
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)

# Provide each advocate details via their username using function based views
# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request, username):
#     advocate = Advocate.objects.get(username=username)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate, many = False)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']
#         advocate.save()
#         serializer = AdvocateSerializer(advocate, many = False)
#         return Response(serializer.data)

#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('Requested data has been deleted.')
    
#Provide each advocate details via their username using Class based views.
class Advocate_detail(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse("Advocate doesn't exists!")

    def get(self, request, username):
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)
    
    def put(self, request, username):
        advocate = self.get_object(username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate, many = False)
        return Response(serializer.data)
    
    def delete(self, request, username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('Requested data has been deleted.')


@api_view(['GET'])
def companies_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many = True)
        return Response(serializer.data)
