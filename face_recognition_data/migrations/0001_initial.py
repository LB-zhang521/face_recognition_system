# Generated by Django 2.2.1 on 2021-01-24 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('user_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='用户编号')),
                ('user_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('entry_time', models.DateTimeField(auto_now_add=True, verbose_name='录入时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('photo', models.ImageField(upload_to='photo/', verbose_name='用户照片')),
            ],
            options={
                'verbose_name': '录入用户列表',
                'verbose_name_plural': '录入用户列表',
            },
        ),
        migrations.CreateModel(
            name='FaceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_data', models.TextField(blank=None, verbose_name='用户人脸数据')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_recognition_data.UserList', verbose_name='用户编号')),
            ],
            options={
                'verbose_name': '用户人脸数据',
                'verbose_name_plural': '用户人脸数据',
            },
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_time', models.DateTimeField(auto_now_add=True, verbose_name='签到时间')),
                ('attendance_img', models.ImageField(upload_to='upload/', verbose_name='用户签到照片')),
                ('attendance_statu', models.BooleanField(default=False, verbose_name='签到状态')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_recognition_data.UserList', verbose_name='签到用户编号')),
            ],
            options={
                'verbose_name': '用户签到记录',
                'verbose_name_plural': '用户签到记录',
            },
        ),
    ]
