# Generated by Django 3.2.9 on 2022-02-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220220_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credit_charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardnumber', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('cv2', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='categorie',
            name='baskets',
            field=models.ManyToManyField(blank=True, null=True, to='core.Basket'),
        ),
        migrations.AlterField(
            model_name='content',
            name='baskets',
            field=models.ManyToManyField(blank=True, null=True, to='core.Basket'),
        ),
    ]
