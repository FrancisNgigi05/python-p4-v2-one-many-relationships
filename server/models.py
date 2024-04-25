# server/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    hire_date = db.Column(db.Date)
    """Bi-directional relationship between employees and reviews"""
    reviews = db.relationship('Review', back_populates="employee", cascade='all, delete-orphan') # Assigning reviews to an employee
    """Time to do the one to one relationship ("has one")"""
    onboarding = db.relationship('Onboarding', uselist=False, back_populates="employee", cascade='all, delete-orphan')
    def __repr__(self):
        return f'<Employee {self.id}, {self.name}, {self.hire_date}>'
class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)

    year = db.Column(db.Integer)
    summary = db.Column(db.String)
    """Adding the foreign key to connect the employees table to reviews table"""
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    """Time to create a relationship between the two tables"""
    employee = db.relationship('Employee', back_populates="reviews") # Assigning each emoployee their reviews

    def __repr__(self):
        return f'<Review {self.id}, {self.year}, {self.summary}>'

class Onboarding(db.Model):
    __tablename__ = 'onboardings'

    id  = db.Column(db.Integer, primary_key=True)

    orientation = db.Column(db.DateTime)
    forms_complete = db.Column(db.Boolean)
    """Adding a foreign key to connect the employees to onboardings table"""
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    """Time to do the one to one relationship ("Belongs to")"""
    employee = db.relationship('Employee', back_populates="onboarding") # making sure that each employee has an onboarding 

    def __repr__(self):
        return f'<Onboarding {self.id}, {self.orientation}, {self.fomrs_complete}>'