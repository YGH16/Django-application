# Generated by Django 4.0 on 2022-02-01 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0011_alter_quarterlyreport_name_alter_quarterlyreport_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_name', models.CharField(max_length=80, null=True)),
                ('pdf', models.FileField(null=True, upload_to='client-agreements/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
