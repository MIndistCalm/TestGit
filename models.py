from peewee import *

db = SqliteDatabase('data.sqlite')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'



class Promotion_and_discount(BaseModel):
    product_name = TextField()
    old_price = FloatField()
    new_price = FloatField()

    class Meta:
        db_table = 'promotions_and_discounts'


class Post(BaseModel):
    post_name = TextField()
    number_of_people_in_the_current_position = IntegerField()

    class Meta:
        db_table = 'posts'


class Client(BaseModel):
    last_name = TextField()
    first_name = TextField()
    third_name = TextField()
    date_of_birth = TextField()
    regular_client = BooleanField()
    phone = TextField()
    mail = TextField()

    class Meta:
        db_table = 'clients'


class Menu(BaseModel):
    product_name = TextField()
    price = FloatField()
    volume = FloatField()
    composition = TextField()

    class Meta:
        db_table = 'menus'


class Supplier(BaseModel):
    organization_name = TextField()
    product_name = TextField()
    quantity_of_goods = TextField()

    class Meta:
        db_table = 'suppliers'


class Furniture_registry(BaseModel):
    name = TextField()
    color = TextField()
    manufacturer = TextField()

    class Meta:
        db_table = 'furniture_registrys'


class Equipment_registry(BaseModel):
    name = TextField()
    equipment_code = TextField()
    brand = TextField()
    manufacturer = TextField()

    class Meta:
        db_table = 'equipment_registrys'


class Advertisement(BaseModel):
    ad_type = TextField()
    price = TextField()

    class Meta:
        db_table = 'advertisements'


class Estimate(BaseModel):
    product_name = TextField()

    class Meta:
        db_table = 'estimates'


class Staff(BaseModel):
    last_name = TextField()
    first_name = TextField()
    third_name = TextField()
    date_of_birth = TextField()
    address = TextField()
    phone = TextField()
    mail = TextField()
    staff_code = TextField()

    class Meta:
        db_table = 'staffs'


class Trade_turnover(BaseModel):
    costs = FloatField()
    revenue = FloatField()
    profit = FloatField()
    product_code = FloatField()

    class Meta:
        db_table = 'trade_turnovers'


class Branch(BaseModel):
    promotions_and_discounts_code = FloatField()
    customer_code = FloatField()
    menu_code = FloatField()
    supplier_code = FloatField()
    furniture_register_code = FloatField()
    equipment_register_code = FloatField()
    advertising_code = FloatField()
    employee_code = FloatField()
    turnover_code = FloatField()

    class Meta:
        db_table = 'branchs'
