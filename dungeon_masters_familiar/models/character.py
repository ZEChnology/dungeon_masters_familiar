from django.db import models
from django.contrib.postgres import fields


class Character(models.Model):
    level = models.IntegerField()

    # Ability Scores
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    saving_throws = fields.ArrayField(models.CharField(max_length=30))

    skills = fields.JSONField()

    # Personal Attributes
    speed = models.IntegerField()
    size = models.CharField(max_length=30)
    eyes = models.CharField(max_length=30)
    skin = models.CharField(max_length=30)
    hair = models.CharField(max_length=30)
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    alignment = models.CharField(max_length=30)
    traits = fields.ArrayField(models.CharField(max_length=30))
    background = models.CharField(max_length=30)

    # Health
    hit_die = models.CharField(max_length=30)
    hit_dice = models.IntegerField()
    hit_points = models.IntegerField()

    proficiencies = fields.ArrayField(models.CharField(max_length=30))
    equipment = fields.ArrayField(models.CharField(max_length=30))
    feats = fields.ArrayField(models.CharField(max_length=30))

    # Magic
    cantrips = fields.ArrayField(models.CharField(max_length=30))
    spells_known = fields.ArrayField(models.CharField(max_length=30))
    spells_prepared = fields.ArrayField(models.CharField(max_length=30))
    spell_slots = fields.JSONField()
    specllcasting_ability = models.CharField(max_length=30)
    spell_attack_bonus = models.IntegerField()
    spell_dc = models.IntegerField()
