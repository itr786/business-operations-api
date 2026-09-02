# API Contract

The API is organized around business resources rather than database tables exposed directly.

## Customers

`GET /api/customers/` supports search by name/email and pagination.

## Projects

`GET /api/projects/?status=active&min_budget=5000`

Projects expose customer relationships, status, budget, and task counts.

## Tasks

`GET /api/tasks/?status=in_progress&due_before=2026-12-31`

Tasks support project filtering and due-date queries.

## Invoices

`GET /api/invoices/?status=overdue`

Invoice totals are calculated from subtotal + tax and lifecycle changes are handled by services.

## Design goals

- predictable REST resource naming
- explicit validation errors
- pagination for collection endpoints
- filtering without embedding query logic in serializers
- business transitions implemented in testable service functions
