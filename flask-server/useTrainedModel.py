from keras.models import load_model
import pandas as pd
import numpy as np
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
model=load_model('predatorCatcher.keras')
df1=pd.read_csv(r"C:\Users\USER\Downloads\train.csv")
input1=np.array(df1.iloc[:,0])
output1=np.array(df1.iloc[:,2])
max_length=400
with open ('tokenizer.json','r',encoding='utf-8') as json_file:
    load_tokenizer=json_file.read()
tokenizer=tokenizer_from_json(load_tokenizer)
test_sequences=tokenizer.texts_to_sequences(input1)
test_padded=pad_sequences(test_sequences,maxlen=max_length,padding='post',truncating='post')
predictions=model.predict(test_padded)
predictions=np.argmax(predictions,axis=-1)
print(predictions)
correct=0
for i in range(len(predictions)):
    if(output1[i]==predictions[i]):
        correct+=1
print(correct/len(input1))