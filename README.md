# Business Operations API

A production-style Django REST API for running a small services business: customers, projects, tasks, invoices, activity, and reporting. The project focuses on API design, relational modeling, validation, filtering, permissions, and maintainable business services rather than a simple CRUD demo.

## Product scope

The API models a realistic operations workflow:

```text
Customer
   │
   ├── Projects ──► Tasks
   │       │
   │       └──────► Project activity
   │
   └── Invoices ──► payment/status lifecycle
```

## Features

- Customer, project, task, and invoice management
- Role-aware API structure
- Search and filtering across operational records
- Pagination-ready list endpoints
- Invoice subtotal/tax/total calculations
- Task assignment and due-date tracking
- Project status and budget tracking
- Activity timeline for operational changes
- Validation kept close to domain rules
- Service layer for reusable business operations
- Automated tests for calculations and workflow rules
- PostgreSQL-ready production configuration

## Architecture

```text
HTTP / REST
    │
    ▼
Django REST Framework
    │
    ├── serializers / validation
    ├── viewsets / filtering
    └── permissions
            │
            ▼
      domain services
            │
            ▼
       Django ORM
            │
            ▼
       PostgreSQL
```

## Project structure

```text
config/                    application configuration
operations/
  models.py                relational domain model
  serializers.py           API representation + validation
  views.py                 resource endpoints
  urls.py                  router configuration
  services/                business operations
  filters.py               query filtering
  tests/                   unit and API tests
requirements.txt
manage.py
```

## Example API surface

```text
GET    /api/customers/
POST   /api/customers/
GET    /api/projects/
PATCH  /api/projects/{id}/
GET    /api/tasks/?status=in_progress
POST   /api/invoices/
GET    /api/invoices/?status=overdue
GET    /api/activity/
```

## Engineering decisions

The project deliberately separates persistence from business operations. For example, invoice totals are derived from monetary fields rather than duplicated state, while workflow changes can be implemented in services and tested without going through HTTP.

## Stack

- Python 3.12
- Django
- Django REST Framework
- PostgreSQL
- pytest / Django TestCase

## Running locally

```bash
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Portfolio note

This is an original portfolio/demo project using generated data and patterns commonly found in internal operations systems. It contains no proprietary employer code or customer information.
