import cv2 as cv
import numpy as np

# pour faire une image vide "noire"
blank = np.zeros((500, 500, 3), dtype='uint8') # np.zeros((500, 500, 3) 500 fait réfence la width et 500 height 3 la couleur
# cv.imshow("Blank", blank)

# 1 Peintre une image en couleur
#blank[:] = 0, 0, 255 # 255 code couleur
#cv.imshow("Red", blank)
blank[200:300, 300:400] = 0, 0, 255 # Peindre la moitié de mon tableau faire un carré en couleur
#cv.imshow("Red", blank)

# 2 Dessiner un rectangle dans l'image
                    # x y   width height  color     epaiseur
cv.rectangle(blank, (0, 0), (250, 250),  (0,255,0), thickness=2) # thickness=cv.FILLED ou -1  ***** (250,250) on peut le remplacer de maniére auto comme (blank.shape[1]//2, blank.shape[0]//2) 
cv.imshow("Rectangle", blank)

# 3. Dessiner un cercle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1 )
cv.imshow("Cercle", blank)

# 4 dessiner une ligne
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3 ) # cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3 )
cv.imshow("Ligne", blank)

# 5 Ecrire du texte dans l'image
cv.putText(blank, 'Bonjour Bassirou CISSE', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)