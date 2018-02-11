# Generated by Django 2.0.2 on 2018-02-11 17:08

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('saving_throws', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('skills', django.contrib.postgres.fields.jsonb.JSONField()),
                ('speed', models.IntegerField()),
                ('size', models.CharField(max_length=30)),
                ('eyes', models.CharField(max_length=30)),
                ('skin', models.CharField(max_length=30)),
                ('hair', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('alignment', models.CharField(max_length=30)),
                ('traits', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('background', models.CharField(max_length=30)),
                ('hit_die', models.CharField(max_length=30)),
                ('hit_dice', models.IntegerField()),
                ('hit_points', models.IntegerField()),
                ('proficiencies', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('equipment', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('feats', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('cantrips', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('spells_known', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('spells_prepared', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('spell_slots', django.contrib.postgres.fields.jsonb.JSONField()),
                ('specllcasting_ability', models.CharField(max_length=30)),
                ('spell_attack_bonus', models.IntegerField()),
                ('spell_dc', models.IntegerField()),
            ],
        ),
    ]
