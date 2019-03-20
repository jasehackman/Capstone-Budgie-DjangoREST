from rest_framework import serializers
from budgy.models import *
from django.contrib.auth.models import User

# Todo: refactor for search
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Displays User info

    """

    class Meta:
        model = User
        fields = "__all__"

class BudgetSerializer(serializers.HyperlinkedModelSerializer):
    """ Displays budget information.


    """
    class Meta:
        model = Budget
        fields = ('name', 'amount', 'spent', 'remaining', 'id', 'user', 'percent', 'archived', 'allocated', 'to_allocate')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """ Displays category information.

    """
    budget_id=serializers.PrimaryKeyRelatedField(queryset=Budget.objects.all(), source='budget')
    class Meta:
        model = Category
        fields = ('name', 'amount', 'budget', 'spent', 'remaining', 'id', 'budget_id', "url", 'percent')

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    """ Displays expense information.

    """
    category_id=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')

    class Meta:
        model = Expense
        fields = ('name', 'amount', 'date', 'notes', 'category_id', 'id')

