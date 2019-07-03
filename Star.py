import math
import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca(xlim=[0,100],ylim=[0,100],aspect=1)

def libra():
	x = np.arange(-10, 10, 0.05)
	y = np.arange(10, 20, 0.1)
	s = np.arange(0, 54, 0.1)
	x0 = [24,30.5,71,78]
	y0 = [61,41,41,61]
	d = []
	# d = sqrt(((x2-x1)**2)+((y2-y1)**2))

	for i in range(len(x0)-1) :
		num0 = math.sqrt(((x0[i+1]-x0[i])**2)+((y0[i+1]-y0[i])**2))
		d.append("%.2f" % num0)
	print("Distance :",d )
	print('\n')
	# print("" :)
	#star-line
	plt.plot([24,30.5,71,78], [61,41,41,61])
	plt.plot([24,30.5,71,78], [61,41,41,61], '*')


	#picture
	plt.plot(x+24, x**2/10+36, 'skyblue', x+24, x/x+45, 'skyblue', y+4, y*1.5+31, 'skyblue', -y+44, y*1.5+31, 'skyblue', y/y+23, y*1.5+31, 'skyblue',
		x+78, x**2/10+36, 'skyblue', x+78, x/x+45, 'skyblue', y+58, y*1.5+31, 'skyblue', -y+98, y*1.5+31, 'skyblue', y/y+77, y*1.5+31, 'skyblue',
		s+24, s/s+60, 'skyblue', s/s+50, s/1.5+25, 'skyblue', s/2+38, s/s+24, 'skyblue')


def pisces():
	x = np.arange(-10, 10, 0.05)
	m = np.arange(-3, 3, 0.05)
	t = np.arange(0, 5, 0.05)
	x0 = [40,25,25,40,50,55,68,80,74,75,72,72,76,77,78,71,72,78,84,85,78]
	y0 = [22,19,25,22,18,16,13,9,19,26,36,41,46,55,60,65,72,79,72,64,60]
	d = []
	# d = sqrt(((x2-x1)**2)+((y2-y1)**2))

	for i in range(len(x0)-1) :
		num0 = math.sqrt(((x0[i+1]-x0[i])**2)+((y0[i+1]-y0[i])**2))
		d.append("%.2f" % num0)
	
	print("Distance :", d)
	print('\n')
	#star-line
	plt.plot([40,25,25,40,50,55,68,80,74,75,72,72,76,77,78,71,72,78,84,85,78], [22,19,25,22,18,16,13,9,19,26,36,41,46,55,60,65,72,79,72,64,60])
	plt.plot([25,25,40,50,55,68,80,74,75,72,72,76,77,78,71,72,78,84,85], [19,25,22,18,16,13,9,19,26,36,41,46,55,60,65,72,79,72,64], '*')
	plt.plot([26,80], [25,73] , 'ko',)

	#picture
	plt.plot(x+30, 1/30*x**2+15.5, 'skyblue', x+30, -1/25*x**2+29, 'skyblue', -1/2*m**2+24.5, m+22, 'skyblue', 
		-1/4*m**2+32, 1.5*m+22, 'skyblue', t+40, t/2+25, 'skyblue', t+40, -t/2+19, 'skyblue', t/t+44, t*2.2+16.5, 'skyblue')
	plt.plot(1/25*x**2+71, x+70, 'skyblue', -1/30*x**2+84.5, x+70, 'skyblue', m+78, 1/2*m**2+75.5, 'skyblue', 
		1.5*m+78, 1/4*m**2+68, 'skyblue', t/2+72.5, t+55, 'skyblue', -t/2+83.5, t+55, 'skyblue', t*2.2+72.5, t/t+54, 'skyblue')


name = "libra"
if name == "libra":
	libra();
	plt.show()
elif name == "pisces":
	pisces();
	plt.show()
