from django.urls import path, include
from rest_framework import routers

from personal_loan.views import PersonalLoanView


urlpatterns = [
    path(
        "personal_loan/",
        PersonalLoanView.as_view({"get": "post"}),
        name="personal_loan",
    ),
]
