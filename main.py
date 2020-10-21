"""
Reads a txt file contains addresses, parses them, then creates a json file contains parsing results
"""
import json

from address_parser.addressline_parser import AddressParser

SOURCE_FILE_PATH = 'samples.txt'

OUTPUT_FILE_PATH = 'parsing_result.json'

if __name__ == '__main__':
    try:
        address_parser = AddressParser()
        output = []
        with open(SOURCE_FILE_PATH) as fh:
            lines = fh.readlines()
        for line in lines:
            try:
                result = address_parser.parse(line)
                output.append({'street': result[1], 'housenumber': result[0]})
            except Exception as e:
                print(e)
        with open(OUTPUT_FILE_PATH, 'w', encoding='utf8') as fh:
            json.dump(output, fh, ensure_ascii=False)
    except IOError:
        print('Can\'t find this path: {}'.format(SOURCE_FILE_PATH))