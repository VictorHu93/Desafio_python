from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def reserve(self, request, pk=None):
        """Reserva um livro se ele estiver disponível."""
        book = self.get_object()
        if book.is_reserved or book.is_borrowed:
            return Response({"message": "Livro não disponível"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Reserva o livro
        book.is_reserved = True
        book.save()
        return Response({"message": "Livro reservado com sucesso"}, status=status.HTTP_200_OK)

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def list(self, request, *args, **kwargs):
        """Lista os livros emprestados para um cliente específico."""
        client_id = kwargs.get('id_client')
        loans = Loan.objects.filter(client__id=client_id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

