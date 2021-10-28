class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x, self.y)
 
def Left_index(points):
    minn = 0
    for i in range(1,len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn
 
def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

 
    if val == 0:
        print(f'Turn [{p}, {q}, {r}] : ({q.y} - {p.y}) * ({r.x} - {q.x}) - ({q.x} - {p.x}) * ({r.y} - {q.y}) = {val} (Collinear)\n')
        return 0
    elif val > 0:
        print(f'Turn [{p}, {q}, {r}] : ({q.y} - {p.y}) * ({r.x} - {q.x}) - ({q.x} - {p.x}) * ({r.y} - {q.y}) = {val} (Right)\n')
        return 1
    else:
        print(f'Turn [{p}, {q}, {r}] : ({q.y} - {p.y}) * ({r.x} - {q.x}) - ({q.x} - {p.x}) * ({r.y} - {q.y}) = {val} (Left)\n')
        return 2
 
def convexHull(points, n):
    if n < 3:
        return
 
    l = Left_index(points)
    print('left most point: {}'.format(points[l]))
 
    hull = []
    print('hull = {}'.format(hull))
    p = l
    q = 0
    while(True):
        print('Adding point {} to hull'.format(points[p]))
        hull.append(points[p])
        print("\nCurrent Hull:", end="")
        for x in hull:
            print(f" {x}", end="")

        print("\n------------------x--------------------x--------------------\n")

        q = 0
        print(f"Point On Hull: {points[p]}\n")
        print('endpoint: {}'.format(points[q]))
 
        for i in range(n):
            print('checking for point {}'.format(points[i]))
             
            if(q==p or orientation(points[p],
                           points[i], points[q]) == 2):
                q = i
                print('new endpoint: {}'.format(points[q]))

        p = q
 
        if(p == l):
            break
 
    print("\nFinal Hull:", end="")
    for x in hull:
        print(f" {x}", end="")

    print("\n------------------x--------------------x--------------------\n")
 
# Driver Code
points = []
points.append(Point(0, 3))
points.append(Point(2, 2))
points.append(Point(1, 1))
points.append(Point(2, 1))
points.append(Point(3, 0))
points.append(Point(0, 0))
points.append(Point(0, 4))
points.append(Point(3, 3))
 
convexHull(points, len(points))