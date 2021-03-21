import matplotlib.pyplot as plt

f = open('data.csv','r')
data = f.read()
f.close()

x = []
y = []
l = []
r = []
for line in data.strip().split('\n')[1:]:
    measureTime,light,powerLeft,powerRight = line.split(';')
    x.append(measureTime)
    y.append(light)
    l.append(powerLeft)
    r.append(powerRight)

plt.axhline(41)

plt.scatter(x,y)

plt.show()