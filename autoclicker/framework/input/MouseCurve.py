import math


def circ(point1, point2, point3):
    ax = point1[0]
    ay = point1[1]
    ax = point1[0]
    ay = point1[1]
    bx = point2[0]
    by = point2[1]
    cx = point3[0]
    cy = point3[1]
    '''find the x,y and radius for the circle through the 3 points'''
    if (ax * by - ax * cy - cx * by + cy * bx - bx * ay + cx * ay) != 0:
        x = .5 * (-pow(ay, 2) * cy + pow(ay, 2) * by - ay * pow(bx, 2) \
                  - ay * pow(by, 2) + ay * pow(cy, 2) + ay * pow(cx, 2) - \
                  pow(cx, 2) * by + pow(ax, 2) * by + pow(bx, 2) * \
                  cy - pow(ax, 2) * cy - pow(cy, 2) * by + cy * pow(by, 2)) \
            / (ax * by - ax * cy - cx * by + cy * bx - bx * ay + cx * ay)
        y = -.5 * (-pow(ax, 2) * cx + pow(ax, 2) * bx - ax * pow(by, 2) \
                   - ax * pow(bx, 2) + ax * pow(cx, 2) + ax * pow(cy, 2) - \
                   pow(cy, 2) * bx + pow(ay, 2) * bx + pow(by, 2) * cx \
                   - pow(ay, 2) * cx - pow(cx, 2) * bx + cx * pow(bx, 2)) \
            / (ax * by - ax * cy - cx * by + cy * bx - bx * ay + cx * ay)
    else:
        return False

    r = pow(pow(x - ax, 2) + pow(y - ay, 2), .5)

    return x, y, r


def findpoint(eq1, eq2, point1, point2):
    '''find the centroid of the overlapping part of two circles
    from their equations'''
    thetabeg = math.acos((point1[0] - eq1[0]) / eq1[2])
    thetaend = math.acos((point2[0] - eq1[0]) / eq1[2])
    mid1x = eq1[2] * math.cos((thetabeg + thetaend) / 2) + eq1[0]
    thetaybeg = math.asin((point1[1] - eq1[1]) / eq1[2])
    thetayend = math.asin((point2[1] - eq1[1]) / eq1[2])
    mid1y = eq1[2] * math.sin((thetaybeg + thetayend) / 2) + eq1[1]

    thetabeg2 = math.acos((point1[0] - eq2[0]) / eq2[2])
    thetaend2 = math.acos((point2[0] - eq2[0]) / eq2[2])
    mid2x = eq2[2] * math.cos((thetabeg2 + thetaend2) / 2) + eq2[0]
    thetaybeg2 = math.asin((point1[1] - eq2[1]) / eq2[2])
    thetayend2 = math.asin((point2[1] - eq2[1]) / eq2[2])
    mid2y = eq2[2] * math.sin((thetaybeg2 + thetayend2) / 2) + eq2[1]
    return [(mid2x + mid1x) / 2, (mid2y + mid1y) / 2]


def get_curve_points(curve):
    for j in range(0, 6):
        newpoints = []
        for i in range(0, len(curve)-3):
            eq = circ(curve[i], curve[i + 1], curve[i + 2])
            eq2 = circ(curve[i + 1], curve[i + 2], curve[i + 3])
            if eq == False or eq2 == False:
                newpoints.append([(curve[i + 1][0] + curve[i + 2][0]) / 2, (curve[i + 1][1] + curve[i + 2][1]) / 2])
            else:
                newpoints.append(findpoint(eq, eq2, curve[i + 1], curve[i + 2]))
        for point in newpoints:
            point[0] = int(round(point[0]))
            point[1] = int(round(point[1]))
        for m in range(0, len(newpoints)):
            curve.insert(2 * m + 2, newpoints[m])

    return curve