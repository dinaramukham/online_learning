# Generated by Django 4.2.7 on 2024-04-04 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='media/photo/')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='media/photo/')),
                ('content', models.TextField()),
                ('link_video', models.TextField()),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.courses')),
            ],
        ),
    ]
