#!/bin/bash/env python3
# python program to convert an IP address to and from decimal and binary


def ip2bin(ip):
    """
    Convert an IP address to binary
    :param ip: IP address
    :return: binary representation of IP address
    """
    return '.'.join(str(bin(int(x))[2:].zfill(8)) for x in ip.split('.'))


def main():
    """
    Main function
    :return: None
    """
    ip = input('Enter an IP address: ')
    print('{} in binary is {}'.format(ip, ip2bin(ip)))


if __name__ == '__main__':
    main()
    exit(0)
