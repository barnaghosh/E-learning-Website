# Generated by Django 3.2.5 on 2021-08-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20210826_0040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AddField(
            model_name='course',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
