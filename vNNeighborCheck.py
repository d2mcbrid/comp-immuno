# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:22:50 2020

@author: davem
"""


import random
#loc needs to be a tuple
def checkaround(cellplacemat, loc, dim = 2):
    if dim == 1:
        x = loc[0]
        xpos = cellplacemat[x + 1]
        xneg = cellplacemat[x - 1]
    elif dim == 2:
        x = loc[0]
        y = loc[1]
        xpos = cellplacemat[x + 1, y]
        xneg = cellplacemat[x - 1, y]
        ypos = cellplacemat[x, y + 1]
        yneg = cellplacemat[x, y - 1]
    elif dim == 3:
        x = loc[0]
        y = loc[1]
        z = loc[2]
        xpos = cellplacemat[x + 1, y, z]
        xneg = cellplacemat[x - 1, y, z]
        ypos = cellplacemat[x, y + 1, z]
        yneg = cellplacemat[x, y - 1, z]
        zpos = cellplacemat[x, y, z + 1]
        zneg = cellplacemat[x, y, z - 1]
    else:
        return print('Dimension not supported')
    prolif_check = 'not prolif'  # for use in the while loop, to check if cell has proliferated into empty space
    # UP   will need to improve this code so that it checks next direction after checking one direction
    choose = np.arange(0,dim*2)# choosing random direction for proliferation
    random.shuffle(choose)
    for n in choose:
        if n == 0:
            if xpos == 0:
                if dim == 2:
                    prolifloc = [x + 1, y]
                
                if dim == 3:
                    prolifloc = [x + 1, y, z]
                
                if dim == 1:
                    prolifloc = [x + 1]
                    
                prolif_check = 'prolif'
                break
        # DOWN
        elif n == 1:
            if xneg == 0:
                if dim == 2:
                    prolifloc = [x - 1, y]
                
                if dim == 3:
                    prolifloc = [x - 1, y, z]
                
                if dim == 1:
                    prolifloc = [x - 1]
                    
                prolif_check = 'prolif'
                break
        # LEFT
        elif n == 2:
            if ypos == 0:
                if dim == 2:
                    prolifloc = [x, y + 1]
                
                if dim == 3:
                    prolifloc = [x, y + 1, z]
                    
                prolif_check = 'prolif'
                break

        # RIGHT
        elif n == 3:
            if yneg == 0:
                if dim == 2:
                    prolifloc = [x, y - 1]
                
                if dim == 3:
                    prolifloc = [x, y - 1, z]
                    
                prolif_check = 'prolif'
                break
        elif n == 4:
            if zpos == 0:

                if dim == 3:
                    prolifloc = [x, y, z + 1]
                    
                prolif_check = 'prolif'
                break
        elif n == 5:
            if zneg == 0:

                if dim == 3:
                    prolifloc = [x, y, z - 1]
                
                    
                prolif_check = 'prolif'
                break
            
    return [prolifloc, prolif_check]

def pushCell(cellplacemat, loc, dim = 2):
    
    random.randint(0,dim*2-1)
    