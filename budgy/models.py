from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    """Defines a budget.

    Returns:
        str -- Budget Name
    """
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    archived = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def allocated(self):
        # Returns how much of the budget total amount has been assigned to categories
        categories = self.category_set.all()
        allocated = 0
        for category in categories:
            allocated += category.amount
        return allocated

    @property
    def to_allocate(self):
        # Returns how much of a budget needs to be put in a category
        to_allocate = self.amount - self.allocated
        return to_allocate

    @property
    def spent(self):
        # Returns how much of the budget has been spent
        categories = self.category_set.all()
        spent = 0
        for category in categories:
            spent += category.spent
        return spent

    @property
    def remaining(self):
        # Returns how much of the budget can still be spent
        remaining = self.amount - self.spent
        return remaining

    @property
    def percent(self):
        # Returns the % of the budget that has been spent
        percent = int((self.spent/self.amount)*100)
        return percent

class Category(models.Model):
    """Defines a Category.

    Returns:
        str -- Category Name
    """
    name = models.CharField(max_length=200)
    amount = amount = models.DecimalField(max_digits=9, decimal_places=2)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    @property
    def spent(self):
        # Returns how much has been spent out of the category
        expenses = self.expense_set.all()
        spent = 0
        for expense in expenses:
            spent += expense.amount
        return spent

    @property
    def remaining(self):
        # Returns how much of the category is left
        remaining = self.amount - self.spent
        return remaining

    @property
    def percent(self):
        # Returns the % of the category that has been spent
        percent = int((self.spent/self.amount)*100)
        return percent

class Expense(models.Model):
    """Defines an expense.

    Returns:
        str -- Expense Name
    """
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateField(default=None, null=True, blank=True)
    notes = models.TextField(default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)








