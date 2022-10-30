from tabnanny import verbose
from django.db import models

class House(models.Model):
    
    """Model Definition for Houses"""
    
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    # price_per_night = models.PositiveIntegerField(
    #     verbose_name="price", help_text="Positive Numbers Only",
    # )
    
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        #varbose_name="Pets Allowed?",
        default=True, 
        help_text="Does this house allow pets?",)
    
    #데이터를 남기고 싶을때 on_delete=models.SET_NULL 사용
    # owner = models.ForeignKey("users.User", on_delete=models.SET_NULL)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


