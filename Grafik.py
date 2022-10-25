#График (точки из файла)
x=[]
y=[]
with open('Point', 'r') as file:
    arr=file.readlines()
    for line in arr:
        arrx, arry = line.split()
        x.append(float(arrx))
        y.append(float(arry))

#Импорт и стили
from matplotlib import pyplot
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.set_title('При длине 50 см')
ax.set_xlabel('Напрежение (мВ)')
ax.set_ylabel('Сила тока (мА)')
ax.grid(True, linestyle='-.')
ax.tick_params(labelsize='medium', width=3)

#Рисование крестов
yerr=[]
for i in y:
    yerr.append(0.002*i+0.01)
ax.errorbar(x, y, yerr, fmt='.', linewidth=2, capsize=6)


#Апроксимация
from scipy.optimize import curve_fit
def mapping(x, a):
    return a * x
args, covar = curve_fit(mapping, x, y)
a = args[0]
xx=[]
yy=[]
for i in range(601):
    xx.append(i)
    yy.append(a * i)
plt.plot(xx, yy)
print("Значение R:", 1/a)

pyplot.show()