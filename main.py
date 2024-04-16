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


def hw_track() -> float:
    return 0.8 * (47.8659 - 41.8691) / 2


def mean_points() -> list[tuple[float, float]]:
    x = get_x_mean_vec()
    y = get_y_mean_vec()
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


# Norms of vectors v and w
def v_norm() -> list[float]:
    x = get_x_mean_vec()
    y = get_y_mean_vec()
    return [np.sqrt((x[i+1] - x[i])**2 + (y[i+1] - y[i])**2) for i in range(0, 20)]


def w_norm() -> list[float]:
    x = get_x_mean_vec()
    y = get_y_mean_vec()
    return [np.sqrt((x[i-1] - x[i])**2 + (y[i-1] - y[i])**2) for i in range(0, 20)]


# Define dot product of vectors as a tuple
def dot() -> list[tuple[float, float]]:
    v = v_vector()
    w = w_vector()
    return [(v[i][0] * w[i][0]) + (v[i][1] * w[i][1]) for i in range(0,20)]


# Find angle of the bisector from dot product formula
def bisector_angle() -> list[float]:
    dotp = dot()
    vn = v_norm()
    wn = w_norm()
    return [np.arccos(dotp[i] / (2 * vn[i] * wn[i])) for i in range(0, 20)]


# Find bisector vector by rotating the w vector of a theta angle
def rotated_w() -> list[tuple[float, float]]:
    for i in range(0, 20):
        theta = bisector_angle()
        w = w_vector()
        z_x = []
        z_y = []
        z_x = [w[i][0] * np.cos(theta[i]) + w[i][1] * np.sin(theta[i]) for i in range(0, 20)]
        z_x.append(z_x)
        z_y = [-w[i][0]*np.sin(theta[i]) + w[i][1]*np.cos(theta[i]) for i in range(0, 20)]
        z_y.append(z_y)
    return [(z_x[i], z_y[i]) for i in range(0, 20)]


# In order to give the right length to the vector we normalize the z vector
# and give it the length of the half width of the track.
# We define the resulting vector as u
def u_vector() -> list[tuple[float, float]]:
    z = rotated_w()
    wn = w_norm()
    hw = hw_track()
    return [((z[i][0] * hw / wn[i]), (z[i][1] * hw / wn[i])) for i in range(0, 20)]


# Rotate the z vector of 180 degrees to find the other set of coordinates
# We call the new vectors as a
def a_vector() -> list[tuple[float, float]]:
    for i in range(0, 20):
        u = u_vector()
        a_x = []
        a_y = []
        a_x = [u[i][0] * np.cos(np.pi) + u[i][1] * np.sin(np.pi) for i in range(0, 20)]
        a_x.append(a_x)
        a_y = [-u[i][0]*np.sin(np.pi) + u[i][1]*np.cos(np.pi) for i in range(0, 20)]
        a_y.append(a_y)
    return [(a_x[i], a_y[i]) for i in range(0, 20)]







# Dot product is negative or positive considering the theta angle (convex or concave)



