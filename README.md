# Software Design Learning Module

## Introduction

This learning module introduces essential software design principles and demonstrates their application through two distinct projects:

- **Task Manager** (a Python-based CLI application)
- **MusicPlayer** (a Python-based desktop application with a tkinter GUI)

The module uses **draw.io** to create diagrams (use case, sequence, class, and CRUD matrix) that guide the design of modular, maintainable software systems. By exploring these projects, you'll learn how to apply **modularisation**, **separation of concerns**, and the **Model-View-Controller (MVC)** pattern to build robust applications.

### Project Repositories:

- [Task Manager](https://github.com/GowerCampbell/TaskManager)  
- [MusicPlayer](https://github.com/GowerCampbell/MusicPlayer)

This module is ideal for learners aiming to master object-oriented software design by combining theory and hands-on experience.

---

## Software Design Principles

### Modularisation

Breaks down systems into independent, reusable modules. Core concepts include:

- **Independence**: Minimize dependencies.
- **Interchangeability**: Swap modules without disruption.
- **Reusability**: Reuse modules across systems.
- **Encapsulation**: Expose only necessary interfaces.
- **Scalability**: Adapt by adding/removing modules.

---

### Use Case Analysis

Captures user-system interactions to define requirements. Diagrams highlight:

- **Actors** (users/systems)
- **Use Cases** (functionalities)
- Helps with stakeholder discussion and testing.

---

### Sequence Diagrams

Illustrate the flow of interactions between components using:

- Lifelines
- Messages
- Activation bars

These help understand system dynamics and performance bottlenecks.

---

### Separation of Concerns (MVC)

Applies the **MVC pattern**:

- **Model**: Data + business logic
- **View**: User interface
- **Controller**: Mediates input and updates

---

### Class Diagrams

Shows static structure:

- **Classes**: Attributes and methods
- **Relationships**: Inheritance, association, etc.

---

### CRUD Matrix

Tracks data operations:

| Entity | Create | Read | Update | Delete |
|--------|--------|------|--------|--------|
| Task   |   X    |  X   |   X    |   X    |

---

## Tools Used

- **draw.io**: Create use case, sequence, class, and CRUD diagrams.
- **Python**:
  - **Task Manager**: File I/O via standard library
  - **MusicPlayer**:
    - `tkinter` (GUI)
    - `pygame` (audio)
    - `sqlite3` (database)
    - `mutagen` (metadata)
    - `pillow` (image processing)
    - `TkinterDnD2` (drag-and-drop functionality)

---

## Project 1: Task Manager

### Overview

A Python CLI app with full CRUD functionality, using file storage and the MVC pattern.

- **Repo**: [Task Manager](https://github.com/GowerCampbell/TaskManager)

### Features

- **Create**: Add task
- **Read**: View tasks
- **Update**: Edit task
- **Delete**: Remove task
- **Mark Complete**

### Design Artifacts

Diagrams (available in `diagrams/` folder):

- **Use Case Diagram**: Actors (User, Admin), Use Cases (Add, Delete, Mark Complete), Includes/Extends
- **Sequence Diagram**: Flow from input → storage
- **Class Diagram**: `Task`, `FileHandler`
- **CRUD Matrix**: As above

### MVC Responsibilities

- **Model**: Data + file operations
- **View**: Displays tasks, handles input
- **Controller**: Coordinates logic + view

### Implementation

In `task_manager.py`:

- `Task` class
- CRUD functions
- File storage

---

## Project 2: MusicPlayer

### Overview

A GUI-based Python desktop app using tkinter + pygame with database integration.

- **Repo**: [MusicPlayer](https://github.com/GowerCampbell/MusicPlayer)

### Features

- Play/Pause, Skip Tracks, Volume
- Playlist Management (CRUD)
- Shuffle/Repeat
- Favorites
- Drag-and-Drop for cover images
- Animated beetle and firefly sprites

### Design Artifacts

Diagrams (available in `diagrams/` folder):

- **Use Case Diagram**: Users & audio system, various media actions
- **Sequence Diagram**: Playing track via GUI → DB → UI
- **Class Diagram**: `MusicPlayer`, `Song`, `Playlist`, DB relations
- **CRUD Matrix**:

| Entity   | Create | Read | Update | Delete |
|----------|--------|------|--------|--------|
| Song     |   X    |  X   |   -    |   -    |
| Playlist |   X    |  X   |   X    |   -    |
| Favorite |   X    |  X   |   -    |   X    |

### MVC Responsibilities

- **Model**: sqlite3 DB, file I/O, `mutagen` metadata
- **View**: tkinter GUI, album art, controls, animations
- **Controller**: User actions → DB/UI updates

### Implementation

In `music_player.py`:

- **Database**: sqlite3 for songs/playlists
- **GUI**: tkinter + drag-and-drop (TkinterDnD2)
- **Audio**: pygame.mixer
- **Metadata**: mutagen
- **Animations**: Sprites in `assets/`

---

## Getting Started with MusicPlayer

```bash
# Clone
git clone https://github.com/GowerCampbell/MusicPlayer.git
cd MusicPlayer

# Install dependencies
pip install pygame mutagen pillow tkinterdnd2

# Setup music folder
# Create and populate `music_folder/`
# Update path in music_player.py if needed

# Run
python music_player.py
```

**Notes**:

- Ensure `assets/` has sprite images (`beetle_sprite.png`, `firefly_sprite.png`)
- Drag-and-drop works for `.png`, `.jpg`, `.jpeg`, `.gif`
- Diagrams available in `diagrams/`

---

## How to Use This Module

### 1. Study the Theory

Review design principles to understand the architectural mindset.

### 2. Explore Task Manager

```bash
# Clone
git clone https://github.com/GowerCampbell/TaskManager
```

- Run `task_manager.py`
- View diagrams in `diagrams/`:
  - Use Case
  - Sequence
  - Class

### 3. Explore MusicPlayer

```bash
# Clone and install
git clone https://github.com/GowerCampbell/MusicPlayer
pip install pygame mutagen pillow tkinterdnd2
```

- Add audio files
- Run `music_player.py`
- Explore features and diagrams

### 4. Extend the Projects

- **Task Manager**: Add categories, GUI, DB storage
- **MusicPlayer**: Add delete, search, queue display

---

## Getting Started

### Prerequisites

- Python 3.x
- Libraries for MusicPlayer:
  - `pygame`
  - `mutagen`
  - `pillow`
  - `tkinterdnd2`

### Setup

```bash
# Clone repos
git clone <repo_url>

# Install MusicPlayer dependencies
pip install -r requirements.txt

# Run
python task_manager.py
python music_player.py
```

---

## Design with draw.io

- Open `.drawio` files in [draw.io](https://draw.io)
- Use diagram descriptions to recreate or modify

---

## Creating and Hosting Diagrams

1. Create diagrams in draw.io
2. Save as `.drawio` files
3. Upload to:

```
Task Manager: TaskManager/diagrams/
MusicPlayer: MusicPlayer/diagrams/
```

4. Make sure filenames match links in README

---

## Conclusion

This module connects theory to real-world projects:

- **Task Manager**: CLI + file storage
- **MusicPlayer**: GUI + DB + audio + animation

Use the diagrams to visualize the software structure. Clone, explore, and build on the code to sharpen your design skills.
