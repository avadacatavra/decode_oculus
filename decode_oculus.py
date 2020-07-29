#!/usr/local/bin/python3

from urllib.parse import unquote
from base64 import standard_b64decode as b64_decode
from zlib import decompress
import json

def decode(message_file):
    with open(message_file, 'r') as file_message:
        full_message = file_message.read()

    _, message_sig = full_message.split("&message=")
    message, _ = message_sig.split("&sig")

    url_parsed = unquote(message)

    if url_parsed[-2:] != "==":
        url_parsed += '='
    
    decoded = b64_decode(url_parsed)
    
    decompressed = decompress(decoded)
    
    return json.loads(decompressed.decode('utf-8'))

if __name__ == "__main__":
    import argparse

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description=
        """decode_oculus.py: Takes a file with the b64 and zlib compressed message and reads it in, prints to stdout""")
    parser.add_argument('--input',
                        required=True,
                        metavar='/path/to/facebook_message.txt',
                        help="Full path to the file which contains a complete message")

    args = parser.parse_args()

    out = decode(args.input)



    with open('message.json', 'w') as f:
        json.dump(out, f)

