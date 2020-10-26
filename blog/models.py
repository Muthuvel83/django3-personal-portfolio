from django.db import models

class Blog(models.Model):
	blogtitle = models.CharField(max_length = 200)
	blogdescription = models.TextField()
	blogdate=models.DateField()

	def __str__(self):
		return self.blogtitle