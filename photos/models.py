from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class photo(models.Model):
    category_name=models.ForeignKey(category,on_delete=models.SET_NULL,null=True)
    description=models.TextField()
    image=models.ImageField()

    



