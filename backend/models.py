import base64
import datetime
import math
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from backend import app, db
from flask import current_app
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from slugify import slugify, Slugify, UniqueSlugify

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.String(64), nullable=False, unique=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    name = db.Column(db.String(64), nullable=True)
    password_hash = db.Column(db.String(128))
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_last_login = Column(DateTime, default=datetime.datetime.utcnow)
    street_shoe_size_in = db.Column(db.String(64), nullable=True, default=None)
    foot_shape = db.Column(db.Integer, default=0)
    gender = db.Column(db.Integer, nullable=False, default=0)
    split_shoe_info = db.Column(db.Integer, default=0)
    climbing_boulder = db.Column(db.Integer, nullable=False, default=0)
    climbing_sport = db.Column(db.Integer, nullable=False, default=0)
    climbing_trad = db.Column(db.Integer, nullable=False, default=0)
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def get_token(self, expires_in=86400):
        now = datetime.datetime.utcnow()
        if self.token and self.token_expiration > now + datetime.timedelta(seconds=60):
            return self.token
        s = Serializer(current_app.config['SECRET_KEY'])
        self.token = s.dumps({'user': self.id}).decode('utf-8')
        self.token_expiration = now + datetime.timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.datetime.utcnow():
            return None
        return user

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def get_climbing_boulder(self):
        if self.climbing_boulder == 0:
            return "V0"
        if self.climbing_boulder == 1:
            return "V1"
        if self.climbing_boulder == 2:
            return "V2"
        if self.climbing_boulder == 3:
            return "V3"
        if self.climbing_boulder == 4:
            return "V4"
        if self.climbing_boulder == 5:
            return "V5"
        if self.climbing_boulder == 6:
            return "V6"
        if self.climbing_boulder == 7:
            return "V7"
        if self.climbing_boulder == 8:
            return "V8"
        if self.climbing_boulder == 9:
            return "V9"
        if self.climbing_boulder == 10:
            return "V10"
        if self.climbing_boulder == 11:
            return "V11"
        if self.climbing_boulder == 12:
            return "V12"
        if self.climbing_boulder == 13:
            return "V13"
        if self.climbing_boulder == 14:
            return "V14+"

    @property
    def get_climbing_sport(self):
        if self.climbing_sport == 0:
            return "5.0"
        if self.climbing_sport == 1:
            return "5.1"
        if self.climbing_sport == 2:
            return "5.2"
        if self.climbing_sport == 3:
            return "5.3"
        if self.climbing_sport == 4:
            return "5.4"
        if self.climbing_sport == 5:
            return "5.5"
        if self.climbing_sport == 6:
            return "5.6"
        if self.climbing_sport == 7:
            return "5.7"
        if self.climbing_sport == 8:
            return "5.8"
        if self.climbing_sport == 9:
            return "5.9"
        if self.climbing_sport == 10:
            return "5.10a"
        if self.climbing_sport == 11:
            return "5.10b"
        if self.climbing_sport == 12:
            return "5.10c"
        if self.climbing_sport == 13:
            return "5.10d"
        if self.climbing_sport == 14:
            return "5.11a"
        if self.climbing_sport == 15:
            return "5.11b"
        if self.climbing_sport == 16:
            return "5.11c"
        if self.climbing_sport == 17:
            return "5.11d"
        if self.climbing_sport == 18:
            return "5.12a"
        if self.climbing_sport == 19:
            return "5.12b"
        if self.climbing_sport == 20:
            return "5.12c"
        if self.climbing_sport == 21:
            return "5.12d"
        if self.climbing_sport == 22:
            return "5.13a"
        if self.climbing_sport == 23:
            return "5.13b"
        if self.climbing_sport == 24:
            return "5.13c"
        if self.climbing_sport == 25:
            return "5.13d"
        if self.climbing_sport == 26:
            return "5.14a+"

    @property
    def get_climbing_trad(self):
        if self.climbing_trad == 0:
            return "5.0"
        if self.climbing_trad == 1:
            return "5.1"
        if self.climbing_trad == 2:
            return "5.2"
        if self.climbing_trad == 3:
            return "5.3"
        if self.climbing_trad == 4:
            return "5.4"
        if self.climbing_trad == 5:
            return "5.5"
        if self.climbing_trad == 6:
            return "5.6"
        if self.climbing_trad == 7:
            return "5.7"
        if self.climbing_trad == 8:
            return "5.8"
        if self.climbing_trad == 9:
            return "5.9"
        if self.climbing_trad == 10:
            return "5.10a"
        if self.climbing_trad == 11:
            return "5.10b"
        if self.climbing_trad == 12:
            return "5.10c"
        if self.climbing_trad == 13:
            return "5.10d"
        if self.climbing_trad == 14:
            return "5.11a"
        if self.climbing_trad == 15:
            return "5.11b"
        if self.climbing_trad == 16:
            return "5.11c"
        if self.climbing_trad == 17:
            return "5.11d"
        if self.climbing_trad == 18:
            return "5.12a"
        if self.climbing_trad == 19:
            return "5.12b"
        if self.climbing_trad == 20:
            return "5.12c"
        if self.climbing_trad == 21:
            return "5.12d"
        if self.climbing_trad == 22:
            return "5.13a"
        if self.climbing_trad == 23:
            return "5.13b"
        if self.climbing_trad == 24:
            return "5.13c"
        if self.climbing_trad == 25:
            return "5.13d"
        if self.climbing_trad == 26:
            return "5.14a+"

    @property
    def get_gender(self):
        if self.gender == 0:
            return "Prefer not to say"
        if self.gender == 1:
            return "Male"
        if self.gender == 2:
            return "Female"

    @property
    def get_foot_shape(self):
        if self.foot_shape == 0:
            return "Not specified"
        if self.foot_shape == 1:
            return "Egyptian"
        if self.foot_shape == 2:
            return "Roman"
        if self.foot_shape == 3:
            return "Greek"
        if self.foot_shape == 4:
            return "Germanic"
        if self.foot_shape == 5:
            return "Celtic"

    @property
    def get_split_shoe_info(self):
        if self.split_shoe_info == 0:
            return "No"
        if self.split_shoe_info == 1:
            return "Yes - Left Shoe Slightly Larger Than Right"
        if self.split_shoe_info == 2:
            return "Yes- Right Shoe Slightly Larger Than Left"

    @property
    def street_shoe_size(self):
        return convert_shoe_size_to_standards(self.street_shoe_size_in)

    @property
    def date_created_readable(self):
        return self.date_created.strftime('%m-%d-%Y')

    @property
    def date_last_login_readable(self):
        return self.date_last_login.strftime('%m-%d-%Y')

    @property
    def provider_id_short(self):
        if 'facebook' in self.provider_id:
            return "fb"
        if 'sizesquirrel' in self.provider_id:
            return "ss"

    def serialize_private(self):
        return {
            'id': self.id,
            'provider_id_short': self.provider_id_short,
            'username': self.username,
            'email': self.email,
            'name': self.name,
            'street_shoe_size_in': self.street_shoe_size_in,
            'street_shoe_size': self.street_shoe_size,
            'date_created_readable': self.date_created_readable,
            'date_last_login_readable': self.date_last_login_readable,
            'get_split_shoe_info': self.get_split_shoe_info,
            'split_shoe_info': self.split_shoe_info,
            'foot_shape': self.foot_shape,
            'get_foot_shape': self.get_foot_shape,
            'gender': self.gender,
            'climbing_boulder': self.climbing_boulder,
            'climbing_sport': self.climbing_sport,
            'climbing_trad': self.climbing_trad,
            'get_gender': self.get_gender,
            'get_climbing_boulder': self.get_climbing_boulder,
            'get_climbing_sport': self.get_climbing_sport,
            'get_climbing_trad': self.get_climbing_trad
        }

    def serialize_public(self):
        return {
            'id': self.id,
            'provider_id_short': self.provider_id_short,
            'username': self.username,
            'street_shoe_size_in': self.street_shoe_size_in,
            'street_shoe_size': self.street_shoe_size,
            'date_created_readable': self.date_created_readable,
            'get_split_shoe_info': self.get_split_shoe_info,
            'split_shoe_info': self.split_shoe_info,
            'get_foot_shape': self.get_foot_shape,
            'get_gender': self.get_gender,
            'get_climbing_boulder': self.get_climbing_boulder,
            'get_climbing_sport': self.get_climbing_sport,
            'get_climbing_trad': self.get_climbing_trad
        }

