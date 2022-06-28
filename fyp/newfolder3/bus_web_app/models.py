from pickle import TRUE
from django.db import models


class Assigntrip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    route = models.ForeignKey('Routes', models.DO_NOTHING)
    bus = models.ForeignKey('Buses', models.DO_NOTHING)
    driversname = models.CharField(max_length=250)
    travel_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'assigntrip'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookingtickets(models.Model):
    fullname = models.CharField(max_length=250)
    froms = models.CharField(max_length=200)
    destinations = models.CharField(max_length=100)
    via = models.CharField(max_length=100)
    ticket_no = models.IntegerField()
    price = models.IntegerField()
    busname = models.CharField(max_length=100)
    busnumber = models.CharField(max_length=100)
    travel_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bookingtickets'


class Buses(models.Model):
    bus_id = models.AutoField(primary_key=True)
    busname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    busnumber = models.TextField()
    busclass = models.CharField(max_length=250)
    insuranceno = models.TextField()
    logo = models.TextField()
    booked_seats = models.ManyToManyField('Seat', blank=TRUE)

    class Meta:
        managed = True
        db_table = 'buses'


class BusesPrice(models.Model):
    id = models.BigAutoField(primary_key=True)
    buses = models.ForeignKey(Buses, models.DO_NOTHING)
    bookingtickets_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'buses_price'
        unique_together = (('buses', 'bookingtickets_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driversname = models.CharField(max_length=250)
    nida = models.TextField()
    licenseno = models.CharField(max_length=50)
    levels = models.CharField(max_length=10)
    phone = models.IntegerField()
    email = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'drivers'


class Notifications(models.Model):
    name = models.TextField()
    type = models.TextField()
    message = models.TextField()
    status = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'notifications'


class Feedback(models.Model):
    name = models.TextField()
    email = models.CharField(unique=True, max_length=250)
    message = models.TextField()
    class Meta:
        managed = False
        db_table = 'feedback'


class Operators(models.Model):
    fullname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    user_type = models.CharField(max_length=250)
    email = models.CharField(unique=True, max_length=250)
    logo = models.TextField()
    officelocation = models.TextField()
    phone = models.IntegerField()
    workingtime = models.TimeField()
    passwords = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'operators'


class Routes(models.Model):
    route_id = models.AutoField(primary_key=True)
    via = models.CharField(max_length=250)
    froms = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'routes'


class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    seat_no = models.IntegerField()
    occupant_first_name = models.CharField(max_length=255)
    occupant_second_name = models.CharField(max_length=255)
    occupant_email = models.CharField(max_length=255)
    purchase_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'seat'

