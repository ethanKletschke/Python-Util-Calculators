from os import _exit as close_prog, system as sys, name as sysname
import re  # Used to test if the GB or MB values contain digits.


# The main class used in the program.
class GBdivMB:
    """The class that contains most of the program's logic."""

    def __init__(self, gigabytes: int, megabytes: int) -> None:
        """Instantiates a `GBdivMB` object.

        Args:
            gigabytes (int): The gigabytes to divide from.
            megabytes (int): The megabytes to divide by.
        """
        self.__gb = gigabytes
        self.__mb = megabytes

    def __str__(self) -> str:
        """Creates a string representation of the `GBdivMB` object,
        which also contains the calculation the program is based off, and
        serves as the main output for the program.

        Returns:
            str: The string representation of this object.
        """

        # Build the string to return.
        to_return = f"GB: {self.__gb:,} ({self.__convertToMB():,} MB)\n"
        to_return += f"MB: {self.__mb:,}\n\n"
        to_return += f"{self.__gb:,} GB ÷ {self.__mb:,} MB = {self.__calculate()}"

        return to_return

    def __convertToMB(self) -> int:
        """Converts the class's `__gb` (gigabytes) private attribute to megabytes
        (MB).

        Returns:
            int: The private `__gb` attribute converted to megabytes.
        """
        return self.__gb * 1024

    def __calculate(self) -> int:
        """Calculates the GB ÷ MB calculation.

        Returns:
            int: The quotient of the `__gb` and `__mb` private fields.
        """
        # Temporarily store the GB of the class to make the actual
        # calculation more readable.
        gb_as_mb = self.__convertToMB()

        # Store the result of the calculation as an integer.
        res = int(gb_as_mb / self.__mb)

        return res


# Clear the terminal screen before the program starts.
sys("cls" if sysname == "nt" else "clear")

# Print the program title.
print('Calculating: "GB ÷ MB"\n\n')

try:
    # Take user input.
    _gb = input("Enter the gigabytes (GB): ")  # GB value to test for invalid input.
    _mb = input("Enter the megabytes (MB): ")  # MB value to test for invalid input.

    gb = 0  # Will store the value of _gb as an int after tests.
    mb = 0  # Will store the value of _mb as an int after tests.

    # test if the GB value contains non-digit characters.
    if re.search(r"\D", _gb):
        raise ValueError("GB cannot contain non-digit characters.")
    else:
        gb = int(_gb)  # Store the GB as an int.

    # Test if the MB value contains non-digit characters.
    if re.search(r"\D", _mb):
        raise ValueError("MB cannot contain non-digit characters.")
    else:
        mb = int(_mb)  # Store the MB as an int.

    # If the GB value is greater than or equal to 1 exabyte (1024 petabytes)
    if gb >= 1073741824:
        # Raise a Value Error.
        raise ValueError("GB value too high.")

    # If the MB value is invalid (less than or equal to 0)
    if mb <= 0:
        # Raise a value error.
        raise ValueError("MB value too low.")

    # Initialise the "GBdivMB" object with the user's input.
    gdm = GBdivMB(gb, mb)

    # Display the output throught the object's
    # string representation (the "__str__()" method).
    print(gdm)
except ValueError as ve:
    # Print the exception and exit the program with status -1.
    print(ve)
    close_prog(-1)
except NameError as ne:
    # Print the exception and exit the program with status -1.
    print(ne)
    close_prog(-1)
except TypeError as te:
    # Print the exception and exit the program with status -1.
    print(te)
    close_prog(-1)
except KeyboardInterrupt:
    print("\n\nExiting...")
    # Close the program with status 0.
    close_prog(0)
except Exception as ex:
    # Print the exception and exit the program with status -1.
    print(ex)
    close_prog(-1)
else:
    # Prompt the user to press enter in order to exit the program.
    input("Press enter to exit.")
    # Clear the terminal screen.
    sys("cls" if sysname == "nt" else "clear")
    # Exit the program with status 0.
    close_prog(0)
