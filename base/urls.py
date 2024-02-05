from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoints),  #Home Url
    path('advocates/',views.advocate_list, name = 'advocates'), #show all advocates & Their details.
    
    # path('advocates/<str:username>/',views.advocate_detail), #Redirect to each advocates using usernames.
    path('advocates/<str:username>/',views.Advocate_detail.as_view()), #Redirect to each advocates using usernames.

    path('companies/',views.companies_list, name = 'companies'), #Redirect to each comapnies list.

]