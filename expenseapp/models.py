from django.db import models

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)

    # Double underscore vainga, appo dhan dashboard-la title neat-ah kaattum
    def __str__(self):
        return self.title