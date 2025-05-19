# Welcome to Software Design
# Written by Gower Campbell

# -----------------------------------------------------------------------------
# Modularisation
# -----------------------------------------------------------------------------

"""
Modularisation involves breaking down complex systems into independent,
interchangeable, and self-contained modules that function autonomously.
This enhances development efficiency, code reusability, and collaboration
among developers.
"""

# Key Principles of Modularisation:
"""
1. Independence: Minimising dependencies on other components for easier testing,
   maintenance, and updates.
2. Interchangeability: Modules can be replaced or upgraded without affecting
   the system (e.g., Database Connector Module).
3. Reusability: Modules like the `print` function can be reused across different
   parts of a system or projects.
4. Encapsulation: Each module encapsulates specific functionality (e.g.,
   authentication) and hides its internal workings.
5. Scalability: Enables the addition or removal of modules to accommodate
   changes in system requirements (e.g., web server).
"""

# Example: Building Automation System
"""
- Temperature-control module: Monitors and controls the HVAC system.
- Lighting-control module: Manages the lighting system based on occupancy and time.
- Security module: Handles access control and surveillance.
- Communication Interface: Central hub for data transmission between modules.
"""

# Benefits of Modularisation:
"""
- Ease of Maintenance: Easier to locate, fix, or update specific parts.
- Enhanced Reusability: Reuse reliable modules across projects.
- Improved Collaboration: Divide workload and address issues independently.
- Scalability: Add or replace modules for seamless growth.
- Simplified Testing: Test individual modules in isolation.
"""

# -----------------------------------------------------------------------------
# Use Case Analysis
# -----------------------------------------------------------------------------

"""
Use Case Analysis visually maps plausible user-system interactions to illustrate
real-world workflows and requirements. It helps meet stakeholder needs, identify
edge cases, and plan rigorous tests.
"""

# Use Case Analysis Diagram Components:
"""
- Actors: Users or external systems interacting with the application.
- Use Cases: Specific functionalities or tasks actors can perform.
- System Boundary: Defines the scope of the application.
- Relationships: Association, Dependency, Generalisation, Include, and Extend.
"""

# Example: Use Case Diagram for a To-Do List Application
"""
- Actors: User, Admin
- Use Cases: Add Task, Delete Task, Mark Task as Complete
- Relationships:
  - Include: Add Task includes Validate Task.
  - Extend: Add Task can optionally include Set Reminder.
"""

# -----------------------------------------------------------------------------
# Sequence Diagrams
# -----------------------------------------------------------------------------

"""
Sequence Diagrams represent the chronological flow of messages and interactions
among different components or objects in a system. They illustrate dynamic
aspects of a system to showcase how various entities achieve a specific task.
"""

# Key Elements of Sequence Diagrams:
"""
- Lifelines: Represent objects or components (e.g., User, View, Database).
- Messages: Arrows indicating communication between lifelines.
- Activation Bars: Show the duration of an object's activity.
- Return Messages: Responses or data flow back to the sender.
"""

# Example: Sequence Diagram for Adding a Task
"""
1. User sends "Add Task Request" to the View.
2. View sends "Validate and Save" to the Model.
3. Model sends "Store Task" to the Database.
4. Database sends "Acknowledgement" back to the Model.
5. Model sends "Add Task Response" to the View.
6. View updates the User Interface.
"""

# -----------------------------------------------------------------------------
# Separation of Concerns
# -----------------------------------------------------------------------------

"""
Separation of Concerns divides an application into distinct components, each
handling a specific responsibility. This improves maintainability, scalability,
and robustness.
"""

# Model-View-Controller (MVC) Pattern:
"""
- Model: Manages data and business logic.
- View: Handles presentation and user interface.
- Controller: Acts as an intermediary between Model and View.
"""

# Example: To-Do List Application
"""
- Model: Task class with attributes like title, description, and status.
- View: Displays the task list and accepts user input.
- Controller: Handles user requests to add, delete, or update tasks.
"""

