"""
Address line parser module
"""
import re


class AddressParser:
    """
    Address line parser class
    """
    patterns = [
        '(?P<street>.*[^,]),*\s,*(?P<number>[0-9].*)',
        '(?P<street>.*[^,]),*\s,*(?P<number>No.+[0-9])',
        '(?P<number>[0-9]+[A-Z]*),*\s,*(?P<street>.*[^,])',
        '(?P<street>.*[^,]),*\s,*(?P<number>[0-9]+[A-Z]*)',
        '(?P<number>[0-9]+[A-Z]*),*\s,*(?P<street>.*[^,])'
    ]

    def parse(self, address):
        """
        input: address line string
        output: (house number, street)
        """
        assert type(address) == str, 'Invalid address type, it should be a string'
        for p in self.patterns:
            match = re.search(p, address)
            if match:
                return match.group('number').strip(), match.group('street').strip()
        raise ValueError('Can\'t parse address: {}'.format(address))
