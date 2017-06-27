#!/usr/bin/python

import sys, socket, struct, time

if len(sys.argv) != 3:
	print sys.argv[0]+" <IP> <PORT>"
	exit()

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], int(sys.argv[2])))

	fp = open("track.txt", "r")
	lines = fp.readlines()
	fp.close()

	coord = []

	for line in lines:
		coord.append(tuple([float(i) for i in line.split(',')]))

	while True:
		for llh in coord:
			buf = struct.pack("fff", llh[0], llh[1], llh[2])
			s.sendall(buf)
			time.sleep(0.5)
	#buffer = struct.pack("fff", 1.1, 2.2, 3.3)
	#s.sendall(buffer)
	s.close()
finally:
	s.close()
