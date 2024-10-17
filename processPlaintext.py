import json

# Load the JSON file
file_name = 'candidate_plaintexts.json'

with open(file_name, 'r') as json_file:
    plaintexts = json.load(json_file)

# Convert the JSON into a list (array) by extracting only the values (candidate plaintexts)
candidates_list = list(plaintexts.values())

# Count the number of words in each candidate and store the results
word_counts = [len(candidate.split()) for candidate in candidates_list]

# Print the word count for each candidate
for i, count in enumerate(word_counts, start=1):
    print(f"Candidate Plaintext #{i} has {count} words.")
