import sys
from naoqi import ALProxy


IP = raw_input("Set the NAO's IP: ")
#IP = "127.0.0.1"
PORT = int(raw_input("Set the NAO's PORT: "))
#PORT = 52338

def get_tts():
	try:
		tts = ALProxy("ALTextToSpeech", IP, PORT)
		return tts
	except Exception,e:
		print "Could not create proxy to ALTextToSpeech"
		print "Error was: ",e
		sys.exit(1)

def get_rp():
	try:
		rp = ALProxy("ALRobotPosture", IP, PORT)
		return rp
	except Exception, e:
		print "Could not create proxy to ALRobotPosture"
		print "Error was: ",e
		sys.exit(1)		

def got_to_posture(name,speed):
	rp = get_rp()
	result = rp.goToPosture(name, speed/100.)
	if result:
		print "Done"
	else:
		print "Error"


def say_text():
	tts = get_tts()
	#Sets the language to english
	tts.setLanguage("English")
	#Sets the text to say
	text = raw_input("What NAO's gonna say? : ")
	tts.say(text)

def show_menu():
	print "\t\t\tNAO Desarrollo - Using NAOqi SDK\n"
	print "\t\t\t\tMENU"
	print "1.- Talk from NAO"
	print "2.- Sit Down"
	print "3.- Stand Up"
	print "4.- Walk away"
	return raw_input("Give me an option: ")


def main():
	option = show_menu()
	if option == "1":
		say_text()
	elif option == "2":
		got_to_posture("Sit",80)
	elif option == "3":
		got_to_posture("Stand",80)
	elif option == "4":
		print "Soon"
	else:
		print "EROR"

while True:
	main()




