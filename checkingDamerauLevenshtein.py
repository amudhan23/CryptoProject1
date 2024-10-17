def damerau_levenshtein(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)

    # Create a distance matrix
    d = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    # Initialize the matrix
    for i in range(len_s1 + 1):
        d[i][0] = i  # Deletion cost
    for j in range(len_s2 + 1):
        d[0][j] = j  # Insertion cost

    # Compute the distance
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1

            # Minimum of deletion, insertion, and substitution
            d[i][j] = min(
                d[i - 1][j] + 1,  # Deletion
                d[i][j - 1] + 1,  # Insertion
                d[i - 1][j - 1] + cost  # Substitution
            )

            # Check for transposition
            if (i > 1 and j > 1 and
                    s1[i - 1] == s2[j - 2] and
                    s1[i - 2] == s2[j - 1]):
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost)

    return d[len_s1][len_s2]


def compute_distances(string1, string2):
    distance = damerau_levenshtein(string1, string2)

    return distance


# Example usage
candidate_plaintexts = [
    "unconquerable tropical pythagoras rebukingly price ephedra",
    "protectorates committeemen refractory narcissus bridlers",
    "incomes shoes porcine pursue blabbered irritable ballets",
    "rejoicing nectar asker dreadfuls kidnappers interstate",
    "headmaster attractant subjugator peddlery vigil dogfights",
    # Add more strings as needed...
]

# Assume you have 60 strings
# For demonstration, let's limit to 5 strings above. Add the remaining strings similarly.
distance_result = compute_distances(candidate_plaintexts[0], candidate_plaintexts[1])

print("distance_result : ",distance_result)
# Print the distance matrix
# for i in range(len(candidate_plaintexts)):
#     print(f"Distances from Candidate Plaintext #{i + 1}: {distance_matrix[i]}")
