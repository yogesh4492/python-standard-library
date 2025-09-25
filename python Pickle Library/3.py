import pickle

data=[11,2,34,55,6]

with open ("File",'wb') as wp:
    pickle.dump(data,wp)

with open("File",'rb') as rp:
    d=pickle.load(rp)
    for i in d:
        print(f"{i} ")



