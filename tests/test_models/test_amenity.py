#!/usr/bin/python3
""" """
import unittest
import models
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from sqlalchemy.exc import OperationalError
from os import getenv


class test_Amenity(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity = Amenity(name="wifi")

    def test_creation(self):
        """ """
        amenity = self.value(id="001", name="wifi")
        self.assertEqual(amenity.name, "wifi")
        self.assertEqual(amenity.id, "001")

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', "not supported")
    def test_no_name(self):
        """ """
        new = self.value()
        with self.assertRaises(OperationalError):
            try:
                new.save()
            except Exception as error:
                models.storage._DBStorage__session.rollback()
                raise error

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', "not supported")
    def test_no_name(self):
        """ """
        amenity = self.value()
        self.assertTrue(isinstance(amenity, Amenity))
