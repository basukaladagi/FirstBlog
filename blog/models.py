from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	slug  = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['-created']
	def __unicode__(self):
		return u'%s'%self.title
	def get_absolute_url(self):
		return reverse('blog.views.post', args =
		[self.slug])
