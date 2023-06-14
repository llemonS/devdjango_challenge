"""Forms with respective fields and validations."""
from django import forms
from .models import Loan


class LoanForm(forms.ModelForm):
    """
    Loan form that permits the regisration from the admin panel.
    """

    class Meta:
        """
        Model and fields that should appear.
        """

        model = Loan
        fields = ("name", "cpf", "loan_value")

    def clean(self):
        """
        Validation of the shown fields on admin panel.
        """
        cleaned_data = super().clean()
        name = cleaned_data.get("name", None)
        if not name:
            raise forms.ValidationError("Missing name.")
        cpf = cleaned_data.get("cpf", None).replace(".", "").replace("-", "")
        if not cpf:
            raise forms.ValidationError("Missing cpf.")
        loan_value = cleaned_data.get("loan_value", None)
        if not loan_value:
            raise forms.ValidationError("Missing loan value.")
        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError("Invalid cpf input.")
