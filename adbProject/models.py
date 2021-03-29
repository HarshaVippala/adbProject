from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comment(models.Model):
    comment_no = models.BigIntegerField(primary_key=True)
    comment_date = models.DateTimeField()
    comment_content = models.CharField(max_length=1024)
    rating = models.IntegerField()
    customer_cust = models.ForeignKey('Customer', models.DO_NOTHING)
    store_store = models.ForeignKey('Store', models.DO_NOTHING)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'comment'


class Commodity(models.Model):
    comm_no = models.BigIntegerField(primary_key=True)
    comm_name = models.CharField(max_length=255)
    comm_price = models.DecimalField(max_digits=10, decimal_places=2)
    comm_discount = models.SmallIntegerField()
    comm_img = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()
    store_store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'commodity'


class Coupon(models.Model):
    coupon_no = models.CharField(primary_key=True, max_length=30)
    discount = models.SmallIntegerField()
    start_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    tbl_last_date = models.DateTimeField()
    store_store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'coupon'


class CouponRecord(models.Model):
    coupon_status = models.FloatField()
    acquired_time = models.DateTimeField()
    used_time = models.DateTimeField(blank=True, null=True)
    customer_cust = models.OneToOneField('Customer', models.DO_NOTHING, primary_key=True)
    tbl_last_date = models.DateTimeField()
    coupon_coupon_no = models.ForeignKey(Coupon, models.DO_NOTHING, db_column='coupon_coupon_no')

    class Meta:
        managed = False
        db_table = 'coupon_record'
        unique_together = (('customer_cust', 'coupon_coupon_no'),)


class CreditCard(models.Model):
    card_no = models.DecimalField(primary_key=True, max_digits=30, decimal_places=0)
    chosen_status = models.TextField()
    expire_date = models.SmallIntegerField()
    cvv = models.SmallIntegerField()
    customer_cust = models.ForeignKey('Customer', models.DO_NOTHING)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'credit_card'


class Customer(models.Model):
    cust_id = models.BigIntegerField(primary_key=True)
    cust_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAddress(models.Model):
    address_id = models.BigIntegerField(primary_key=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    tbl_last_date = models.DateTimeField()
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'customer_address'


class Deliveryman(models.Model):
    deli_id = models.BigIntegerField(primary_key=True)
    deli_type = models.CharField(max_length=23)
    deli_phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'deliveryman'


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


class Employee(models.Model):
    emp_no = models.BigIntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_role = models.CharField(max_length=30)
    password = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeDeliveryman(models.Model):
    deliveryman_deli = models.OneToOneField(Deliveryman, models.DO_NOTHING, primary_key=True)
    employee_emp_no = models.OneToOneField(Employee, models.DO_NOTHING, db_column='employee_emp_no')
    pay_rate = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'employee_deliveryman'


class Invoice(models.Model):
    order_order_no = models.BigIntegerField(unique=True)
    order_price = models.DecimalField(max_digits=30, decimal_places=0)
    time_generated = models.DateTimeField()
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING)
    invoice_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class Order(models.Model):
    order_no = models.BigIntegerField(primary_key=True)
    order_status = models.IntegerField()
    placed_time = models.DateTimeField()
    est_pick_up_time = models.DateTimeField(blank=True, null=True)
    pick_up_time = models.DateTimeField(blank=True, null=True)
    est_deliveried_time = models.DateTimeField(blank=True, null=True)
    deliveried_time = models.DateTimeField(blank=True, null=True)
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)
    store_store = models.ForeignKey('Store', models.DO_NOTHING)
    customer_address_address = models.OneToOneField(CustomerAddress, models.DO_NOTHING)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.DateTimeField(blank=True, null=True)
    tbl_last_date = models.DateTimeField()
    credit_card_card_no = models.ForeignKey(CreditCard, models.DO_NOTHING, db_column='credit_card_card_no')
    invoice_invoice_id = models.FloatField(unique=True)

    class Meta:
        managed = False
        db_table = 'order'


class OrderCommTransaction(models.Model):
    amount = models.SmallIntegerField()
    commodity_comm_no = models.OneToOneField(Commodity, models.DO_NOTHING, db_column='commodity_comm_no', primary_key=True)
    order_order_no = models.ForeignKey(Order, models.DO_NOTHING, db_column='order_order_no')
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_comm_transaction'
        unique_together = (('commodity_comm_no', 'order_order_no'),)


class OutsourcingCompany(models.Model):
    outsource_company_id = models.BigIntegerField(primary_key=True)
    outsource_company_name = models.CharField(max_length=100)
    outsource_company_email = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'outsourcing_company'


class OutsourcingDeliveryman(models.Model):
    deliveryman_deli = models.OneToOneField(Deliveryman, models.DO_NOTHING, primary_key=True)
    outsource_emp_id = models.BigIntegerField()
    outsourcing_company_outsource_company = models.ForeignKey(OutsourcingCompany, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'outsourcing_deliveryman'


class Payment(models.Model):
    payment_type = models.CharField(max_length=1)
    payment_ts = models.DateTimeField()
    invoice_invoice = models.ForeignKey(Invoice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment'


class Store(models.Model):
    store_id = models.BigIntegerField(primary_key=True)
    store_name = models.CharField(max_length=255)
    store_type = models.CharField(max_length=1)
    store_phone = models.CharField(max_length=30)
    store_contact_person = models.CharField(max_length=30)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    tbl_last_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'


class StoreDeliveryman(models.Model):
    deliveryman_deli = models.OneToOneField(Deliveryman, models.DO_NOTHING, primary_key=True)
    store_emp_no = models.FloatField()
    store_store = models.ForeignKey(Store, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store_deliveryman'