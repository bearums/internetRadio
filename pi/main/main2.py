
import time
import os
import smbus
import subprocess
from subprocess import Popen
from mpg123 import MPyg123Player

player = MPyg123Player()

#from pot_functions import * 
#from btn_functions import * 
def do_nothing():
	"""this function does nothing"""
	
	
btn1_on = do_nothing
btn1_off = do_nothing

btn2_on = do_nothing
btn2_off = do_nothing

btn3_on = do_nothing
btn3_off = do_nothing

btn4_on = do_nothing
btn4_off = do_nothing

btn5_on = do_nothing
btn5_off = do_nothing

btn6_on = do_nothing
btn6_off = do_nothing

buffer_val = 2 # min. change pot value must have for action to occur



	


#read station list into python 
station_list=[]
name_list=[]
media_list=[]
with open('stations', 'r') as f :
	for l in f: 
		s= l.strip().split("=")[-1]
		d_type = l.strip().split("=")[0][0]
		if d_type == 's':
			station_list.append(s)
		if d_type == 'n':
			name_list.append(s)
		if "speak_names" in l.strip().split("=")[0] :
			speak_names = s
			
	
print station_list
print name_list
print speak_names

os.system('mkdir -p station_name_voices')
for i in range(0, len(name_list)):
	if speak_names:
		subprocess.call(['espeak' ,'-w', 'station_name_voices/{}.wav'.format(i), '-s' ,'120' , name_list[i]])
	
	#ml = Player.media_list_new(['station_name_voices/{}.wav'.format(i), station_list[i]])
	#media_list.append(ml)
	
	

def is_between(low, high, val):
	if val > low and val <= high:
		return True
	else:
		return False	

def potval_to_station(pval, station_list=station_list):
	"""min potval = 8
		max potval =76 """
	if is_between(8, 18, pval):
		return 0#station_list[0]
	if is_between(18, 28, pval):
		return 1#station_list[1]
	if is_between(28, 38, pval):
		return 2#station_list[2]
	if is_between(38, 48, pval):
		return 3#station_list[3]
	if is_between(48, 58, pval):
		return 4#station_list[4]
	if is_between(58, 68, pval):
		return 5#station_list[5]
	if is_between(68, 78, pval):
		return 6#station_list[6]
	else:
		return 0
		


def play_station(s):
	player.pause()
	#Popen(['mpg123', '-o', 'alsa', '--no-control', '-q', 'station_name_voices/{}.wav'.format(s),'&'])
	Popen(['aplay', 'station_name_voices/{}.wav'.format(s)])
	print station_list[s]
	#Popen(['mpg123', '-o', 'alsa', '--no-control', '-q', station_list[s], '&'])
	player.play_song(station_list[s])
	
	
def change_volume(val):
	#amixer sset 'PCM' 16%
    #Popen(['amixer', 'set', 'Master', 'unmute'])
    Popen(['amixer', 'sset',"'PCM'",  '{}%'.format(val)],stdout=open(os.devnull, 'wb'))	


def read(register):
        data = bus.read_byte_data(address, register)
        return data
        
        
	
bus = smbus.SMBus(1)
address = 0x50

pot1 = 0
pot2 = 0
pot3 = 0
pot4 = 0

btn_1 = 0
btn_2 = 0
btn_3 = 0
btn_4 = 0
btn_5 = 1 #button 5 is wired up wrong way round
btn_6 = 0


curr_station = -1

while True:
	# read in values of pots
	a1 = read(1)
	a2 = read(2)
	a3 = read(3)
	a4 = read(4)
	
	#convert values to range 0-100
	a1 = int(100*a1/256.0)
	a2 = int(100*a2/256.0)
	a3 = int(100*a3/256.0)
	a4 = int(100*a4/256.0)
	
	#read in values of buttons 
	a5 = read(5)
	a6 = read(6)
	a7 = read(7)
	a8 = read(8)
	a9 = read(9)
	a10 = read(10)
	
	
	#check for change of pot1
	#if a1 != pot1:
	if a1 < pot1 -buffer_val or a1 > pot1 +buffer_val:
		pot1 = a1
		print 'changing pot1 ', pot1
		#pot1_func(pot1)
		change_volume(pot1)
	#pot2
	#if a2 != pot2:
	if a2 < pot2 -buffer_val or a2 > pot2 +buffer_val:
		pot2 = a2
		print 'changing pot2 ', pot2
		new_station = potval_to_station(pot2)
		if new_station != curr_station:
					print pot2 ,' changing station to ', new_station
					a=play_station(new_station )
					curr_station = new_station
		
	#pot3
	if a3 != pot3:
		pot3 = a3
		#print 'changing pot3 ', pot3
		#pot3_func(pot3)
	#pot4
	if a4 != pot4:
		pot4 = a4
		#pot4_func(pot4)
		#print 'changing pot4 ', pot4
		
	#check for change in button status
	#1
	if a5 != btn_1:
		if a5 ==1:
			btn1_on() 
			#print 'btn1 pushed!'
		if a5 ==0:
			btn1_off()
			#print 'btn1 released!'
		btn_1= a5
	#2
	if a6 != btn_2:
		if a6==1:
			btn2_on() 
			#print 'btn2 pushed!'
		if a6==0:
			btn2_off() 
			#print 'btn2 released!'
		btn_2= a6
	#3
	if a7 != btn_3:
		if a7 ==1:
			btn3_on() 
			#print 'btn3 pushed!'
		if a7 ==0:
			btn3_off() 
			#print 'btn3 released!'
		btn_3= a7
	#4
	if a8 != btn_4:
		if a8 ==1:
			btn4_on() 
			#print 'btn4 pushed!'
		if a8 ==0:
			btn4_off()  
			#print 'btn4 released!'
		btn_4= a8
	#5 - NOTE a9=1 means button released
	if a9 != btn_5:
		if a9 ==1:
			btn5_off() 
			#print 'btn5 released!'
		if a9 ==0:
			btn5_on() 
			#print 'btn5 pushed!'
		btn_5= a9
	#6
	if a10 != btn_6:
		if a10 ==1:
			btn6_on() 
			#print 'btn6 pushed!'
		if a10 ==0:
			btn6_off() 
			#print 'btn6 released!'
		btn_6= a10
		
        time.sleep(0.04)


	

