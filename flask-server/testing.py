from keras.models import load_model
import pandas as pd
import numpy as np
from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
with open ('tokenizer.json','r',encoding='utf-8') as json_file:
    load_tokenizer=json_file.read()
input1=np.array(["Hey there 😊, just thinking about how amazing our last date was. The way your smile lights up the room is something I can't get enough of. Can't wait to see you again and share more of those sweet moments together. You mean the world to me ❤️."])
max_length=400
model=load_model('predatorCatcher.keras')
tokenizer=tokenizer_from_json(load_tokenizer)
test_sequences=tokenizer.texts_to_sequences(input1)
test_padded=pad_sequences(test_sequences,maxlen=max_length,padding='post',truncating='post')
predictions=model.predict(test_padded)
predictions=np.argmax(predictions,axis=-1)
print(predictions)