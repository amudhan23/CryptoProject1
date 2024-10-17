import json
from math import log10
import sys
import random
import re
import Levenshtein

from checkingDamerauLevenshtein import compute_distances
from fuzzywuzzy import fuzz
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Adding json plaintext into array
file_path = 'candidate_plaintexts.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Create an array to store the candidates
ptext_dict = []


# Append each candidate to the array
for key, value in data.items():
    ptext_dict.append(value)



CHAR_SET = [chr(i) for i in range(ord('a'), ord('z') + 1)]
CHAR_SET.append(chr(ord(' ')))

# frequency table
freq_table = {
    'A': 8.12,
    'B': 1.49,
    'C': 2.78,
    'D': 4.25,
    'E': 12.02,
    'F': 2.23,
    'G': 2.02,
    'H': 6.09,
    'I': 7.00,
    'J': 0.15,
    'K': 0.77,
    'L': 4.03,
    'M': 2.41,
    'N': 6.95,
    'O': 7.68,
    'P': 1.93,
    'Q': 0.10,
    'R': 5.99,
    'S': 6.28,
    'T': 9.10,
    'U': 2.76,
    'V': 0.98,
    'W': 2.36,
    'X': 0.15,
    'Y': 2.00,
    'Z': 0.07,
    ' ': 11.00,
}

quadgram_tbl = {}
trigram_tbl = {}
bigram_tbl = {}



# Load bigram_tbl with english bigrams
with open('english_bigrams.txt') as f:
    for line in f:
        key, amount = line.split(' ')
        bigram_tbl[key] = int(amount)

# Load trigram_tbl with english trigrams
with open('english_trigrams.txt') as f:
    for line in f:
        key, amount = line.split(' ')
        trigram_tbl[key] = int(amount)

with open('english_quadgrams.txt') as f:
    for line in f:
        key, amount = line.split(' ')
        quadgram_tbl[key] = int(amount)

# total amount of trigrams in table
N = sum(trigram_tbl.values())
floor = log10(0.01/N)

# total amount of bigrams in table
NB = sum(bigram_tbl.values())

NQ = sum(quadgram_tbl.values())

for key in trigram_tbl:
    trigram_tbl[key] = log10(float(trigram_tbl[key])/N)

for key in bigram_tbl:
    bigram_tbl[key] = log10(float(bigram_tbl[key])/NB)

for key in quadgram_tbl:
    quadgram_tbl[key] = log10(float(quadgram_tbl[key])/NQ)

def frequency_counter(ct):
    curr_ct_freq = {}
    copy_freq_table = freq_table.copy()
    N = 0
    for c in ct:
        if c not in curr_ct_freq:
            curr_ct_freq = 1
        else:
            curr_ct_freq += 1
        N += 1

    for key in curr_ct_freq:
        freq = float(curr_ct_freq[key] / N) * 10
        
        for letter in copy_freq_table:
            freq_table[letter]

def generate_decryption_key():
    # frequency_counter(ct)
    return random.sample(range(0, 27), 27)

def score(ct, key):
    dt = decrypt_text(ct, key)
    quadgram_score = 0
    trigram_score = 0
    bigram_score = 0
    score = 0
    for i in range(len(dt) - 2):
        trigram_score += trigram_tbl.get(dt[i:i + 3].upper(), floor)
    for i in range(len(dt) - 1):
        bigram_score += bigram_tbl.get(dt[i:i + 2].upper(), floor)
    for i in range(len(dt) - 3):
        quadgram_score += quadgram_tbl.get(dt[i: i + 4].upper(), floor)
    score = 2 * quadgram_score + (0.85 * trigram_score) + 0.75 * (bigram_score)
    return score

def decrypt_text(ct, key):
    decrypted_text = ""
    for character in ct:
        index = None
        if character == " ":
            index = key[26]
        else:
            index = key[ord(character) - ord('a')]
        decrypted_character = CHAR_SET[index]
        decrypted_text += decrypted_character
    return decrypted_text

def InnerHillClimb(ct, key):
    innerScore = score(ct,key)
    best_inner_key = key
    for i in range (2000):
            randi = random.randint(0, 26)
            randj = random.randint(0, 26)
    # for i in range(26):
    #     for j in range(27 - i):
    #         randi = j
    #         randj = j + i
            curr_key = best_inner_key[:]
            curr_key[randi], curr_key[randj] = curr_key[randj], curr_key[randi]
            curr_innerScore = score(ct, curr_key)
            if curr_innerScore > innerScore:
                innerScore = curr_innerScore
                best_inner_key = curr_key
    return innerScore, best_inner_key

def RandomInitKey(ct):
    bestInitScore = float('-inf')
    bestKey = None
    key = generate_decryption_key()
    initScore, initKey = InnerHillClimb(ct, key)
    if initScore > bestInitScore:
        bestInitScore = initScore
        bestKey = initKey
    return bestInitScore, bestKey


#
# # Your strings
# string1 = "unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped overdecorates linked smitten trickle scanning cognize oaken casework significate influenceable precontrived clockers defalcation fruitless splintery kids placidness regenerate harebrained liberalism neuronic clavierist attendees matinees prospectively bubbies longitudinal raving relaxants rigged oxygens chronologist briniest tweezes profaning abeyances fixity gulls coquetted budgerigar drooled unassertive shelter subsoiling surmounted frostlike jobbed hobnailed fulfilling jaywalking testabilit"
# string2 = "protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms denunciation chronaxy imperilment incurred defrosted beamy opticopupillary acculturation scouting curiousest tosh preconscious weekday reich saddler politicize mercerizes saucepan bifold chit reviewable easiness brazed essentially idler dependable predicable locales rededicated cowbird kvetched confusingly airdrops dreggier privileges tempter anaerobes glistened sartorial distrustfulness papillary ughs proctoring duplexed pitas traitorously unlighted cryptographer odysseys metamer either meliorat"
#
# # Calculate the similarity score
# similarity_score = fuzz.ratio(string1, string2)




