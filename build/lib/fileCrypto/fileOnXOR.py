try:
	from Crypto.Cipher import XOR
except:
	import sys
	sys.exit("You Need To Download First pycrypto Module.\nusing the following command : 'pip3 install pycrypto'")

import time
import hashlib
import base64
import platform
import os

class fileOnXOR():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	import fileCrypto
	key = "123456789"  #Hir You Can Say Key Is Like Password For Your File
	myfile = fileCrypto.fileOnXOR("exemple.jpg", key)
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path,key,extension='.filecrypto'):
		"""To Get The File Direction And The Key From User"""
		self.path = str(path)
		tmp = hashlib.md5(key.encode('utf8')).hexdigest()
		self.key = str.encode(tmp)
		self.extension = str(extension)
		

	def encrypt(self,timerPrinting=False):
		"""To give the Order To Encrypt The File"""
		t = time.time()
		#Check If The File is 
		if self.extension not in self.path:
			with open(self.path, 'rb') as file:
				file_data = file.read()
			#Start To CHecking The PlatForm
			# if platform.system() == "Windows":
			# 	self.path_dir = self.path.split("\\")[-1]
			# elif platform.system() == "Linux":
			# 	self.path_dir = self.path.split('/')[-1]
			# #End Checking Wich Platform
			# print('Encryption of '+self.path_dir+'...')
			# print('It\'s may take a will')
			######################### XOR Algorithm #########################
			cipher = XOR.new(self.key)
			self.encoded = base64.b64encode(cipher.encrypt(file_data))
			#################################################################
			 #print('writing in you file ...')
			os.remove(self.path)
			with open(str(self.path) + self.extension,"wb") as outfile:
				outfile.write(self.encoded)
			if timerPrinting:
				print('Done In '+str(time.time() -t))
			else:
				pass
		else:
			print("The File is already encrypt")

	def decrypt(self,timerPrinting=False):
		t = time.time()
		"""To Give The Order To Decrypt The File"""
		if self.extension in self.path:
			with open(self.path,'rb') as file:
				file_data = file.read()
			#Start To CHecking The PlatForm
			# if platform.system() == "Windows":
			# 	self.path = self.path.split("\\")[-1]
			# elif platform.system() == "Linux":
			# 	self.path = self.path.split('/')[-1]
			# End Checking Wich Platform
			# print("Decrypting of "+str(self.path)+"...")
			############################################################################
			cipher = XOR.new(self.key)
			self.decoded = cipher.decrypt(base64.b64decode(file_data))
			############################################################################
			self.path2 = self.path.replace(self.extension,"")
			os.remove(self.path)
			# print('Writing in Your File...')
			with open(self.path2,'wb') as outfile:
				outfile.write(self.decoded)
			if timerPrinting:
				print('Done In '+str(time.time() -t))
			else:
				pass
		else:
			print("The File is Not Encrypted To Decrypted")

