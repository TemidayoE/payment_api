from django.db import models

# Create your models here.
class Transaction(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  email = models.EmailField()
  amount = models.PositiveIntegerField()
  reference = models.CharField(max_length= 100, unique= True)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20, default='success')
  
  def __str__(self):
      return self.reference
  