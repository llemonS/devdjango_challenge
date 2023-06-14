"""Serializers for personal loan app."""
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
    CharField,
    DecimalField,
)

from django.core.validators import RegexValidator

from .models import Loan


class PersonalLoanSerializer(ModelSerializer):
    """
    Model serializer for loan model.
    """

    class Meta:
        """
        Serialize all loan fields.
        """

        model = Loan
        fields = (
            "name",
            "cpf",
            "address",
            "loan_value",
        )

    name = CharField(max_length=200, required=True)
    cpf = CharField(
        max_length=14,
        validators=[
            RegexValidator(
                regex=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", message="Invalid CPF format"
            )
        ],
        required=True,
    )
    address = CharField(required=True)
    loan_value = DecimalField(max_digits=20, decimal_places=2, required=True)

    def validate_cpf(self, cpf):
        """
        Perse symbols from cpf and store only its digits.
        """
        cpf = cpf.replace(".", "").replace("-", "")
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError("Cpf must have 11 digits.")
        else:
            return cpf