# 1{'name':'men'},
# 2{'name':'women'},
# 3{'name':'unisex'},
# 4{'name':'kids'},


class Gender(db.Model):
    __tablename__ = 'gender'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    @property
    def pretty_format_gender(self):

        if self.name == 'men':
            return 'Men\'s'
        if self.name == 'women':
            return 'Women\'s'
        else:
            return self.name.capitalize()

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_pretty': self.pretty_format_gender
        }


# 1|evolv|US
# 2|five ten|US
# 3|la sportiva|EUR
# 4|mad rock|US
# 5|scarpa|EUR
# 6|boreal|US
# 7|tenaya|US
# 8|climb x|US
# 9|red chili|US
# 10|eb|EUR
# 11|simond|EUR
# 12|butora|US
# 13|cypher|US
# 14|ocun|EUR
# 15|salewa|US
# 16|adidas|US
# 17|andrea boldrini|EUR
# 18|asolo|EUR
# 19|lowa|US
# 20|zamberlan|EUR
# 21|mammut|UK
# 22|garmont|UK
# 23|the north face|US
# 24|millet|UK
# 25|so ill|US
# 26|arcteryx|US
# 27|black diamond|US
# 28|unparallel|US
# 29|rock on|US
# 30|acopa|US
# 31|wildclimb|EUR



