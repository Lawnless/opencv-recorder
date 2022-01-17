import numpy as np 
import cv2

# Windows ve MAC kullanıcıları için PILLOW.
from PIL import ImageGrab

# Linux kullanıcıları için pyscreenshot.
#import pyscreenshot as ImageGrab

cozunurluk_x = 1366
cozunurluk_y = 768
fps_deger = 5.0

dktur = cv2.VideoWriter_fourcc(*'MJPG') # MJPG, DIVX, XVID
cikti = cv2.VideoWriter("video.avi", dktur, fps_deger, (cozunurluk_x, cozunurluk_y))

while True:
	img = ImageGrab.grab()
	img_np = np.array(img)
	cerceve = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) # Renkleri değiştirebilirsiniz.
	cv2.imshow("Ekran Kaydı", cerceve)
	cikti.write(cerceve)
	if cv2.waitKey(1) == 27: # ESC tuşu kaydı durdurur.
		break

cikti.release()
cv2.destroyAllWindows()
