from django.contrib import admin
from .models import Users
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    def description1(self,objcd ):
        return ' This is our name '
    def description2(self,objcd ):
        return ' This is our pwd '
    list_display = ('name','password','description1','description2')
    search_fields = ('name','id')
admin.site.register(Users,UsersAdmin)
