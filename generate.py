#!/usr/bin/python

# forked from https://gist.github.com/dims/5000f40c539b6eac914f#file-keyutils-py

import ecdsa
import ecdsa.der
import ecdsa.util
import hashlib
import os
import re
import struct
import sys

b58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def base58encode(n):
    result = ''
    while n > 0:
        result = b58[n%58] + result
        n /= 58
    return result

def base256decode(s):
    result = 0
    for c in s:
        result = result * 256 + ord(c)
    return result

def countLeadingChars(s, ch):
    count = 0
    for c in s:
        if c == ch:
            count += 1
        else:
            break
    return count

# https://en.bitcoin.it/wiki/Base58Check_encoding
def base58CheckEncode(version, payload):
    s = chr(version) + payload
    checksum = hashlib.sha256(hashlib.sha256(s).digest()).digest()[0:4]
    result = s + checksum
    leadingZeros = countLeadingChars(result, '\0')
    return '1' * leadingZeros + base58encode(base256decode(result))

def privateKeyToWif(key_hex):
    return base58CheckEncode(0x80, key_hex.decode('hex'))

def privateKeyToPublicKey(s):
    sk = ecdsa.SigningKey.from_string(s.decode('hex'), curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    return ('\04' + sk.verifying_key.to_string()).encode('hex') # https://en.bitcoin.it/wiki/File:PubKeyToAddr.png

def pubKeyToAddr(s):
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(hashlib.sha256(s.decode('hex')).digest())
    return base58CheckEncode(0, ripemd160.digest())

def keyToAddr(s):
    return pubKeyToAddr(privateKeyToPublicKey(s))

def keyPairFromPassword(password):
    private_key = hashlib.sha256(password).digest().encode('hex') # same as `echo -n "foobar" | openssl dgst -sha256`
    print "Passphrase                     : %s " % password
    print "Secret Exponent (Uncompressed) : %s " % private_key
    print "Private Key (Uncompressed)     : %s " % privateKeyToWif(private_key)
    print "Public Key                     : %s " % privateKeyToPublicKey(private_key)
    print "Address                        : %s " % keyToAddr(private_key)
    print "\nVerify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!"
    return

def keyPairFromRandom():
    private_key = os.urandom(32).encode('hex')
    print "Generating random private key. Pass an argument to generate from passphrase."
    print "Passphrase                     : ?  "
    print "Secret Exponent (Uncompressed) : %s " % private_key
    print "Private Key (Uncompressed)     : %s " % privateKeyToWif(private_key)
    print "Public Key                     : %s " % privateKeyToPublicKey(private_key)
    print "Address                        : %s " % keyToAddr(private_key)
    print "\nVerify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!"
    return

if len(sys.argv) == 1:
    keyPairFromRandom()
elif len(sys.argv) == 2:
    keyPairFromPassword(sys.argv[1])
else:
    print "Failed! Too many arguments"
    sys.exit(1)
