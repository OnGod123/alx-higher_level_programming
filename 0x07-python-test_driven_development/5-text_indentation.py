def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    - text (str): The input text.

    Returns:
    - None

    Raises:
    - TypeError: If text is not a string.

    Examples:
    >>> text_indentation("This is a sample text. It has multiple sentences? Each separated by a period.")
    This is a sample text
    It has multiple sentences
    Each separated by a period

    >>> text_indentation("Another example: What is your name?")
    Another example
    What is your name

    >>> text_indentation(123)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into words
    words = text.split()

    # Initialize variables to store the modified text
    modified_text = ""
    line = ""

    # Iterate through each word
    for word in words:
        # Check if the word ends with ., ?, or :
        if word.endswith(('.', '?', ':')):
            modified_text += line.strip() + '\n\n'
            line = word.rstrip('.?:') + ' '
        else:
            line += word + ' '

    # Print the modified text with 2 new lines after each sentence-ending word
    print(modified_text + line.strip())

# Uncomment the line below if you want to run doctests
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

