from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class User(AbstractUser):
	indra = models.CharField(max_length=100 , blank=True , null=True)

	def __str__(self):
		if self.first_name : return self.first_name
		else: return self.username
	
class Area(models.Model):
	name = models.CharField(max_length=150, blank=False, null=False, unique=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=150, blank=False, null=False, unique=True)
	
	def __str__(self):
		return self.name


class Complain(models.Model):
	unique_number = models.UUIDField(primary_key=True, unique=True, null=False, blank=False , editable=False , default=uuid.uuid4 )
	name = models.CharField(max_length = 150, blank = False, null = False)
	description = models.TextField(blank = False, null = False)
	category = models.ForeignKey(Category)
	area = models.ForeignKey(Area)
	user = models.OneToOneField(User)
	on_date = models.DateTimeField(auto_now_add= True, auto_now = False)
	status = models.CharField(max_length = 150, blank = False, null = False)

	def __str__(self):
		return str(self.unique_number)

def get_image_filename():
		return str(uuid.uuid4()[:8])

class ProductImage(models.Model):
	image = models.ImageField(upload_to = get_image_filename)
	complain = models.ForeignKey(Complain)
