from peewee import *

db = SqliteDatabase('data.sqlite')


class BaseModel(Model):
    id = PrimaryKeyField(unque=True)


    class Meta:
        database = db
        order_by = 'id'


class Promotion_and_discount(BaseModel):
    product_name = TextField()
    old_price = FloatField()
    new_price = FloatField()

    class Meta:
        db_table = 'Promotions_and_discounts'


class Post(BaseModel):
    post_name = TextField()
    Number_of_people_in_the_current_position = FloatField()


    class Meta:
        db_table = 'Posts'



class Clients(BaseModel):
    last_name = TextField()
    first_name = TextField()
    third_name = TextField()
    date_of_birth = TextField()
    regular_client = BooleanField()
    phone = TextField()
    mail = TextField()


    class Meta:
        db_table = 'Posts'


class Menu(BaseModel):
    pass


class Suppliers(BaseModel):
    pass


class Furniture_registry(BaseModel):
    pass


class Equipment_registry(BaseModel):
    pass


class Advertisement(BaseModel):
    pass


class Estimate(BaseModel):
    pass


class Staff(BaseModel):
    pass


class Trade_turnover(BaseModel):
    pass


class Branch(BaseModel):
    pass


