import numpy as np

def create_matrix5(img, i, j):
    
    """ Kreiranje numerično polje za 25 elementi, iz začetnega indeksa [i,j]
    iz podano sliko ki bo ustrezalo velikosti kernela 1x25.
    
    * i - indeks za popis vrstice 
    * j - indeks za popis stolpce
    * img - sivinsko sliko
    """
    
    matrix = np.array([
                        img[0+i, 0+j],img[0+i, 1+j],img[0+i, 2+j],img[0+i, 3+j],img[0+i, 4+j],
                        img[1+i, 0+j],img[1+i, 1+j],img[1+i, 2+j],img[1+i, 3+j],img[1+i, 4+j],
                        img[2+i, 0+j],img[2+i, 1+j],img[2+i, 2+j],img[2+i, 3+j],img[2+i, 4+j],
                        img[3+i, 0+j],img[3+i, 1+j],img[3+i, 2+j],img[3+i, 3+j],img[3+i, 4+j],
                        img[4+i, 0+j],img[4+i, 1+j],img[4+i, 2+j],img[4+i, 3+j],img[4+i, 4+j]
                        ])
    return matrix


def gauss2D(img, kernel):
    """ Iteriranje skozi vse vrednosti slikovnih pikslov v x in v y smeri in množenje vsaka pikselna matrika z kernel polje  
    * img - sivinska slika
    * kernel - 1x25 numerično polje 
    """
    print("Using gauss2D from gaussModul.py...")
    height = img.shape[0]
    width = img.shape[1]
    pixels = []
    
    for i in range(0, height-4):
        for j in range(0, width-4):
            matrix = create_matrix5(img, i, j)
            new_pixel = (matrix * kernel).sum() / kernel.sum()
            pixels.append(new_pixel)

    new_img = np.array(pixels).reshape(height-4, width-4) 
    print("gauss2D successfully applied")
    return new_img
