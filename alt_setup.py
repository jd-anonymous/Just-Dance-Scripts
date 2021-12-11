from ctypes import WINFUNCTYPE
import json, struct, time
from unidecode import unidecode

def log_message(message: str):
    """
    Function for logging message
    to console

    :param message: Message
    :return: None
    """

    print(
        "[LOG]",
        int(time.time()),
        message
    )

def raw_text_encode(string: str):
    """
    Function for encoding raw text
    to Just Dance serialization format

    :param string: Text
    :return: Encoded text in Just Dance serialization format
    """

    # Decoding our text from unicode
    decoded_unicode_text: str = unidecode(string)

    # Encoding our string to bytes
    bytes_: bytes = decoded_unicode_text.encode()

    # __len__ function can fucked up our encoded raw text
    # if we will use not encoded string in it
    return struct.pack(">I", len(bytes_)) + bytes_

def alt_map_encode(information: dict):
    """
    Function for encoding alternate information
    to Just Dance serialization format

    :param alt: Alternate information
    :return: Encoded alternate information in Just Dance serialization format
    """
    
    # Encoding our MapName to Just Dance 
    # serialization format
    encoded_map_name: bytes = raw_text_encode(information["MapName"])

    # Packing our LocaleID to 4 bytes
    packed_localeid: bytes = struct.pack(">I", information["LocaleId"])

    return (
        encoded_map_name +
        b'\x00\x00\x00\x04\xFF\xFF\xFF\xFF' +
        packed_localeid +
        b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'
    )

def main():
    with open("alt_inject.json", "rb") as configuration_file:
        # Reading configuration json
        configuration_dict: dict = json.load(configuration_file)

    with open("alt.ckd", "wb") as file:
        # Getting count of alternates
        count_of_alternates: int = len(configuration_dict["ALTMAP"])

        # Writing & packing count of alternates to 4 bytes
        file.write(
            struct.pack(">I", count_of_alternates)
        )

        # Logging information about it in console
        log_message(
            "Count of alternates is packed & writed!"
        )

        # Encoding array of alternates 
        # to Just Dance serialization format
        for alternate_information in configuration_dict["ALTMAP"]:
            # Encoding alternate information 
            # to Just Dance serialization format
            encode_alternate_information: bytes = alt_map_encode(alternate_information)

            # Writing our encoded alternate information
            file.write(
                encode_alternate_information
            )

            # Logging information about it in console
            log_message(
                f"Information about {alternate_information['MapName']} encoded & writed!"
            )

    # Ending screen
    log_message(
        "Modify gameconfig.isg.ckd, where the list of alt codenames are listed."
    )
    input()

if __name__ == "__main__":
    main()