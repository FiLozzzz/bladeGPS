#!/usr/bin/python

import os
import sys, socket, struct

if len(sys.argv) != 4:
    print sys.argv[0]+" <DEV> <IP> <PORT>"
    exit()

dev = os.open(sys.argv[1], os.O_RDWR)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[2], int(sys.argv[3])))
    while 1:
        data = os.read(dev,100)
        data_split = data.split(',')

        if(data[1:6]=='GLGGA'):
            latitude = float(data_split[2]) / 100
            latitude = int(latitude) + (latitude % 1) / 60
            #latitude = float(data_split[2][0:2])
            #latitude = latitude + float(data_split[2][2:])/60

            longitude = float(data_split[4])  / 100
            longitude = int(longitude) + (longitude % 1) / 60
            #longitude = float(data_split[4][0:3])
            #longitude = longitude + float(data_split[4][3:])/60

            height = float(data_split[8])
            
            print '=========================='
            print ' Glonass reading'
            print ' -----------------'
            print 'latitude    ' , latitude
            print 'longitude   ' , longitude
            print 'height      ' , height
            print '=========================='
            print ' '

            buffer = struct.pack("fff", latitude, longitude, height)
            s.sendall(buffer)

except (KeyboardInterrupt, SystemExit):
    print "\nKilling Thread..."
finally:
    s.close()