CONSTANT_BRANDS = [
    'evolv',
    'five ten',
    'la sportiva',
    'mad rock',
    'scarpa',
    'boreal',
    'tenaya',
    'climb x',
    'red chili',
    'eb',
    'simond',
    'butora',
    'cypher',
    'ocun',
    'salewa',
    'adidas',
    'andrea boldrini',
    'asolo',
    'lowa',
    'zamberlan',
    'mammut',
    'garmont',
    'the north face',
    'millet',
    'so ill',
    'arcteryx',
    'black diamond',
    'unparallel',
    'rock on', 
    'acopa',
    'wildclimb']


class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    sizing = db.Column(db.String(64), nullable=False, server_default='US')

    @property
    def name_slug(self):
        custom_slugify = Slugify(to_lower=True)
        custom_slugify.safe_chars = '+.ii'

        return custom_slugify(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_slug': self.name_slug,
            'sizing': self.sizing
        }


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'))
    brand = relationship('Brand')
    model = db.Column(db.String(64), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('gender.id'))
    gender = relationship('Gender')
    small_image_url = db.Column(db.String(64), nullable=True)
    medium_image_url = db.Column(db.String(64), nullable=True)
    thumbnail_cache = Column(DateTime, default=None)
    type = db.Column(db.String(64), nullable=False, server_default='rock')
    asin = db.Column(db.String(64), nullable=True)
    offer_url = db.Column(db.String(64), nullable=True)
    user_items = relationship("User_Item")
    average_rating = db.Column(db.String(64), nullable=True, default=None)

    average_rating_egyptian = db.Column(db.String(64), nullable=True)
    count_egyptian = db.Column(db.Integer, default=0)
    average_rating_roman = db.Column(db.String(64), nullable=True)
    count_roman = db.Column(db.Integer, default=0)
    average_rating_greek = db.Column(db.String(64), nullable=True)
    count_greek = db.Column(db.Integer, default=0)
    average_rating_germanic = db.Column(db.String(64), nullable=True)
    count_germanic = db.Column(db.Integer, default=0)
    average_rating_celtic = db.Column(db.String(64), nullable=True)
    count_celtic = db.Column(db.Integer, default=0)

    popular_foot_shape = db.Column(db.String(64), nullable=True)

    popular_fit_descriptor = db.Column(db.String(64), nullable=True)

    highest_rated_foot_shape = db.Column(db.String(64), nullable=True)

    # climbing skill
    average_rating_beginner_climbers = db.Column(db.String(64), nullable=True)
    count_beginner_climbers = db.Column(db.Integer, default=0)
    average_rating_advanced_climbers = db.Column(db.String(64), nullable=True)
    count_advanced_climbers = db.Column(db.Integer, default=0)
    average_rating_expert_climbers = db.Column(db.String(64), nullable=True)
    count_expert_climbers = db.Column(db.Integer, default=0)

    # foot_shapes:
    # egyptian 1
    # roman 2
    # greek 3
    # germanic 4
    # celtic 5

    # types:
    # approach
    # mountain
    # rock
    # hiking

    @property
    def short_size_standard(self):
        if self.brand.sizing == 'US':
            if self.gender_id == 2:
                return "USW"
            else:
                return "USM"
        if self.brand.sizing == 'UK':
            return "UK"
        else:
            return "EUR"

    @property
    def is_shoe_thumbnail_stale(self):
        # returns true if thumbnail_cache is missing or more than 10 days old.
        if self.thumbnail_cache is None or (datetime.datetime.utcnow() - self.thumbnail_cache) > datetime.timedelta(10):
            return "true"
        else:
            return "false"

    @property
    def shoe_image(self):
        if self.medium_image_url is not None:
            return self.medium_image_url.replace('http://', 'https://')
        if self.small_image_url is not None:
            return self.small_image_url.replace('http://', 'https://')
        else:
            return "/images/placeholder_"+self.type+".png"

    @property
    def model_slug(self):
        custom_slugify = Slugify(to_lower=True)
        custom_slugify.safe_chars = '+.ii'

        return custom_slugify(self.model)

    @property
    def ratings(self):
        return [
            {
                'foot_shape_descriptor': 'Egyptian',
                'foot_shape_descriptor_id': 1,
                'avg_rating': float("{0:.2f}".format(float(self.average_rating_egyptian))),
                'count': self.count_egyptian
            },
            {
                'foot_shape_descriptor': 'Roman',
                'foot_shape_descriptor_id': 2,
                'avg_rating': float("{0:.2f}".format(float(self.average_rating_roman))),
                'count': self.count_roman
            },
            {
                'foot_shape_descriptor': 'Greek',
                'foot_shape_descriptor_id': 3,
                'avg_rating': float("{0:.2f}".format(float(self.average_rating_greek))),
                'count': self.count_greek
            },
            {
                'foot_shape_descriptor': 'Germanic',
                'foot_shape_descriptor_id': 4,
                'avg_rating': float("{0:.2f}".format(float(self.average_rating_germanic))),
                'count': self.count_germanic
            },
            {
                'foot_shape_descriptor': 'Celtic',
                'foot_shape_descriptor_id': 5,
                'avg_rating': float("{0:.2f}".format(float(self.average_rating_celtic))),
                'count': self.count_celtic
            }
        ]

    # serialize with minimal attributes
    def minimal_serialize(self):
        return {
            'id': self.id,
            'brand': self.brand.serialize(),
            'model': self.model,
            'gender': self.gender.serialize(),
            'type': self.type,
            'shoe_image': self.shoe_image,
        }

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand.serialize(),
            'model': self.model,
            'model_slug': self.model_slug,
            'gender': self.gender.serialize(),
            'gender_id': self.gender_id,
            'type': self.type,
            'short_size_standard': self.short_size_standard,
            'shoe_image': self.shoe_image,
            'stats': {
                'avg_rating': float('{0:.2f}'.format(float(self.average_rating))),
                'count': len(self.user_items),
                'popular_fit_descriptor': self.popular_fit_descriptor,
                'ratings': self.ratings,
                'highest_rated_foot_shape': self.highest_rated_foot_shape,
                'by_skill': [
                    {
                        'skill': 'beginner',
                        'rating': self.average_rating_beginner_climbers,
                        'count': self.count_beginner_climbers
                    },
                    {
                        'skill': 'advanced',
                        'rating': self.average_rating_advanced_climbers,
                        'count': self.count_advanced_climbers
                    },
                    {
                        'skill': 'expert',
                        'rating': self.average_rating_expert_climbers,
                        'count': self.count_expert_climbers
                    }
                ]
            }
        }


