#!/usr/bin/env python

import math

WGS84_RADIUS = 6378137.0
WGS84_ECCENTRICITY = 0.0818191908426

a = WGS84_RADIUS
e = WGS84_ECCENTRICITY

e2 = e*e

fp = open("track.txt", "r")
op = open("track.csv", "w")

lines = fp.readlines()
fp.close()

time = float(0)

for i in range(10):
		for line in lines:
				llh = [float(i) for i in line.split(',')]
				clat = math.cos(llh[0]/180*math.pi)
				slat = math.sin(llh[0]/180*math.pi)
				clon = math.cos(llh[1]/180*math.pi)
				slon = math.sin(llh[1]/180*math.pi)
				d = e * slat
				
				n = a/math.sqrt(1.0 - d*d)
				nph = n + llh[2]
				
				tmp = nph * clat
				op.write(",".join([str(time), str(tmp*clon), str(tmp*slon), str(((1.0 - e2)*n + llh[2]) * slat)])+"\n")
				time = time + 0.1

op.close()
