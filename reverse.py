# Make a function that reverses a string.
#Used slicing instead of the for loop.


def reverse(str):
    return str[::-1]

string_reverse = reverse("Grant")

print(string_reverse)

def test_string_reverse():
    assert reverse("Grant") == "tnarG"
