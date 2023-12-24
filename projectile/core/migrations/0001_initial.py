# Generated by Django 5.0 on 2023-12-24 15:44

import autoslug.fields
import core.utils
import django.db.models.deletion
import uuid
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone_number', models.CharField(db_index=True, max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, db_index=True, max_length=255, null=True, unique=True)),
                ('nid', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(blank=True, db_index=True, max_length=255)),
                ('last_name', models.CharField(blank=True, db_index=True, max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='first_name', unique=True)),
                ('gender', models.CharField(blank=True, choices=[('FEMALE', 'Female'), ('MALE', 'Male'), ('UNKNOWN', 'Unknown'), ('OTHER', 'Other')], default='UNKNOWN', max_length=20)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, upload_to=core.utils.get_user_media_path_prefix, verbose_name='Profile_image')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('kind', models.CharField(choices=[('ADMIN', 'Admin'), ('ORGANIZATION_STAFF', 'Organization Staff'), ('ORGANIZATION_ADMIN', 'Organization Admin'), ('SUPER_ADMIN', 'Super Admin'), ('UNDEFINED', 'Undefined')], default='UNDEFINED', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'System User',
                'verbose_name_plural': 'System Users',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('country', models.CharField(db_index=True, max_length=200)),
                ('kind', models.CharField(choices=[('OTHER', 'Other'), ('EDUCATION', 'Education'), ('SOFTWARE_DEVELOPMENT', 'Software Development')], default='OTHER', max_length=64)),
                ('logo', versatileimagefield.fields.VersatileImageField(blank=True, upload_to='logos', verbose_name='logo_image')),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organization_users', to='core.organization'),
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('otp', models.CharField(max_length=6)),
                ('type', models.CharField(choices=[('PASSWORD_RESET', 'Password Reset'), ('PHONE_NUMBER_RESET', 'Phone Number Reset'), ('OTHER', 'Other')], default='OTHER', max_length=30)),
                ('is_used', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_otps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'OTP',
            },
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('DRAFT', 'DRAFT'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], db_index=True, default='ACTIVE', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('phone', models.CharField(db_index=True, max_length=24)),
                ('reset_status', models.CharField(choices=[('FAILED', 'Failed'), ('SUCCESS', 'Success'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('type', models.CharField(choices=[('SELF', 'Self'), ('MANUAL', 'Manual')], default='SELF', max_length=20)),
                ('entry_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('otp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='password_reset_otps', to='core.otp')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='password_reset_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PasswordReset',
            },
        ),
    ]
