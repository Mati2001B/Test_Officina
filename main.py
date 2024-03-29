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


def example_out_fun() -> list[tuple[float, float]]:
    return [(10., 10.) for _ in range(0, 21)]
    # same as
    # return [(10., 10.)] * 20
    # it creates a list inserting in a loop (0->19) the same element (10.,10.)
    # the underscore is used to define a variable that will not be used


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

