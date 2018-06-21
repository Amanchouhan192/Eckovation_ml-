book ={}

book['rob']={
	
	'name' : 'rob',
	'email': 'rob@gmail.com',
	'address' : 'lrc delhi',
	'age' : '12'

}

book['rick']={
	
	'name' : 'rick',
	'email': 'rick@gmail.com',
	'address' : 'lrc mubai',
	'age' : '16'

}
import json

s = json.dumps(book)
print(s)