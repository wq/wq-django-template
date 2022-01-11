from django.conf import settings{% if with_gis %}
import django.contrib.gis.db.models.fields{% endif %}
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, help_text='The date when the observation was taken', null=True, verbose_name='Date')),{% if with_gis %}
                ('geometry', django.contrib.gis.db.models.fields.PointField(help_text='The location of the observation', srid=4326, verbose_name='Location')),{% endif %}
                ('photo', models.ImageField(blank=True, help_text='Photo of the observation', null=True, upload_to='observations', verbose_name='Photo')),
                ('notes', models.TextField(blank=True, help_text='Field observations and notes', null=True, verbose_name='Notes')),
                ('category', models.ForeignKey(blank=True, help_text='Observation type', null=True, on_delete=django.db.models.deletion.PROTECT, to='{{ project_name }}_survey.category', verbose_name='Category')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='submitted by')),
            ],
            options={
                'verbose_name_plural': 'observations',
                'ordering': ['-date'],
            },
        ),
    ]
