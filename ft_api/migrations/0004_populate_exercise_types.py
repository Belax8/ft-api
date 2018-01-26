from django.db import migrations, models


def create_exercise_types(apps, schema_editor):
    ExerciseType = apps.get_model('ft_api', 'ExerciseType')

    types = [
        {'name': 'jogging', 'description': 'jogging', 'multiplier': 0.40},
        {'name': 'walking', 'description': 'walking', 'multiplier': 0.05},
        {'name': 'swimming', 'description': 'swimming', 'multiplier': 0.60},
        {'name': 'basketball', 'description': 'basketball', 'multiplier': 0.70},
        {'name': 'soccer', 'description': 'soccer', 'multiplier': 0.70},
        {'name': 'football', 'description': 'football', 'multiplier': 0.85},
        {'name': 'lacrosse', 'description': 'lacrosse', 'multiplier': 0.95},
        {'name': 'frisbee', 'description': 'frisbee', 'multiplier': 0.60},
        {'name': 'golf', 'description': 'golf', 'multiplier': 0.05}
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
