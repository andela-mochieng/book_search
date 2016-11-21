from django.test import TestCase, Client
from django.core.urlresolvers import reverse 
from search.models import Category, Book


class TestSearchView(TestCase):

    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')
        self.book_title = {'title': 'Test book title'}
        self.category_name = {'name': 'History'}
        self.create_category = Category.objects.create(name=self.category_name)
        self.create_book = Book.objects.create(name=self.book_title, category=self.create_category)

    def test_book_search_successfull(self):
        """Test available book is returned when searched"""
        response = self.client.get(self.search_url, self.book_title)
        self.assertTrue(response.status_code, 200)
        self.assertIn(response.values()['request'], self.book_title)
        



    def test_book_search_unsuccessful(self):
        """Test unavailable book returns 404 """
        response = self.client.get(self.search_url, {'title': 'Anything test'})
        self.assertTrue(response.status_code, 404 )


            