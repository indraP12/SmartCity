from django.contrib import admin
from .models import User,Area,Category,Complain,ProductImage

# Register your models here.
admin.site.register(User)
admin.site.register(Area)
admin.site.register(Category)
admin.site.register(Complain)
admin.site.register(ProductImage)