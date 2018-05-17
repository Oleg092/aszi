from django.db import models

class Users(models.Model):
    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    firstname = models.CharField(
        'Фамилия',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        'Имя',
        max_length=40,
        null=True,
        blank=True
    )
    middlename = models.CharField(
        'Отчество',
        max_length=40,
        null=True,
        blank=True
    )
    birdDate = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    password = models.CharField(###кароч для шифрования этого говна напишем спец класс. и перед тем как заливать в базу пароль шифруем его
        'Пароль',###а при авторизации для проверки дешифруем. И норм
        null=False,
        max_length=30
    )
    register_date = models.DateField(
        'Дата регистрации',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Активен',
        default=True
    )
    is_admin = models.BooleanField(
        'Суперпользователь',
        default=False
    )

