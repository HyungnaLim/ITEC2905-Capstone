from traceback import print_tb

from peewee import *

db = SqliteDatabase('cats.sqlite')

# create objects & define each field so that peewee can create entities to store data in a table
# peewee will also create auto incrementing integer for id
class Owner(Model):
    name = CharField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.id}: {self.name}'


class Cat(Model):
    name = CharField()
    color = CharField()
    age = IntegerField()
    owner = ForeignKeyField(Owner, backref='cats')  # relationship between tables
    # backref - what is this object(Cat) refer to in the point of view of Owner

    class Meta:
        database = db

    # string method to display information of the object
    def __str__(self):
        return f'{self.id}: {self.name}, {self.color}, {self.age}, Owner {self.owner}'


db.connect()
db.create_tables( [Cat, Owner] )   # square bracket here!

# pragma TABLE_INFO(cat) - sqlite command to inspect the table info


# clear data from table - just for testing
Cat.delete().execute()
Owner.delete().execute()


# create data - make sure to save to insert into the table!
sam = Owner(name='Sam')
sam.save()

kate = Owner(name='Kate')
kate.save()

jenny = Owner(name='Jenny')
jenny.save()

# adding Cat data to the database
zoe = Cat(name='Zoe', color='Ginger', age=3, owner=sam)
zoe.save()

holly = Cat(name='Holly', color='Tabby', age=5, owner=kate)
holly.save()

fluffy = Cat(name='Fluffy', color='Black', age=1, owner=jenny)
fluffy.save()

cats = Cat.select()     # query object, can't access each cat by index
for cat in cats:
    print(cat)

list_of_cats = list(cats)   # regular Python list, can access each object with index
print(list_of_cats)

print(fluffy.owner.name)    # print the name of fluffy's owner

# update data
fluffy.age = 2
fluffy.save()

print('After Fluffy update')
cats = Cat.select()
for cat in cats:
    print(cat)

# update with where clause & return the number of rows modified
rows_modified = Cat.update(age=6).where(Cat.name == 'Holly').execute()

print('After Holly update')
cats = Cat.select()
for cat in cats:
    print(cat)

print(f'{rows_modified} row updated!')

mark = Owner(name='Mark')
mark.save()

# buzz = Cat(name='Buzz', color='Gray', age=3)  - This will cause error cus of no owner
buzz = Cat(name='Buzz', color='Gray', age=3, owner=mark)
buzz.save()

cats_who_are_3 = Cat.select().where(Cat.age == 3)
for cat in cats_who_are_3:
    print(cat, ' is three')

cats_with_l_in_name = Cat.select().where(Cat.name % '*l*')   # star sign is a wild card
for cat in cats_with_l_in_name:
    print(cat, ' has l in name')

# case-insensitive search using .contains()
cats_with_b_in_name = Cat.select().where(Cat.name.contains('b'))
for cat in cats_with_b_in_name:
    print(cat, ' has b in name')

zoe_from_db = Cat.get_or_none(name='Zoe')   # find 1 data from database
print(zoe_from_db)

zoe_from_db = Cat.get_or_none(name='Shadow')
print(zoe_from_db)

cat_1 = Cat.get_by_id(1)    # search by id
print(cat_1)

# This will raise error because the id doesn't exist
# cat_100 = Cat.get_by_id(100)
# print(cat_100)

# use this method instead so that it returns none when the matching data does not exist
cat_100 = Cat.get_or_none(Cat.id == 100)
print(cat_100)

# count
total = Cat.select().count()
print(total)

# count with where clause
total_cats_who_are_5 = Cat.select().where(Cat.age == 3).count()
print(total_cats_who_are_5)

# sort - ascending order
cats_by_name = Cat.select().order_by(Cat.name, Cat.age)
print(list(cats_by_name))

# sort - descending order
cats_by_age = Cat.select().order_by(Cat.age.desc())
print(list(cats_by_age))

# limit
first_3 = Cat.select().order_by(Cat.name).limit(3)
print(list(first_3))

# delete
rows_deleted = Cat.delete().where(Cat.name == 'Holly').execute()
print(rows_deleted, list(Cat.select()))

