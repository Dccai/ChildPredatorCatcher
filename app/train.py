import pandas as pd
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.regularizers import l2
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import tokenizer_from_json

from nltk.corpus import stopwords

STOPWORDS=set(stopwords.words('english'))
df1=pd.read_csv(r"C:\Users\USER\Downloads\train.csv")
df2=pd.read_csv(r"C:\Users\USER\Downloads\pedoChatLogsv2.csv")
#inputs=np.array(df2.iloc[:,0])
#print(inputs)
#maxLen=0
#iterateArray=df2.iloc[:,0]
#for i in iterateArray:
 #   maxLen=max(maxLen,len(i))
#print(maxLen)

input1=np.array(df1.iloc[:,0])
output1=np.array(df1.iloc[:,2])
input2=np.array(df2.iloc[:,0])
output2=np.array(df2.iloc[:,1])
output=np.concatenate((output1,output2),axis=0)
input=np.concatenate((input1,input2),axis=0)
numOfSamples=len(input)
shuffled_indices=np.random.permutation(numOfSamples)
input=input[shuffled_indices]
output=output[shuffled_indices]
vocab_size=5000
embedding_dim=16
max_length=400
trunc_type='post'
oov_tok='<OOV>'
train_portion=0.8
train_size=int(len(input)*train_portion)
train_input=input[0:train_size]
train_output=output[0:train_size]
val_input=input[train_size:]
val_output=output[train_size:]
#tokenizer=Tokenizer(num_words=vocab_size,oov_token=oov_tok)
#tokenizer.fit_on_texts(train_input)
#tokenizer_json = tokenizer.to_json()
#with open('tokenizer.json', 'w', encoding='utf-8') as json_file:
 #   json_file.write(tokenizer_json)
with open ('tokenizer.json','r',encoding='utf-8') as json_file:
    load_tokenizer=json_file.read()
tokenizer=tokenizer_from_json(load_tokenizer)
word_index=tokenizer.word_index
#print(dict(list(word_index.items())[:10]))
train_sequences=tokenizer.texts_to_sequences(train_input)
train_padded=pad_sequences(train_sequences,maxlen=max_length,padding='post',truncating=trunc_type)
validation_sequences=tokenizer.texts_to_sequences(val_input)
val_padded=pad_sequences(validation_sequences,maxlen=max_length,padding='post',truncating=trunc_type)
model=Sequential([
    keras.layers.Embedding(vocab_size,embedding_dim),
    keras.layers.Bidirectional(LSTM(embedding_dim)),
    Dropout(0.5),
    Dense(embedding_dim,activation='relu',kernel_regularizer=l2(0.01)),
    Dropout(0.5),
    Dense(2,activation='softmax')
])
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
num_epochs = 10
history = model.fit(train_padded, train_output, epochs=num_epochs, validation_data=(val_padded, val_output), verbose=2,batch_size=128)
model.save('predatorCatcher.keras')

