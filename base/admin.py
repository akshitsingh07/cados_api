from django.contrib import admin
from base.models import Advocate, Company

# Register models here to access on superuser/admin panel for easy access.
class Advocate_Admin(admin.ModelAdmin):
    list_display = ('username',)

class Company_Admin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Advocate, Advocate_Admin)
admin.site.register(Company, Company_Admin)