# Generated by Django 3.2.5 on 2021-08-23 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20210823_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.course'),
        ),
        migrations.AlterField(
            model_name='question',
            name='marks',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
