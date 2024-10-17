import random
import math
from collections import Counter

ENGLISH_FREQ = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28,
    'R': 6.02, 'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61,
    'F': 2.30, 'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11,
    'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07
}

# Example of English bigram frequencies (partial)
ENGLISH_BIGRAM_FREQ = {
    'TH': 0.0271, 'HE': 0.0232, 'IN': 0.0203, 'ER': 0.0178, 'AN': 0.0161,
    'RE': 0.0141, 'ON': 0.0135, 'AT': 0.0124, 'EN': 0.0124, 'ND': 0.0122
    # Add more common bigrams and normalize them to sum to 1
}

# Example of English trigram frequencies (partial)
ENGLISH_TRIGRAM_FREQ = {
    'THE': 0.0181, 'AND': 0.0073, 'ING': 0.0072, 'HER': 0.0051, 'THA': 0.0042
    # Add more common trigrams and normalize them to sum to 1
}

# Normalize the frequencies to sum to 1 (bigram & trigram)
TOTAL_BIGRAM_FREQ = sum(ENGLISH_BIGRAM_FREQ.values())
ENGLISH_BIGRAM_FREQ = {k: v / TOTAL_BIGRAM_FREQ for k, v in ENGLISH_BIGRAM_FREQ.items()}

TOTAL_TRIGRAM_FREQ = sum(ENGLISH_TRIGRAM_FREQ.values())
ENGLISH_TRIGRAM_FREQ = {k: v / TOTAL_TRIGRAM_FREQ for k, v in ENGLISH_TRIGRAM_FREQ.items()}


# Utility function to compute letter, bigram, and trigram frequency score
def frequency_score(text):
    """Calculate a score based on how close the letter, bigram, and trigram frequencies
    of the text are to the expected English frequencies."""

    score = 0

    # Letter frequency score
    letter_freq = Counter(text.upper())
    total_letters = sum(letter_freq.values())

    if total_letters > 0:
        for char, freq in ENGLISH_FREQ.items():
            actual_freq = letter_freq[char] / total_letters if char in letter_freq else 0
            score += abs(actual_freq - freq)

    # Bigram frequency score
    bigram_freq = Counter([text[i:i + 2].upper() for i in range(len(text) - 1)])
    total_bigrams = sum(bigram_freq.values())

    if total_bigrams > 0:
        for bigram, freq in ENGLISH_BIGRAM_FREQ.items():
            actual_freq = bigram_freq[bigram] / total_bigrams if bigram in bigram_freq else 0
            score += abs(actual_freq - freq)

    # Trigram frequency score
    trigram_freq = Counter([text[i:i + 3].upper() for i in range(len(text) - 2)])
    total_trigrams = sum(trigram_freq.values())

    if total_trigrams > 0:
        for trigram, freq in ENGLISH_TRIGRAM_FREQ.items():
            actual_freq = trigram_freq[trigram] / total_trigrams if trigram in trigram_freq else 0
            score += abs(actual_freq - freq)

    return -score  # Inverted score because we want to minimize the distance from expected values


# Simulated Annealing Algorithm
def simulated_annealing(ciphertext, initial_key, max_iterations=6000, temperature=1.0, cooling_rate=0.995):
    current_key = initial_key.copy()
    current_decryption = decrypt(current_key, ciphertext)
    current_score = frequency_score(current_decryption)

    best_key = current_key.copy()
    best_score = current_score

    for i in range(max_iterations):
        # Create a new candidate key by swapping two random letters
        new_key = current_key.copy()
        a, b = random.sample(list(new_key.keys()), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]

        # Decrypt the ciphertext using the new key
        new_decryption = decrypt(new_key, ciphertext)
        new_score = frequency_score(new_decryption)

        # Calculate the acceptance probability
        score_diff = new_score - current_score
        acceptance_prob = math.exp(score_diff / temperature) if score_diff < 0 else 1

        # Accept the new key with a probability based on the score difference
        if score_diff > 0 or random.random() < acceptance_prob:
            current_key = new_key
            current_score = new_score
            current_decryption = new_decryption

            # Update the best key if the new key is better
            if current_score > best_score:
                best_key = current_key
                best_score = current_score

        # Cool down the temperature
        temperature *= cooling_rate

    return best_key, best_score


# Utility functions for encryption and decryption (same as before)
def encrypt(key, plaintext):
    return ''.join([key.get(char, char) for char in plaintext.upper()])


def decrypt(key, ciphertext):
    reversed_key = {v: k for k, v in key.items()}
    return ''.join([reversed_key.get(char, char) for char in ciphertext])


# Create a random key for testing purposes (for encrypting)
def create_random_key():
    letters = list(ENGLISH_FREQ.keys())
    shuffled = letters.copy()
    random.shuffle(shuffled)
    return dict(zip(letters, shuffled))


# Example usage
plaintext = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"

# Create a random key for encryption
random_key = create_random_key()

# Encrypt the plaintext
ciphertext = encrypt(random_key, plaintext)
print("Ciphertext:", ciphertext)

# Initial random key guess for decryption
initial_key_guess = create_random_key()

# Perform simulated annealing to decrypt the ciphertext
best_key, best_score = simulated_annealing(ciphertext, initial_key_guess)

# Decrypt using the best key found
decrypted_text = decrypt(best_key, ciphertext)
print("\nDecrypted Text:", decrypted_text)
print("Best Key:", best_key)
print("Best Score:", best_score)
