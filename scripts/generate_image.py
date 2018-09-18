##! packages/python3/bin/ python3.6

import numpy as np
import matplotlib
matplotlib.use('agg')
from matplotlib import pyplot as plt
#import astropy

def generate_blank_image(row_num,col_num,rms=1,bg=0):
    
    array = rms*np.random.random((row_num,col_num))+bg
    return array

    
def source_psf(x,y,pos_x,pos_y,sigma_x=1.,sigma_y=1.,flux=1.):

    g = (flux/(2.*np.pi*sigma_x*sigma_y)) * np.exp(-( (x-pos_x)**2/sigma_x**2 + (y-pos_y)**2/sigma_y**2) / 2.)
    return g

def generate_star_position(length_x,length_y,num_star):

    pos_x = length_x*(np.random.random_sample((num_star,))-0.5)
    pos_y = length_y*(np.random.random_sample((num_star,))-0.5) 

    return [pos_x,pos_y]

def add_position_error(pos,pos_error=0.1):

    pos[0] = pos[0] + pos_error*np.random.randn(len(pos[0]))
    pos[1] = pos[1] + pos_error*np.random.randn(len(pos[1]))
    
    return pos

def add_quasar(data,pos_q1,pos_q2,flux1,flux2):

    data = data + source_psf(x,y,pos[0][i],pos[1][i])
    return data

def add_sources(length_x,length_y,acsperpix,pos_error,num_star):

    np.random.seed(0)
    sampling_x,sampling_y = int(length_x/acsperpix),int(length_y/acsperpix)
    data = generate_blank_image(sampling_x,sampling_y,rms=0.01,bg=0)
    x, y = np.meshgrid(np.linspace(-length_x/2,length_x/2,sampling_x), np.linspace(-length_y/2,length_y/2,sampling_y))
    
    pos = generate_star_position(length_x,length_y,num_star)
    pos = add_position_error(pos,pos_error)

    for i in range(len(pos[0])):
        data = data+source_psf(x,y,pos[0][i],pos[1][i])
 
    data = data + source_psf(x,y,pos_q1[0],pos_q1[1],flux_q1)
    data = data + source_psf(x,y,pos_q2[0],pos_q2[1],flux_q2)
    
    '''
    for i in range(1,20):
        pos_x = length_x*(np.random.random_sample()-0.5)
        pos_y = length_y*(np.random.random_sample()-0.5)
        data = data+source_psf(x,y,pos_x,pos_y)
    '''

    return data

if __name__ == '__main__' :
    #data = add_sources(2024,4048,0.26)
    data = add_sources(500,500,0.26,0.1,100)
    plt.imshow(data)
    plt.savefig("test.png")

