try:
	from Crypto.Cipher import Blowfish
	from Crypto import Random
except:
	import sys
	sys.exit("You Need To Download First pycrypto Module.\nusing the following command : 'pip3 install pycrypto'")

import time
import hashlib
import platform
import base64
import os

class fileOnBlowfish():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	import fileCrypto
	key = "123456789"  #Hir You Can Say Key Is Like Password For Your File
	myfile = fileCrypto.fileOnBlowfish("exemple.jpg", key)
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path,key,extension='.filecrypto'):
		self.path = str(path)
		tmp = hashlib.md5(key.encode('utf8')).hexdigest()
		self.key = str.encode(tmp) 
		self.extension = str(extension)

	def encrypt(self,timerPrinting=False):
		"""To give the Order To Encrypt The File"""

		t = time.time() 
		if self.extension not in self.path:
			with open(self.path,'rb') as infile:
				file_data = infile.read()
			#Start To CHecking The PlatForm
			# if platform.system() == "Windows":
			# 	self.path_dir = self.path.split("\\")[-1]
			# elif platform.system() == "Linux":
			# 	self.path_dir = self.path.split('/')[-1]
			# #End Checking Wich Platform
			# print('Encryption of '+self.path_dir+'...')
			# print('It\'s may take a will')
			################################### Blowfish Algorithm ##############################
			bs = Blowfish.block_size
			iv = Random.new().read(bs)
			padding = b"}"
			p = lambda s: s+(bs - len(s) % bs )*padding
			c= Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
			encrypt = iv + c.encrypt(p(file_data))
			self.encrypt = base64.b64encode(encrypt) 
			################################################################
			#print("writing in your file ...")
			os.remove(self.path)
			with open(self.path + self.extension,"wb") as newfile:
				newfile.write(self.encrypt)
			if timerPrinting:
				print('Done In '+ time.time() -t)
		else:
			print('The File is already encrypt.')


	def decrypt(self,timerPrinting=False):
		"""Give The Order To Decrypt"""

		t = time.time() 
		if self.extension in self.path:
			with open(self.path,'rb') as infile:
				file_data = infile.read()
			# #Start Checking the Platform
			# if platform.system() == 'Windows':
			# 	self.path = self.path.split('\\')[-1]
			# elif platform.system() == 'Linux':
			# 	self.path = self.path.split('/')[-1]
			# # END Checking
			# print('Decryption of '+ self.path +"...")
			######################### Blowfish Decryption Algorithm ###############
			bs = Blowfish.block_size
			realData = base64.b64decode(file_data)[8:]
			iv = base64.b64decode(file_data)[:8]
			decrypt = Blowfish.new(self.key, Blowfish.MODE_CBC, iv)
			self.decrypt = decrypt.decrypt(realData)
			########################### End Blowfish #########################
			#print('Writing in your file...')
			self.out = self.path.replace(self.extension,'')
			os.remove(self.path)
			with open(self.out,'wb') as outfile:
				outfile.write(self.decrypt)
			if timerPrinting:
				print("Done in ",time.time() - t)
			
		else:
			print('The File is Not Encrypted To Decrypted.')
