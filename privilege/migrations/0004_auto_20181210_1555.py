# Generated by Django 2.1.2 on 2018-12-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privilege', '0003_auto_20181205_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='privilege',
            old_name='group',
            new_name='rolegroup',
        ),
        migrations.RemoveField(
            model_name='privilege',
            name='role',
        ),
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.AddField(
            model_name='role',
            name='role',
            field=models.ManyToManyField(to='privilege.Privilege'),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ManyToManyField(to='privilege.Role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, verbose_name='用户密码'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
    ]