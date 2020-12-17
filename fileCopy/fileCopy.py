import shutil

#any directory of PC is acceptable
file_src ='D:/Game Development Pictures/army1.png'
f_src = open(file_src, 'rb')

#any directory of PC is acceptable
file_dest = 'C:/Users/ASUS/Desktop/Web Scraping/armyKKP.jpg'
f_dest = open(file_dest, 'wb')

shutil.copyfileobj(f_src, f_dest)