def outerHillClimb(ct):

    best_score, bestKey = RandomInitKey(ct)


    for i in range(25):
        score, curr_key = RandomInitKey(ct)
        if score > best_score:
            best_score = score
            bestKey = curr_key
    
    return bestKey



def position_weighted_match(str1, str2):
    """
    Compare two strings by matching their characters and accounting for positional differences.
    Higher score indicates a better match with less positional difference.
    """
    # Initial fuzzy ratio (basic string matching score)
    match_score = fuzz.ratio(str1, str2)

    # Adjusting the score by penalizing positional mismatches
    penalty = 0
    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        if str1[i] == str2[i]:
            continue  # No penalty for exact match at same position
        else:
            # Penalize based on how far the characters are in the strings
            penalty += abs(i - str2.find(str1[i])) if str1[i] in str2 else len(str2)

    # Scale the penalty down to a fraction of the length
    weighted_penalty = penalty / max(len(str1), len(str2))

    # Calculate final score by reducing penalty from initial match score
    final_score = match_score - weighted_penalty/10
    return final_score




def cosine_weighted_match(str1, str2):
# Convert strings to word count vectors
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([str1, str2])

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix)
    print("TF-IDF Cosine Similarity:", cosine_sim[0][1])
    return cosine_sim[0][1]



# def decipher(ct):
#
#     bestKey = outerHillClimb(ct)
#
#     pt = decrypt_text(ct, bestKey)
#
#     # select most likely answer
#     # minOps = float('inf')
#     minOps = float('-inf')
#     answer = ""
#
#     for pos_pt in ptext_dict:
#         # currOps = compute_distances(pt, pos_pt)
#         currOps = fuzz.ratio(pt, pos_pt)
#         # currOps=position_weighted_match(pt,pos_pt)
#         # currOps = cosine_weighted_match(pt, pos_pt)
#         print("Score : ",currOps)
#         # currOps = Levenshtein.distance(pt, pos_pt)
#         if currOps > minOps:
#             minOps = currOps
#             answer = pos_pt
#
#     # print(f"\nbestKey: {bestKey}")
#     # print(f"\nplaintext: {answer}")
#     return bestKey, answer



    


# if __name__ == "__main__":
#     ct = input("Enter the Ciphertext")

#     decipher(ct)
    # guess = decipher(ct)
    # sys.stdout.write(f'My plaintext guess is:{guess}')

import Levenshtein
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.util import ngrams
from collections import Counter


# Cosine Similarity Calculation
def cosine_sim_score(decrypted_text, plaintexts):
    vectorizer = CountVectorizer().fit_transform([decrypted_text] + plaintexts)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return cosine_sim


# Levenshtein Distance Calculation
def levenshtein_score(decrypted_text, plaintexts):
    lev_distances = [Levenshtein.distance(decrypted_text, pt) for pt in plaintexts]
    # Inverse the distances for the scoring (higher score is better)
    lev_scores = [1 / (dist + 1) for dist in lev_distances]
    return lev_scores


# N-gram Similarity Calculation
def ngram_similarity(text1, text2, n=3):
    ngrams1 = Counter(ngrams(text1.split(), n))
    ngrams2 = Counter(ngrams(text2.split(), n))
    common_ngrams = ngrams1 & ngrams2
    return sum(common_ngrams.values())


def ngram_sim_score(decrypted_text, plaintexts, n=3):
    return [ngram_similarity(decrypted_text, pt, n) for pt in plaintexts]


# Combined Scoring Function
def combined_score(decrypted_text, plaintexts, ngram_n=3, weights=(0.4, 0.3, 0.3)):
    # Get scores from all three methods
    cos_sim_scores = cosine_sim_score(decrypted_text, plaintexts)
    lev_scores = levenshtein_score(decrypted_text, plaintexts)
    ngram_sim_scores = ngram_sim_score(decrypted_text, plaintexts, n=ngram_n)

    # Normalize all scores
    max_cos_sim = max(cos_sim_scores)
    max_ngram_sim = max(ngram_sim_scores)

    if max_cos_sim > 0:
        cos_sim_scores = [score / max_cos_sim for score in cos_sim_scores]  # Normalize to [0, 1]

    if max_ngram_sim > 0:
        ngram_sim_scores = [score / max_ngram_sim for score in ngram_sim_scores]  # Normalize to [0, 1]

    # Combine scores based on weights
    combined_scores = [
        (weights[0] * cos_sim + weights[1] * lev + weights[2] * ngram)
        for cos_sim, lev, ngram in zip(cos_sim_scores, lev_scores, ngram_sim_scores)
    ]

    # Return the index of the best match and the combined scores
    best_match_index = combined_scores.index(max(combined_scores))
    return best_match_index, combined_scores


plaintexts = ptext_dict


def decipher(ct):

    bestKey = outerHillClimb(ct)

    pt = decrypt_text(ct, bestKey)

    best_match_index, combined_scores = combined_score(pt, plaintexts, ngram_n=3)
    return bestKey, ptext_dict[best_match_index]



