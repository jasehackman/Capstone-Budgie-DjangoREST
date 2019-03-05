from django.shortcuts import render
from budgy.models import *
from budgy.serializers import *
from rest_framework import viewsets
from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
import json


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    filterset_fields = ( 'budget_id', 'name')



class ExpenseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    filterset_fields = ( 'category_id', 'name')


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def register_user(request):
    req_body = json.loads(request.body.decode())
    new_user=User.objects.create_user(
        username=req_body['username'],
        password=req_body['password'],
        email=req_body['email'],
        first_name=req_body['first_name'],
        last_name=req_body['last_name']
    )

    token= Token.object.create(user=new_user)

    data=json.dumps({'token':token.key})
    return HttpResponse(data,content_type='application/json')
