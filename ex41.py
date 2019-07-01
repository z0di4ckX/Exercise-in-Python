import random
from urllib import urllib
import sys

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDS = []

PHRASES = {
    "class %%%%(%%%%):":
        "Make a class name %%%% That is-a %%%%.",
    "class %%%%(object):\n\tdef__init__(self,***)":
        "class %%%% has-a function name *** that takes self and @@@ parameters.",
    "*** = %%%%()":
        "Set *** to an instance of class %%%%.",
    "***.***(@@@)":
        "Form *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "Form *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASES_FIRST  = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).redlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        # fake parameters lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until the hit CTRL-D
try:
    while True:
        snippet = PHRASES.keys()
        random.shuffle(snippet)

        for snippet in snippet:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER: %s\n\n" % answer)
except EOFError:
    print("\nBye")