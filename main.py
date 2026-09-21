import curses
from curses import wrapper
from collections import deque
import time


# ─────────────────────────────────────────────
# MAZE
# ─────────────────────────────────────────────

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


# ─────────────────────────────────────────────
# COLORS
# ─────────────────────────────────────────────

BLUE = 1
RED = 2
GREEN = 3
YELLOW = 4
WHITE = 5


# ─────────────────────────────────────────────
# FIND POSITION
# ─────────────────────────────────────────────

def find_start(maze, symbol):
    """Find the position of a specific symbol."""

    for row, line in enumerate(maze):
        for col, value in enumerate(line):

            if value == symbol:
                return row, col

    return None


# ─────────────────────────────────────────────
# FIND NEIGHBORS
# ─────────────────────────────────────────────

def find_neighbors(maze, row, col):
    """Return all valid neighboring positions."""

    neighbors = []

    directions = [
        (-1, 0),  # UP
        (1, 0),   # DOWN
        (0, -1),  # LEFT
        (0, 1)    # RIGHT
    ]

    for row_change, col_change in directions:

        new_row = row + row_change
        new_col = col + col_change

        # Check boundaries
        if not (0 <= new_row < len(maze)):
            continue

        if not (0 <= new_col < len(maze[0])):
            continue

        # Don't walk through walls
        if maze[new_row][new_col] == "#":
            continue

        neighbors.append((new_row, new_col))

    return neighbors


# ─────────────────────────────────────────────
# DRAW MAZE
# ─────────────────────────────────────────────

def draw_maze(stdscr, maze, visited=None, path=None, current=None):

    visited = visited or set()
    path = path or []

    for row, line in enumerate(maze):

        for col, value in enumerate(line):

            position = (row, col)
            screen_col = col * 2

            # Current BFS position
            if position == current:
                stdscr.addstr(
                    row,
                    screen_col,
                    "● ",
                    curses.color_pair(YELLOW)
                )

            # Final path
            elif position in path:
                stdscr.addstr(
                    row,
                    screen_col,
                    "◆ ",
                    curses.color_pair(GREEN)
                )

            # Visited cells
            elif position in visited:
                stdscr.addstr(
                    row,
                    screen_col,
                    "· ",
                    curses.color_pair(WHITE)
                )

            # Start
            elif value == "O":
                stdscr.addstr(
                    row,
                    screen_col,
                    "O ",
                    curses.color_pair(BLUE)
                )

            # End
            elif value == "X":
                stdscr.addstr(
                    row,
                    screen_col,
                    "X ",
                    curses.color_pair(RED)
                )

            # Wall / empty space
            else:
                stdscr.addstr(
                    row,
                    screen_col,
                    f"{value} ",
                    curses.color_pair(BLUE)
                )


# ─────────────────────────────────────────────
# DISPLAY STATUS
# ─────────────────────────────────────────────

def draw_status(stdscr, message):

    height, width = stdscr.getmaxyx()

    status = message

    if len(status) < width:
        stdscr.addstr(
            height - 2,
            0,
            status,
            curses.color_pair(WHITE)
        )


# ─────────────────────────────────────────────
# BFS PATHFINDING
# ─────────────────────────────────────────────

def find_path(maze, stdscr):

    start = find_start(maze, "O")
    end = find_start(maze, "X")

    if start is None or end is None:
        return None

    # Queue contains:
    # (current_position, path_to_current_position)
    queue = deque()

    queue.append((start, [start]))

    visited = {start}

    while queue:

        current, path = queue.popleft()

        # ───── Draw current BFS step ─────

        stdscr.clear()

        draw_maze(
            stdscr,
            maze,
            visited=visited,
            current=current
        )

        draw_status(
            stdscr,
            f"BFS searching... Visited: {len(visited)}"
        )

        stdscr.refresh()

        time.sleep(0.12)

        # ───── Check if destination reached ─────

        if current == end:

            # Animate final path
            for position in path:

                stdscr.clear()

                draw_maze(
                    stdscr,
                    maze,
                    visited=visited,
                    path=path[:path.index(position) + 1],
                    current=position
                )

                draw_status(
                    stdscr,
                    f"Path found! Length: {len(path) - 1}"
                )

                stdscr.refresh()

                time.sleep(0.08)

            return path

        # ───── Explore neighbors ─────

        row, col = current

        for neighbor in find_neighbors(maze, row, col):

            if neighbor in visited:
                continue

            visited.add(neighbor)

            new_path = path + [neighbor]

            queue.append(
                (neighbor, new_path)
            )

    return None


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main(stdscr):

    # Don't show cursor
    curses.curs_set(0)

    # Initialize colors
    curses.start_color()

    curses.init_pair(
        BLUE,
        curses.COLOR_BLUE,
        curses.COLOR_BLACK
    )

    curses.init_pair(
        RED,
        curses.COLOR_RED,
        curses.COLOR_BLACK
    )

    curses.init_pair(
        GREEN,
        curses.COLOR_GREEN,
        curses.COLOR_BLACK
    )

    curses.init_pair(
        YELLOW,
        curses.COLOR_YELLOW,
        curses.COLOR_BLACK
    )

    curses.init_pair(
        WHITE,
        curses.COLOR_WHITE,
        curses.COLOR_BLACK
    )

    # Run BFS
    path = find_path(MAZE, stdscr)

    # Final screen
    stdscr.clear()

    if path:

        draw_maze(
            stdscr,
            MAZE,
            path=path
        )

        draw_status(
            stdscr,
            f"✓ Shortest path found! "
            f"Steps: {len(path) - 1} | Press any key to exit."
        )

    else:

        draw_status(
            stdscr,
            "✗ No path found. Press any key to exit."
        )

    stdscr.refresh()

    stdscr.getch()


# ─────────────────────────────────────────────
# START PROGRAM
# ─────────────────────────────────────────────

wrapper(main)
