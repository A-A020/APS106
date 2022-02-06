#####################################################
# APS106 Winter 2021 - Lab 3 - Measurement Parser   #
# Student Name: Chiung-Ting (Bella) Huang
# PRA Section: PRA0104
#####################################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    
    i = email.find('.')
    j = email.find('@')
    return email[i+1:j].upper() + ',' + email[:i].upper()


###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2,")
    3
    
    >>> count_measurements("Control, 7.5,")
    1
    """
     
    substring = ','
    return int(s.count(substring)/2)


######################################
# Part 3 - Calculate Control Average #
######################################

def calc_control_average(s):
    """
    (str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the average of the three control site measurements to one
    decimal place
    
    >>> calc_control_average("Control,7.4,Control,7.2,Control,7.6,")
    7.4
    
    >>> calc_control_average("Control,10.2,Control,11.2,Control,9.6,")
    10.3
    
    >>> calc_control_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9,")
    7.2
    """
    
    a = s.find('Control')      
    b = s[a+8:].find(',')
    first_measurement = float(s[a+8:a+8+b])     
    c = s[a+8:].find('Control')
    d = s[a+8+c+8:].find(',')
    second_measurement = float(s[a+8+c+8:a+8+c+8+d])
    e = s[a+8+c+8:].find('Control')
    f = s[a+8+c+8+e+8:].find(',')
    third_measurement = float(s[a+8+c+8+e+8:a+8+c+8+e+8+f])
    
    return float(round((first_measurement + second_measurement + third_measurement)/3,1))


###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info):
    """
    (str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of control site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9,")
    'DOMINGUEZ,DINA,7,7.2'
    
    >>> generate_summary("jamie.riggs@company.com, 14/12/20, B, 5.6, Control, 5.5, Db, 3.2, Control, 6.1, Control, 5.9,")
    'RIGGS,JAMIE,5,5.8'
    """
    
    i = measurement_info.find('.')
    j = measurement_info.find('@')
    technician_name = measurement_info[i+1:j].upper() + ',' + measurement_info[:i].upper()
    substring = ','
    total_measurement = int((measurement_info.count(substring)-2)/2)
    a = measurement_info.find('Control')      
    b = measurement_info[a+8:].find(',')
    first_measurement = float(measurement_info[a+8:a+8+b])     
    c = measurement_info[a+8:].find('Control')
    d = measurement_info[a+8+c+8:].find(',')
    second_measurement = float(measurement_info[a+8+c+8:a+8+c+8+d])
    e = measurement_info[a+8+c+8:].find('Control')
    f = measurement_info[a+8+c+8+e+8:].find(',')
    third_measurement = float(measurement_info[a+8+c+8+e+8:a+8+c+8+e+8+f])
    control_average = float(round((first_measurement + second_measurement + third_measurement)/3,1))

    return technician_name + ',' + str(total_measurement) + ',' + str(control_average)


if __name__ == '__main__':
    import doctest
    doctest.testmod()