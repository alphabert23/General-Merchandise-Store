# Generated by Django 3.1.1 on 2020-10-01 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('middle_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('street', models.CharField(default='', max_length=50)),
                ('brgy', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('province', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('zip_code', models.IntegerField(default=0)),
                ('birthdate', models.DateField()),
                ('status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widow/er'), ('D', 'Divorced')], default='S', max_length=1)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('spouse_name', models.CharField(default='', max_length=50)),
                ('spouse_occupation', models.CharField(default='', max_length=50)),
                ('no_of_children', models.IntegerField()),
                ('mother_name', models.CharField(default='', max_length=50)),
                ('mother_occupation', models.CharField(default='', max_length=50)),
                ('father_name', models.CharField(default='', max_length=50)),
                ('father_occupation', models.CharField(default='', max_length=50)),
                ('height', models.FloatField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('religion', models.CharField(default='', max_length=50)),
                ('elementary_school', models.CharField(default='', max_length=50)),
                ('elementary_grade', models.FloatField(default=1)),
                ('elementary_year_completed', models.IntegerField(default=0)),
                ('elementary_awards', models.TextField(default='')),
                ('junioir_high_school', models.CharField(default='', max_length=50)),
                ('junior_high_grade', models.FloatField(default=1)),
                ('junior_high_year_completed', models.IntegerField(default=0)),
                ('junior_high_awards', models.TextField(default='')),
                ('senior_high_school', models.CharField(default='', max_length=50)),
                ('senior_high_grade', models.FloatField(default=1)),
                ('senior_high_year_completed', models.IntegerField(default=0)),
                ('senior_high_awards', models.TextField(default='')),
                ('college_school', models.CharField(default='', max_length=50)),
                ('college_course', models.CharField(default='', max_length=50)),
                ('college_level', models.IntegerField(default=0)),
                ('college_year_completed', models.IntegerField(default=0)),
                ('college_awards', models.TextField(default='')),
                ('post_graduate_school', models.CharField(default='', max_length=50)),
                ('post_graduate_course', models.CharField(default='', max_length=50)),
                ('post_graduate_level', models.IntegerField(default=0)),
                ('post_graduate_year_completed', models.IntegerField(default=0)),
                ('post_graduate_awards', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_registered', models.DateField(auto_now_add=True)),
                ('category', models.CharField(max_length=30)),
                ('pname', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('image1', models.ImageField(upload_to='')),
                ('image2', models.ImageField(upload_to='')),
                ('image3', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.person')),
                ('picture', models.ImageField(upload_to='')),
                ('date_registered', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=('pages.person',),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('sponsor', models.CharField(default='', max_length=50)),
                ('date', models.DateField()),
                ('venue', models.CharField(default='', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.customer')),
            ],
            options={
                'verbose_name': 'Training',
                'verbose_name_plural': 'Trainings',
            },
        ),
    ]