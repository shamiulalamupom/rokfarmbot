import math

def heliocentric_orbit(start_x, start_y, total_rounds):
    """
    Generate a graph-like orbit path where the orbit expands symmetrically (x and y go one extra step per round).

    Args:
        start_x (int): Initial X-coordinate of the center.
        start_y (int): Initial Y-coordinate of the center.
        total_rounds (int): Number of orbits to generate.

    Returns:
        list: List of (x, y) coordinates in the orbit pattern.
    """
    x, y = start_x, start_y
    path = [(x, y)]  # Initialize the path with the start point
    orbit_radius = 1  # Initial orbit radius

    for round in range(total_rounds):
        # Directions with steps: [(dx, dy, steps)]
        directions = [
            (0, 1, orbit_radius),                                                  # Up
            (1, 0, orbit_radius + round),       # Right
            (0, -1, orbit_radius * 2),                                             # Down
            (-1, 0, orbit_radius * 2),                                             # Left
            (0, 1, orbit_radius),                                                  # Up
        ]

        for dx, dy, steps in directions:
            for _ in range(steps):
                x += dx
                y += dy
                path.append((x, y))

        # Increase orbit radius after completing a full round
        orbit_radius += 1

    return path


import matplotlib.pyplot as plt

if __name__ == "__main__":
    center_x, center_y = 0, 0
    total_steps = 3

    orbit_path = heliocentric_orbit(center_x, center_y, total_steps)

    # Extract x and y coordinates
    x_coords, y_coords = zip(*orbit_path)

    # Plot the orbit path
    plt.figure(figsize=(6, 6))
    plt.plot(x_coords, y_coords, marker="o", markersize=5, linestyle="-", color="blue")
    plt.scatter([center_x], [center_y], color="red", label="Center Point")
    plt.title("Heliocentric Orbit Simulation")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.legend()
    plt.grid()
    plt.axis("equal")
    plt.show()