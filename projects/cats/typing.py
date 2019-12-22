"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    result = []

    for p in paragraphs:
        if select(p):
            result.append(p)

    if len(result) >= k + 1:
        return result[k]
    else:
        return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"

    def select(para):
        splited = split(remove_punctuation(lower(para)))
        for s in splited:
            for t in topic:
                if s == t:
                    return True
        return False

    return select
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    acc_num = 0

    if len(typed_words) == 0:
        return 0.0

    for word_num in range(0, min(len(reference_words), len(typed_words))):
        if typed_words[word_num] == reference_words[word_num]:
            acc_num += 1

    return acc_num / len(typed_words) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 * (60 / elapsed)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word

    tmp_word = user_word
    tmp_diff = limit

    for w in valid_words:
        curr_diff = diff_function(user_word, w, limit)
        # decrease the lowest diff (tmp_diff) if necessary
        # and deal with the situation when only one 'diff' reaches limit while others all above
        if curr_diff < tmp_diff or curr_diff == tmp_diff == limit:
            tmp_word = w
            tmp_diff = curr_diff

    return tmp_word

    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    >>> swap_diff("car", "cad")
    1
    >>> swap_diff("this", "that")
    2
    >>> swap_diff("one", "two")
    3
    >>> swap_diff("from", "form")
    2
    >>> swap_diff("awe", "awesome")
    4
    >>> swap_diff("someawe", "awesome")
    6
    >>> swap_diff("awful", "awesome")
    5
    """
    # BEGIN PROBLEM 6
    if limit < 0:
        return float('inf')
    elif len(start) == 0 or len(goal) == 0:
        return abs(len(goal) - len(start))
    elif start[0] != goal[0]:
        return 1 + swap_diff(start[1:], goal[1:], limit - 1)
    else:
        return swap_diff(start[1:], goal[1:], limit)
    # END PROBLEM 6


def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    >>> edit_diff("ash", "hash")
    1
    >>> edit_diff("roses", "arose")     # roses -> aroses -> arose
    2
    >>> edit_diff("tesng", "testing")   # tesng -> testng -> testing
    2
    >>> edit_diff("rlogcul", "logical") # rlogcul -> logcul -> logicul -> logical
    3
    """
    if limit < 0:
        return float('inf')

    elif len(start) == 0 or len(goal) == 0:
        return abs(len(goal) - len(start))

    elif start[0] == goal[0]:
        return edit_diff(start[1:], goal[1:], limit)

    else:
        add_diff = 1 + edit_diff(start, goal[1:], limit - 1)
        remove_diff = 1 + edit_diff(start[1:], goal, limit - 1)
        substitute_diff = 1 + edit_diff(start[1:], goal[1:], limit - 1)
        return min(add_diff, remove_diff, substitute_diff)


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    num = 0
    for num in range(len(typed)):
        if typed[num] != prompt[num]:
            break

    if num == len(typed) - 1 and typed[num] == prompt[num]:
        num += 1

    send({'id': id, 'progress': num / len(prompt)})
    return num / len(prompt)
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    fastest_times = []
    output = []

    # add the fastest time to fastest time list
    for wt_num in range(n_words):
        fastest_time = min(elapsed_time(wt[wt_num + 1]) - elapsed_time(wt[wt_num]) for wt in word_times)
        fastest_times.append(fastest_time)

    # for each player compare their time to the fastest time (and margin)
    for wt in word_times:
        fast_word = []
        for time_num in range(n_words):
            elaps_time = elapsed_time(wt[time_num + 1]) - elapsed_time(wt[time_num])
            if elaps_time == fastest_times[time_num] or abs(elaps_time - fastest_times[time_num]) <= margin:
                fast_word.append(word(wt[time_num + 1]))
        output.append(fast_word)

    return output

    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
