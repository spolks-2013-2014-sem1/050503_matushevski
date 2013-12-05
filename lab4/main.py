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

def sigurg(signo, sigobj):
    try:
        data = s.recv(2, socket.MSG_OOB)
        time.sleep(0.001)
        if data == b"Q":
            #print("Recieved ", RECV_LEN, " from ", SEND_LEN)
			sys.stdout.write("@")
			sys.stdout.flush()
    except socket.error:
        print("Error: ", socket.error)



def start_client():
	global RECV_LEN
	global SEND_LEN
	
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:
		host = socket.gethostname()
		s.connect((host,port))
	else: 
		return 0
	file_name=raw_input('Input file name: ')
	f = open(file_name,'ab')
	
	SEND_LEN = int(s.recv(10).decode("utf-8"));
	print 'File for receive: ', SEND_LEN, ' bytes'
	print '=10======50======90='
	while 1:
		data = s.recv(BUF_SIZE)
		time.sleep(0.001)
		if not data: 
			print ''
			print 'Data has been received'
			break
		f.write(data)
		RECV_LEN += len(data)
	s.close()
		
	
def start_server():
	port = int(raw_input('Input port: '))   
	if 0 <= port <= 65535:

		s.bind(("",port))
		s.listen(1)
		conn, addr = s.accept()
		print 'Connected with client. IP:', addr[0]
		
	else: return 0
	file_name=raw_input('Input file name: ')
	
	conn.send(bytes(str(os.path.getsize(file_name)).encode("utf-8")))
	time.sleep(0.001)
	
	count = int(os.path.getsize(file_name)/BUF_SIZE/20)       
	if count == 0:
		count = 4
	oob = 0
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
		time.sleep(0.001)
		oob += 1
		if oob == count:
			conn.send(b"!Q", socket.MSG_OOB)
			oob = 0
	conn.close()
	
signal.signal(signal.SIGTERM, sigterm)
signal.signal(signal.SIGINT, sigterm)
signal.signal(signal.SIGURG, sigurg)			
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)				#for more fast socket closing
fcntl.fcntl(s.fileno(), fcntl.F_SETOWN, os.getpid())

if sys.argv[1] == 'client':												
	print 'Starting client...'
	start_client()
if sys.argv[1] == 'server':												
	print 'Starting server...'
	start_server()
