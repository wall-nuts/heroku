from django.contrib import admin

# Register your models here.
from django.contrib import admin
from first.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    fields = ('title','authors','publisher','publication_date')
    filter_horizontal = ('authors',)
    # raw_id_fields = ('publisher',)
    #数据太多的时候（几千条）下拉框会加载每个publisher，时间会比较久，使用这条换成文本框。

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
