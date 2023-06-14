from django.apps import AppConfig


class PersonalLoanConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "personal_loan"

    def ready(self):
        import personal_loan.signals
        import personal_loan.tasks
