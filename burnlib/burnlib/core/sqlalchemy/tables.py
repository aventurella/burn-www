from __future__ import absolute_import
from sqlalchemy import event
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import DDL
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import UniqueConstraint

metadata = MetaData()

# CREATE DATABASE bigmethod_test WITH owner vagrant encoding 'utf8' LC_CTYPE "C" LC_COLLATE "C" TEMPLATE "template0";

'''
[user]
id | email         | first_name | last_name        | password
--------------------------------------------------------------
1  | foo@bar.com   | Clark      | Venturella       | <hash>
2  | lucy@bark.com | Lucy       | Venturella       | <hash>
'''

user = Table('user', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(60), index=True, unique=True),
)

'''
[user_extra]
id | blitz_id
-------------------------------------------------------
1  | <hex>
2  | <hex>
'''
user_extra = Table('user_extra', metadata,
    Column('id', Integer,
            ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),
            primary_key=True),

    Column('game_center_id', String, index=True, unique=True, nullable=True),
    Column('ios_push_notification_id', String, index=True, unique=True, nullable=True),
)
