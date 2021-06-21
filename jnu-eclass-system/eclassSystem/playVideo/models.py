from django.db import models

# Create your models here.
class Video(models.Model):
	lectureVideoID = models.BigIntegerField(primary_key = True)
	lectureVideo = models.CharField(max_length = 20)
	lectureName = models.CharField(max_length = 20)
	fileName = models.CharField(max_length = 20)
	
	def __str__(self):
		return lectureVideo