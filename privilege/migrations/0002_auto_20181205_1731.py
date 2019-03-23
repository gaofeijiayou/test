# Generated by Django 2.1.2 on 2018-12-05 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('privilege', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterModelOptions(
            name='privilege',
            options={'verbose_name': '权限管理', 'verbose_name_plural': '权限管理'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '角色管理', 'verbose_name_plural': '角色管理'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户管理', 'verbose_name_plural': '用户管理'},
        ),
        migrations.AddField(
            model_name='privilege',
            name='action',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privilege',
            name='rolegroup',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='privilege.RoleGroup'),
            preserve_default=False,
        ),
    ]