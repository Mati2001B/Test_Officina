import numpy as np
def get_x_mean_vec() -> list[float]:
    """
    Represents the mean value of the x coord for all the segments.
    A track is approximated to N segments (in our case divided in 21 segments).
    :return: the list of all the approximated x coordinates, each index refers to the segment (0-> first segment)
    """
    return [
        -1.,
        -0.208053691275168,
        0.583892617449664,
        1.37623134191865,
        2.00816396915341,
        2.25000000000000,
        2.25000000000000,
        2.25000000000000,
        2.19203606378251,
        1.73898945276698,
        1.,
        0.208053691275168,
        -0.583892617449664,
        -1.37623134191865,
        -2.00816396915341,
        -2.25000000000000,
        -2.25000000000000,
        -2.25000000000000,
        -2.19203606378251,
        -1.73898945276698,
        -1.
    ]


def get_y_mean_vec() -> list[float]:
    """
    Represents the mean value of the y coord for all the segments.
    A track is approximated to N segments (in our case divided in 21 segments).
    :return: the list of all the approximated y coordinates, each index refers to the segment (0-> first segment)
    """

    return [
        2.25000000000000,
        2.25000000000000,
        2.25000000000000,
        2.19203606378251,
        1.73898945276698,
        1.,
        0.208053691275168,
        -0.583892617449664,
        -1.37623134191865,
        -2.00816396915341,
        -2.25000000000000,
        -2.25000000000000,
        -2.25000000000000,
        -2.19203606378251,
        -1.73898945276698,
        -1.,
        -0.208053691275168,
        0.583892617449664,
        1.37623134191865,
        2.00816396915341,
        2.25000000000000
    ]


def get_track_width() -> float:
    """
    Get the track width (divide it by 2 if you need the distance from the center to outer)
    :return: track width
    """
    return 0.8 * (47.8659 - 41.8691)


x = get_x_mean_vec()
y = get_y_mean_vec()


def mean_points() -> list[tuple[float, float]]:
    return [(x[i], y[i]) for i in range(len(x))]


if __name__ == "__main__":
    # You need to calculate the outer and inner boundaries.
    # use the provided functions to get the data.
    # create a new function that does the
    # calculation and then return the result (without side effect)
    # so the desired output would be having a list of (x,y) coord for inner boundary
    # and (x,y) coord for outer boundary (each with 20 elements, since we have 20 segments)
    # (x,y) is a tuple => list[tuple[float]]
    # GL HF
    pass  # no operation, used to say that the fun does nothing. remove it!


# Half width of track
hw = 0.8 * (47.8659 - 41.8691) / 2

"""
We iteratively calculate the angle described by the segments connecting three subsequent points.
The bisector of said angle coincides with the section of the track in the i-th point of the triad.
"""

# Define vectors v connecting points (i) and (i+1) as a tuple
def v_vector() -> list[tuple[float, float]]:
    x = get_x_mean_vec()
    y = get_y_mean_vec()
    return [((x[i+1] - x[i]), (y[i+1] - y[i])) for i in range(0, 20)]


# Define vectors w connecting points (i) and (i-1) as a tuple
def w_vector() -> list[tuple[float, float]]:
    x = get_x_mean_vec()
    y = get_y_mean_vec()
    return [((x[i-1] - x[i]), (y[i-1] - y[i])) for i in range(0, 20)]


v = v_vector()
w = w_vector()


# Norms of vectors v and w
def v_norm() -> list[float]:
    return [np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2) for i in range(0, 20)]


def w_norm() -> list[float]:
    return [np.sqrt((x[i-1] - x[i])**2 + (y[i-1] - y[i])**2) for i in range(0, 20)]


vn = v_norm()
wn = w_norm()


# Define dot product of vectors as a tuple
def dot() -> list[tuple[float, float]]:
    return [(v[i][0] * w[i][0]) + (v[i][1] * w[i][1]) for i in range(0,20)]


dot = dot()


# Find angle of the bisector from dot product formula
def theta() -> list[float]:
    return [np.arccos(dot[i] / (2 * vn[i] * wn[i])) for i in range(0, 20)]


theta = theta()


# Find coordinates of the bisector from the dot product formula
def bisector() -> list[tuple[float, float]]:
    return [((vn[i]*hw*np.cos(theta[i])/v[i][0]), (vn[i]*hw*np.cos(theta[i])/v[i][1])) for i in range(0, 20)]


z = bisector()


