# Software Design: Learning about Diagrams Module

## Introduction

This learning module introduces essential software design principles through two projects:

- **Task Manager** (a Python-based CLI application)
- **MusicPlayer** (a Python-based desktop application with a tkinter GUI)

This module uses **draw.io** to create diagrams (use case, sequence, class, and CRUD matrix) for designing modular, maintainable software. You'll learn **modularisation**, **separation of concerns**, and the **Model-View-Controller (MVC)** pattern to build robust applications.

### Project Repositories:

- [Task Manager](https://github.com/GowerCampbell/TaskManager)  
- [MusicPlayer](https://github.com/GowerCampbell/MusicPlayer)

This module is ideal for mastering object-oriented design with theory and hands-on experience.

---

## Software Design Principles

### Modularisation

Breaks systems into independent, reusable modules:

- **Independence**: Minimize dependencies.
- **Interchangeability**: Swap modules seamlessly.
- **Reusability**: Use modules across systems.
- **Encapsulation**: Expose only necessary interfaces.
- **Scalability**: Add/remove modules easily.

---

### Use Case Analysis

Captures user-system interactions to define requirements:

- **Actors** (users/systems)
- **Use Cases** (functionalities)
- Useful for stakeholder discussions and testing.

---

### Sequence Diagrams

Show interaction flows between components:

- Lifelines
- Messages
- Activation bars

Helps identify system dynamics and bottlenecks.

---

### Separation of Concerns (MVC)

Uses the **MVC pattern**:

- **Model**: Data + business logic
- **View**: User interface
- **Controller**: Mediates input and updates

---

### Class Diagrams

Depicts static structure:

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

- **draw.io**: For creating diagrams (use case, sequence, class, CRUD).
- **Python**:
  - **Task Manager**: File I/O via standard library
  - **MusicPlayer**:
    - `tkinter` (GUI)
    - `pygame` (audio)
    - `sqlite3` (database)
    - `mutagen` (metadata)
    - `pillow` (image processing)
    - `TkinterDnD2` (drag-and-drop)

---

## Project 1: Task Manager

### Overview

A Python CLI app with full CRUD functionality, using file storage and MVC.

- **Repo**: [Task Manager](https://github.com/GowerCampbell/TaskManager)

### Features

- **Create**: Add task
- **Read**: View tasks
- **Update**: Edit task
- **Delete**: Remove task
- **Mark Complete**

### Design Artifacts

Diagrams (in `diagrams/taskmanager_diagrams/`):

- **Use Case Diagram**: [TM_UseCaseDiagram.pdf](diagrams/taskmanager_diagrams/TM_UseCaseDiagram.pdf) - Actors (User, Admin), Use Cases (Add, Delete, Mark Complete)
- **Sequence Diagram**: [TM_SequenceDiagram.pdf](diagrams/taskmanager_diagrams/TM_SequenceDiagram.pdf) - Flow from input to storage
- **Class Diagram**: [TM_ClassDiagram.pdf](diagrams/taskmanager_diagrams/TM_ClassDiagram.pdf) - `Task`, `FileHandler`
- **CRUD Matrix**: [CRUD_TM.pdf](docs/CRUD_TM.pdf)

### MVC Responsibilities

- **Model**: Data + file operations
- **View**: Displays tasks, handles input
- **Controller**: Coordinates logic + view

### Implementation

In `knotes.py`:

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

Diagrams (in `diagrams/musicplayer_diagrams/`):

- **Use Case Diagram**: [MP_UseCaseDiagram.pdf](diagrams/musicplayer_diagrams/MP_UseCaseDiagram.pdf) - Users & audio system, media actions
- **Sequence Diagram**: [MP_SequenceDiagram.pdf](diagrams/musicplayer_diagrams/MP_SequenceDiagram.pdf) - Playing track via GUI → DB → UI
- **Class Diagram**: [MP_ClassDiagram.pdf](diagrams/musicplayer_diagrams/MP_ClassDiagram.pdf) - `MusicPlayer`, `Song`, `Playlist`, DB relations
- **CRUD Matrix**: [CRUD_MP.pdf](docs/CRUD_MP.pdf)

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

In `music_player.py` (assumed, not visible in screenshot):

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
- Drag-and-drop supports `.png`, `.jpg`, `.jpeg`, `.gif`
- Diagrams in `diagrams/musicplayer_diagrams/`

---

## How to Use This Module

### 1. Study the Theory

Review design principles to understand the architectural mindset.

### 2. Explore Task Manager

```bash
# Clone
git clone https://github.com/GowerCampbell/TaskManager
```

- Run `knotes.py`
- View diagrams in `diagrams/taskmanager_diagrams/`:
  - [Use Case](diagrams/taskmanager_diagrams/TM_UseCaseDiagram.pdf)
  - [Sequence](diagrams/taskmanager_diagrams/TM_SequenceDiagram.pdf)
  - [Class](diagrams/taskmanager_diagrams/TM_ClassDiagram.pdf)

### 3. Explore MusicPlayer

```bash
# Clone and install
git clone https://github.com/GowerCampbell/MusicPlayer
pip install pygame mutagen pillow tkinterdnd2
```

- Add audio files
- Run `music_player.py`
- Explore features and diagrams in `diagrams/musicplayer_diagrams/`

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
python knotes.py
python music_player.py
```

---

## Design with draw.io

- Open `.drawio` files in [draw.io](https://draw.io):
  - Task Manager: [TM_ClassDiagram.drawio](diagrams/drawio_files/TM_ClassDiagram.drawio), [TM_SequenceDiagram.drawio](diagrams/drawio_files/TM_SequenceDiagram.drawio), [TM_UseCaseDiagram.drawio](diagrams/drawio_files/TM_UseCaseDiagram.drawio)
  - MusicPlayer: (assumed similar `.drawio` files for MusicPlayer, not visible in screenshot)
- Use diagram descriptions to recreate or modify

---

## Creating and Hosting Diagrams

1. Create diagrams in draw.io
2. Save as `.drawio` files
3. Upload to:

```
Task Manager: diagrams/drawio_files/
MusicPlayer: diagrams/drawio_files/
```

4. Export as PDF to:

```
Task Manager: diagrams/taskmanager_diagrams/
MusicPlayer: diagrams/musicplayer_diagrams/
```

5. Ensure filenames match links in README

---

## Conclusion

This module connects theory to practice:

- **Task Manager**: CLI + file storage
- **MusicPlayer**: GUI + DB + audio + animation

Use the diagrams to visualize structure. Clone, explore, and extend the code to enhance your design skills.


# Software Design Learning Module

## Introduction

This learning module introduces essential software design principles through two projects:

- **Task Manager** (a Python-based CLI application)
- **MusicPlayer** (a Python-based desktop application with a tkinter GUI)

The module uses **draw.io** to create diagrams (use case, sequence, class, and CRUD matrix) for designing modular, maintainable software. You'll learn **modularisation**, **separation of concerns**, and the **Model-View-Controller (MVC)** pattern to build robust applications.

### Project Repositories:

- [Task Manager](https://github.com/GowerCampbell/TaskManager)  
- [MusicPlayer](https://github.com/GowerCampbell/MusicPlayer)

This module is ideal for mastering object-oriented design with theory and hands-on experience.

---

## Software Design Principles

### Modularisation

Breaks systems into independent, reusable modules:

- **Independence**: Minimize dependencies.
- **Interchangeability**: Swap modules seamlessly.
- **Reusability**: Use modules across systems.
- **Encapsulation**: Expose only necessary interfaces.
- **Scalability**: Add/remove modules easily.

---

### Use Case Analysis

Captures user-system interactions to define requirements:

- **Actors** (users/systems)
- **Use Cases** (functionalities)
- Useful for stakeholder discussions and testing.

---

### Sequence Diagrams

Show interaction flows between components:

- Lifelines
- Messages
- Activation bars

Helps identify system dynamics and bottlenecks.

---

### Separation of Concerns (MVC)

Uses the **MVC pattern**:

- **Model**: Data + business logic
- **View**: User interface
- **Controller**: Mediates input and updates

---

### Class Diagrams

Depicts static structure:

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

- **draw.io**: For creating diagrams (use case, sequence, class, CRUD).
- **Python**:
  - **Task Manager**: File I/O via standard library
  - **MusicPlayer**:
    - `tkinter` (GUI)
    - `pygame` (audio)
    - `sqlite3` (database)
    - `mutagen` (metadata)
    - `pillow` (image processing)
    - `TkinterDnD2` (drag-and-drop)

---

## Project 1: Task Manager

### Overview

A Python CLI app with full CRUD functionality, using file storage and MVC.

- **Repo**: [Task Manager](https://github.com/GowerCampbell/TaskManager)

### Features

- **Create**: Add task
- **Read**: View tasks
- **Update**: Edit task
- **Delete**: Remove task
- **Mark Complete**

### Design Artifacts

Diagrams (in `diagrams/taskmanager_diagrams/`):

- **Use Case Diagram**: [TM_UseCaseDiagram.pdf](diagrams/taskmanager_diagrams/TM_UseCaseDiagram.pdf) - Actors (User, Admin), Use Cases (Add, Delete, Mark Complete)
- **Sequence Diagram**: [TM_SequenceDiagram.pdf](diagrams/taskmanager_diagrams/TM_SequenceDiagram.pdf) - Flow from input to storage
- **Class Diagram**: [TM_ClassDiagram.pdf](diagrams/taskmanager_diagrams/TM_ClassDiagram.pdf) - `Task`, `FileHandler`
- **CRUD Matrix**: [CRUD_TM.pdf](docs/CRUD_TM.pdf)

### MVC Responsibilities

- **Model**: Data + file operations
- **View**: Displays tasks, handles input
- **Controller**: Coordinates logic + view

### Implementation

In `knotes.py`:

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

Diagrams (in `diagrams/musicplayer_diagrams/`):

- **Use Case Diagram**: [MP_UseCaseDiagram.pdf](diagrams/musicplayer_diagrams/MP_UseCaseDiagram.pdf) - Users & audio system, media actions
- **Sequence Diagram**: [MP_SequenceDiagram.pdf](diagrams/musicplayer_diagrams/MP_SequenceDiagram.pdf) - Playing track via GUI → DB → UI
- **Class Diagram**: [MP_ClassDiagram.pdf](diagrams/musicplayer_diagrams/MP_ClassDiagram.pdf) - `MusicPlayer`, `Song`, `Playlist`, DB relations
- **CRUD Matrix**: [CRUD_MP.pdf](docs/CRUD_MP.pdf)

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

In `music_player.py` (assumed, not visible in screenshot):

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
- Drag-and-drop supports `.png`, `.jpg`, `.jpeg`, `.gif`
- Diagrams in `diagrams/musicplayer_diagrams/`

---

## How to Use This Module

### 1. Study the Theory

Review design principles to understand the architectural mindset.

### 2. Explore Task Manager

```bash
# Clone
git clone https://github.com/GowerCampbell/TaskManager
```

- Run `knotes.py`
- View diagrams in `diagrams/taskmanager_diagrams/`:
  - [Use Case](diagrams/taskmanager_diagrams/TM_UseCaseDiagram.pdf)
  - [Sequence](diagrams/taskmanager_diagrams/TM_SequenceDiagram.pdf)
  - [Class](diagrams/taskmanager_diagrams/TM_ClassDiagram.pdf)

### 3. Explore MusicPlayer

```bash
# Clone and install
git clone https://github.com/GowerCampbell/MusicPlayer
pip install pygame mutagen pillow tkinterdnd2
```

- Add audio files
- Run `music_player.py`
- Explore features and diagrams in `diagrams/musicplayer_diagrams/`

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
python knotes.py
python music_player.py
```

---

## Design with draw.io

- Open `.drawio` files in [draw.io](https://draw.io):
  - Task Manager: [TM_ClassDiagram.drawio](diagrams/drawio_files/TM_ClassDiagram.drawio), [TM_SequenceDiagram.drawio](diagrams/drawio_files/TM_SequenceDiagram.drawio), [TM_UseCaseDiagram.drawio](diagrams/drawio_files/TM_UseCaseDiagram.drawio)
  - MusicPlayer: (assumed similar `.drawio` files for MusicPlayer, not visible in screenshot)
- Use diagram descriptions to recreate or modify

---

## Creating and Hosting Diagrams

1. Create diagrams in draw.io
2. Save as `.drawio` files
3. Upload to:

```
Task Manager: diagrams/drawio_files/
MusicPlayer: diagrams/drawio_files/
```

4. Export as PDF to:

```
Task Manager: diagrams/taskmanager_diagrams/
MusicPlayer: diagrams/musicplayer_diagrams/
```

5. Ensure filenames match links in README

---

## Conclusion

This module connects theory to practice:

- **Task Manager**: CLI + file storage
- **MusicPlayer**: GUI + DB + audio + animation

Use the diagrams to visualize structure. Clone, explore, and extend your code to enhance your design skills.


