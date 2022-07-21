# Generated by Django 3.2 on 2022-07-21 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=150, null=True)),
                ('sort_name', models.CharField(blank=True, max_length=150, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_name'],
            },
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('friendly_name', models.CharField(blank=True, max_length=150, null=True)),
                ('sort_name', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['sort_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13)),
                ('title', models.CharField(max_length=256)),
                ('sort_title', models.CharField(max_length=256)),
                ('year', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('rating_count', models.PositiveIntegerField()),
                ('plot', models.TextField()),
                ('description', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books_app.author')),
            ],
            options={
                'ordering': ['sort_title'],
            },
        ),
        migrations.CreateModel(
            name='AwardDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_year', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=256)),
                ('award', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books_app.award')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books_app.book')),
            ],
            options={
                'ordering': ['award_year'],
            },
        ),
        migrations.AddField(
            model_name='award',
            name='books',
            field=models.ManyToManyField(blank=True, through='books_app.AwardDetails', to='books_app.Book'),
        ),
    ]
