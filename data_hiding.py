# Example to understand Data Hiding in Python

# Creating a class named 'simple'
class simple:

  def __init__(self):
    # Public variables (can be accessed from outside the class)
    self.value_1 = 1
    self.value_2 = 2

    # Private variable (name starts with double underscore '__')
    # Cannot be accessed directly from outside the class
    self.__value_3 = 3

  # Public method (normal method, name does not start with double underscore)
  def _A1_(self):
    print('apple')

  # Public method (even though name starts with a single underscore,
  # it’s just a hint for internal use only, but still accessible)
  def _B2_(self):
    print('ball')

  # Private method (name starts with double underscore '__')
  # Cannot be accessed directly from outside the class
  def __c3_(self):
    print('carrot')


# Creating an object of class simple
s = simple()

# -------------------------------------------
# Important Points to Remember:

# Public variables (value_1 and value_2) can be accessed like this:
print(s.value_1)  # Output: 1
print(s.value_2)  # Output: 2

# Private variable (__value_3) cannot be accessed directly
# If you try: print(s.__value_3) --> It will give an error
# But it can still be accessed like this (not recommended):
print(s._simple__value_3)  # Output: 3
# This is called **Name Mangling** (Python internally renames the variable)

# Public methods can be called easily:
s._A1_()  # Output: apple
s._B2_()  # Output: ball

# Private method (__c3_) cannot be called directly:
# s.__c3_() --> Error!
# But it can be accessed using Name Mangling:
s._simple__c3_()  # Output: carrot

# -------------------------------------------

# Summary:
# - Single underscore (_) before a variable/method: "protected" (only a hint, still public)
# - Double underscore (__) before a variable/method: "private" (name mangled, not easily accessible)
# - Data Hiding means: preventing direct access to private variables/methods from outside the class.
# - Python does not have *true* private variables (like Java or C++), but uses conventions and Name Mangling.
