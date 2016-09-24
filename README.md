# hashcheck
Python script to report and test a file hash.

* Generates SHA256, SHA1, or MD5 hash of a given file.
* Optionally, takes a hash value as input and compares it to the file's hash.
* SHA1 is default hashing algorithm, but SHA256 or MD5 can be specified.
* Blocksize 65536 is default, but any other blocksize can be specified.


```
./hashcheck.py -h
usage: hashcheck.py [-h] -i INPUTFILE [-H HASHVALUE] [-t {sha256,sha1,md5}]
                    [-b BLOCKSIZE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file to check hash on
  -H HASHVALUE, --hashvalue HASHVALUE
                        input hash value, if you want to automatically compare
  -a {sha256,sha1,md5}, --algorithm {sha256,sha1,md5}
                        input hash algorithm type
  -b BLOCKSIZE, --blocksize BLOCKSIZE
                        specify a blocksize
```
