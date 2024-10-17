import requests


def get_random_words(count):
    """Fetch a list of random words from the RandomWordAPI."""
    url = f'https://random-word-api.herokuapp.com/word?number={count}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return []


def generate_english_string(target_length):
    """Generate a string of random English words with total length equal to target_length."""
    generated_string = ""

    while len(generated_string) < target_length:
        # Fetch a random word
        random_words = get_random_words(1)

        if random_words:
            word = random_words[0]
            # Check if we can add the word (including a space if not the first word)
            if len(generated_string) + len(word) + (1 if generated_string else 0) <= target_length:
                if generated_string:
                    generated_string += " "  # Add space before the word if it's not the first word
                generated_string += word  # Add the new word

    # Trim to ensure the string is exactly target_length
    if len(generated_string) > target_length:
        generated_string = generated_string[:target_length]  # Trim the string to target length if needed

    # Ensure that the final string has exactly the target length
    if len(generated_string) < target_length:
        # Add extra spaces if we have less than the target length
        generated_string += " " * (target_length - len(generated_string))

    return generated_string


# Generate a string of length 600
result = generate_english_string(600)
print(result)
print("Total length:", len(result))
