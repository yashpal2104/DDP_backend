# Generated by Django 4.1.7 on 2024-04-03 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ddpui", "0063_permission_role_rolepermission"),
    ]

    operations = [
        migrations.AddField(
            model_name="orguser",
            name="new_role",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="ddpui.role"
            ),
        ),
    ]
