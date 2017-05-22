store = []


def sort_by_last_letter(string):
    """
    Task: Define a function that takes a list of strings as input
          parameter. Defines a local function that returns the last
          letter of the string. Your main function returns a sorted
          list based on the last letter.
    :param string: A list of strings
    :return: sorted list based on last letter
    """

    # A local function
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)

    # Hint: use the local function as a lambda to the sorted built-in
    #       function
    return sorted(string, key=last_letter)


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def html_tag(tag):
    """
    Create a html tag based on input
    :param tag: Tag
    :return: a callable function
    """
    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))
    return wrap_text


def main():
    names = ["Hugo", "Maria", "Peter", "El Chapo", "Mario"]
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print(sort_by_last_letter(names))
    print("--------------------------")


if __name__ == '__main__':
    main()
    exit(0)
