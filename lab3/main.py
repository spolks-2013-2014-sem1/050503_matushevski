#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket
BUF_SIZE = 32*1024

def start_client():
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				#for more fast socket closing
		host = socket.gethostname()
		s.connect((host,port))
	else: 
		return 0
	file_name=raw_input('Input file name: ')
	f = open(file_name,'ab')
	
	while 1:
		data = s.recv(BUF_SIZE)
		if not data: 
			print 'Data has been received'
			break
		f.write(data)
	s.close()
		
	
def start_server():
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:
		s = socket.socket()
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				#for more fast socket closing
		s.bind(("",port))
		s.listen(1)
		conn, addr = s.accept()
		print 'Connected with client. IP:', addr[0]
		
	else: return 0
	file_name=raw_input('Input file name: ')
	f = open(file_name)
	while 1:
		data = f.read(BUF_SIZE)
		if not data: 
			print 'Data has been transfered'
			break
		try:
			conn.send(data)
		except socket.error:
			print 'Transfering failed'
			sys.exit
	conn.close()
	
			
			
		


def main():
	if sys.argv[1] == 'client':												
		print 'Starting client...'
		start_client()
	if sys.argv[1] == 'server':												
		print 'Starting server...'
		start_server()
	return 0


if __name__ == '__main__':
	main()
