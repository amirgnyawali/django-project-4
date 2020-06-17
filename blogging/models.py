from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	def __str__(self):
		return self.title
	#title
	title = models.CharField(max_length=128)
	#text
	text = models.TextField(blank=True)
	#author
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#created_date
	created_date = models.DateTimeField(auto_now_add=True)
	#modified_date
	modified_date = models.DateTimeField(auto_now=True)
	#published_date
	published_date = models.DateTimeField(blank=True, null=True)

class Category(models.Model):
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'
	#name
	name = models.CharField(max_length=128)
	#description
	description = models.TextField(blank=True)
	#posts
	posts = models.ManyToManyField(Post, blank=True, related_name='categories')
