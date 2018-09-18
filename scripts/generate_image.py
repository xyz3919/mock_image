##! packages/python3/bin/ python3.6

import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
#import astropy

def generate_blank_image(row_num,col_num,rms=1,bg=0):
    
    array = rms*np.random.random((row_num,col_num))+bg
    return array

#print generate_blanck_image(2024,4048)
    
def source_psf(x,y,pos_x,pos_y,sigma_x=1.,sigma_y=1.,flux=1.):

    #print(((x-pos_x)**2/sigma_x**2 + (y-pos_y)**2/sigma_y**2) / 2.)
    #print(np.exp(-( (x-pos_x)**2/sigma_x**2 + (y-pos_y)**2/sigma_y**2) / 2.))
    g = (flux/(2.*np.pi*sigma_x*sigma_y)) * np.exp(-( (x-pos_x)**2/sigma_x**2 + (y-pos_y)**2/sigma_y**2) / 2.)
#    g = (flux/(2*np.pi*size_psf**2)) * np.exp(-( (d-mu)**2 / ( 2.0 * size_psf**2 ) ) )
#    print(np.sum(g))
    return g

def add_sources(length_x,length_y,acsperpix):

    sampling_x,sampling_y = int(length_x/acsperpix),int(length_y/acsperpix)
    data = generate_blank_image(sampling_x,sampling_y,rms=0.01,bg=0)
    x, y = np.meshgrid(np.linspace(-length_x/2,length_x/2,sampling_x), np.linspace(-length_y/2,length_y/2,sampling_y))
    np.random.seed(0)
    for i in range(1,20):
        pos_x = length_x*(np.random.random_sample()-0.5)
        pos_y = length_y*(np.random.random_sample()-0.5)
        data = data+source_psf(x,y,pos_x,pos_y)

    return data

#data = add_sources(2024,4048,0.26)
data = add_sources(100,100,0.26)
plt.imshow(data)
plt.savefig("test.png")
#print(source_psf())

