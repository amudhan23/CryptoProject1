import json
import random
from encryption import create_pairings, encryption
from decryption import decipher

# ptext_dict = [
#     "unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped overdecorates linked smitten trickle scanning cognize oaken casework significate influenceable precontrived clockers defalcation fruitless splintery kids placidness regenerate harebrained liberalism neuronic clavierist attendees matinees prospectively bubbies longitudinal raving relaxants rigged oxygens chronologist briniest tweezes profaning abeyances fixity gulls coquetted budgerigar drooled unassertive shelter subsoiling surmounted frostlike jobbed hobnailed fulfilling jaywalking testabilit",
#     "protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms denunciation chronaxy imperilment incurred defrosted beamy opticopupillary acculturation scouting curiousest tosh preconscious weekday reich saddler politicize mercerizes saucepan bifold chit reviewable easiness brazed essentially idler dependable predicable locales rededicated cowbird kvetched confusingly airdrops dreggier privileges tempter anaerobes glistened sartorial distrustfulness papillary ughs proctoring duplexed pitas traitorously unlighted cryptographer odysseys metamer either meliorat",
#     "incomes shoes porcine pursue blabbered irritable ballets grabbed scything oscillogram despots pharynxes recompensive disarraying ghoulish mariachi wickerwork orientation candidnesses nets opalescing friending wining cypher headstrong insubmissive oceanid bowlegs voider recook parochial trop gravidly vomiting hurray friended uncontestable situate fen cyclecars gads macrocosms dhyana overruns impolite europe cynical jennet tumor noddy canted clarion opiner incurring knobbed planeload megohm dejecting campily dedicational invaluable praecoces coalescence dibbuk bustles flay acuities centimeters l",
#     "rejoicing nectar asker dreadfuls kidnappers interstate incrusting quintessential neglecter brewage phosphatic angle obliquely bean walkup outflowed squib tightwads trenched pipe extents streakier frowning phantasmagories supinates imbibers inactivates tingly deserter steerages beggared pulsator laity salvageable bestrode interning stodgily cracker excisions quanted arranges poultries sleds shortly packages apparat fledge alderwomen halvah verdi ineffectualness entrenches franchising merchantability trisaccharide limekiln sportsmanship lassitudes recidivistic locating iou wardress estrus potboi",
#     "headmaster attractant subjugator peddlery vigil dogfights pixyish comforts aretes felinities copycat salerooms schmeering institutor hairlocks speeder composers dramatics eyeholes progressives reminiscent hermaphrodism simultaneous spondaics hayfork armory refashioning battering darning tapper pancaked unaffected televiewer mussiness pollbook sieved reclines restamp cohosh excludes homelier coacts refashioned loiterer prospectively encouragers biggest pasters modernity governorships crusted buttoned wallpapered enamors supervisal nervily groaning disembody communion embosoming tattles pancakes",
# ]

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

print(len(ptext_dict))


print(ptext_dict[7])

#algo starts


for i in range(10):
    # generate a key
    key = random.sample(range(0, 27), 27) # t == 27

    create_pairings(key)

    prob = 0.2

    # chooses a random plain text
    # random_pt = random.choice(ptext_dict)
    random_pt = ptext_dict[i]

    for j in range(2):

    # encrypt the plain text with the key
        print("Plaintext : ",ptext_dict[i])
        print("Prob : ",prob)
        ciphertext, num_of_random_characters = encryption(key, random_pt, prob)

        print("ciphertext : ", ciphertext)

        bestKey, guesstext = decipher(ciphertext)

        if random_pt == guesstext:
            print(f"FOUND ANSWER with random_prob: {prob}\n and num_rand: {num_of_random_characters}")
            print(f"answer: {random_pt}")
            print(f"guess answer: {guesstext}")
        else:
            print(f"DIDNT FIND ANSWER with random_prob: {prob} and num_rand: {num_of_random_characters}")
            print(f"answer: {random_pt}")
            print(f"guess answer: {guesstext}")
        prob += .10



