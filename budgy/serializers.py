from rest_framework import serializers
from budgy.models import *
from django.contrib.auth.models import User

# Todo: refactor for search
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

class BudgetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Budget
        fields = ('name', 'amount', 'spent', 'remaining', 'id')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'amount', 'budget', 'spent', 'remaining', 'id')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Expense
        fields = "__all__"
