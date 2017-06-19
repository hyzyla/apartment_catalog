from django.db import models

# Create your models here.
class Project(models.Model):

	name = models.CharField(max_length=1024)
	time_ready = models.DateField()
	geo = models.CharField(max_length=1024)
	bood_company = models.ForeignKey("BoodCompany", on_delete=models.CASCADE)
	district = models.ForeignKey("District", on_delete=models.CASCADE)

class Apartment(models.Model):

	area_living = models.IntegerField()
	area_total = models.IntegerField()
	room_count = models.IntegerField()
	price = models.IntegerField()
	project = models.ForeignKey("Project", on_delete=models.CASCADE)

	def __repr__(self):
		return "{} кімнатна квартира ({} грн) {}/{}"\
			.format(self.room_count, self.price, self.area_total, self.area_living,)

	def __str__(self):
		return self.__repr__()


class BoodCompany(models.Model):

	name = models.CharField(max_length=1024)
	geo_office = models.CharField(max_length=1024)
	ceo = models.CharField(max_length=1024)

class District(models.Model):

	name = models.CharField(max_length=1024)
	location = models.CharField(max_length=1024)

	def __repr__(self):
		return "{} ({})".format(self.name, self.location)

	def __str__(self):
		return self.__repr__()

class Picture(models.Model):

	picture = models.ImageField(upload_to="media")
	apartment = models.ForeignKey("Apartment", on_delete=models.CASCADE)
