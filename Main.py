import socket
import logging

from config import configuration

i = configuration()

server = i.server
port = i.port
channel = i.channel
user = i.user
passw = i.passw
readbuffer = i.readbuffer

#Start loging
logging.basicConfig(filename="WheeleBot.log", level=logging.DEBUG)

#Connect to server
s = socket.socket()
s.connect((server, port))

#Send required information to Authenitcate wtih the server
s.send("PASS " + passw + "\r\n")
s.send("NICK " + user + "\r\n")
s.send("USER " + user + "\r\n")
s.send("JOIN " + channel + "\r\n")


#Maintain connection
while True:
	data = s.recv(4096)
	print data

	#Main help command
	if data.find('!help') != -1:
		from lib.text_to_send import help_command
		fetch = help_command()
		
		s.send("PRIVMSG " + channel +  " : " + fetch.help_msg)

	#Help with social commands
	elif data.find('!socialCmds') != -1:
		from lib.text_to_send import help_command_social
		fetch = help_command_social()
		
		s.send("PRIVMSG " + channel +  " : " + fetch.help_social)

	#Help with Misc commands
	elif data.find('!miscCmds') != -1:
		from lib.text_to_send import help_command_misc
		fetch = help_command_misc()
		
		s.send("PRIVMSG " + channel +  " : " + fetch.help_misc)

	#More help info
	elif data.find('!infoCmds') != -1:
		from lib.text_to_send import help_command_info
		fetch = help_command_info()
		
		s.send("PRIVMSG " + channel +  " : " + fetch.help_info)

