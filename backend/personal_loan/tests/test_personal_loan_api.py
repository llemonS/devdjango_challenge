"""Tests to ensure that personal loan endpoint works properly."""
import json

from django.test import TestCase
from django.urls import reverse

from personal_loan.models import Loan

from rest_framework.test import APIClient


class PersonalLoanApiTestCase(TestCase):
    """
    Testcase covering the endpoint responsible for registering new loans.
    """

    def setUp(self):
        """
        Initial setup to perform the tests.
        """
        self.client = APIClient()

    def test_proposal_loan_get(self):
        """
        Make sure that whena get is made, the status code returns 405.
        """
        response = self.client.get(reverse("personal_loan"))
        response_content = response.content.decode("utf-8")
        response_dict = json.loads(response_content)
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response_dict, {"detail": 'Method "GET" not allowed.'})

    def test_proposal_loan_post_incomplete(self):
        """
        Make sure that when a incomplete post is made, the status code returns 201.
        """
        payload = {
            "name": "",
            "cpf": "154.245.256-51",
            "address": "anonymous street",
            "loan_value": 10000.00,
        }
        response = self.client.post(
            reverse("personal_loan"), data=payload, format="json"
        )
        response_content = response.content.decode("utf-8")
        response_dict = json.loads(response_content)
        self.assertEqual(response_dict, {"name": ["This field may not be blank."]})
        self.assertEqual(response.status_code, 400)

    def test_proposal_loan_post_wrong_cpf(self):
        """
        Make sure that when a incomplete post is made, the status code returns 201.
        """
        payload = {
            "name": "name",
            "cpf": "154.245.25651",
            "address": "anonymous street",
            "loan_value": 10000.00,
        }
        response = self.client.post(
            reverse("personal_loan"), data=payload, format="json"
        )
        response_content = response.content.decode("utf-8")
        response_dict = json.loads(response_content)
        self.assertEqual(response_dict, {"cpf": ["Invalid CPF format"]})
        self.assertEqual(response.status_code, 400)

    def test_proposal_loan_post(self):
        """
        Make sure that when a post is made, the status code returns 201.
        """
        payload = {
            "name": "jose",
            "cpf": "154.245.256-51",
            "address": "anonymous street",
            "loan_value": 10000.00,
        }
        response = self.client.post(
            reverse("personal_loan"), data=payload, format="json"
        )
        new_loan = Loan.objects.get(name=payload["name"])
        self.assertEqual(payload["name"], new_loan.name)
        self.assertIsNot(payload["cpf"], new_loan.cpf)
        self.assertEqual(new_loan.proposal_status, "unknown")
        self.assertEqual(response.status_code, 201)
