
with open("/usr/share/dict/words") as f:
    five_letter_words = [line.strip().lower() for line
                         in f if len(line.strip()) == 5]

