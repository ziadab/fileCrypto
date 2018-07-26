try:
	import pyaes
except:
	sys.exit("You Need To Download First pyaes Module.\nusing the following command : 'pip3 install pyaes'")

import time
import platform
import base64
import os
import hashlib

class fileOnAES():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	import fileCrypto
	key = "123456789"  #Hir You Can Say Key Is Like Password For Your File
	myfile = fileCrypto.fileOnAES("exemple.jpg", key)
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path,key,extension='.cry'):
		"""To Get The File Direction And The Key From User"""
		self.path = str(path)
		tmp = hashlib.md5(key.encode('utf8')).hexdigest()
		self.key = str.encode(tmp) 
		self.extension = str(extension)


	def encrypt(self):
		"""To give the Order To Encrypt The File"""
		t = time.time()
		#Check If The File is 
		if self.extension not in self.path:
			with open(self.path, 'rb') as file:
				file_data = file.read()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path_dir = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path_dir = self.path.split('/')[-1]
			#End Checking Wich Platform
			print('Encryption of '+self.path_dir+'...')
			print('It\'s may take a will')
			######################### AES Algorithm #########################
			aes = pyaes.AESModeOfOperationCTR(self.key)
			self.encoded = aes.encrypt(file_data)
			#################################################################
			print('writing in you file ...')
			os.remove(self.path)
			with open(str(self.path) + self.extension,'wb') as newfile:
				newfile.write(self.encoded)
			print('Done In '+str(time.time() -t))
		else:
			print("The File is already encrypt")

	def decrypt(self):
		"""To Give The Order To Decrypt The File"""
		t = time.time()
		if self.extension in self.path:
			with open(self.path,'rb') as file:
				file_data = file.read()
			#Start CHecking The PlatForm
			if platform.system() == "Windows":
				self.path = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path = self.path.split('/')[-1]
			#End Checking Wich Platform
			print("Decrypting of "+str(self.path)+"...")
			############################################################################
			aes = pyaes.AESModeOfOperationCTR(self.key)
			self.decoded = aes.decrypt(file_data)
			############################################################################
			self.path2 = self.path.replace(self.extension,"")
			os.remove(self.path)
			print('Writing in Your File...')
			with open(self.path2, "wb") as newfile:
				newfile.write(self.decoded)
			print('Done In '+str(time.time() -t))
		else:
			print("The File is Not Encrypted To Decrypted")

