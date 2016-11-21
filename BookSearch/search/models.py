from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __unicode__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return "{} in category {}".format(self.title, self.category)