class User_Item(db.Model):
    __tablename__ = 'user_item'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship('User')
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    item = relationship('Item', overlaps='user_items')
    rating = db.Column(db.Integer)
    size = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.UnicodeText())
    fit = db.Column(db.Integer, default=2)
    size_in = db.Column(db.String(64), nullable=False)
    comments_date = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def shoe_size(self):
        return convert_shoe_size_to_standards(self.size_in)

    @property
    def size_standard(self):
        if self.size > 32:
            return "EUR"
        else:
            return "US"

    @property
    def fit_descriptor(self):
        if self.fit == 1:
            return "Aggressive"
        if self.fit == 2:
            return "Normal"
        if self.fit == 3:
            return "Comfortable"

    @property
    def comments_date_readable(self):
        if self.comments_date is None:
            return None
        return self.comments_date.strftime('%m-%d-%Y')
    
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'item_id': self.item_id,
            'item': self.item.serialize(),
            'rating': self.rating,
            'comments': self.comments,
            'comments_date_readable': self.comments_date_readable,
            'fit': self.fit,
            'fit_descriptor': self.fit_descriptor,
            'size': self.size,
            'size_in': self.size_in,
            'size_standard': self.size_standard,
        }

# Utility Functions


def convert_shoe_size_to_standards(inches):
    if inches is None or inches == 0 or inches == '':
        size_standards = dict({})
        return size_standards
    inches = float(inches)

    us_m_size = (inches - 7.33333)/.33333
    us_w_size = us_m_size + 1
    uk_size = us_m_size - 1
    eur_size = uk_size * 1.33333 + 31.33333

    size_standards = dict({
        # 'EURRAW': float("{0:.3f}".format(eur_size)),
        'EUR': customRound(eur_size),
        # 'USMRAW': us_m_size,
        'USM': customRound(us_m_size),
        'USW': customRound(us_w_size),
        'UK': customRound(uk_size)
    })
    return size_standards


def customRound(number):
    return round(float("{0:.2f}".format(number)) * 2) / 2
