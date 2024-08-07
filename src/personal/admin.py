from django.contrib import admin
from personal.models import farmermodels

# Register your models here.
@admin.register(farmermodels)
class farmeradmin(admin.ModelAdmin):
	list_display=['name','age','city','livestock','crop','profit_or_loss']


