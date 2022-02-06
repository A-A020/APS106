##############################
# APS106 Winter 2021 - Lab 4 #
# Student Name: Chiung-Ting (Bella) Huang
# PRA Section: PRA0104
##############################

def rectangle_overlap(rect1_bl_x,rect1_bl_y,
                      rect1_tr_x,rect1_tr_y,
                      rect2_bl_x,rect2_bl_y,
                      rect2_tr_x,rect2_tr_y):
    """
    (int,int,int,int,int,int,int,int) -> str
    
    Function determines whether two rectangles overlap. When rectangles
    overlap, the function checks for the following scenarios
        1. The two rectangles share the same coordinates
        2. The first rectangle is contained within the second
        3. The second rectangle is contained within the first
        4. The rectangles have overlapping area, but neither is completely
           contained within the other
    
    Function inputs represent x and y coordinates of bottom left and top right
    corners of rectangles (see lab document)
           
    The function return one of the following strings corresponding to the 
    scenario
        "no overlap"
        "identical coordinates"
        "rectangle 1 is contained within rectangle 2"
        "rectangle 2 is contained within rectangle 1"
        "rectangles overlap"
    
    >>> rectangle_overlap(-1,1,3,5,6,0,9,2)
    'no overlap'
    
    >>> rectangle_overlap(-1,0,3,4,-1,0,3,4)
    'identical coordinates'
    
    >>> rectangle_overlap(2,1,3,2,1,-5,10,6)
    'rectangle 1 is contained within rectangle 2'
    
    >>> rectangle_overlap(2,1,13,20,10,2,11,6)
    'rectangle 2 is contained within rectangle 1'
    
    >>> rectangle_overlap(1,1,10,20,7,18,30,33)
    'rectangles overlap'
    
    """
    
    if rect1_bl_x >= rect2_bl_x and rect1_bl_y >= rect2_bl_y and rect1_tr_x <= rect2_tr_x and rect1_tr_y <= rect2_tr_y:
        if rect1_bl_x == rect2_bl_x and rect1_bl_y == rect2_bl_y and rect1_tr_x == rect2_tr_x and rect1_tr_y == rect2_tr_y:
            return "identical coordinates"
        else:
            return "rectangle 1 is contained within rectangle 2"
    elif rect1_bl_x <= rect2_bl_x and rect1_bl_y <= rect2_bl_y and rect1_tr_x >= rect2_tr_x and rect1_tr_y >= rect2_tr_y:
        if rect1_bl_x == rect2_bl_x and rect1_bl_y == rect2_bl_y and rect1_tr_x == rect2_tr_x and rect1_tr_y == rect2_tr_y:
            return "identical coordinates"
        else:
            return "rectangle 2 is contained within rectangle 1"
    elif (rect1_bl_x <= rect2_bl_x <= rect1_tr_x and rect1_bl_y <= rect2_bl_y <= rect1_tr_y) or (rect2_bl_x <= rect1_bl_x <= rect2_tr_x and rect2_bl_y <= rect1_bl_y <= rect2_tr_y) or (rect2_bl_x <= rect1_bl_x <= rect2_tr_x and rect2_bl_y <= rect1_tr_y <= rect2_tr_y) or (rect1_bl_x <= rect2_bl_x <= rect1_tr_x and rect1_bl_y <= rect2_tr_y <= rect1_tr_y) or (rect1_bl_x <= rect2_tr_x <= rect1_tr_x and rect1_bl_y <= rect2_tr_y <= rect1_tr_y) or (rect1_bl_x <= rect2_tr_x <= rect1_tr_x and rect1_bl_y <= rect2_tr_y <= rect1_tr_y) or (rect2_bl_x <= rect1_tr_x <= rect2_tr_x and rect2_bl_y <= rect1_tr_y <= rect2_tr_y) or (rect1_bl_x <= rect2_tr_x <= rect1_tr_x and rect1_bl_y <= rect2_tr_y <= rect1_tr_y) or (rect1_bl_x <= rect2_bl_x <= rect2_tr_x <= rect1_tr_x and rect2_bl_y <= rect1_bl_y <= rect1_tr_y <= rect1_tr_y) or (rect2_bl_x <= rect1_bl_x <= rect1_tr_x <= rect2_tr_x and rect1_bl_y <= rect2_bl_y <= rect2_tr_y <= rect1_tr_y):
        if (rect1_bl_x == rect2_bl_x and rect1_bl_y == rect2_bl_y) or (rect1_tr_x == rect2_tr_x and rect1_tr_y == rect2_tr_y) or (rect1_bl_x == rect2_tr_x and rect1_bl_y == rect2_tr_y) or (rect2_bl_x == rect1_tr_x and rect2_bl_y == rect1_tr_y) or (rect1_bl_y == rect2_tr_y and rect1_tr_x == rect2_bl_x) or (rect2_bl_y == rect1_tr_y and rect2_tr_x == rect1_bl_x):
            return "no overlap"
        else:
            return "rectangles overlap"
    else:
        return "no overlap"

if __name__ == '__main__':
    import doctest
    doctest.testmod()