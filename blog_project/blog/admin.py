from django.contrib import admin
from blog.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','body','publish','create','update','status']
    prepopulated_fields = {'slug':('title',)}
    list_filter = ['status',"create","publish","author"]
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']

admin.site.register(Post,PostAdmin)
