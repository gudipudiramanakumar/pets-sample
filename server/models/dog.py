from datetime import datetime
from enum import Enum
from . import db
from .base import BaseModel
from sqlalchemy.orm import validates, relationship

# Define an Enum for dog status
class AdoptionStatus(Enum):
    AVAILABLE = 'Available'
    ADOPTED = 'Adopted'
    PENDING = 'Pending'

class Dog(BaseModel):
    __tablename__ = 'dogs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    description = db.Column(db.Text)
    
    # Adoption status
    status = db.Column(db.Enum(AdoptionStatus), default=AdoptionStatus.AVAILABLE)
    intake_date = db.Column(db.DateTime, default=datetime.now)
    adoption_date = db.Column(db.DateTime, nullable=True)
    
    @validates('name')
    def validate_name(self, key, name):
        return self.validate_string_length('Dog name', name, min_length=2)
    
    @validates('gender')
    def validate_gender(self, key, gender):
        if gender not in ['Male', 'Female', 'Unknown']:
            raise ValueError("Gender must be 'Male', 'Female', or 'Unknown'")
        return gender
    
    @validates('description')
    def validate_description(self, key, description):
        if description is not None:
            return self.validate_string_length('Description', description, min_length=10, allow_none=True)
        return description
    
    @validates('age')
    def validate_age(self, key, age):
        """
        Validate dog age to ensure it's between 0 and 20 years.
        
        Args:
            key: The field name being validated
            age: The age value to validate
            
        Returns:
            int: The validated age
            
        Raises:
            ValueError: If age is outside the valid range (0-20)
        """
        if age is not None:
            # Check for boolean values first (they're technically int/float in Python)
            if isinstance(age, bool):
                raise ValueError("Age must be a number")
            
            if not isinstance(age, (int, float)):
                raise ValueError("Age must be a number")
            
            if age < 0:
                raise ValueError("Age cannot be negative")
            
            if age > 20:
                raise ValueError("Age cannot be greater than 20 years")
        
        return age
    
    def __repr__(self):
        return f'<Dog {self.name}, ID: {self.id}, Status: {self.status.value}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'breed': self.breed.name if self.breed else None,
            'age': self.age,
            'gender': self.gender,
            'description': self.description,
            'status': self.status.name if self.status else 'UNKNOWN'
        }