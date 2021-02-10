from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Password(models.Model):
    title = models.CharField(max_length=122)
    website = models.CharField(max_length=122)
    user = models.CharField(max_length=122)
    myRange=models.CharField(max_length=122)
    wpass=models.CharField(max_length=100,default="l")
    pass_author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
    
    def __str__(self):
        return self.title



class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username
	
    def save(self,*args,**kwargs):

        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height>300 and img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




    