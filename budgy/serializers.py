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
        fields = ('name', 'amount', 'spent', 'remaining', 'id', 'user')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # budget=BudgetSerializer(read_only=True)
    budget_id=serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all(), source='budget')
    class Meta:
        model = Category
        fields = ('name', 'amount', 'budget', 'spent', 'remaining', 'id', 'budget_id')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    category_id=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'date', 'notes', 'category_id', 'id')

