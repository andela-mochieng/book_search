from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from search.models import Category, Book


class TestSearchView(TestCase):

    def setUp(self):
        self.client = Client()
        self.search_url = reverse('search')
        self.book_title = 'Test Book'
        self.book_title2 = {'title': 'Test Book'}
        self.category_name = {'name': 'History'}
        self.category_name2 = 'History'
        self.create_category = Category.objects.create(
            name=self.category_name2)
        self.create_book = Book.objects.create(
            title=self.book_title, category=self.create_category)

    def test_booktitle_partial_search_successfully(self):
        """Test available book is returned when searched"""
        response = self.client.get(self.search_url, self.book_title2)
        self.assertTrue(response.status_code, 200)
        self.assertIn('Test', str(response.context['request']))

    def test_book_search_successfully(self):
        """Test available book is returned when searched"""
        response = self.client.get(self.search_url, self.book_title2)
        self.assertTrue(response.status_code, 200)
        print(str(response.context['request']))
        self.assertContains(self.book_title, str(response.context['request']))

    def test_partial_category_name_search_is_unsucessful(self):
        """Test partial category name search is unsucessful"""
        response = self.client.get(self.search_url, self.category_name)
        self.assertNotIn('histo', str(response.context['request']))

    def test_exact_category_name_search_is_successfully(self):
        """Test exact category name search is successfully"""
        response = self.client.get(self.search_url, self.category_name)
        self.assertTrue(response.status_code, 200)
        self.assertIn(self.category_name2, str(response.context['request']))    

    def test_book_search_unsuccessfully(self):
        """Test search unavailable book returns all the books """
        response = self.client.get(self.search_url, {'title': 'Anything test'})
        all_books = Book.objects.all()
        self.assertTrue(response.status_code, all_books)
