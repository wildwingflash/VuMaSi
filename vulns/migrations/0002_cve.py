# Generated by Django 2.2.4 on 2020-04-23 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vulns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_id', models.CharField(max_length=30)),
                ('vulnerability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cves', to='vulns.Vulnerability')),
            ],
        ),
    ]
