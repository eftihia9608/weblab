import requests  # εισαγωγή της βιβλιοθήκης

x=input('Dwse th url')
url=x
print('H dieuthinsh pou dothhke einai:',x)

r=requests.get(x, headers={"content-type":"text"})

print('\n\n')

print('Oi headers einai:',r.headers)
print('\n\n')
print('To logismiko tou exyphrethth einai:',r.headers['Server'])
print('\n\n')

#print(r.cookies.keys)

for cookie in r.cookies:
    if cookie.name == 'NONE':
        print('H url den exei cookies')
    
    else:
        expires = cookie.expires
        print('H url exei cookies ta opoia einai egkyra gia diasthma',expires)
              
