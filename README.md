# DevDjango_challenge:
Challenge to develop a management system for personal loan.

## Stack:
- Django
- Django Rest Framework
- Django Celery
- React

## Setup Steps:
1 - In order to run the project, one shall clone this repo and run:
```
docker-compose up --build
```
2 - Install node modules using:
```
docker exec -it react sh -c "npm install"
```
3 - Stop the enviroment using `CTRL+C` and finally run:
```
docker-compose up
```
## Backend Testing:
If you want to run tests on backend:
```
docker-compose exec -it backend python manage.py test
```

## Project Structure:

 - Django admin Panel:
The admin can access it through the URL `http://0.0.0.0:8000/admin` using `superadmin` and `superpass` credentials.
 - Djando Rest Framework:
 Loans can be posted directly on the URL `http://0.0.0.0:8000/api/personal_loan/` if desired.
 - React Frontend:
 To register a new loan proposal form, the user can access `http://0.0.0.0:3000`

## Definition of Done (DoD):
  - Fields name, cpf, address, loan_value. ☑
  - Form page to fill the proposal (using React). ☑
  - Proposal Validation algorithm as celery task (half approved and rejected at `loan_proposal_status_task`). ☑
  - Admin view of loan objects. ☑
  - Readme.md containing steps to run the project. ☑
  - Default user (`superadmin` `superpass`) ☑
  - Docstring coverage (out of initial scope) ☑
  - TDD implemented (out of initial scope) ☑
  - Dockerized application (out of initial scope) ☑
