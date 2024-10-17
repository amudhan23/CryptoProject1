import random

CHAR_SET = [chr(i) for i in range(ord('a'), ord('z') + 1)]
CHAR_SET.append(' ')

# ptext_dict = [
#     "unconquerable tropical pythagoras rebukingly price ephedra barmiest hastes spades fevers cause wisped overdecorates linked smitten trickle scanning cognize oaken casework significate influenceable precontrived clockers defalcation fruitless splintery kids placidness regenerate harebrained liberalism neuronic clavierist attendees matinees prospectively bubbies longitudinal raving relaxants rigged oxygens chronologist briniest tweezes profaning abeyances fixity gulls coquetted budgerigar drooled unassertive shelter subsoiling surmounted frostlike jobbed hobnailed fulfilling jaywalking testabilit",
#     "protectorates committeemen refractory narcissus bridlers weathercocks occluding orchectomy syncoms denunciation chronaxy imperilment incurred defrosted beamy opticopupillary acculturation scouting curiousest tosh preconscious weekday reich saddler politicize mercerizes saucepan bifold chit reviewable easiness brazed essentially idler dependable predicable locales rededicated cowbird kvetched confusingly airdrops dreggier privileges tempter anaerobes glistened sartorial distrustfulness papillary ughs proctoring duplexed pitas traitorously unlighted cryptographer odysseys metamer either meliorat",
#     "incomes shoes porcine pursue blabbered irritable ballets grabbed scything oscillogram despots pharynxes recompensive disarraying ghoulish mariachi wickerwork orientation candidnesses nets opalescing friending wining cypher headstrong insubmissive oceanid bowlegs voider recook parochial trop gravidly vomiting hurray friended uncontestable situate fen cyclecars gads macrocosms dhyana overruns impolite europe cynical jennet tumor noddy canted clarion opiner incurring knobbed planeload megohm dejecting campily dedicational invaluable praecoces coalescence dibbuk bustles flay acuities centimeters l",
#     "rejoicing nectar asker dreadfuls kidnappers interstate incrusting quintessential neglecter brewage phosphatic angle obliquely bean walkup outflowed squib tightwads trenched pipe extents streakier frowning phantasmagories supinates imbibers inactivates tingly deserter steerages beggared pulsator laity salvageable bestrode interning stodgily cracker excisions quanted arranges poultries sleds shortly packages apparat fledge alderwomen halvah verdi ineffectualness entrenches franchising merchantability trisaccharide limekiln sportsmanship lassitudes recidivistic locating iou wardress estrus potboi",
#     "headmaster attractant subjugator peddlery vigil dogfights pixyish comforts aretes felinities copycat salerooms schmeering institutor hairlocks speeder composers dramatics eyeholes progressives reminiscent hermaphrodism simultaneous spondaics hayfork armory refashioning battering darning tapper pancaked unaffected televiewer mussiness pollbook sieved reclines restamp cohosh excludes homelier coacts refashioned loiterer prospectively encouragers biggest pasters modernity governorships crusted buttoned wallpapered enamors supervisal nervily groaning disembody communion embosoming tattles pancakes",
# ]

pairings = {}

otherpairings = {}

key_answer = [0 for _ in range(27)]

def create_pairings(key):
    for i in range(len(key)):
        pairings[CHAR_SET[i]] = CHAR_SET[key[i]]
        otherpairings[CHAR_SET[key[i]]] = CHAR_SET[i]
        key_answer[key[i]] = i

def monoalpha(character, replace):
    # check if pairing already exists
    if character in pairings:
        return pairings[character]
    print(replace)

    pairings[character] = CHAR_SET[replace]

    return CHAR_SET[replace]
    

# Monoalpha substitution cipher with random chars for randomness
def encryption(key, message, prob):
    ciphertext = ""
    ciphertext_pointer = 1
    message_pointer = 0
    num_rand_characters = 0
    prob_of_random_ciphertext = prob
    L = len(message)

    while ciphertext_pointer <= L + num_rand_characters:
        coin_value = random.random()
        if prob_of_random_ciphertext <= coin_value:
            j = (CHAR_SET.index(message[message_pointer]))
            ciphertext += monoalpha(message[message_pointer], key[j])
            message_pointer += 1
        elif coin_value < prob_of_random_ciphertext:
            random_character = random.choice(CHAR_SET)
            ciphertext += random_character
            num_rand_characters += 1

        ciphertext_pointer += 1
        # print(f"\nNumber of Random Characters: {num_rand_characters}")        
    return ciphertext, num_rand_characters

# # generate a key
# key = random.sample(range(0, 27), 27) # t == 27

# create_pairings(key)

# # chooses a random plain text
# random_pt = random.choice(ptext_dict)

# # encrypt the plain text with the key
# ciphertext = encryption(key, random_pt)

# print(f"\nPlaintext: {random_pt}")
# print(f"\nKey: {key}")
# print(f"\nCiphertext: {ciphertext}")
# print(f"\nPairings: {pairings}")
# # print(f"\nNewKeyPairings: {otherpairings}")
# print(f"\nKey_Answer: {key_answer}")
