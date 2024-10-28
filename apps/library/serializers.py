from rest_framework import serializers
from .models import Book, Loan

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'is_reserved', 'is_borrowed']

class LoanSerializer(serializers.ModelSerializer):
    fee_details = serializers.SerializerMethodField()

    class Meta:
        model = Loan
        fields = ['id', 'book', 'loan_date', 'due_date', 'fee_details']

    def get_fee_details(self, obj):
        return obj.calculate_fee()
