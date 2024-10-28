from rest_framework.test import APITestCase, APIClient
from rest_framework import status

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_books_route(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reserve_book(self):
        response = self.client.post('/books/1/reserve/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_access(self):
        response = self.client.get('/books/protected/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
