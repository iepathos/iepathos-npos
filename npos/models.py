# encoding: utf-8
from django.db import models

# Active Npo Manager to keep track of which Npos I have set to active on the site
class ActiveNpoManager(models.Manager):
	def get_query_set(self):
		return super(ActiveNpoManager, self).get_query_set().filter(is_active=True)

# Tax Exempt Non-Profit Organizations
class Npo(models.Model):
	name = models.CharField(max_length=100) # Name of Organization
	city = models.CharField(max_length=50) # City
	state = models.CharField(max_length=2) # State Abbreviation
	ein = models.CharField(max_length=9) #Unique IRS Electronic Identification Number
	country = models.CharField(max_length=13) # Country should be United States

	is_active = models.BooleanField(u'Active')
	objects = models.Manager()
	active = ActiveNpoManager()

	# Ads shown
	
	# Total views received 
	# Total clicks received through iepathos
	# Money raised today through iepathos
	# Total money raised through iepathos
	
	###
	
	
	class Meta:
		verbose_name = u'NPO'
		verbose_name_plural = u'NPOs'

	def __unicode__(self):
		return self.name
		
	@models.permalink
	def get_absolute_url(self):
		return ('npos_npo_detail', (), {'name': self.name})
