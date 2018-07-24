# fileCrypto

Encryption and Decryption Files Was Never Easier Than Before and for EVERYONE !!!

## Dependencies

* pyaes
* pycrypto

## Features

* Anyone Can Use It, Beginner or Profissional
* No Hard Coding To Encrypt and Decrypt File Anymore
* Work In Any Platform (Linux, Mac Os, Windows)

## What's algorithm that is in fileCrypto ?

* AES
* XOR
* Base64(**Without Key**)
* Base32(**Without Key**)
* Base16(**Without Key**)

## Hmm What Is Key ?


This seems to be a point of confusion for many people new to using encryption. You can think of the key as the "password". However, these algorithms require the "password" to be a specific length.

But You can Use Any length You want No Problem, **Wait What You Just Say Specific LENGTH**

Yeah. I did But I Use MD5 Hash To Get The Specific length. However, The Input Was .

## How I Can Use It ??

Like I Say In Description It's Almost Easy For Every One To Use It.

Let's Give  Exemple For Each algorithm

## AES

#### Encryption

```python

import fileCrypto

#For fileOnAES is 3 parametre
#The First is The File Derection
#Seconde Is for The Key(password) 
#This Last is for extension and I Make The Defaut One is '.cry'
aes = fileCrypto.fileOnAES('exemple.jpg','123456789')

# encrypt() methode is to give the order to encrypt the file
# decrypt() methode is to give the order to decrypt the file

aes.encrypt()

#[Out]:exemple.jpg.cry
```
For The Extension you can use what ever u want **Don't forget to Start The Extension with a dot '.'**

Exemple :
	**.enc**
	**.ree**
	**.yourName**


#### Decryption

```python

import fileCrypto

#For fileOnAES is 3 parametre
#The First is The Encrypt File Derection 
#Seconde Is for The Key(password) That U USe
#This Last is for extension and I Make The Defaut One is '.cry' 
#But Use WHat You Encrypt With

aes = fileCrypto.fileOnAES('exemple.jpg.cry','123456789')

# encrypt() methode is to give the order to encrypt the file
# decrypt() methode is to give the order to decrypt the file

aes.decrypt()

#[Out]:exemple.jpg
```

## XOR

#### Encryption

```python

import fileCrypto

#For fileOnAES is 3 parametre
#The First is The File Derection
#Seconde Is for The Key(password) 
#This Last is for extension and I Make The Defaut One is '.cry'
xor = fileCrypto.fileOnXOR('exemple.jpg','123456789')

# encrypt() methode is to give the order to encrypt the file
# decrypt() methode is to give the order to decrypt the file

xor.encrypt()

#[Out]:exemple.jpg.cry
```
For The Extension you can use what ever u want **Don't forget to Start The Extension with a dot '.'**

Exemple :
	**.enc**
	**.ree**
	**.yourName**

#### Decryption 

```python

import fileCrypto

#For fileOnAES is 3 parametre
#The First is The Encrypt File Derection 
#Seconde Is for The Key(password) That U USe
#This Last is for extension and I Make The Defaut One is '.cry' 
#But Use WHat You Encrypt With

xor = fileCrypto.fileOnXOR('exemple.jpg.cry','123456789')

# encrypt() methode is to give the order to encrypt the file
# decrypt() methode is to give the order to decrypt the file

xor.decrypt()

#[Out]:exemple.jpg
```

## Base64, Base32, Base16(**No Key For This 3 Algorithm**)

Hir Is Different Then Other
In Those Algorithm you will Use encode and decode methode because there are not for encryption but for coding data

#### Encode

```python

import fileCrypto

#For fileOnAES is two parametre
#The First is The File Derection
#This Last is for extension and I Make The Defaut One is '.cry'
base64 = fileCrypto.fileOnBase64('exemple.jpg','123456789')

# encode() methode is to give the order to encrypt the file
# decode() methode is to give the order to decrypt the file

base64.encrypt()

#[Out]:exemple.jpg.cry
```
For The Extension you can use what ever u want **Don't forget to Start The Extension with a dot '.'**

Exemple :
	**.enc**
	**.ree**
	**.yourName**

#### Decode 

```python

import fileCrypto

#For fileOnAES is 2 parametre
#The First is The Encrypt File Derection 
#This Last is for extension and I Make The Defaut One is '.cry' 
#But Use WHat You Encrypt With

base64 = fileCrypto.fileOnBase64('exemple.jpg.cry','123456789')

# encode() methode is to give the order to encrypt the file
# decode() methode is to give the order to decrypt the file

base64.decrypt()

#[Out]:exemple.jpg
```

Just Change The **fileOnBase64** to **fileOnBase32** or **fileOnBase16** If you want Use an diffirent algo for base

FAQ
---

#### What You Will Do In Futur 

I will Add Other Encryption ALgorithm

Like :

* Blowfish
* DES 
* DES3
* ARC2
...

#### How do I get a question I have added?

E-mail me at zain.work02@gmail.com with any questions, suggestions and comments 


#### Can I give you my money?

Umm... Ok? 😄

_Bitcoin_  - `19MNfdTtGSxuBZpcKXJPVc3KbRnohxARMJ` 

