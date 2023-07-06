from PIL import Image
mac = Image.open('example.jpg')
print(type(mac))
#mac.show()
print(mac.size)
print(mac.filename)
print(mac.format_description)

#Cropping images
print(mac.crop((0,0,100,100)))
pencils = Image.open('pencils.jpg')
print(pencils)
#sac = Image.open('pencils.jpg')
#sac.show()
print(pencils.size)
x = 0
y = 0

w = 1950 / 3
h = 1300 / 10
print(pencils.crop((x,y,w,h)))

#BOTTOM pencils
x = 0
y = 1100

w = 1950 / 3
h = 1300
print(pencils.crop((x,y,w,h)))