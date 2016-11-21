from django.test import TestCase
from search.models import Category, Book


class TestSearchModels(TestCase):
    """Test search app  models"""

    def setUp(self):
        self.category_name = "History"
        self.book_title = "Test book"
        self.category = Category.objects.create(name=self.category_name)
        self.book = Book.objects.create(title=self.book_title, category=self.category)


    def test_category_model_is_created(self):
        initial_count = Category.objects.count()
        category_model = Category.objects.create(name="Python")
        after_count = Category.objects.count()
        self.assertEqual(after_count, initial_count+1)

    

