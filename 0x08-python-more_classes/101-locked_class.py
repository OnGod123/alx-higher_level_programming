class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError(f"{type(self).__name__} object has no attribute '{name}'")
        object.__setattr__(self, name, value)

# Example usage:
locked_obj = LockedClass()

# This will raise an AttributeError because 'last_name' is not allowed
try:
    locked_obj.last_name = "Doe"
except AttributeError as e:
    print(e)

# This is allowed since it's the first_name attribute
locked_obj.first_name = "John"

# This will raise an AttributeError because 'age' is not allowed
try:
    locked_obj.age = 30
except AttributeError as e:
    print(e)

