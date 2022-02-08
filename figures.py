class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def numInRange(nin, n1, n2):
    if n1 > n2:
        return n1 >= nin and n2 <= nin
    else:
        return n1 <= nin and n2 >= nin

def pointInRange(pin, p1, p2):
    return numInRange(pin.x, p1.x, p2.x) and numInRange(pin.y, p1.y, p2.y)

class Figure:
    def __init__(self, points):
        self.points = points

    def pointIntersects(self, point):
        for i in range(len(self.points)):
            firstpoint = self.points[i]
            secondpoint = self.points[(i + 1) % len(self.points)]
            if firstpoint.x == secondpoint.x:
                if numInRange(point.y, firstpoint.y, secondpoint.y):
                    return True
            elif firstpoint.y == secondpoint.y:
                if numInRange(point.x, firstpoint.x, secondpoint.x):
                    return True
            else:
                # (x - x1)(y1 - y2) = (y - y1)(x1 - x2)
                if pointInRange(point, firstpoint, secondpoint) and (point.x - firstpoint.x)*(firstpoint.y - secondpoint.y) == (point.y - firstpoint.y)*(firstpoint.x - secondpoint.x):
                    return True
    
if __name__ == "__main__":
    fig = Figure([Point(0, 0), Point(2, 2), Point(4, 2)])
    print("Test 1:", fig.pointIntersects(Point(1,1)))
    print("Test 2:", not fig.pointIntersects(Point(1,2)))
