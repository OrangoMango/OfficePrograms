import time, sys

ex = 0

maxtime = time.time() + (45*60)
sec = 0
f = open("Timekprtime.txt", "w")
f.close()

try:
	while True:
		f = open("Timekprtime.txt", "a")
		current_time = time.asctime()
		now = time.time() + (ex*60)
		extra = int((maxtime-now)/60)
		string = str(current_time) + " >><< " + str(extra) + "min/45min " + "[" + str(sec) + "] [" + str(int(sec/60)) + "]"
		print(string) #Wed 26 Jun 12:45:23 2019 >><< 32min/45min [805] [13]
		f.write(string+"\n")
		time.sleep(1)
		sec += 1
		f.close()
except:
	print("An error occured")
