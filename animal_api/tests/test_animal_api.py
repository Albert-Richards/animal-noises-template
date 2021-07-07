from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestAnimalApi(TestBase):
    def test_get_animal(self):
        for num in range(20):
            response = self.client.get(url_for('get_animal'))
            self.assertIn(response.data.decode("utf-8"),["cow", "pig", "horse"])
    
    def test_get_noise(self):
        response = self.client.post(url_for('get_noise'), data="cow")
        self.assertEqual(response.data.decode("utf-8"),"moo")
