from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from django.views.generic import ListView
from .models import Category, Book


class SearchView(ListView):
    """Create search functionality"""
    model = Book
    template_name = 'search/base.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        querystring = self.request.GET.get('q', '')
        category_name = self.request.GET.get('category', '')
        results = ""
        if querystring and category_name:
            results = Book.objects.filter(
                Q(title__icontains=querystring) &
                Q(category__name__iexact=category_name))

        elif category_name:
            results = Book.objects.filter(
                category__name__iexact=category_name)
        elif querystring:
            results = Book.objects.filter(title__icontains=querystring)
        else:
            return Book.objects.all()
        if not results:
            print(results)
            raise Http404('No book or category with name exists')
        else:
            return results
