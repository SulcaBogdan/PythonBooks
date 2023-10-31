from typing import List

text= """The first thing that stands between you and writing your first, real,
piece of code, is learning the skill of breaking problems down into
achievable little actions that a computer can do for you. Of course,
you and the computer will also need to be speaking a common language,
but we'll get to that topic in just a bit.
Now breaking problems down into a number of steps may sound a new
skill, but its actually something you do every day. Let’s look at an
example, a simple one: say you wanted to break the activity of fishing
down into a simple set of instructions that you could hand to a robot,
who would do your fishing for you. Here’s our first attempt to do that,
check it out:
.
.
.
You’re going to find these simple statements or instructions are the
first key to coding, in fact every App or software program you’ve ever
used has been nothing more than a (sometimes large) set of simple
instructions to the computer that tell it what to do."""


def count_sentences(text):
    count = 0
    terminals = "!?.;"
    if terminals in text:
        count += 1
    return count

def count_words(text):
    count = 0
    words = text.split()
    for i in words:
        count += 1
    return count

def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count += word_count
    return count
def count_syllables_in_word(word):
    count = 0
    if len(word) <= 3:
        return 1

    vowels = "aeiouAEIOU"
    prev_char_was_vowels = False
    for char in word:
        if char in vowels:
            if not prev_char_was_vowels:
                count+=1
            prev_char_was_vowels = True
        else:
            prev_char_was_vowels = False
    return count


def compute_readability(text):
    total_words = count_words(text)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(text.split())
    score = 0
    print(total_words)
    print(total_sentences)
    print(total_syllables)


print(compute_readability(text))











