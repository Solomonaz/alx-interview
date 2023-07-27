#!/usr/bin/python3
""" UTF-8 Validation """



def validUTF8(data):
    def get_num_bytes(char):
        # Count the number of leading ones in the binary representation to determine the byte length
        num_bytes = 0
        mask = 1 << 7  # 10000000
        while char & mask:
            num_bytes += 1
            mask >>= 1
        return num_bytes

    # Loop through the data list
    i = 0
    while i < len(data):
        num_bytes = get_num_bytes(data[i])

        # Check if the byte length is within the valid range (1 to 4 bytes)
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check the subsequent bytes for validity
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or (data[i] >> 6) != 0b10:  # The next bytes should start with '10'
                return False

        i += 1  # Move to the next character

    return True
