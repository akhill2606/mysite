# Generated by Django 3.1 on 2020-10-06 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20201006_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='site',
            name='area_hectare',
        ),
        migrations.RemoveField(
            model_name='site',
            name='state',
        ),
        migrations.AddField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.category'),
        ),
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='iso',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.iso'),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.region'),
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='site',
            name='states',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.states'),
        ),
    ]
