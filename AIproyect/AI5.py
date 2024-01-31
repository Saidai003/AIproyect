import random
from collections import defaultdict

class SimpleLanguageModel:
    def __init__(self):
        self.word_freqs = defaultdict(int)

    def train(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    self.word_freqs[word] += 1

    def generate_word(self):
        total_words = sum(self.word_freqs.values())
        rand_index = random.randint(0, total_words-1)
        cumulative_freq = 0
        for word, freq in self.word_freqs.items():
            cumulative_freq += freq
            if cumulative_freq > rand_index:
                return word

    def evaluate_and_update(self, filename, num_iterations, num_words):
        with open(filename, 'r', encoding='utf-8') as f:
            for _ in range(num_iterations):
                f.seek(0)  # Regresa al inicio del archivo para cada iteración
                words = f.read().strip().split()
                for i in range(0, len(words), num_words+1):
                    generated_word = self.generate_word()
                    if i+num_words < len(words) and words[i+num_words] != generated_word:
                        self.word_freqs[generated_word] = max(0, self.word_freqs[generated_word]-1)
                    elif i+num_words < len(words):
                        self.word_freqs[generated_word] += 1

    def predict_next_word(self, input_words):
        return self.generate_word()

# Uso del modelo
model = SimpleLanguageModel()
model.train('0_palabras_todas.txt')
num_iterations = int(input("Ingrese el número de iteraciones: "))
num_words = int(input("Ingrese el número de palabras para comparar: "))
model.evaluate_and_update('texto.txt', num_iterations, num_words)
while True:
    input_words = input("Ingrese palabras: ")
    print("La siguiente palabra podría ser:", model.predict_next_word(input_words))
