from django.contrib import admin
from .models import Product




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","create_date", "is_in_stock", "update_date")
    list_editable = ( "is_in_stock",)
    list_display_links = ("create_date", )
    ordering = ("update_date",) 
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"




admin.site.register(Product,ProductAdmin)

admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway meltem" 
admin.site.index_title = "Welcome to Clarusway Meltem Portal"