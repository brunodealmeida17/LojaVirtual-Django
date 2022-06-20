from autoslug import AutoSlugField
from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel
from PIL import Image
import os
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    Status = models.CharField(
        default = "V",
        max_length = 1,
        choices =(
            ('1', 'Aprovado'),
            ('2', 'Criado'),
            ('3', 'Reprovado'),
            ('4', 'Pendente'),
            ('5', 'Enviado'),
            ('6', 'Estornado'),
            ('7', 'Finalizado'),
            
        )
    )
    
    def __str__(self):
        return f'Pedido Nº: {self.pk}'
    
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    
class Ordersitem(TimeStampedModel):
    orders = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255, verbose_name="Produto")
    product_id = models.PositiveIntegerField(verbose_name="Id do produto")
    variation = models.CharField(max_length=255, verbose_name="Variação do pedido")
    variation_id = models.PositiveIntegerField(verbose_name="Id da variação")
    price = models.FloatField(verbose_name="Preco do Produto")
    promotion = models.FloatField(default=0, verbose_name="Preço promocional")
    quantidade = models.PositiveIntegerField(verbose_name="quantidades")
    image = models.CharField(max_length=2000)
    
    
    def __str__(self):
        return f'pedido {self.orders}'
    
    
    class Meta:
        verbose_name = "Item do pedido"
        verbose_name_plural = "Itens dos pedidos"
    
        

