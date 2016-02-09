from django.contrib import admin
from signup.models import UserProfile, Order



# Register your models here.
class UserProfileInlines(admin.StackedInline):
    model = Order
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
    fields = ['phone']
    inlines = [UserProfileInlines]
    
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Order)