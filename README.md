# Business Operations API

A Django REST API portfolio project for managing customers, projects, tasks, and invoices with clear service boundaries and PostgreSQL-friendly models.

## Features

- Customer and project management
- Task assignment and status tracking
- Invoice lifecycle and totals
- Filtering, pagination, and validation
- Permission-ready API structure
- Automated test-friendly service layer

## Stack

Python · Django · Django REST Framework · PostgreSQL

## API design

Resources are exposed as conventional REST endpoints, while business rules live outside serializers where possible so they can be tested independently.

This is a portfolio/demo project and contains no proprietary customer data or employer code.
