d = {'k1':1, 'k2':2}
#print({x:x**2 for x in zip(['a','b'],range(2))})
for k in d.iteritems():
    print(k)

d.viewitems()