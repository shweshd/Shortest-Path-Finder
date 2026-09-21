# Shortest Path Finder

A terminal-based maze solver built with **Python** that uses the **Breadth-First Search (BFS)** algorithm to find the shortest path from a starting point to a destination.

The maze is visualized directly in the terminal using Python's `curses` library. The program shows the BFS algorithm exploring the maze step by step and then animates the shortest path once the destination is reached.

---

## Features

* Finds the **shortest path** using Breadth-First Search (BFS)
* Automatically detects the starting point (`O`)
* Automatically detects the destination (`X`)
* Visualizes BFS exploration in real time
* Displays visited cells during the search
* Highlights the cell currently being explored
* Animates the final shortest path
* Displays the number of visited cells
* Displays the final path length
* Detects when no path exists
* Uses a queue for BFS traversal
* Uses `curses` for terminal-based visualization
* Supports custom 2D maze layouts

---

## Demo

The maze uses the following symbols:

| Symbol | Meaning        |
| ------ | -------------- |
| `#`    | Wall           |
| `O`    | Starting point |
| `X`    | Destination    |
| ` `    | Open path      |

During the search, the program uses different symbols to visualize the algorithm:

| Symbol | Meaning                     |
| ------ | --------------------------- |
| `●`    | Current cell being explored |
| `·`    | Visited cell                |
| `◆`    | Shortest path               |
| `O`    | Starting point              |
| `X`    | Destination                 |

---

## How It Works

The program first searches the maze for:

```text
O → Starting point
X → Destination
```

It then uses **Breadth-First Search (BFS)** to explore the maze.

BFS explores cells level by level:

```text
             Start
               ↓
        ┌──────┴──────┐
        ↓             ↓
     Level 1       Level 1
        ↓             ↓
     Level 2       Level 2
        ↓
     Level 3
        ↓
   Destination
```

Because BFS explores all positions at the current distance before moving to the next distance, the first time it reaches the destination, the path is the **shortest path** when every movement has the same cost.

---

## BFS Process

The algorithm follows these steps:

1. Find the starting position `O`.
2. Find the destination `X`.
3. Add the starting position to the queue.
4. Mark the starting position as visited.
5. Remove the next position from the queue.
6. Find its neighboring cells.
7. Ignore walls (`#`).
8. Ignore cells that have already been visited.
9. Add valid neighbors to the queue.
10. Continue until `X` is reached.
11. Return and animate the shortest path.
12. If the queue becomes empty, report that no path exists.

---

## Example Maze

The maze can be represented as a 2D list:

```python
MAZE = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
```

You can modify the maze to create your own layouts.

The program automatically searches for `O` and `X`, so the pathfinding algorithm does not need their coordinates to be manually provided.

---

## Visualization

During BFS, the terminal displays the algorithm's progress:

```text
BFS searching... Visited: 18
```

Once the destination is found:

```text
Path found! Length: 14
```

The final screen displays:

```text
Shortest path found! Steps: 14 | Press any key to exit.
```

If no valid route exists:

```text
No path found. Press any key to exit.
```

---

## Technologies Used

* **Python**
* `curses`
* `collections.deque`
* `time`

### Python Concepts Used

* Functions
* Lists
* 2D lists
* Tuples
* Sets
* Queues
* Loops
* Conditional statements
* Coordinate systems
* Graph traversal
* Breadth-First Search
* Time-based animation

---

## Project Structure

```text
Shortest-Path-Finder/
│
├── main.py
└── README.md
```

---

## Installation

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

Clone the repository:

```bash
git clone https://github.com/shweshd/Shortest-Path-Finder.git
```

Navigate into the project directory:

```bash
cd Shortest-Path-Finder
```

---

## Windows Installation

Python's standard library does not include `curses` support on Windows.

Install the Windows-compatible package:

```bash
pip install windows-curses
```

After installation, run the program:

```bash
python main.py
```

---

## Running the Project

Run:

```bash
python main.py
```

The terminal will display the maze and begin the BFS search automatically.

The algorithm will:

```text
Find O
   ↓
Start BFS
   ↓
Explore neighboring cells
   ↓
Mark visited cells
   ↓
Find X
   ↓
Animate shortest path
   ↓
Display path length
```

Press any key after the result is displayed to exit the program.

---

## Algorithm

### Breadth-First Search (BFS)

Breadth-First Search is a graph traversal algorithm that explores nodes level by level.

In this project, each accessible cell in the maze can be treated as a **node**, while movement between adjacent cells represents an **edge**.

For example:

```text
    A
   / \
  B   C
 / \
D   E
```

BFS explores:

```text
A
↓
B, C
↓
D, E
```

The project applies the same idea to the maze grid.

---

## Why BFS Finds the Shortest Path

Suppose every movement has a cost of `1`:

```text
O → → → X
```

This path has:

```text
3 movements
```

BFS checks paths based on their distance from the starting position.

Therefore, when BFS reaches `X`, there cannot be another path with fewer movements that has not already been considered.

This makes BFS suitable for finding the shortest path in an **unweighted maze**.

---

## Data Structures

### `deque`

The program uses:

```python
from collections import deque
```

A `deque` is used as the BFS queue.

New positions are added using:

```python
queue.append(position)
```

The next position is removed using:

```python
queue.popleft()
```

This gives the required **FIFO (First In, First Out)** behavior of BFS.

### `set`

The program uses a set to store visited cells:

```python
visited = {start}
```

This prevents the algorithm from repeatedly exploring the same cell.

---

## Time Complexity

For a grid containing `V` accessible cells and `E` connections:

```text
Time Complexity:  O(V + E)
Space Complexity: O(V)
```

For a rectangular grid with `rows × columns` cells, this can be approximated as:

```text
Time:  O(rows × columns)

Space: O(rows × columns)
```

The exact amount of work depends on the number of accessible cells in the maze.

---

## Important Limitation

BFS finds the shortest path based on the **number of movements**.

It assumes that every movement has the same cost:

```text
↑ = 1
↓ = 1
← = 1
→ = 1
```

If different cells have different movement costs, BFS is not the appropriate algorithm.

Algorithms such as **Dijkstra's Algorithm** or **A*** can be used for weighted pathfinding.

---

## Future Improvements

Possible improvements for this project include:

* Add DFS pathfinding
* Add Dijkstra's algorithm
* Add A* pathfinding
* Generate random mazes
* Allow users to enter their own maze
* Load mazes from text files
* Add adjustable animation speed
* Add keyboard controls
* Display execution time
* Compare BFS, DFS, Dijkstra, and A*
* Add multiple start and destination points
* Add weighted maze cells
* Add a graphical interface using Pygame

---

## Learning Goals

This project was created to practice:

* Python programming
* Functions
* 2D lists
* Tuples
* Sets
* Queues
* `deque`
* Graph traversal
* Breadth-First Search
* Shortest-path algorithms
* Coordinate-based navigation
* Terminal visualization
* Algorithm complexity

---

## Author

**Shwesh Dubey**

GitHub: [@shweshd](https://github.com/shweshd)

---

## License

This project is open source and available under the **MIT License**.
