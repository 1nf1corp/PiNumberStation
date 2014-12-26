#!/usr/bin/python

import subprocess # for calling console
import math
import time
import wave

message = "korn101, github"

sounds = ["zero.wav", "one.wav", "two.wav", 
		"three.wav", "four.wav", "five.wav", 
		"six.wav", "seven.wav", "eight.wav", "niner.wav"]
		
alpha = ["alpha", "bravo", "charlie", "delta",  "echo", "foxtrot", "golf", 
		"hotel", "india", "juliet", "kilo", "lima", "mike", "november", "oscar",
		"papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor",
		"whiskey", "x-ray", "yankee", "zulu"]

def main():
	
	print("PiNumberStation started...")
	'''
	for x in range(0, len(message)):
		print(str(message[x]))
	'''
	return
	
def playMessage():
	
	subprocess.call(["sudo", "./pifm", "./message.wav"])
	
	return
	
def getVO( character ):
	if character.isdigit() == True:
		return sounds[int(character)]
	else:
		if character == ',' or character == ' ':
			return "_comma.wav"
		if character == '.':
			return "_period.wav"
		
		
		if character.isalpha() == True:
			return "/alpha/" + str(alpha[ord(character) - 97] + ".wav")
		
	
def constructWav( strMessage ):
	
	infiles = []
	
	'''
	import audiolab, scipy
	a, fs, enc = audiolab.wavread('file1.wav')
	b, fs, enc = audiolab.wavread('file2.wav')
	c = scipy.vstack((a,b))
	audiolab.wavwrite(c, 'file3.wav', fs, enc)
	'''
	
	# determine infiles for message.
	i=0
	infiles.append("./vo/on1.wav")
	infiles.append("./vo/misc/buzzer.wav")
	
	for character in strMessage:
		infiles.append("./vo/" + getVO(character))
		print(infiles[i])
		i = i + 1
		
	infiles.append("./vo/off2.wav")
	
	#infiles = ["sound_1.wav", "sound_2.wav"]
	
	outfile = "message.wav"
	
	data= []
	for infile in infiles:
	    w = wave.open(infile, 'rb')
	    data.append( [w.getparams(), w.readframes(w.getnframes())] )
	    w.close()

	output = wave.open(outfile, 'wb')
	output.setparams(data[0][0])
	
	for x in range(0, len(infiles)):
		output.writeframes(data[x][1])
	
	#output.writeframes(data[0][1])
	#output.writeframes(data[1][1])
	#output.writeframes(data[2][1])
	output.close()
	
	return
	

# START:
main()
#constructWav(message)
print("Synthesizing Message..")
constructWav(message)
print("Synthesis Completed.. Broadcast Begin")
playMessage()
print("Done")