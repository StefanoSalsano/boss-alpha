from django.db import models

# Create your models here.
class Poll(models.Model):
    def __unicode__(self):
        return self.question    
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __unicode__(self):
        return self.choice
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()


#test for form

#table with user
#class UserSubmit (models.Model):
    #username = models.CharField(max_length = 60)
    #password = models.CharField(max_length = 60)
    #mailAdd = models.CharField(max_length = 120)