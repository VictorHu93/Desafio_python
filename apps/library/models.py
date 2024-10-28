from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_reserved = models.BooleanField(default=False)
    is_borrowed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Loan(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()

    def calculate_fee(self):
        from datetime import datetime
        days_overdue = (datetime.now() - self.due_date).days
        if days_overdue <= 0:
            return {"days_overdue": 0, "fee": 0, "daily_interest": 0}
        elif days_overdue <= 3:
            return {"days_overdue": days_overdue, "fee": 0.03, "daily_interest": 0.002}
        elif days_overdue <= 5:
            return {"days_overdue": days_overdue, "fee": 0.05, "daily_interest": 0.004}
        else:
            return {"days_overdue": days_overdue, "fee": 0.07, "daily_interest": 0.006}
