import logging
from personal_loan.models import Loan
from celery import shared_task


@shared_task(bind=True, name="loan_proposal_status")
def loan_proposal_status_task(self, loan_id):
    """
    Task that changes proposal status based on the number of approved and rejected ones.
    """
    loan = Loan.objects.get(id=loan_id)
    try:
        approved_loans = Loan.objects.filter(proposal_status="approved").count()
        rejected_loans = Loan.objects.filter(proposal_status="rejected").count()
        if approved_loans >= rejected_loans:
            loan.proposal_status = "rejected"
            logging.info("Loan Rejected")
        else:
            loan.proposal_status = "approved"
            logging.info("Loan Approved")
        loan.save()
    except Exception as error:
        logging.error(f"Exception: {error}")
    finally:
        logging.warning("Task done!")
