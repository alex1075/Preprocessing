from shapely.geometry import Polygon


def overlap(rect1,rect2):
    p1 = Polygon([(rect1[0],rect1[1]), (rect1[1],rect1[1]),(rect1[2],rect1[3]),(rect1[2],rect1[1])])
    p2 = Polygon([(rect2[0],rect2[1]), (rect2[1],rect2[1]),(rect2[2],rect2[3]),(rect2[2],rect2[1])])
    # print(p1.intersects(p2))
    try:
        return(p1.intersects(p2))
    except:
        # print(p1)
        # print(p2)
        return False

def overlap_area(rect1,rect2):
    p1 = Polygon([(rect1[0],rect1[1]), (rect1[1],rect1[1]),(rect1[2],rect1[3]),(rect1[2],rect1[1])])
    p2 = Polygon([(rect2[0],rect2[1]), (rect2[1],rect2[1]),(rect2[2],rect2[3]),(rect2[2],rect2[1])])
    # print(p1.intersects(p2))
    try:
        # print(p1.intersection(p2).area)
        return(p1.intersection(p2).area)
    except:
        # print(p1)
        # print(p2)
        return 0