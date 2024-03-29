# Generated by Django 2.1.9 on 2019-06-17 02:22

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=63, populate_from=['title'])),
                ('text', models.TextField()),
                ('pub_date', models.DateField()),
                ('startups', models.ManyToManyField(to='organizer.Startup')),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'verbose_name': 'blog post',
                'ordering': ['-pub_date', 'title'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
