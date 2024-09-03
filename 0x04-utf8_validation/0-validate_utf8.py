#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    method that represents a valid UTF-8 encoding
    """

    # initilize the number of bytes
    n_bytes = 0

    # masks to check significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # loop through each integer in the data list
    for num in data:
        # get only the 8 least significant bits
        byte = num & 0xFF

        # deteremine how many bytes in UTF-8 character
        if n_bytes == 0:
            if (byte >> 5) == 0b110:  # 2 bytes
                n_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3 bytes
                n_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4 bytes
                n_bytes = 3
            elif (byte >> 7):  # 1 byte must start with 0
                return false
        else:
            # check for valid continuation byte
            if not (byte & mask1 and not (byte & mask2)):
                return false

            # decrease the remaining bytes
            n_bytes -= 1

            # no remaining bytes expected, data is valid UTF-8
    return n_bytes == 0
