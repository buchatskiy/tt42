from django.db import models

class LogRequest(models.Model):

    date = models.DateTimeField('Date time', auto_now_add=True)
    request_method = models.CharField('Request_method', max_length=20)
    path = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s [%s]' % (
            self.date.strftime('%Y-%m-%d %H:%M:%S'),
            self.request_method
        )
