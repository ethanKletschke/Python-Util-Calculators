import os


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

# Print the program title
print("Calculating \n\"GB ÷ MB\"\n\n")

try:
    gb = int(input("Enter the gigabytes (GB): "))
    mb = int(input("Enter the megabytes (MB): "))

    gdm = GBdivMB(gb, mb)
    
    # Display the output throught the object's
    # string representation ( the "__str__()" method).
    print(gdm)
except ValueError as ve:
    print(ve)    
    os._exit(-1)
except NameError as ne:
    print(ne)
    os._exit(-1)
except TypeError as te:
    print(te)
    os._exit(-1)
except KeyboardInterrupt as ki:
    print("\n\nExiting...")
    os._exit(0)
except Exception as ex:
    print(ex)
    os._exit(-1)
