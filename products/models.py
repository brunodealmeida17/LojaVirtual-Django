from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from PIL import Image
import os
from django.conf import settings


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Category(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")

    class Meta:
        ordering = ("name",)
        verbose_name = "Categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:list_by_category", kwargs={"slug": self.slug})


class Product(TimeStampedModel):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE, verbose_name="Categoria"
    )
    name = models.CharField(max_length=255, verbose_name="Nome")
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name")
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True, verbose_name="Imagem da capa")
    description = models.TextField(blank=True)
    information = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    type = models.CharField(
        default = "V",
        max_length = 1,
        choices =(
            ('S', 'VARIAÇÃO'),
            ('N', 'NONE'),
        )
    )
    
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width <= new_width:            
            img_pil.close()
            
        new_height = round((new_width * original_height) / original_width)
        
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        
        
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.image:
            self.resize_image(self.image, max_image_size)
            
    
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        list_by_category = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    class Meta:        
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
class Variation(models.Model):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    preco_promocional = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    estoque = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.nome or self.produto.nome
    
    class Meta:        
        verbose_name = "Variaçao"
        verbose_name_plural = "Variações"

class Images(models.Model):
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    
    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        
        if original_width <= new_width:            
            img_pil.close()
            
        new_height = round((new_width * original_height) / original_width)
        
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        
        
        
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        max_image_size = 800
        
        if self.image:
            self.resize_image(self.image, max_image_size)
            
    def __str__(self):
        return self.produto.name
    
    
    
    class Meta: 
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens do produto"