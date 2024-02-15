# importing textwrap from the library
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width) # the .fill() function is used to wrap the text according to the user input

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
