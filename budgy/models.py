from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    archived = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def allocated(self):
        categories = self.category_set.all()
        allocated = 0
        for category in categories:
            allocated += category.amount
        return allocated

    @property
    def to_allocate(self):
        to_allocate = self.amount - self.allocated
        return to_allocate

    @property
    def spent(self):
        categories = self.category_set.all()
        spent = 0
        for category in categories:
            spent += category.spent
        return spent

    @property
    def remaining(self):
        remaining = self.amount - self.spent
        return remaining

    @property
    def percent(self):
        percent = int((self.spent/self.amount)*100)
        return percent

class Category(models.Model):
    name = models.CharField(max_length=200)
    amount = amount = models.DecimalField(max_digits=9, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    @property
    def spent(self):
        expenses = self.expense_set.all()
        spent = 0
        for expense in expenses:
            spent += expense.amount
        return spent

    @property
    def remaining(self):
        remaining = self.amount - self.spent
        return remaining

    @property
    def percent(self):
        percent = int((self.spent/self.amount)*100)
        return percent

class Expense(models.Model):
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(default=None, null=True, blank=True)
    notes = models.TextField(default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)








