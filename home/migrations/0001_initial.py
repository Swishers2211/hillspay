# Generated by Django 4.2.1 on 2023-12-16 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.PositiveSmallIntegerField(default=0)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Карзина',
                'verbose_name_plural': 'Карзины',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Category_Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Категория игр')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория игры',
                'verbose_name_plural': 'Категория игр',
            },
        ),
        migrations.CreateModel(
            name='Category_Сurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('diversity', models.CharField(max_length=15, verbose_name='Единицы валют')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Внутриигровая валюта',
                'verbose_name_plural': 'Внутриигровые валюты',
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=60, verbose_name='Краткое описание')),
                ('price_for_1_piece', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена за 1 шт')),
                ('status', models.SmallIntegerField(choices=[(0, 'Продан'), (1, 'Поддержка'), (2, 'Возврат')], default=0, verbose_name='Статус')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('availability', models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
            },
        ),
        migrations.CreateModel(
            name='Deal_Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_for_1_piece', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена за 1 шт')),
                ('quantity', models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')),
                ('status', models.SmallIntegerField(choices=[(0, 'Продан'), (1, 'Поддержка'), (2, 'Возврат')], default=0, verbose_name='Статус')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('availability', models.PositiveSmallIntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Сделка валюты',
                'verbose_name_plural': 'Сделки валют',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название игры')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание игры')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Фото игры')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='PlatForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Платформа',
                'verbose_name_plural': 'Платформы',
            },
        ),
        migrations.CreateModel(
            name='PlatForm_Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Платформа валюты',
                'verbose_name_plural': 'Платформы валют',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=60, verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Подробное описание')),
                ('price_for_1_piece', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена за 1 шт')),
                ('availability', models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Фото товара')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Product_Сurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_for_1_piece', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена за 1 шт')),
                ('availability', models.PositiveSmallIntegerField(default=1, verbose_name='Наличие')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images', verbose_name='Фото товара')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
            ],
            options={
                'verbose_name': 'Товар - валюта',
                'verbose_name_plural': 'Товары - валюты',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_role', models.CharField(max_length=160, verbose_name='Подзаголовок')),
                ('violation', models.TextField(verbose_name='Нарушение')),
                ('punishment', models.TextField(verbose_name='Наказание')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правила',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название подкатегории')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Дата размещения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Отзыв')),
                ('price_for_1_piece', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена за 1 шт')),
                ('saleman_comment', models.TextField(verbose_name='Ответ продавца')),
                ('status', models.SmallIntegerField(choices=[(0, 'Продан'), (1, 'Поддержка'), (2, 'Возврат')], default=0, verbose_name='Статус')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.game', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
