Use this updated `README.md` with your project name and GitHub username:

````markdown id="49321"
# Shortest Path Finder

A terminal-based maze solver built with Python that uses the **Breadth-First Search (BFS)** algorithm to find the shortest path from a starting point to a destination.

The maze is visualized directly in the terminal using Python's `curses` library, allowing you to watch the algorithm explore the maze step by step.

## Features

- Finds the shortest path using **Breadth-First Search (BFS)**
- Visualizes the pathfinding process in the terminal
- Uses a queue to implement BFS
- Tracks visited cells to prevent repeated exploration
- Uses `curses` for terminal-based visualization
- Works with a predefined 2D maze

## Technologies Used

- **Python**
- `curses`
- `queue`
- `time`

## How It Works

The maze uses the following symbols:

| Symbol | Meaning |
|--------|---------|
| `#` | Wall |
| `O` | Starting position |
| `X` | Destination |
| ` ` | Open path |

The program starts at `O` and explores neighboring cells using **BFS**.

BFS explores the maze level by level:

```text
Start
  ↓
Nearby cells
  ↓
Next level of cells
  ↓
Next level
  ↓
Destination
````

Since BFS explores cells based on their distance from the starting point, it finds the **shortest path** when every movement has the same cost.

## Project Structure

```text
Shortest-Path-Finder/
│
├── main.py
└── README.md
```

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

## Running the Project

Run the program:

```bash
python main.py
```

The maze will appear in the terminal and the BFS algorithm will begin searching for the destination.

### Windows Users

The `curses` module is not included by default with Python on Windows.

Install the Windows-compatible version:

```bash
pip install windows-curses
```

Then run:

```bash
python main.py
```

## Algorithm

### Breadth-First Search (BFS)

BFS uses a **queue (FIFO)** to explore the maze.

The basic process is:

1. Find the starting position.
2. Add the starting position to the queue.
3. Remove the next position from the queue.
4. Check its neighboring cells.
5. Ignore walls and already visited cells.
6. Add valid neighboring cells to the queue.
7. Continue until the destination is reached.

### Time Complexity

For a grid containing `V` accessible cells and `E` connections:

```text
Time Complexity:  O(V + E)
Space Complexity: O(V)
```

For a grid, this can be represented approximately as:

```text
Time:  O(rows × columns)
Space: O(rows × columns)
```

## Future Improvements

* Add DFS pathfinding
* Add Dijkstra's algorithm
* Add A* pathfinding
* Generate random mazes
* Allow users to create custom mazes
* Add adjustable animation speed
* Display the number of visited cells
* Display path length
* Display execution time
* Add a graphical interface using Pygame

## Learning Goals

This project was created to practice:

* Python programming
* Functions
* 2D lists
* Queues
* Sets
* Graph traversal
* Breadth-First Search
* Pathfinding
* Terminal-based visualization
* Algorithm complexity

## Author

**Shwesh Dubey**

GitHub: [@shweshd](https://github.com/shweshd)

## License

This project is open source and available under the MIT License.

```
```
