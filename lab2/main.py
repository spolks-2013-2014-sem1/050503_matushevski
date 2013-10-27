#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import socket

#PORT = 50005

def start_server(PORT):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				#for more fast socket closing
	s.bind(("",PORT))
	s.listen(1)
	conn, addr = s.accept()
	print 'Connected with client. IP:', addr[0]
	
	while 1:
		data = conn.recv(1024)
		if not data: break
		conn.send(data)
		if data.rstrip() == "finish him":					#catching exit 
			print 'Oh no, its the end...I was so young...'
			conn.shutdown(socket.SHUT_RDWR)
			break
	conn.close()
	
	

def main():
	if len(sys.argv) != 2:								#default port
		print 'Without argument will be using default port 50000'
		start_server(50000)
	else:										#input port
		PORT = int(sys.argv[1])
		print 'Will be using port', sys.argv[1]
		start_server(PORT)
	return 0


if __name__ == '__main__':
	main()
