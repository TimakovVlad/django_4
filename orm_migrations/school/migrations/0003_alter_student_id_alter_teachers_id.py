# Generated by Django 5.0.4 on 2024-04-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teachers_remove_student_teacher_alter_student_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]