Generate bitcoin keypair
========================

## Python script

### Generate from passphrase
```bash
python generate.py "foo bar"
```
Outputs                        
```
Passphrase                     : foo bar
Secret Exponent (Uncompressed) : fbc1a9f858ea9e177916964bd88c3d37b91a1e84412765e29950777f265c4b75
Private Key (Uncompressed)     : 5KjAN2k1pD5jiCwBD2XVLLy5Jb4QBndjAn5eVp7UuKg8EmhnTbD
Public Key                     : 04f9f496bc07a951b2668676c6a3a85cc950b2f1da75ad2b05ec2e4ff298b645d02446c9eb520a10fb9694343f10b1d44004ac3f451b4680b8f682a26a80c8d6b3
Address                        : 12XwtdC18Xcp1crHvLGQ6gx2De4HskwwYq

Verify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!
```

This is deterministic. It will output the same no matter where and how many times you run it. That's why you only need to write down or remember the passphrase. A good passphrase should use at least 8 different words picked randomly from a 100,000+ words dictionary.

### Generate random
```bash
python generate.py
```

Outputs     
```
Generating random private key. Pass an argument to generate from passphrase.
Passphrase                     : ?  
Secret Exponent (Uncompressed) : 32fa531c1a4383493e340441044ae36988bf389b86ba1e62811629569d95f000
Private Key (Uncompressed)     : 5JCjjyadcYotxu12rmLnTj966qXXXoSt8fyfyewNX6aU3MULUHS
Public Key                     : 0423d353bb2a53894adda5163d304b20ba60e2f7a193ff3991a34e3b00f7b1afe0913c610bb50ae491f9e4b1e08fd4124714fe8fe6889f52f167a8887179bb6326
Address                        : 16ZYUCWPvAv8Vktr2MDukUHZQRE4MwAasq

Verify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!
```

## Shell / OpenSSL script

Generate random
```bash
./generate.sh
```

Outputs     
```
Passphrase                     : ?
Secret Exponent (Uncompressed) : 07e9be8383e6fd2b9f5fd4860972fb1cce8036a0f2a34e7fa7955ee7399feb6c
Private Key (Uncompressed)     : ?
Public Key                     : ?
Adress                         : 04e71973ae8ff3b73d89a7a52bb1a2d77b9e285a260c65d2d891e9f9e23a7ee3818ecd224bfecbd5ac61d3184de8befea1dabc2a2b1744c12c52f720d7ca9f5572

Verify correctness by visiting https://brainwalletx.github.io/#generator. Never test anything you intend to use!
```


## Verify

Use https://brainwalletx.github.io/#generator to verify the correctness of keypair generation.

**NB: Only verify dummy passwords. Not passwords you intend to use.**

## Useful links
- https://blockchain.info/address/1CWHWkTWaq1K5hevimJia3cyinQsrgXUvg
- https://bitcoin.stackexchange.com/questions/59644/how-do-these-openssl-commands-create-a-bitcoin-private-key-from-a-ecdsa-keypair/59646#59646
- https://gist.github.com/dims/5000f40c539b6eac914f#file-keyutils-py
- https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses
- https://raw.githubusercontent.com/grondilu/bitcoin-bash-tools/master/bitcoin.sh
