#!/usr/bin/python3
""" Defines The DBStorage engine"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """MySQL Engine"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize a DBStorage instance"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"),
	        pool_pre_ping=True
        ))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries on the current database session"""
        objectsDict = dict()
        if cls == None:
            query = self.__session.query(
                User, State, City, Amenity, Place, Review).all()
            for listObjects in query:
                for object_ in listObjects:
                    className = object_.__class__
                    id_ = object_.id
                    classId = className + "." + id_
                    objectsDict[classId] = object_
        else:
            query = self.__session.query(cls).all()
            for object_ in query:
                className = object_.__class__
                id_ = object_.id
                classId = className + "." + id_
                objectsDict[classId] = object_
        return objectsDict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
			       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
