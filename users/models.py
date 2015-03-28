from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField()
    email = models.EmailField(unique=True)
    jabber = models.CharField(max_length=30, blank=True)
    skype = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    other_contacts = models.TextField(blank=True)

    def __unicode__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']