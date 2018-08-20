from django.db import models

class Projects(models.Model):
	name=models.CharField(max_length=50)
	image=models.ImageField(upload_to='pro')
	desc=models.TextField()
	pub_date=models.DateTimeField()

	def __str__(self):
		return self.name

class Messages(models.Model):
	title=models.CharField(max_length=100)
	message=models.TextField()
	name_writer=models.CharField(max_length=100)
	when=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title