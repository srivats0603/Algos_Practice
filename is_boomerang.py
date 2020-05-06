class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        y1_y0 = (points[1][1]-points[0][1])
        y2_y0 = (points[2][1]-points[0][1])
        y2_y1 = (points[2][1]-points[1][1])
        x1_x0 = (points[1][0]-points[0][0])
        x2_x0 = (points[2][0]-points[0][0])
        x2_x1 = (points[2][0]-points[1][0])
        if ((y1_y0 == 0) and (x1_x0 == 0)) or (((y2_y0 == 0) and (x2_x0 == 0))) or (((y2_y1 == 0) and (x2_x1 == 0))):
            return False
        if (x1_x0 == 0) or (x2_x0 == 0) :
            if (x2_x0 == 0) and (x1_x0 == 0):
                return False
            else:
                return True
        slope1 = y1_y0/x1_x0
        slope2 = y2_y0/x2_x0
        #print(slope1,slope2)
        if slope1 == slope2:
            return False
        else:
            return True