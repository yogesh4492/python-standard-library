import pickle 

def storedata():
    yogesh={'key':"Yog",'name':'Yogesh','age':20}
    Anuj={'key':'Aj','name':'Anuj','age':19}

    db={}
    db['yogesh']=yogesh
    db['Anuj']=Anuj

    dbfile=open("File",'ab')#append with binary 

    pickle.dump(db,dbfile)

    dbfile.close()

def data():
    dbfile=open("File",'rb')
    db=pickle.load(dbfile)

    for i in db:
        print(f"{i} => {db[i]}")

    dbfile.close()

if __name__=="__main__":
    storedata()
    data()