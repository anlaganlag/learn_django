from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.

class Classification(models.Model):
    list_display = ("title",)
    title = models.CharField(max_length=100,blank=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "v_classification"
    def __str__(self):
        return self.title


class Video(models.Model):
    STATUS_CHOICES = (
        ('0', '发布中'),
        ('1', '未发布'),
    )
    title = models.CharField(max_length=100,blank=True, null=True)
    desc = models.CharField(max_length=255,blank=True, null=True)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE, null=True,blank=True)
    file = models.FileField(max_length=255)
    cover = models.ImageField(upload_to='cover/',blank=True, null=True)
    status = models.CharField(max_length=1 ,choices=STATUS_CHOICES, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, max_length=20)
    def __str__(self):
        return self.title