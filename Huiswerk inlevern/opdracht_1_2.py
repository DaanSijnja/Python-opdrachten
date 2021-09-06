'''Radialen naar dergees en andersom'''

pi = 3.141592

def rad_to_degrees(rad):
    '''radialen naar graden'''
    deg = (180/pi)*rad
    return deg

def degrees_to_rad(deg):
    '''graden naar radialen'''
    rad = (pi/180)*deg
    return rad

def hz_to_rpm(hz):
    '''hertz naar toertal per minuut'''
    rpm = hz*60
    return rpm

def rpm_to_hz(rpm):
    '''hertz naar toertal per minuut'''
    hz = rpm/60
    return hz

'''3 radialen'''
print('rad = 3 Degrees = ' + str(rad_to_degrees(3)) + '\n')

'''69 graden'''
print('Degrees = 69 Rad = ' + str(degrees_to_rad(69)) + '\n')

'''500 hertz'''
print('hertz = 500 RPM = ' + str(hz_to_rpm(500)) + '\n')

'''110 RPM'''
print('RPM = 110 hertz = ' + str(rpm_to_hz(110))+ '\n')