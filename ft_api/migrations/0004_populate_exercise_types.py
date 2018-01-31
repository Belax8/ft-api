from django.db import migrations, models


def create_exercise_types(apps, schema_editor):
    ExerciseType = apps.get_model('ft_api', 'ExerciseType')

    types = [
        {'name': 'Jogging', 'description': 'Going on a jogging', 'multiplier': 0.40},
        {'name': 'Walking', 'description': 'Going on a walking', 'multiplier': 0.05},
        {'name': 'Swimming', 'description': 'Going swimming', 'multiplier': 0.60},
        {'name': 'Basketball', 'description': 'Playing basketball', 'multiplier': 0.70},
        {'name': 'Soccer', 'description': 'Playing soccer', 'multiplier': 0.70},
        {'name': 'Football', 'description': 'Playing football', 'multiplier': 0.85},
        {'name': 'Lacrosse', 'description': 'Playing lacrosse', 'multiplier': 0.95},
        {'name': 'Frisbee', 'description': 'Playing frisbee', 'multiplier': 0.60},
        {'name': 'Golf', 'description': 'Playing golf', 'multiplier': 0.05}
    ]
    for ex_type in types:
        et = ExerciseType(**ex_type)
        et.save()


class Migration(migrations.Migration):
    dependencies = [
        ('ft_api', '0003_auto_20180126_0507')
    ]

    operations = [
        migrations.RunPython(create_exercise_types, reverse_code=migrations.RunPython.noop),
    ]
