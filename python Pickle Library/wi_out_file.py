import pickle

yogesh={'key':"Yog",'name':'Yogesh','age':20}
Anuj={'key':'Aj','name':'Anuj','age':19}

db={}
db['Yogesh']=yogesh
db['Anuj']=Anuj
#for storing
b=pickle.dumps(db)

#for Loading
Mykeys=pickle.loads(b)
print(Mykeys)

