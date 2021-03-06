# Generated by Django 2.1.5 on 2019-02-24 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquarium_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibits',
            fields=[
                ('exhibitID', models.CharField(db_column='exhibitID', max_length=25, primary_key=True, serialize=False)),
                ('exhibitName', models.CharField(db_column='exhibitName', max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('estimatedGal', models.IntegerField(blank=True, null=True)),
                ('desiredTurnover', models.IntegerField(blank=True, null=True)),
                ('systemFlow', models.IntegerField(blank=True, null=True)),
                ('creationDate', models.DateTimeField(blank=True, db_column='creationDate', null=True)),
                ('updateDate', models.DateTimeField(blank=True, db_column='updateDate', null=True)),
                ('type', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'db_table': 'Exhibits',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectExhibits',
            fields=[
                ('projectid', models.ForeignKey(db_column='projectID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='aquarium_app.Projects')),
                ('newconstruction', models.BooleanField(blank=True, db_column='newConstruction', null=True)),
                ('creationdate', models.DateTimeField(blank=True, db_column='creationDate', null=True)),
                ('updatedate', models.DateTimeField(blank=True, db_column='updateDate', null=True)),
            ],
            options={
                'db_table': 'Project_Exhibits',
                'managed': False,
            },
        ),
    ]
