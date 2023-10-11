from django.db import models
class slider(models.Model):
    DICSCOUNT_DEAL=(
        ('HOT DEALS','HOT DEALS'),
        ('New Arraivels','New Arraivels'),

    )
    image=models.ImageField(upload_to='media/slider_image')
    discount_del=models.CharField(choices=DICSCOUNT_DEAL,max_length=100)
    sale=models.IntegerField()
    brand_name=models.CharField(max_length=200)
    dicount=models.IntegerField()
    link=models.CharField(max_length=500)
    def __str__(self):
        return self.brand_name

# Create your models here.
