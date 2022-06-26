from django.db import models



class Bitcoin(models.Model):
    timestamp = models.DateTimeField(blank=False,null=False)
    price = models.CharField(max_length=50,blank=False,null=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} {self.price} {self.created_at}"