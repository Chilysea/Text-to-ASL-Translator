from sklearn.preprocessing import LabelEncoder
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

# Example data
english_sentences = [
    "I am hungry",
    "Thank you very much",
    "Please help me"
]

asl_sequences = [
    ['I', 'hungry'],
    ['thank', 'you', 'much'],
    ['please', 'help', 'me']
]

# Tokenize the English sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(english_sentences)
encoded_english = tokenizer.texts_to_sequences(english_sentences)

# Pad the sequences to ensure uniform length
max_length_english = max(len(seq) for seq in encoded_english)
padded_english = pad_sequences(encoded_english, maxlen=max_length_english, padding='post')

# Encode ASL signs
all_asl_labels = [label for sequence in asl_sequences for label in sequence]
asl_label_encoder = LabelEncoder()
asl_label_encoder.fit(all_asl_labels)
encoded_asl_sequences = [asl_label_encoder.transform(sequence) for sequence in asl_sequences]

# Pad ASL sequences
max_length_asl = max(len(seq) for seq in encoded_asl_sequences)
padded_asl = pad_sequences(encoded_asl_sequences, maxlen=max_length_asl, padding='post')

print("Padded English sequences:", padded_english)
print("Padded ASL sequences:", padded_asl)
