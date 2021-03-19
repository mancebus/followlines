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
print x
print y
plt.axhline(41)
#x = range(1,len(y)+1)
plt.scatter(x,y)
#plt.plot(x,l)
#plt.plot(x,r)
plt.show()