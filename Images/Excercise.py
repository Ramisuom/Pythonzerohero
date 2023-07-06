from PIL import Image
words = Image.open('word_matrix.png')
mask = Image.open('mask.png')
#words.show()
#mask.show()

words.paste(mask,(0,0),mask)
print(words.size)
mask = mask.resize((1015,559))
print(words.size)
mask.putalpha(200)
words.paste(mask,(0,0),mask)
print(words)