# something.py

__all__ = ['_private_variable', 'PublicClass']

# The rest is the same as before

public_variable = 42
_private_variable = 141

def public_function():
    print("I'm a public function! yay!")

def _private_function():
    print("Ain't nobody accessing me from another module...usually")

class PublicClass(object):
    pass

class _WeirdClass(object):
    pass
