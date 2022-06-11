from django.db import migrations


def add_data(apps, schema_editor):
    Roles = apps.get_model("core", "Roles")
    db_alias = schema_editor.connection.alias
    Roles.objects.using(db_alias).bulk_create([
        Roles(name=1),
        Roles(name=2)
    ])
    Status = apps.get_model("core", "RequestStatus")
    Status.objects.using(db_alias).bulk_create([
        Status(status=1),
        Status(status=2),
        Status(status=3)
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data, None)
    ]
