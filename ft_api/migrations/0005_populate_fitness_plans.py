from django.db import migrations, models


def create_fitness_plan_types(apps, schema_editor):
    FitnessPlanType = apps.get_model('ft_api', 'FitnessPlanType')

    types = [
        {'name': 'light', 'description': 'Lose a quarter lb per week', 'pounds_per_week': 0.25},
        {'name': 'normal', 'description': 'Lose a half lb per week', 'pounds_per_week': 0.50},
        {'name': 'hard', 'description': 'Lose 1 lb per week', 'pounds_per_week': 1.00},
        {'name': 'Insane', 'description': 'Lose 2 lbs per week', 'pounds_per_week': 2.00}
    ]
    for fp_type in types:
        fpt = FitnessPlanType(**fp_type)
        fpt.save()


class Migration(migrations.Migration):
    dependencies = [
        ('ft_api', '0004_populate_exercise_types')
    ]

    operations = [
        migrations.RunPython(create_fitness_plan_types, reverse_code=migrations.RunPython.noop),
    ]

