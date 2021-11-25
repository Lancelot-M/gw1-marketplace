# Generated by Django 3.2.9 on 2021-11-25 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('total_unit', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('money_used', models.CharField(max_length=100)),
                ('seller', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.category')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.group')),
            ],
            options={
                'ordering': ['item', 'total_unit', 'total_price'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='group_parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.group'),
        ),
    ]
