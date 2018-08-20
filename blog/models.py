from django.db import models

class Event(models.Model):
	name=models.CharField(max_length=100)
	desc=models.TextField()
	image=models.ImageField(upload_to='event')
	date=models.DateTimeField()

	def __str__(self):
		return self.name

	def staff(self):
		return self.desc[:255]