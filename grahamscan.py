from functools import *

def convex_hull_graham(points):

    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
    ch = {1: "left", -1: "right", 0: "no turn"}

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)
    
    def turnans(p, q, r):
        print(f"{q}: Turn Value: ({q[0]} - {p[0]})*({r[1]} - {p[1]}) - ({r[0]} - {p[0]})*({q[1]} - {p[1]}) = {(q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])}")
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        print(f"Current Hull: {hull}")
        if len(hull) > 1:
            print(f"Point checked {r}: found {ch[turn(hull[-2], hull[-1], r)]}")
        while len(hull) > 1 and turnans(hull[-2], hull[-1], r) != TURN_LEFT:
            print(f"Point popped: {hull[-1]}")
            hull.pop()
        if not len(hull) or hull[-1] != r:
            print(f"Pushed {r}")
            hull.append(r)
        print()
        return hull

    points = sorted(points)
    print(f"Leftmost Point: {points[0]}")
    print(f"Pointlist: {points}")
    # print("Left")
    l = reduce(_keep_left, points, [])
    # print("Up")
    # u = reduce(_keep_left, reversed(points), [])
    return l + [list(points[0])] or l

print(convex_hull_graham(
    [
        (0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)
    ]
))