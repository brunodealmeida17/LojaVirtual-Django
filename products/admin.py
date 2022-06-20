from django.contrib import admin

from . import models

admin.site.site_header = 'your_header'
admin.site.site_title = 'site_title'
admin.site.index_title = 'Painel administrative da loja'



class Meta:
    verbose_name="Produto"
    verbose_name_plural="Produtos"

class VariationInline(admin.TabularInline):
    model = models.Variation   
    extra = 1
    
class ImageInline(admin.TabularInline):
    model = models.Images
    extra = 2
   
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationInline, ImageInline]
    
  



admin.site.register(models.Category, verbose_name="Categoria")
admin.site.register(models.Product, ProductAdmin, verbose_name="Produtos")
admin.site.register(models.Variation)
admin.site.register(models.Images)