from numpy import loadtxt, genfromtxt

data = loadtxt("data3.csv", comments='#', delimiter=',', skiprows=1)
print(data)

data2 = genfromtxt()