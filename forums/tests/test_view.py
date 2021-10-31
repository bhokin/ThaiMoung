"""Tests for Registration."""
from django.test import TestCase
from django.urls import reverse


class RegistrationViewTests(TestCase):
    """Tests for sign in and sign up."""

    def test_registration_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('sign_in_and_sign_up'))
        self.assertEqual(response.status_code, 200)

    def test_main_view(self):
        """Tests that after we get into the page, we must get a status code of 200"""
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
