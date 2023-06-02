# A* Search Visualizer
Required software: Python 3

To run the program: cd into 'search visualizer' directory, then run GUI.py

This project aims to visualize how the A* pathfinding algorithm runs and show the effects of different heuristics. The user is able to choose a starting position on the grid, a desired goal position, draw obstacles, choose a heuristic, and run the A* search algorithm to find a path from the start to the goal. This visualizer supports the following heuristics:

Manhattan distance: The Manhattan distance performs comparatively well. It is consistent, ensuring optimality/finding the shortest path. Compared to the other consistent heuristics listed here, it checks a relatively low amount of states/grid positions, making it efficient.

Euclidean distance: Another consistent heuristic. However, it checks more unnecessary grid positions than the Manhattan heuristic, since the Manhattan distance is always greater than or equal to the Euclidean distance.

Trivial heuristic: Always returns 0. The A* search algorithm essentially turns into a Uniform-Cost Search. While it is less computationally efficient, this still guarantees the finding the shortest path.

Double Manhattan: An inadmissible heuristic that returns double the Manhattan distance. This causes the A* search to degrade into a Greedy Breadth-First-Search algorithm. Less positions are checked, but finding the shortest path is not guaranteed.

Exact Heuristic: An exact heuristic value is computed by running another A* search for the given grid position. This causes the runtime to be very slow, but it is interesting to see how an exact heuristic leads to exploring the least amount of grid positions while still being optimal.

Controls:

Make/remove walls: click and drag on the grid

Choose starting position: enter the x,y coordinates and press the "Start" button

Choose goal position: enter the x,y coordinates and press the "Destination" button

Run pathfinding: choose the heuristic from the dropdown menu and press "Start Search"

Clear the grid: press "Clear"