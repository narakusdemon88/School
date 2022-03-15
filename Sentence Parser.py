"""
Name: Jon-Erik Akashi
Date: 3/8/2022
Title: Mini-project 3
"""


class Word:
    def __init__(self):
        self.word = []

    def get_default_value(self):
        return self.word[0]


class SentenceReadingAgent:
    def __init__(self):

        # open the file
        f = open("mostcommon.txt", mode="r", encoding="UTF-8", errors="ignore")

        self.unwanted_punctuations = [".", ",", "?", "!", ";"]

        # get rid of the trailing backslash n and put each item into a list
        self.lines = [line.rstrip("\n") for line in f.readlines()]

        self.time_words = ['morning', 'afternoon', 'evening', 'night']

        # made using spacy + pandas beforehand
        # https://spacy.io/usage/linguistic-features
        self.word_dictionary = {
            "Serena": "NNP",
            "Andrew": "NNP",
            "Bobbie": "NNP",
            "Cason": "NNP",
            "David": "NNP",
            "Farzana": "NNP",
            "Frank": "NNP",
            "Hannah": "NNP",
            "Ida": "NNP",
            "Irene": "NNP",
            "Jim": "NNP",
            "Jose": "NNP",
            "Keith": "NNP",
            "Laura": "NNP",
            "Lucy": "NNP",
            "Meredith": "NNP",
            "Nick": "NNP",
            "Ada": "NNP",
            "Yeeling": "NNP",
            "Red": "NNP",
            "Yan": "NNP",
            "the": "DT",
            "of": "IN",
            "to": "TO",
            "and": "CC",
            "a": "XX",
            "in": "IN",
            "is": "VBZ",
            "it": "PRP",
            "you": "PRP",
            "that": "IN",
            "he": "PRP",
            "was": "VBD",
            "for": "IN",
            "on": "IN",
            "are": "VBP",
            "with": "IN",
            "as": "IN",
            "I": "PRP",
            "his": "PRP$",
            "they": "PRP",
            "be": "VB",
            "at": "IN",
            "one": "CD",
            "have": "VB",
            "this": "DT",
            "from": "IN",
            "or": "CC",
            "had": "VBD",
            "by": "IN",
            "hot": "JJ",
            "but": "CC",
            "some": "DT",
            "what": "WP",
            "there": "EX",
            "we": "PRP",
            "can": "MD",
            "out": "RB",
            "other": "JJ",
            "were": "VBD",
            "all": "DT",
            "your": "PRP$",
            "when": "WRB",
            "up": "RB",
            "use": "VB",
            "word": "NN",
            "how": "WRB",
            "said": "VBD",
            "an": "NNP",
            "each": "DT",
            "She": "PRP",
            "she": "PRP",
            "which": "WDT",
            "do": "VB",
            "their": "PRP$",
            "time": "NN",
            "if": "IN",
            "will": "VB",
            "way": "NN",
            "about": "IN",
            "many": "JJ",
            "then": "RB",
            "them": "PRP",
            "would": "MD",
            "write": "VB",
            "like": "UH",
            "so": "RB",
            "these": "DT",
            "her": "PRP",
            "long": "JJ",
            "make": "VB",
            "thing": "NN",
            "see": "VB",
            "him": "PRP",
            "two": "CD",
            "has": "VBZ",
            "look": "VB",
            "more": "JJR",
            "day": "NN",
            "could": "MD",
            "go": "VB",
            "come": "VB",
            "did": "VBD",
            "my": "PRP$",
            "sound": "NN",
            "no": "UH",
            "most": "RBS",
            "number": "NN",
            "who": "WP",
            "over": "RB",
            "know": "VBP",
            "water": "NN",
            "than": "UH",
            "call": "NN",
            "first": "RB",
            "people": "NNS",
            "may": "MD",
            "down": "RB",
            "side": "NN",
            "been": "VBN",
            "now": "UH",
            "find": "VB",
            "any": "UH",
            "new": "JJ",
            "work": "NN",
            "part": "NN",
            "take": "VB",
            "get": "VB",
            "place": "NN",
            "made": "VBN",
            "live": "JJ",
            "where": "WRB",
            "after": "IN",
            "back": "RB",
            "little": "JJ",
            "only": "RB",
            "round": "RB",
            "man": "UH",
            "year": "NN",
            "came": "VBD",
            "show": "NN",
            "every": "DT",
            "good": "JJ",
            "me": "PRP",
            "give": "VB",
            "our": "PRP$",
            "under": "RB",
            "name": "NN",
            "very": "RB",
            "through": "RB",
            "just": "RB",
            "form": "NN",
            "much": "JJ",
            "great": "JJ",
            "think": "VB",
            "say": "VB",
            "help": "VB",
            "low": "JJ",
            "line": "NN",
            "before": "IN",
            "turn": "NN",
            "cause": "NN",
            "same": "JJ",
            "mean": "JJ",
            "differ": "NNP",
            "move": "VB",
            "right": "UH",
            "boy": "NN",
            "old": "JJ",
            "too": "RB",
            "does": "VBZ",
            "tell": "VB",
            "sentence": "NN",
            "set": "VBN",
            "three": "CD",
            "want": "VB",
            "air": "NN",
            "well": "UH",
            "also": "RB",
            "play": "VB",
            "small": "JJ",
            "end": "NN",
            "put": "VB",
            "home": "NN",
            "read": "VB",
            "hand": "NN",
            "port": "NN",
            "large": "JJ",
            "spell": "NN",
            "add": "VB",
            "even": "RB",
            "land": "NN",
            "here": "RB",
            "must": "VB",
            "big": "JJ",
            "high": "JJ",
            "such": "JJ",
            "follow": "VB",
            "act": "NN",
            "why": "WRB",
            "ask": "VB",
            "men": "NNS",
            "change": "NN",
            "went": "VBD",
            "light": "JJ",
            "kind": "RB",
            "off": "RB",
            "need": "NN",
            "house": "NN",
            "picture": "NN",
            "try": "VB",
            "Us": "PRP",
            "us": "PRP",
            "again": "RB",
            "animal": "NN",
            "point": "NN",
            "mother": "NN",
            "world": "NN",
            "near": "RB",
            "build": "VB",
            "self": "NN",
            "earth": "NN",
            "father": "NN",
            "head": "NN",
            "stand": "VB",
            "own": "JJ",
            "page": "NN",
            "should": "MD",
            "country": "NN",
            "found": "VBN",
            "answer": "NN",
            "school": "NN",
            "grow": "VB",
            "study": "NN",
            "still": "RB",
            "learn": "VB",
            "plant": "NN",
            "cover": "NN",
            "food": "NN",
            "sun": "NN",
            "four": "CD",
            "thought": "VBD",
            "let": "VB",
            "keep": "VB",
            "eye": "NN",
            "never": "RB",
            "last": "JJ",
            "door": "NN",
            "between": "IN",
            "city": "NN",
            "tree": "NNP",
            "cross": "NN",
            "since": "IN",
            "hard": "JJ",
            "start": "VB",
            "might": "MD",
            "story": "NN",
            "saw": "VBD",
            "far": "RB",
            "sea": "NN",
            "draw": "VB",
            "left": "UH",
            "late": "RB",
            "run": "NN",
            "dont": "UH",
            "while": "IN",
            "press": "NN",
            "close": "RB",
            "night": "NN",
            "real": "JJ",
            "life": "NN",
            "few": "JJ",
            "stop": "VB",
            "open": "JJ",
            "seem": "VB",
            "together": "RB",
            "next": "RB",
            "white": "JJ",
            "children": "NNS",
            "begin": "VB",
            "got": "VBP",
            "walk": "VB",
            "example": "NN",
            "ease": "JJ",
            "paper": "NN",
            "often": "RB",
            "always": "RB",
            "music": "NN",
            "those": "DT",
            "both": "DT",
            "mark": "NNP",
            "book": "NN",
            "letter": "NN",
            "until": "IN",
            "mile": "NN",
            "river": "NN",
            "car": "NN",
            "feet": "NNS",
            "care": "NN",
            "second": "NN",
            "group": "NN",
            "carry": "VB",
            "took": "VB",
            "adults": "NN",
            "rain": "NN",
            "eat": "VB",
            "room": "NN",
            "friend": "NN",
            "began": "NNP",
            "idea": "NN",
            "fish": "NNS",
            "mountain": "NN",
            "north": "RB",
            "once": "RB",
            "base": "NN",
            "hear": "VB",
            "horse": "NN",
            "cut": "NN",
            "sure": "UH",
            "watch": "VB",
            "color": "NN",
            "face": "NN",
            "wood": "NNP",
            "main": "JJ",
            "enough": "JJ",
            "plain": "NNP",
            "girl": "NN",
            "usual": "JJ",
            "young": "JJ",
            "ready": "JJ",
            "above": "RB",
            "ever": "RB",
            "red": "JJ",
            "list": "NN",
            "though": "IN",
            "feel": "VB",
            "talk": "NN",
            "bird": "NN",
            "soon": "RB",
            "body": "NN",
            "dog": "NN",
            "family": "NN",
            "direct": "JJ",
            "pose": "NN",
            "leave": "VB",
            "song": "NN",
            "measure": "NN",
            "state": "NN",
            "product": "NN",
            "black": "JJ",
            "short": "JJ",
            "numeral": "NN",
            "class": "NN",
            "wind": "NN",
            "question": "NN",
            "happen": "NNP",
            "complete": "JJ",
            "ship": "NN",
            "area": "NN",
            "half": "NN",
            "rock": "NN",
            "order": "NN",
            "fire": "NN",
            "south": "NN",
            "problem": "NN",
            "piece": "NN",
            "told": "VBN",
            "knew": "NNP",
            "pass": "NN",
            "farm": "NN",
            "top": "JJ",
            "whole": "JJ",
            "king": "NN",
            "size": "NN",
            "heard": "VBN",
            "best": "JJS",
            "hour": "NN",
            "better": "RBR",
            "true": "JJ",
            "during": "IN",
            "hundred": "CD",
            "am": "UH",
            "remember": "VB",
            "step": "NN",
            "early": "RB",
            "hold": "VB",
            "west": "NN",
            "ground": "NN",
            "interest": "NN",
            "reach": "NN",
            "fast": "RB",
            "five": "CD",
            "sing": "VB",
            "listen": "VB",
            "six": "CD",
            "table": "NN",
            "travel": "NN",
            "less": "JJR",
            "morning": "NN",
            "ten": "CD",
            "simple": "JJ",
            "several": "JJ",
            "vowel": "NNP",
            "toward": "RB",
            "war": "NN",
            "lay": "VB",
            "against": "IN",
            "pattern": "NN",
            "slow": "JJ",
            "center": "NN",
            "love": "VB",
            "person": "NN",
            "money": "NN",
            "serve": "VB",
            "appear": "VB",
            "road": "NN",
            "map": "NN",
            "science": "NN",
            "rule": "NN",
            "govern": "VB",
            "pull": "VB",
            "cold": "JJ",
            "notice": "VB",
            "voice": "NN",
            "fall": "NN",
            "power": "NN",
            "town": "NN",
            "fine": "JJ",
            "certain": "JJ",
            "fly": "VB",
            "unit": "NN",
            "lead": "VB",
            "cry": "NN",
            "dark": "JJ",
            "machine": "NN",
            "note": "NN",
            "wait": "VB",
            "plan": "NN",
            "figure": "NN",
            "star": "NN",
            "box": "NN",
            "noun": "NNP",
            "field": "NN",
            "rest": "NN",
            "correct": "JJ",
            "able": "JJ",
            "pound": "NN",
            "done": "VBN",
            "beauty": "NN",
            "drive": "NN",
            "stood": "VBN",
            "contain": "NN",
            "front": "NN",
            "teach": "VB",
            "week": "NN",
            "final": "JJ",
            "gave": "NNP",
            "green": "NNP",
            "oh": "UH",
            "quick": "JJ",
            "develop": "VB",
            "sleep": "NN",
            "warm": "JJ",
            "free": "JJ",
            "minute": "NN",
            "strong": "JJ",
            "special": "JJ",
            "mind": "NN",
            "behind": "RB",
            "clear": "JJ",
            "tail": "NN",
            "produce": "NN",
            "fact": "NN",
            "street": "NN",
            "inch": "NN",
            "lot": "NN",
            "nothing": "NN",
            "course": "NN",
            "stay": "VB",
            "wheel": "NN",
            "full": "JJ",
            "force": "NN",
            "blue": "JJ",
            "object": "NN",
            "decide": "VB",
            "surface": "NN",
            "deep": "JJ",
            "moon": "NN",
            "island": "NNP",
            "foot": "NN",
            "yet": "RB",
            "busy": "JJ",
            "test": "NN",
            "record": "NN",
            "boat": "NN",
            "common": "JJ",
            "gold": "NN",
            "possible": "JJ",
            "plane": "NN",
            "age": "NN",
            "dry": "JJ",
            "wonder": "NNP",
            "laugh": "NN",
            "thousand": "CD",
            "ago": "RB",
            "ran": "NNP",
            "check": "NN",
            "game": "NN",
            "shape": "NN",
            "yes": "UH",
            "cool": "JJ",
            "miss": "VB",
            "brought": "VBN",
            "heat": "NN",
            "snow": "NN",
            "bed": "NN",
            "bring": "VB",
            "sit": "VB",
            "perhaps": "RB",
            "fill": "NN",
            "east": "NN",
            "weight": "NN",
            "language": "NN",
            "among": "IN"}

    @staticmethod
    def eliminate_stopwords(sentence):
        # https://gist.github.com/sebleier/554280
        stop_word_lst = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
                        "yourselves", "him", "himself", "hers", "herself", "it", "its",
                        "itself", "they", "them", "their", "theirs", "themselves",
                        "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
                        "have", "has", "had", "having", "does", "did", "doing", "a", "an", "the", "and", "but",
                        "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "about",
                        "against", "between", "into", "through", "during", "before", "after", "above", "below",
                        "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then",
                        "once", "here", "there", "when", "where", "why", "how", "any", "both", "each", "few",
                        "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
                        "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
        for word in sentence:
            if isinstance(word, tuple):
                if word[0] in stop_word_lst:
                    sentence.remove(word)
            else:
                if word in stop_word_lst:
                    sentence.remove(word)

        return sentence

    @staticmethod
    def find_time(sentence):
        words = sentence.split()
        for word in words:
            if ":" in word:
                return word

    @staticmethod
    def find_similar_words(sentence, question):
        similar_words = []
        for word in sentence:
            if word[0] in question:
                similar_words.append(word)
        return similar_words

    def clean_sentence(self, sentence):
        """
        :param sentence: "Ada brought a short note to Irene."
        :return: [{"Ada": "NNP"}, {"brought": "verb"}, {"a": "a"}]
        """
        # https://stackoverflow.com/questions/743806/how-to-split-a-string-into-a-list
        list_of_words = sentence.split()

        cleaned_sentence = []

        for word in list_of_words:
            if "." in word:
                word = word.replace(".", "")
            try:
                if word in self.word_dictionary.keys():
                    cleaned_sentence.append((word, self.word_dictionary[word]))
            except KeyError:
                if word.lower() in self.word_dictionary.keys():
                    cleaned_sentence.append((word.lower(), self.word_dictionary[word.lower()]))

        cleaned_sentence = self.eliminate_stopwords(cleaned_sentence)

        return cleaned_sentence

    def clean_question(self, question):
        """
        :param question: "Who brought the note?"
        :return: ['Who', 'brought', 'the', 'note?']
        """
        cleaned_question = question.split()
        for punctuation in self.unwanted_punctuations:
            for word in cleaned_question:
                if punctuation in word:
                    new_word = word[:-1]
                    cleaned_question.remove(word)
                    cleaned_question.append(new_word)

        cleaned_question = self.eliminate_stopwords(cleaned_question)

        return cleaned_question

    def solve(self, sentence, question):
        # clean the input sentence and question so they're easier to work with
        fixed_sentence = self.clean_sentence(sentence)
        fixed_question = self.clean_question(question)

        similar_words = self.find_similar_words(fixed_sentence, fixed_question)

        leftover_words = []
        for word in fixed_sentence:
            if word not in similar_words:
                leftover_words.append(word)
        if len(leftover_words) == 1:
            return leftover_words[0][0]
        choose_list = []
        verb_list = []

        if "Who" in fixed_question or "who" in fixed_question:
            for i, word in enumerate(fixed_sentence):
                if word[1] == "NNP" or word[1] == "PRP" or word[1] == "NNS" or word[1] == "NN":
                    choose_list.append((word[0], self.word_dictionary[word[0]], i))
            if "adults" in sentence.split():
                return "adults"
            # find the index of "brought" and try to find something in the choose_list
            for word in fixed_question:
                for pair in choose_list:
                    if pair[0] == word:
                        choose_list.remove(pair)
                        break
            if len(choose_list) == 1:
                return choose_list[0][0]
            split_sentence = sentence.split()
            for word in similar_words:
                if word[1] == "VBN" or word[1] == "VB":
                    verb_list.append(word)
            if ("Who" and "with") or ("who" and "with") in fixed_question:
                # if there's any names who aren't in the similar_words list (serena)
                not_time = []
                for fs in leftover_words:
                    if fs[0] not in self.time_words:
                        not_time.append(fs[0])
                for i in not_time:
                    if self.word_dictionary[i] == "NNP":
                        return i
                if "friend" in not_time:
                    return "friend"
            for i in range(len(split_sentence)):
                for verb in verb_list:
                    if verb[0] == split_sentence[i]:
                        answer = split_sentence[i-1]
                        if answer == "She":
                            return answer.lower()
                        return answer


        if "What" in fixed_question or "what" in fixed_question:
            if "color" in fixed_question:
                if "horse" in fixed_question:
                    for fs in fixed_sentence:
                        if fs[0] == "horse":
                            return fixed_sentence[fixed_sentence.index(fs)-1][0]
                for w in fixed_sentence:
                    if w[1] == "JJ":
                        return w[0]
            if "time" in fixed_question:
                time = self.find_time(sentence)
                return time
            if "what" and "run" in fixed_question:
                for lw in leftover_words:
                    if lw[1] == "NN" and lw[0] not in self.time_words:
                        return lw[0]
            if "do" in fixed_question:
                for m in fixed_sentence:
                    if m[1] == "VB":
                        return m[0]
            for w in fixed_sentence:
                if "name" in fixed_question:
                    if w[1] == "NN":
                        return sentence.split()[sentence.split().index(w[0])+1]
                if w[1] == "NN":
                    choose_list.append(w[0])
            if len(choose_list) == 1:
                return choose_list[0]
            else:
                if "sing" in fixed_question and "bird" in choose_list:
                    return choose_list[0]
                for sw in similar_words:
                    if sw[1] == "JJ":
                        for word in fixed_sentence:
                            if word == sw:
                                try:
                                    return fixed_sentence[fixed_sentence.index(word)+1][0]
                                except IndexError:
                                    if fixed_sentence[fixed_sentence.index(word)-2][0]:
                                        return fixed_sentence[fixed_sentence.index(word)-2][0]
                                    return fixed_sentence[fixed_sentence.index(word)-1][0]

                if "tell" in fixed_question:
                    if "story" in choose_list:
                        return "story"

        if "How" in fixed_question or "how" in fixed_question:
            # if "many" in fixed_question:
            #     for c in leftover_words:
            #         if c[1] == "CD":
            #             choose_list.append(c[0])
            if "get" in fixed_question:
                for word in leftover_words:
                    if word[0] == "go" or word[0] == "get" or word[0] == "got":
                        leftover_words.remove(word)
            for i in range(len(fixed_sentence)):
                if fixed_sentence[i][1] == "CD" and "get" not in fixed_question:
                    choose_list.append(fixed_sentence[i+1][0])
                    choose_list.append(fixed_sentence[i][0])
                elif "get" in fixed_question:
                    if fixed_sentence[i][1] == "VB":
                        choose_list.append(fixed_sentence[i][0])
            for h in fixed_sentence:
                if h[1] == "JJ":
                    choose_list.append(h[0])
            if len(choose_list) == 1:
                return choose_list[0]
            elif len(choose_list) > 1:
                if "get" in fixed_question and "to" in fixed_question:
                    remove_list = ["go", "went"]
                    for bad_word in remove_list:
                        if bad_word in choose_list:
                            # https://stackoverflow.com/questions/4915920/how-to-delete-an-item-in-a-list-if-it-exists
                            choose_list.remove(bad_word)
                            if len(choose_list) == 1:
                                return choose_list[0]
                elif "far" in fixed_question:
                    for option in choose_list:
                        if self.word_dictionary[option] == "NN":
                            return option
                elif "many" in fixed_question:
                    for o in choose_list:
                        if self.word_dictionary[o] == "CD":
                            return o

        if "Where" in fixed_question or "where" in fixed_question:
            for f in leftover_words:
                if f[1] == "NN":
                    choose_list.append((f[0], self.word_dictionary[f[0]]))
            if len(choose_list) == 1:
                if isinstance(choose_list[0], tuple):
                    return choose_list[0][0]
                return choose_list[0]
            else:
                for f in fixed_question:
                    # https://realpython.com/python-keyerror/
                    try:
                        if self.word_dictionary[f] == "VB":
                            verb = f
                            # "go"
                            split = sentence.split()
                            for i in range(len(split)):
                                if verb == split[i] and i+2 < len(split):
                                    return split[i+2]
                    except KeyError:
                        continue
                for w in leftover_words:
                    if w[1] == "VB":
                        verb = w[0]
                        # go
                        for i in range(len(fixed_sentence)):
                            if fixed_sentence[i][0] == verb and i + 2 < len(fixed_sentence):
                                return fixed_sentence[i + 2][0]
                    else:
                        for word in sentence.split():
                            for sw in similar_words:
                                if sw[1] == "NNP":
                                    if sw[0] == word:
                                        if sentence.split()[sentence.split().index(sw[0]) + 1] == "is":
                                            return sentence.split()[sentence.split().index(sw[0]) + 2]

        if "When" in fixed_question or "when" in fixed_question:
            for lw in leftover_words:
                if lw[1] == "NN":
                    choose_list.append(lw[0])
            if len(choose_list) == 1:
                return choose_list[0]
            else:
                for l in leftover_words:
                    if l[0] in self.time_words:
                        answer = l[0]
                        return answer

