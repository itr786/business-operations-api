from django.db import transaction

from operations.models import Project, Task


PROJECT_TRANSITIONS = {
    "planned": {"active", "cancelled"},
    "active": {"on_hold", "completed", "cancelled"},
    "on_hold": {"active", "cancelled"},
}


@transaction.atomic
def change_project_status(project: Project, status: str) -> Project:
    allowed = PROJECT_TRANSITIONS.get(project.status, set())
    if status not in allowed:
        raise ValueError(f"Invalid project transition: {project.status} -> {status}")
    project.status = status
    project.save(update_fields=["status"])
    return project


@transaction.atomic
def complete_task(task: Task) -> Task:
    if task.status == "done":
        return task
    if task.status == "cancelled":
        raise ValueError("Cancelled tasks cannot be completed")
    task.status = "done"
    task.save(update_fields=["status"])
    return task
