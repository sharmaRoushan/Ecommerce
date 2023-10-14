from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save

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

class banner_area(models.Model):
    image=models.ImageField(upload_to='Pic/banner')
    discount_del=models.CharField(max_length=100)
    quet=models.CharField(max_length=100)
    dicount=models.IntegerField()
    link=models.CharField(max_length=500)

    def __str__(self):
        return self.quet
class MainCategory(models.Model):
    name=models.CharField(max_length=150)
    def __str__(self):
        return self.name
class Category(models.Model):
    main_category=models.ForeignKey(MainCategory,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name +"--"+ self.main_category.name
class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.category.main_category.name+"--"+self.category.name+"--"+self.name
class Section (models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Product(models.Model):
    total_quantity=models.IntegerField()
    availablity=models.IntegerField()
    fetucher_image=models.CharField(max_length=150)
    product_name=models.CharField(max_length=150)
    price=models.IntegerField()
    discount=models.IntegerField()
    product_information=RichTextField()
    model_name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.CharField(max_length=150)
    deprecation=RichTextField()
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    slug=models.SlugField(default='',max_length=500,null=True,blank=True)
    def __str__(self):
        return self.product_name
    def get_absolute_ulr(self):
        from django.urls import reverse
        return reverse ("product_detail",kwargs={'slug': self.slug})
    class Meta:
        db_table="app_Product"

def create_slug(instance,new_slug=None):
    slug=slugify(instance.product_name)
    if new_slug is not None:
        slug=new_slug
    qs=Product.objects.filter(slug=slug).order_by('-id')
    exists=qs.exists()
    if exists:
        new_slug="%s-%s"%(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=create_slug(instance)
pre_save.connect(pre_save_post_receiver,Product)
    
class Product_image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image_url=models.CharField(max_length=200)


class Additional_infomation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    specification=models.CharField(max_length=100)
    detail=models.CharField(max_length=100)


    