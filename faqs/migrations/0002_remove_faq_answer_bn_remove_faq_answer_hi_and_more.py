# Generated by Django 5.0.6 on 2025-02-02 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='answer_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='answer_hi',
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
    ]
