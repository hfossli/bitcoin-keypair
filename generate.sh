#!/bin/bash

openssl_path='/usr/local/opt/openssl/bin/openssl'

PRIVATE_PEM=`     $openssl_path ecparam -genkey -name secp256k1 -rand /dev/urandom -noout 2> /dev/null`
PUBLIC_PEM=`      $openssl_path ec -in <(echo "${PRIVATE_PEM}") -pubout 2> /dev/null`
SECRET_EXPONENT=` $openssl_path ec -in <(echo "${PRIVATE_PEM}") -outform DER 2> /dev/null|tail -c +8|head -c 32|xxd -p -c 32`
ADRESS=`          $openssl_path ec -in <(echo "${PRIVATE_PEM}") -pubout -outform DER 2> /dev/null|tail -c 65|xxd -p -c 65`

echo "Passphrase                     : ?"
echo "Secret Exponent (Uncompressed) : $SECRET_EXPONENT"
echo "Private Key (Uncompressed)     : ?"
echo "Public Key                     : ?"
echo "Adress                         : $ADRESS"
echo ""
echo "Verify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!"
