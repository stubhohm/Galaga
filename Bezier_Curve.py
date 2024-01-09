import math


def bezier_curve(
    starting_point,
    starting_control_point,
    finishing_point,
    finishing_control_point,
    time_step,
):
    P0 = starting_point
    P1 = starting_control_point
    P2 = finishing_point
    P3 = finishing_control_point
    t = time_step
    """
    Calculate the position and slope of a cubic Bézier curve at time t.

    Parameters:
    - defined above, wordy, entry varaibles, but makes it easier to understand when using function
    - P0, P1, P2, P3: Control points as (x, y) tuples.
    - t: Time step (0 <= t <= 1).

    Returns:
    - (x, y): Position on the curve at time t.
    - (dx, dy): Slope (derivative) of the curve at time t.
    """
    x = (
        (1 - t) ** 3 * P0[0]
        + 3 * (1 - t) ** 2 * t * P1[0]
        + 3 * (1 - t) * t**2 * P2[0]
        + t**3 * P3[0]
    )
    y = (
        (1 - t) ** 3 * P0[1]
        + 3 * (1 - t) ** 2 * t * P1[1]
        + 3 * (1 - t) * t**2 * P2[1]
        + t**3 * P3[1]
    )

    # Calculate the derivatives for the slope
    dx = (
        3 * (1 - t) ** 2 * (P1[0] - P0[0])
        + 6 * (1 - t) * t * (P2[0] - P1[0])
        + 3 * t**2 * (P3[0] - P2[0])
    )
    dy = (
        3 * (1 - t) ** 2 * (P1[1] - P0[1])
        + 6 * (1 - t) * t * (P2[1] - P1[1])
        + 3 * t**2 * (P3[1] - P2[1])
    )

    return (x, y), (dx, dy)


if __name__ == "__main__":
    print(
        "this main only runs if this file is ran, not if another program executes it: Bezier Curves"
    )
