# Generated by Django 4.1.2 on 2023-04-05 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maison', '0007_alter_house_options_alter_meubles_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['-date_added']},
        ),
        migrations.AlterModelOptions(
            name='meubles',
            options={'ordering': ['-date_added']},
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_Nom_proprio',
            new_name='Nom_proprio',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_date_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_quartier',
            new_name='quartier',
        ),
        migrations.RenameField(
            model_name='house',
            old_name='h_ville',
            new_name='ville',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_Nom_entreprise',
            new_name='Nom_entreprise',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_date_added',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_quartier',
            new_name='quartier',
        ),
        migrations.RenameField(
            model_name='meubles',
            old_name='m_ville',
            new_name='ville',
        ),
        migrations.RemoveField(
            model_name='house',
            name='h_category',
        ),
        migrations.AddField(
            model_name='house',
            name='category',
            field=models.CharField(choices=[('M', 'Maison'), ('A', 'Studio'), ('S', 'Studio'), ('C', 'Chambre')], default='maison', max_length=30),
        ),
        migrations.AddField(
            model_name='house',
            name='tel_proprio',
            field=models.IntegerField(default='698575401'),
        ),
        migrations.AddField(
            model_name='meubles',
            name='tel_entreprise',
            field=models.IntegerField(default='698575401'),
        ),
    ]