# -----------------------------------------------------------------------------
# Class Diagrams
# -----------------------------------------------------------------------------

"""
Class Diagrams visually represent the static structure of an application,
illustrating classes, their attributes, and relationships.
"""

# Example: Library Management System
"""
- Book Class:
  - Attributes: title (String), author (String), ISBN (String)
  - Methods: getDetails()
- Library Class:
  - Attributes: books (List<Book>)
  - Methods: addBook(book), searchBook(title)
- DigitalBook Class (inherits from Book):
  - Additional Attribute: format (String)
- ReferenceBook Class (inherits from Book):
  - Additional Attribute: citations (List<String>)
  - Additional Method: addCitation(citation)
"""

# Relationships in Class Diagrams:
"""
- Inheritance: DigitalBook and ReferenceBook inherit from Book.
- Association: Library has a list of Books.
"""

# -----------------------------------------------------------------------------
# CRUD Matrix
# -----------------------------------------------------------------------------

"""
A CRUD Matrix documents the relationships between entities (usually database tables)
and the CRUD (Create, Read, Update, Delete) operations that can be performed on them.
"""

# Example: Task Management System
"""
- Task Entity:
  - Create (C): Add a new task.
  - Read (R): Retrieve task details.
  - Update (U): Modify task details.
  - Delete (D): Remove a task.
"""



# Task Class Definition


class Task:
    """Class representing a Task entity with attributes:
    task_id, title, and description."""

    def __init__(self, task_id, title, description):
        """Initialize a new Task instance."""
        self.task_id = task_id
        self.title = title
        self.description = description


# Sample Data
tasks_data = [
    Task(1, "Task 1", "Description for Task 1"),
    Task(2, "Task 2", "Description for Task 2"),
    Task(3, "Task 3", "Description for Task 3"),
]


# CRUD Operations
def display_tasks():
    """Display information for all tasks."""
    print("Tasks:")
    for task in tasks_data:
        print(f"ID: {task.task_id}, Title: {task.title}, "
              f"Description: {task.description}")
    print()


def create_task(title, description):
    """Create a new task and add it to the tasks_data list."""
    new_id = len(tasks_data) + 1
    new_task = Task(new_id, title, description)
    tasks_data.append(new_task)
    print(f"Task '{title}' created successfully!\n")


def read_task(task_id):
    """Read and display information for a task based on its ID."""
    for task in tasks_data:
        if task.task_id == task_id:
            print(f"Task found - ID: {task.task_id}, Title: {task.title}, "
                  f"Description: {task.description}\n")
            return
    print(f"Task with ID {task_id} not found.\n")


def update_task(task_id, new_title, new_description):
    """Update the title and description of a task based on its ID."""
    for task in tasks_data:
        if task.task_id == task_id:
            task.title = new_title
            task.description = new_description
            print("Task updated successfully!\n")
            return
    print(f"Task with ID {task_id} not found.\n")


def delete_task(task_id):
    """Delete a task based on its ID."""
    for i, task in enumerate(tasks_data):
        if task.task_id == task_id:
            del tasks_data[i]
            print("Task deleted successfully!\n")
            return
    print(f"Task with ID {task_id} not found.\n")


# Demonstration of CRUD Operations
print("Initial Tasks:")
display_tasks()

create_task("New Task", "Description for the new task")
print("Tasks after creating a new task:")
display_tasks()

read_task(2)

update_task(1, "Updated Task 1", "New description for Task 1")
print("Tasks after updating Task 1:")
display_tasks()

delete_task(3)
print("Tasks after deleting Task 3:")
display_tasks()

# -----------------------------------------------------------------------------
# Conclusion
# -----------------------------------------------------------------------------

"""
- Modularisation breaks down complex systems into manageable modules.
- Use Case Analysis maps user-system interactions for better planning.
- Sequence Diagrams illustrate the flow of interactions between components.
- Separation of Concerns ensures clean, maintainable, and scalable code.
- Class Diagrams provide a visual representation of the application's structure.
- CRUD Matrices document relationships and operations between entities.
"""




