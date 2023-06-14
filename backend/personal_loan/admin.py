"""Admin containing the respective models and data."""
from django.contrib import admin
from .models import Loan
from .forms import LoanForm


class PersoalLoanAdmin(admin.ModelAdmin):
    """
    Modeladmin containing customized form validations and fields to manage.
    """

    form = LoanForm
    search_fields = ("cpf",)
    list_display = ("name", "cpf", "loan_value", "proposal_status")
    list_filter = ["proposal_status"]

    def get_queryset(self, request):
        return (
            super(PersoalLoanAdmin, self).get_queryset(request).order_by("created_at")
        )


admin.site.register(Loan, PersoalLoanAdmin)
