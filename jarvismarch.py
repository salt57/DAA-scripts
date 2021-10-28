class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(self.x, self.y)
 
def Left_index(points):
     
    '''
    Finding the left most point
    '''
    minn = 0
    for i in range(1,len(points)):
        if points[i].x < points[minn].x:
            minn = i
        elif points[i].x == points[minn].x:
            if points[i].y > points[minn].y:
                minn = i
    return minn
 
def orientation(p, q, r):
    '''
    To find orientation of ordered triplet (p, q, r).
    The function returns following values
    0 --> p, q and r are collinear
    1 --> Clockwise
    2 --> Counterclockwise
    '''
    val = (q.y - p.y) * (r.x - q.x) - \
          (q.x - p.x) * (r.y - q.y)

    print('turn value for triplet {}, {}, {} is : {}'.format(p,q,r,val))
 
    if val == 0:
        print('collinear points')
        return 0
    elif val > 0:
        print('lies on the right')
        return 1
    else:
        print('lies on the left')
        return 2
 
def convexHull(points, n):
     
    # There must be at least 3 points
    if n < 3:
        return
 
    # Find the leftmost point
    l = Left_index(points)
    print('left most point: {}'.format(points[l]))
 
    hull = []
    print('hull = {}'.format(hull))
     
    '''
    Start from leftmost point, keep moving counterclockwise
    until reach the start point again. This loop runs O(h)
    times where h is number of points in result or output.
    '''
    p = l
    q = 0
    while(True):
         
        # Add current point to result
        print('add point {} to hull'.format(points[p]))
        hull.append(points[p])
        for x in hull:
            print(x)
        print('\n\n')
 
        '''
        Search for a point 'q' such that orientation(p, q,
        x) is counterclockwise for all points 'x'. The idea
        is to keep track of last visited most counterclock-
        wise point in q. If any point 'i' is more counterclock-
        wise than q, then update q.
        '''
        q = 0
        print('endpoint: {}'.format(points[q]))
 
        for i in range(n):
            print('checking for point {}'.format(points[i]))
             
            # If i is more counterclockwise
            # than current q, then update q
            if(q==p or orientation(points[p],
                           points[i], points[q]) == 2):
                q = i
                print('new endpoint: {}'.format(points[q]))
 
        '''
        Now q is the most counterclockwise with respect to p
        Set p as q for next iteration, so that q is added to
        result 'hull'
        '''
        p = q
 
        # While we don't come to first point
        if(p == l):
            break
 
    # Print Result
    for x in hull:
        print(x)
 
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