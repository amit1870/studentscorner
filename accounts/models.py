from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo

class UserProfile(BaseOrderInfo):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return 'User Profile for: ' + self.user.username
