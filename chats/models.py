from django.db import models
from django.contrib.auth.models import User
from main_app.models import consultation

# Create your models here.

class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    consultation_id =  models.ForeignKey(consultation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    def __unicode__(self):
        return self.message




class Feedback(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField()

    def __unicode__(self):
        return self.feedback