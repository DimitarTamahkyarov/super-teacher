# Generated by Django 5.1.2 on 2024-11-11 21:25

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=300)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('date_time_of_publication', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('to_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacherprofile')),
            ],
            options={
                'ordering': ['-date_time_of_publication'],
                'indexes': [models.Index(fields=['date_time_of_publication'], name='common_comm_date_ti_d3f02d_idx')],
            },
        ),
    ]
