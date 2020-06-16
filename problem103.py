# Problem #103
#
# Given a string and a set of characters, return the shortest substring containing all the characters in the set.
#
# For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".
#
# If there is no substring containing all the characters in the set, return null.


def substring(message: str, char_set: set) -> str:
    if message is not None and not char_set:
        return ""

    shortest = message
    found = False

    # starting on each char of the message
    for i in range(len(message)):
        working_set = char_set.copy()
        working_string = message
        working_start = None
        # look for the char in the rest of the message
        for j in range(i, len(message)):
            # if found one of the chars
            if message[j] in working_set:
                # and it is the first char found
                if working_start is None:
                    # save the starting index
                    working_start = j
                # remove it from the set
                working_set.remove(message[j])
            # if all char on the set were found
            if not working_set:
                found = True
                # get the substring
                working_string = message[working_start:j+1]
                break

        # get the shortest substring
        shortest = min(shortest, working_string, key=len)

    # if all chars were never found in any substring, return none
    if not found:
        return None

    return shortest


assert (substring("", {})) == ""
assert (substring("a", {})) == ""
assert (substring("", {"a"})) is None
assert (substring("a", {"a"})) == "a"
assert (substring("figehaeci", {"a", "e", "i"})) == "aeci"
assert (substring("figehaeci", {"f", "e", "c"})) == "figehaec"
assert (substring("figehaeci", {"a", "e", "f"})) == "figeha"
assert (substring("figehaeci", {"a"})) == "a"
assert (substring("fgehaec", {"a", "e", "i"})) is None
assert (substring("figehaeci", {"a", "e", "q"})) is None
