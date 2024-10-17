import json

# Your data
plaintexts = {
    "Candidate Plaintext #1": """unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped ...""",
    "Candidate Plaintext #2": """protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms ...""",
    "Candidate Plaintext #3": """incomes shoes porcine pursue blabbered irritable ballets grabbed scything oscillogram despots ...""",
    "Candidate Plaintext #4": """rejoicing nectar asker dreadfuls kidnappers interstate incrusting quintessential neglecter brewage ...""",
    "Candidate Plaintext #5": """headmaster attractant subjugator peddlery vigil dogfights pixyish comforts aretes felinities copycat ..."""
}

# Save to a file in the current directory
file_name = 'candidate_plaintexts.json'
with open(file_name, 'w') as json_file:
    json.dump(plaintexts, json_file, indent=4)

print(f"File saved as {file_name}")
