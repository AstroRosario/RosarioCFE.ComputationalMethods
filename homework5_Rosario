import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy.fft import dct, idct

#loading and plotting data, dow.txt
f=np.loadtxt('dow.txt')
with open('dow.txt') as f:
    lines=f.readlines()
    x = [float(line.split()[0]) for line in lines]
plt.plot(x)
plt.title('Dow Jones Industrial Average 2006-2010') #average prices on the US stock market
plt.show()

#setting the first 10% for dow.txt
def fft10(dow):
    f=np.loadtxt('dow.txt')
    coeff=np.fft.fft(f)
    plt.plot(f, 'r', label='{}'.format(dow))
    for i in range(len(coeff)):
        if i > len(coeff) * 0.1:
            coeff[i]=0
    inv=np.fft.ifft(coeff) #inverse Fourier Transform 
    plt. plot(inv, 'b', label='10%')
    plt.show()

#setting the first 2% for dow.txt
def fft2(dow):
    f=np.loadtxt('dow.txt')
    coeff=np.fft.fft(f)
    plt.plot(f, 'r', label='{}'.format(dow))
    for i in range(len(coeff)):
        if i > len(coeff) * 0.02:
            coeff[i]=0
    inv=np.fft.ifft(coeff) #inverse Fourier Transform 
    plt. plot(inv, 'b', label='2%')
    plt.show()

#loading and plotting data, dow2.txt
f=np.loadtxt('dow2.txt')
with open('dow2.txt') as f:
    lines=f.readlines()
    x = [float(line.split()[0]) for line in lines]
plt.plot(x)
plt.title('Dow Jones Industrial Average 2004-2008') #average prices on the US stock market 2004-2008
plt.show()

#setting the first 10% for dow2.txt
from cProfile import label

#dow2 data fit 10% & 2%
def fft2_10(dow2):
    f=np.loadtxt('dow2.txt')
    coeff=np.fft.fft(f)
    b=np.copy(coeff)
    plt.plot(f, 'r', label='{}'.format(dow2))
    for i in range(len(coeff)):
        if i > len(coeff) * 0.02:
            coeff[i]=0
    for i in range(len(b)):
        if i >len(b)* 0.1:
            b[i]=0
    inv=np.fft.ifft(coeff) #inverse Fourier Transform 
    inv_b=np.fft.ifft(b)
    plt. plot(inv, 'b', label='2%')
    plt. plot(inv_b, 'g', label='10%')

#analysis using discrete cosine transforms
def cos2(dow2):
    f=np.loadtxt('dow2.txt')
    coeff=dct(f)
    plt.plot(f, 'r', label='{}'.format(dow2))
    for i in range(len(coeff)):
      if i>len(coeff)* 0.02:
         coeff[i]=0
      inv=idct(coeff) #inverse
      plt.plot(inv, 'b', label="2% with DCT")
      plt.show()

def cos2ftt2(dow2):
    f=np.loadtxt('dow2.txt')
    coeff_fft=np.fft.fft(f)
    coeff_cos=dct(f)
    plt.plot(f, 'r', label='{}'.format(dow2))
    for i in range(len(coeff_cos)):
        if i >len(coeff_cos) * 0.02:
            coeff_cos[i]=0
    for i in range(len(coeff_fft)):
        if i >len(coeff_fft) *0.02:
            coeff_fft[i]=0
    inv_fft=np.fft.ifft(coeff_fft) #inverse value
    inv_cos=idct(coeff_cos) 
    plt.plot(inv_cos, 'g', label='cos')
    plt.show()


#argparse argument
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('dow.txt', type=int)
parser.add_argument('dow2.txt', type=int)
func_map={'fft10':fft10, 'fft2':fft2,'fft2_10':fft2_10, 'cos2': cos2, 'cos2ftt2':cos2ftt2}
func=parser.args.func_map
args=parser.parse_args()
print(func)