"""Models for the personal loan project."""
import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Loan(models.Model):
    """
    Initial attributes for personal loan.
    """

    class ProposalChoices(models.TextChoices):
        """
        Choices available per loan.
        """

        UNKNOWN = "unknown", _("Unknown")
        APPROVED = "approved", _("Approved")
        REJECTED = "rejected", _("Rejected")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    address = models.TextField(blank=False)
    loan_value = models.DecimalField(max_digits=20, decimal_places=2)
    proposal_status = models.CharField(
        max_length=8, choices=ProposalChoices.choices, default=ProposalChoices.UNKNOWN
    )

    def __str__(self):
        return f"{self.name}, {self.cpf}"
