from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	tag_title = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.tag_title


class Snippet(models.Model):
	snippet_title = models.CharField(max_length=255)
	content = models.TextField()
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=True, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	timestamp= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.snippet_title

