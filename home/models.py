from django.db import models
import os
class Userdetails(models.Model):
    user_id = models.IntegerField(unique=True)
    phone = models.IntegerField(unique=True,default=0)
    designation = models.CharField(max_length=150)
    organization = models.CharField(max_length=250)
    type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    
class Productsdetails(models.Model):
    users_id = models.CharField(max_length=300)
    product_name = models.CharField(max_length=250,unique=True)
    organization_name = models.CharField(max_length=250)
    vendors_name = models.CharField(max_length=1000)
    p_type = models.CharField(max_length=50)
    issue_date = models.DateField()

class Productstatus(models.Model):
    product_id = models.IntegerField(unique=True)
    status = models.CharField(max_length=50)
    update_user = models.CharField(max_length=250)
    update_date = models.DateField()

class Notice(models.Model):
    notice_name = models.CharField(max_length=500)
    upload_date = models.DateField()
    file = models.FileField()
    def filename(self):
        return os.path.basename(self.file.name)