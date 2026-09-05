from django.db import migrations


def populate_result_metrics(apps, schema_editor):
    Result = apps.get_model('results', 'Result')

    for result in Result.objects.all().iterator():
        percentage = (float(result.marks) / float(result.full_marks)) * 100

        if percentage >= 90:
            result.grade = 'A+'
            result.gpa = 4.0
        elif percentage >= 80:
            result.grade = 'A'
            result.gpa = 3.6
        elif percentage >= 70:
            result.grade = 'B+'
            result.gpa = 3.2
        elif percentage >= 60:
            result.grade = 'B'
            result.gpa = 2.8
        elif percentage >= 50:
            result.grade = 'C+'
            result.gpa = 2.4
        elif percentage >= 40:
            result.grade = 'C'
            result.gpa = 2.0
        else:
            result.grade = 'F'
            result.gpa = 0.0

        result.save(update_fields=['grade', 'gpa'])


class Migration(migrations.Migration):
    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_result_metrics, migrations.RunPython.noop),
    ]