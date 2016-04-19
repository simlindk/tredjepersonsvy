import socket
import re

def testMethod(data):
	print "Data is: " + data

def shutDownServer():
	sys.exit(0)

def error(text):
	print "Something went wrong, " + text	

def startEko():
	print "starting eko or not... testing hihi.."

# Takes a string were the first value is the command and the second value should contain data.
def doCommand(text):
	try:
		command = text.split()[0]
	except ValueError:
		return
		
	if command == "test":
		try:
			data = text.split()[1]
		except ValueError:
			error("Value Error in text.split()[1]")
			return text
		except IndexError:
			return "Message didn't contain any data"	
		testMethod(data)
	elif command == 'shutdown':
		shutDownServer()
	elif command == 'startEko':
		startEko()
		return "sending_pulse"
	else:
		error("could not find command") 
	return (text + " Complete!")

def Main():
	host = '127.0.0.1'
	port = 5001

	print "Server is running..."

	s = socket.socket()
	s.bind((host, port))

	s.listen(1) # the number is how many connection to listen to
	c, addr = s.accept() # c = current connection
	print"Connection from: "  + str(addr)

	while True:
		data = c.recv(1024).decode() #max buffer data 1024
		if not data:
			break # ends connections if no data

		data = doCommand(data);
		c.send(data.encode())
	c.close()

if __name__ == '__main__':
	Main()

