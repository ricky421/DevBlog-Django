from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length = 73)
	#slug-field should be pre-populated later on
	slug = models.SlugField(default = '')
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	#author
	author = models.ForeignKey(User, on_delete=models.CASCADE, default = None)

	def __str__(self):
		return self.title

	def snippet(self):
		return ' '.join(self.body.split(' ')[:15]) + '...'