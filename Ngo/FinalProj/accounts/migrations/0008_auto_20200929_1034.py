# Generated by Django 3.1.1 on 2020-09-29 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20200927_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='NgoRequirementDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='donationdetail',
            name='requirement',
        ),
        migrations.AddField(
            model_name='donationdetail',
            name='req',
            field=models.CharField(default='not filled', max_length=100),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='founder',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Requirement',
        ),
        migrations.AddField(
            model_name='ngorequirementdetail',
            name='ngo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ngo'),
        ),
    ]