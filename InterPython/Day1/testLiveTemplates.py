import math


class Point:
    """
    Represents a point in 2D geometric space
    """
    def __init__(self, x=0, y=0):
        """
        Initializes the position of a new point.
        If they are not specified, the point defaults to the origin.
        :param x: x coordinate
        :param y: y coordinate
        """
        self.x = x
        self.y = y

    def reset(self):
        """
        Reset the point to the origin in 2D space.
        :return: Nothing
        """
        self.move(0,0)

    def move(self, x, y):
        """
        Move a point to a new location in 2D space.
        :param x: x coordinate
        :param y: y coordinate
        :return: Nothing
        """
        self.x = x
        self.y = y

    def calculate_distance(self, other_point):
        """
        Calculate the distance from this point to a second point passed as a parameter.
        This function uses Pythagorean theorem to calculate the distance between two points.
        :param other_point: The second point to calculate distance
        :return: The distance between two points
        """
        # x = math.fabs(other_point.x - self.x)
        # y = math.fabs(other_point.y - self.y)
        # dist = math.sqrt(x**2 + y**2)
        return math.sqrt(
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)


def main():
    p1 = Point()
    print(p1.x, p1.y)
    p2 = Point(5,8)
    print(p2.x, p2.y)
    p2.reset()
    print(p2.x, p2.y)
    p2.move(3,4)
    print(p2.x, p2.y)
    # test calculate_distance
    print(p1.calculate_distance(p2))
    # Test Tool (assert)
    # Program will exit if False (or zero, empty, None)
    assert(p2.calculate_distance(p1) ==
           p1.calculate_distance(p2))


if __name__ == '__main__':
    main()
    exit(0)
