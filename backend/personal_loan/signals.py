from django.db.models.signals import post_save
from django.dispatch import receiver
from personal_loan.tasks import loan_proposal_status_task
from personal_loan.models import Loan

@receiver(post_save, sender=Loan)
def evaluate_loan_status(sender, instance, created, **kwargs):
      if created:
            loan_proposal_status_task.delay(instance.id)

post_save.connect(evaluate_loan_status, sender=Loan)