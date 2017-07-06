#!/usr/bin/python

import sys, socket, struct, time

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("localhost", 8081))
	#s.connect(("192.168.1.147", 8080))

	#fp = open("track.txt", "r")
	fp = open("track.csv", "r")
	lines = fp.readlines()
	fp.close()

	coord = []

	for line in lines:
		coord.append(tuple([float(i) for i in line.split(',')]))

	while True:
		for xyz in coord:
			buf = struct.pack("fff", xyz[1], xyz[2], xyz[3])
			s.sendall(buf)
			time.sleep(1.0)
	#buffer = struct.pack("fff", 1.1, 2.2, 3.3)
	#s.sendall(buffer)
	s.close()
finally:
	s.close()
