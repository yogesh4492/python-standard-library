import pickle

data={'name':'yogesh','roll':22,'subject':['c','c++','python']}

with open('tok.pickle','wb') as e:
    pickle.dump(data,e)
print("Data serilization success !!!")
