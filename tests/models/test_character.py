from django.test import TestCase
from dungeon_masters_familiar.models import Character


class CharacterTests(TestCase):
    def test_saves_attributes_needed_by_dnd_5e(self):
        character = Character.objects.create(
            level=1,
            strength=8,
            dexterity=14,
            constitution=10,
            intelligence=18,
            wisdom=16,
            charisma=11,
            saving_throws=['Intelligence', 'Wisdom'],
            skills={'Perception': 10},
            speed=20,
            size='M',
            eyes='black',
            skin='gold',
            hair='green',
            age=10000,
            name='Zargothrax',
            alignment='LE',
            traits=['vane'],
            background=(
                'An ancient wizard of powerful evil, Zargothrax will not rest until he '
                'has claimed the peaceful city of Dundee.'
            ),
            hit_die='d6',
            hit_dice=1,
            hit_points=6,
            proficiencies=[
                'daggers',
                'darts',
                'slings',
                'quarterstaffs',
                'light crossbows',
            ],
            equipment=['robe', 'quarterstaff'],
            feats=[],
            cantrips=['Detect Magic'],
            spells_known={0: 1},
            spells_prepared=['Detect Magic'],
            spell_slots={0: 4},
            spellcasting_ability='Intelligence',
            spell_attack_bonus=4,
            spell_save_dc=14,
        )
        created_characters = Character.objects.all()
        self.assertEqual(len(created_characters), 1)
        self.assertEqual(created_characters[0].name, character.name)
