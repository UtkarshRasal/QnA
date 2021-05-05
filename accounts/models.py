from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid, datetime
from base.models import BaseModel
from .userManager import UserManager

"""custom user model"""
class User(AbstractUser, BaseModel):
	username	 = None
	email		 = models.EmailField(max_length=255, unique=True, db_index=True)
	is_verified  = models.BooleanField(default=False)
	is_active	 = models.BooleanField(default=True)
	is_staff 	 = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	class Meta:
		ordering  = ['-created_at']
		verbose_name_plural = 'User'
	
	def __str__(self):
		return self.email
