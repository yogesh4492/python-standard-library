import pickle
import time

data={'key':1,'name':'yogesh','age':20}
start_time=time.time()

with open ("file",'wb') as wp:
    pickle.dump(data,wp)
serialization_time=time.time()-start_time

start_time1=time.time()
with open("file",'rb') as rp:
    d=pickle.load(rp)
desir_time=time.time()-start_time1

print(d)
print(f"{serialization_time:.10f}")
print(f"{desir_time:.10f}")




