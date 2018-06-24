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
    birthDate = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    password = models.CharField(
        'Пароль',
        null=False,
        max_length=500
    )
    regDate = models.DateField(
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

    def __str__(self):
        return self.email


class Architecture(models.Model):
    arch_id = models.IntegerField(
        primary_key=True,
    )
    description = models.CharField(
        'Описание особенностей архитектуры',
        max_length=200,
    )

    def __str__(self):
        return self.description


class Requirements(models.Model):
    req_id = models.CharField(
        max_length=5,
    )
    require = models.CharField(
        'Название требования с СрЗИ из приказа ФСТЭК 21',
        max_length=5,
    )
    description = models.CharField(
        'Описание требования к СрЗИ',
        max_length=500,
        null=False,
    )
    defensible = models.BooleanField(
        'Закрывается ли программными методами',
        default=True,
    )

    pdn_lvl = models.IntegerField(
    )

    def __str__(self):
        return self.description


class Arch_reqs(models.Model):
    id_arcreq = models.IntegerField(
        primary_key=True,
    )
    arch_id = models.ForeignKey(
        Architecture,
        on_delete=models.CASCADE,
    )
    id = models.ForeignKey(
        Requirements,
        on_delete=models.CASCADE,
    )


class Defence(models.Model):
    def_id = models.IntegerField(
        primary_key=True,
    )
    def_name = models.CharField(
        'Название СрЗИ',
        max_length=100,
        null=False,
    )
    def_dev = models.CharField(
        'Разработчик СрЗИ',
        max_length=40,
        null=False,
    )
    def_cert = models.DateField(
        'Дата истечения сертификата ФСТЭК',
        null=False,
    )
    def_desc = models.CharField(
        'Описание СрЗИ',
        max_length=500,
        null=False,
    )
    def_os = models.CharField(
        'Флаг типа ОС',
        max_length=1,
        null=False,
    )
    requirements = models.ManyToManyField(
        Requirements,
    )

    def __str__(self):
        return self.def_name


class Def_type(models.Model):
    type_id = models.IntegerField(
        primary_key=True,
    )
    description = models.CharField(
        'Описание типа затрат',
        default=False,
        max_length=50,
        null=False,
    )

    def __str__(self):
        return self.description


class Def_price(models.Model):
    price_id = models.IntegerField(
        primary_key=True,
    )
    type_id = models.ForeignKey(
        Def_type,
        on_delete=models.CASCADE,
    )
    def_id = models.ForeignKey(
        Defence,
        on_delete=models.CASCADE,
    )


class Def_cost(models.Model):
    cost_id = models.IntegerField(
        primary_key=True,
    )
    price_id = models.ForeignKey(
        Def_price,
        on_delete=models.CASCADE,
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
    )


class User_price(models.Model):
    user_id = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
    )
    cost_id = models.ForeignKey(
        Def_cost,
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        null=False,

    )