from sqlalchemy import Column, Date, Integer, Numeric, String, text, Table, INT
from app.connection import Base, engine


class Usuario(Base):

    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Numeric(4, 2), nullable=False)
    age = Column(INT, nullable=False)

    def to_dict(self):
        dic = {
            'id' : self.id,
            'name' : self.name,
            'age' : self.age,
            'height' : str(self.height)
        }
        return dic


    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # def __repr__(self):
    #     return {'name' : self.name, 'age' : self.age, 'height' : self.height}

    # def __str__(self):
    #     return 'Person(name=' + self.name + ', age=' + str(self.age) + ', height=' + str(self.height) + ')'