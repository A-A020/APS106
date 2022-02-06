##########################################
# APS106 W2021 - Lab 6 - Corner Detector #
##########################################

#from lab6_image_utils import display_image, image_to_pixels # UNCOMMENT this line to use the load/display image utils
from operator import itemgetter

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################
def rgb_to_grayscale(rgb_img):
    """
    (list) -> list
    
    Function converts an image of RGB pixels to grayscale.
    Input list is a nested list of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be rounded to the nearest
    integer.
    """
    new_list = []
    for item in rgb_img:
        R = item[0]
        G = item[1]
        B = item[2]
        value = 0.3*R + 0.59*G + 0.11*B
        new_list.append(round(value))
    return new_list

############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (List, List) -> float
    
    Performs a 1-dimensional dot product operation
    """
    if not len(x) != len(y):
        return float(sum([x[i] * y[i] for i in range(len(x))]))
    else:
        return None

######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (list, int, int, list, int) -> list
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a list of pixels from the
    segment.
    
    img is a list of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element list defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    empty_list = []
    matrix = [img[i:i+width] for i in range(0,len(img),width)]
    n = (N-1)/2
    i = int(centre_coordinate[1] - n)
    for sublist in matrix:
        while i <= int(centre_coordinate[1] + n):
            first_element = matrix[i][int(centre_coordinate[0]-n):int(centre_coordinate[0]+n+1)]
            i += 1
            empty_list.append(first_element)
    final_list = []
    for element in empty_list:
        for item in element:
            final_list.append(item)
    return final_list

######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (list, int, int, list) -> list
    
    Apply the kernel filter defined within the two-dimensional list kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional list of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional list defining a NxN filter kernel, n must be an odd integer
    
    The function returns the list of pixels from the filtered image
    """

    n = int((len(kernel[0])-1)/2) 
    m = n
    p = n
    matrix = [img[i:i+width] for i in range(0,len(img),width)]
    kernel_list = []
    for element in kernel:
        for item in element:
            kernel_list.append(item)     
    
    i = 0
    while i < n:
        matrix[i] = [0] * width
        for sublist in matrix:
            sublist[i] = 0
        i += 1
    j = height - 1
    while j > (height-n-1):
        matrix[j] = [0] * width
        for sublist in matrix:
            sublist[j] = 0
        j -= 1
    
    while p < (height - n):
        while m < (width - n):
            coordinate = [int(m),int(p)]
            segment = extract_image_segment(img, width, height, coordinate, len(kernel[0]))
            multiply = dot(segment,kernel_list)
            matrix[p][m] = int(multiply)
            m += 1
        p += 1
        m = n
    
    final_list = []
    for element in matrix:
        for item in element:
            final_list.append(item)
        
    return final_list

###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (List, List) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.
    
    STUDENTS DO NOT NEED TO EDIT THIS FUNCTION

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (list, int, int, float) -> list
    
    Computes the corner strength of each pixel within an image
    and returns a list of potential corner locations sorted from strongest
    to weakest.
    
    STUDENTS DO NOT NEED TO EDIT THIS FUNCTION
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = [[-1, 0, 1],
                            [-2, 0, 2],
                            [-1, 0, 1]]
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = [[-1,-2,-1],
                              [ 0, 0, 0],
                              [ 1, 2, 1]]
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    offset = 1
    corners = []
    for i_y in range(offset, height-offset):
        for i_x in range(offset, width-offset):
            Ix_window = extract_image_segment(Ix, width, height, [i_x, i_y], 3)
            Iy_window = extract_image_segment(Iy, width, height, [i_x, i_y], 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                corners.append([corner_strength,[i_x,i_y]])

    # sort
    corners.sort(key=itemgetter(0))
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return corner_locations


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (list, float) -> list
    
    Filters any corners that are within a region with a stronger corner.
    Returns a list of corners that are at least min_distance away from
    any other stronger corner.
    
    corners is a list of two-element coordinate lists representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    empty_list = []
    empty_list.append(corners[0])
    corners.remove(corners[0])
    for sublist in corners:
        i = 0
        distance = (((sublist[0] - empty_list[i][0])**2 + (sublist[1] - empty_list[i][1])**2)**(1/2))
        if distance >= 10:
            empty_list.append(sublist)
            corners.remove(sublist)
            i += 1
    return empty_list