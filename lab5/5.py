#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket, signal, sys, os, time, fcntl

BUF_SIZE = 128
RECV_LEN = 0
PACK_LEN = 0
SEND_LEN = 0


def sigterm(signo, sigobj):
    print("SIGTERM: {0} Exitting...".format(signo))
    sys.exit()


def start_client():
	global RECV_LEN
	global SEND_LEN
	
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:
		host = socket.gethostname()
		s.bind((host,port))
	else: 
		return 0
	file_name=raw_input('Input file name: ')
	f = open(file_name,'ab')
	
	while 1:
		data,addr = s.recvfrom(BUF_SIZE)
		time.sleep(0.001)
		if data == "": 
			print 'Data has been received'
			break
		f.write(data)
		#RECV_LEN += len(data)
	s.close()
		
	
def start_server():
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:
		host = socket.gethostname()
	else: return 0
	file_name=raw_input('Input file name: ')

	f = open(file_name,'rb')
	
	while 1:
		data = f.read(BUF_SIZE)
		if not data: 
			print 'Data has been transfered'
			break
		try:
			s.sendto(data,(host,port))
		except socket.error:
			print 'Transfering failed'
			sys.exit
		
		time.sleep(0.001)
	s.close()
	
signal.signal(signal.SIGTERM, sigterm)
signal.signal(signal.SIGINT, sigterm)		
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				#for more fast socket closing
fcntl.fcntl(s.fileno(), fcntl.F_SETOWN, os.getpid())

if sys.argv[1] == 'client':												
	print 'Starting client...'
	start_client()
if sys.argv[1] == 'server':												
	print 'Starting server...'
	start_server()
