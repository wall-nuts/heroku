from django.contrib import admin
from hello.models import Blog,Record
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','tag','author')

class RecordAdmin(admin.ModelAdmin):
    list_display = ('id','way','strength','date')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Record,RecordAdmin)

