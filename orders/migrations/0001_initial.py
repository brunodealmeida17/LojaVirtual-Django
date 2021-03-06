# Generated by Django 4.0.5 on 2022-06-18 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('Status', models.CharField(choices=[('1', 'Aprovado'), ('2', 'Criado'), ('3', 'Reprovado'), ('4', 'Pendente'), ('5', 'Enviado'), ('6', 'Estornado'), ('7', 'Finalizado')], default='V', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderstem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('product', models.CharField(max_length=255, verbose_name='Produto')),
                ('product_id', models.PositiveIntegerField(verbose_name='Id do produto')),
                ('variation', models.CharField(max_length=255, verbose_name='Variação do pedido')),
                ('variation_id', models.PositiveIntegerField(verbose_name='Id da variação')),
                ('price', models.FloatField(verbose_name='Preco do Produto')),
                ('promotion', models.FloatField(default=0, verbose_name='Preço promocional')),
                ('quantidade', models.PositiveIntegerField(verbose_name='quantidades')),
                ('image', models.CharField(max_length=2000)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': 'Item do pedido',
                'verbose_name_plural': 'Itens dos pedidos',
            },
        ),
    ]
