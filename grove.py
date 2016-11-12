import time
import mraa


while True:
	pot = mraa.Aio(0)
	potVal = pot.read()
	potVal2 = potVal
	potVal3 = int(potVal2/10)
	if potVal3>10:
		if potVal3>50:
			for x in xrange(1,potVal3):
				print"*",
			print ""
		else:
			for x in xrange(1,potVal3):
				print"o",
			print ""



# import time
# import mraa
# #import numpy as np
# #import matplotlib.pyplot as plt
# #import matplotlib.animation as animation

# from flask import Flask, url_for, send_from_directory

# app = Flask(__name__)

# @app.route("/")
# def sound():
# 	pot = mraa.Aio(0)
# 	potVal = pot.read()
# 	potVal2 = potVal / 1024.0
# 	return str(potVal2)


# # @app.route("/graph")
# # 	plt.plot([1,2,3,4])
# # 	plt.ylabel('some numbers')
# # 	plt.show()


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80)

# Connect the Grove Loudness Sensor to analog port A0
# SIG,NC,VCC,GND

# pot = mraa.Aio(0)
# while True:
#     try:
#         sensor_value = mraa.Aio(0)
#         potVal = pot.read()
#         potVal2 = potVal / 1024.0
#         print potVal2

#     except IOError:
#         print "Error"

# @app.route("/graph")
# def graph():
# 	def update_line(num, data, line):
#     	line.set_data(data[..., :num])
#     	return line,
#     fig1 = plt.figure()

# 	data = np.random.rand(2, 25)
# 	l, = plt.plot([], [], 'r-')
# 	plt.xlim(0, 1)
# 	plt.ylim(0, 1)
# 	plt.xlabel('Time')
# 	plt.title('Sound Intensity')
# 	line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
# 	                                   interval=50, blit=True)

# 	fig2 = plt.figure()

# 	x = np.arange(-9, 10)
# 	y = np.arange(-9, 10).reshape(-1, 1)
# 	base = np.hypot(x, y)
# 	ims = []
# 	for add in np.arange(15):
# 	    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))

# 	im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
# 	                                   blit=True)
	
# 	plt.show()