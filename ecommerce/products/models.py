from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save

from django.conf import settings
# Create your models here.
# T-Shirt 1
# Active Wear 2
# Women's Clothing 3
import os

class SliderImage(models.Model):
	imageslide = models.ImageField(upload_to='sliders/')
	img_name = models.CharField(max_length=120)

	def __str__(self):
		return self.img_name

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)

	price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100,null=True, blank=True)
	slug = models.SlugField(unique=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	update_defaults = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	class Meta:
		unique_together = ('title', 'slug')

	def get_price(self):
		return self.price

	def get_absolute_url(self):
		return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
	product = models.ForeignKey(Product)
	image = models.ImageField(upload_to='')
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.product.title
