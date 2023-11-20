from datetime import datetime

from sqlalchemy import Boolean, Float, Column, Integer, String, DateTime, func, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship
from .database import Base
from enum import Enum as PythonEnum, Enum
# from sqlalchemy.sql.expression import text
from sqlalchemy.event import listen

class BaseEntity(Base):
    __abstract__ = True

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
    deleted_at = Column(DateTime, nullable=True)

class OrderEntity(Base):
    __tablename__ = 'Orders'

    order_id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Integer, default=0)
    status = Column(String, nullable=False)
    delivery_address = Column(String)
    contact = Column(String(length=15))

    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime,
        server_default=func.now(),
        server_onupdate=func.now(),
        nullable=False,
    )
    deleted_at = Column(DateTime, nullable=True)

    discount_id = Column(Integer, ForeignKey('Discounts.discount_id'))  # Fix the reference here
    discount = relationship('DiscountEntity', lazy='joined')
    payment_id = Column(Integer, ForeignKey('Payments.payment_id'))  # Fix the reference here
    payment = relationship('PaymentEntity', lazy='joined')

    user_id = Column(Integer, ForeignKey('Users.user_id'))  # Fix the reference here
    user = relationship('UserEntity', lazy='joined')

    employee_id = Column(Integer, ForeignKey('Employees.employee_id'))  # Fix the reference here
    employee = relationship('EmployeeEntity', lazy='joined')

    shipping_id = Column(Integer, ForeignKey('Shippings.shipping_id'))  # Fix the reference here
    shipping = relationship('ShippingEntity', lazy='joined')


class PaymentEntity(Base):
    __tablename__ = 'Payments'

    payment_id = Column(Integer, primary_key=True, index=True)
    payment_name = Column(String)
    description = Column(String)

    orders = relationship('OrderEntity', back_populates='payment')


class DiscountEntity(Base):
    __tablename__ = 'Discounts'

    discount_id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    expired = Column(Date, nullable=False)
    percent = Column(Integer)

    # Mối quan hệ OneToMany với ProductEntity
    products = relationship('ProductEntity', back_populates='discount')

    # Mối quan hệ OneToMany với OrderEntity
    orders = relationship('OrderEntity', back_populates='discount')

class ShippingEntity(Base):
    __tablename__ = 'Shippings'

    shipping_id = Column(Integer, primary_key=True, index=True)
    shipping_name = Column(String(100), nullable=False)
    ship_cost = Column(Float, default=0, nullable=False)
    estimated_time = Column(Integer, nullable=False)

    # Mối quan hệ OneToMany với OrderEntity
    orders = relationship('OrderEntity', back_populates='shipping')

class UserEntity(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String)
    avatar_url = Column(String)
    gender = Column(String(50))
    birthday = Column(Date, nullable=False)
    address = Column(String)
    phone = Column(String(10), nullable=False)

    # Mối quan hệ OneToOne với AccountEntity
    email = Column(String(50), ForeignKey('Accounts.email'))
    account = relationship('AccountEntity', back_populates='user')

    # Mối quan hệ OneToOne với EmployeeEntity
    employee_id = Column(String(50), ForeignKey('Employees.employee_id'))
    employee = relationship('EmployeeEntity', back_populates='user')

    # Mối quan hệ OneToMany với OrderEntity
    orders = relationship('OrderEntity', back_populates='user')

class EmployeeEntity(Base):
    __tablename__ = 'Employees'

    employee_id = Column(String(50), primary_key=True, index=True)
    salary = Column(Integer, default=0)
    work_status = Column(Boolean, default=True)

    # Mối quan hệ OneToOne với UserEntity
    user = relationship('UserEntity', back_populates='employee', uselist=False)

    # Mối quan hệ OneToMany với OrderEntity
    orders = relationship('OrderEntity', back_populates='employee')

    # Mối quan hệ ManyToOne với PositionEntity
    position_id = Column(Integer, ForeignKey('Positions.position_id'))
    position = relationship('PositionEntity', back_populates='employees', lazy='joined')

class PositionEntity(Base):
    __tablename__ = 'Positions'

    position_id = Column(Integer, primary_key=True, index=True)
    position_name = Column(String(100), nullable=False)
    offer = Column(Numeric(precision=10, scale=2), nullable=False, default=1)

    # Mối quan hệ OneToMany với EmployeeEntity
    employees = relationship('EmployeeEntity', back_populates='position')

# class RoleEnum(PythonEnum):
#     User = 'User'
#     Admin = 'Admin'


class AccountEntity(Base):
    __tablename__ = 'Accounts'

    email = Column(String(50), primary_key=True, index=True)
    password = Column(String, nullable=False)
    status = Column(Boolean, default=True)
    refresh_token = Column(String, default=None)

    # Sửa đổi ở đây
    role = Column(String)

    # Mối quan hệ OneToOne với UserEntity
    user = relationship('UserEntity', back_populates='account')

    def emailToLowerCase(self):
        self.email = self.email.lower()


class CategoryEntity(Base):
    __tablename__ = 'Categories'

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(50), nullable=False)
    description = Column(String)
    category_url = Column(String)

    # Mối quan hệ OneToMany với ProductEntity
    products = relationship('ProductEntity', back_populates='category')

class ImageEntity(Base):
    __tablename__ = 'Images'

    image_id = Column(String, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('Products.product_id'))
    url = Column(String, nullable=False)

    product = relationship('ProductEntity', back_populates='images')


class ProductEntity(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, nullable=False)
    vote = Column(Integer, default=0)
    price = Column(Integer, default=0, nullable=False)
    unit_price = Column(Integer, default=0, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)
    status = Column(Boolean, default=True)

    description = Column(String)
    operation_system = Column(String(100), nullable=False)
    hardware = Column(String(100), nullable=False)
    warranty_time = Column(Integer, nullable=False)

    images = relationship('ImageEntity', back_populates='product')

    category_id = Column(Integer, ForeignKey('Categories.category_id'))
    category = relationship('CategoryEntity', back_populates='products')

    discount_id = Column(Integer, ForeignKey('Discounts.discount_id'))
    discount = relationship('DiscountEntity', back_populates='products')

    color = Column(String(50), nullable=False)
    battery = Column(Integer, nullable=False)
    screen = Column(Numeric(precision=10, scale=2), nullable=False)
    memory = Column(Integer, nullable=False)
    front_camera = Column(Integer, nullable=False)
    behind_camera = Column(Integer, nullable=False)
    ram = Column(Integer, nullable=False)

    @classmethod
    def validate_unit_price(cls, mapper, connection, target):
        if target.unit_price > target.price:
            raise ValueError('Invalid unit price')

listen(ProductEntity, 'before_insert', ProductEntity.validate_unit_price)
listen(ProductEntity, 'before_update', ProductEntity.validate_unit_price)