'''
assignment module
Author: Alex Rathbun
'''
def math(num1, num2=3.141592653, verbose=True):
    """Perform a mathematical operation."""
    if verbose:
        print(f"The sum of {num1} and {num2} is {num1 + num2}")
        num_list = [num1, num2]
        num_list.sort()
        print(num_list)

def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that's going to be made."""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')


def favorite_book(title):
  """Print a favorite book title."""
  print(f"One of my favorit books is {title}.")


if __name__ == '__main__':
    math(5, 3.14)
    math(7, 9, False)
    math(7, 9)
    make_shirt('medium', 'Hello World')
    favorite_book('The Catcher in the Rye')
