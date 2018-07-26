import time
import platform 
import base64
import os

class fileOnBase16():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	import fileCrypto
	myfile = fileCrypto.fileOnBase16("exemple.jpg")
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path,extension='.cry'):
		self.path = str(path)
		self.extension = str(extension)
		
	def encode(self):
		"""To give the Order To Encrypt The File"""
		t = time.time()
		if self.extension not in self.path:
			file = open(self.path,"rb")
			file_data = file.read()
			file.close()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path_dir = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path_dir = self.path.split('/')[-1]
			#End Checking Wich Platform
			print('Encryption of '+self.path_dir+'...')
			print('It\'s may take a will')
			######################### Base 64 ##########################
			self.encoded = base64.b16encode(file_data)
			############################################################
			print('writing in you file ...')
			os.remove(self.path)
			newfile = open(str(self.path) + self.extension,"wb")
			newfile.write(self.encoded)
			newfile.close()
			print('Done In '+str(time.time() -t))
		else:
			print("The File is already encrypt")

	def decode(self):
		"""To Give The Order To Decrypt The File"""
		t = time.time()
		if ".cry" in self.path:
			file = open(self.path,"rb")
			file_data = file.read()
			file.close()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path = self.path.split('/')[-1]
			#End Checking Wich Platform
			print("Decrypting of "+str(self.path)+"...")
			######################## Base64 Decoding ###################
			self.decoded = base64.b16decode(file_data)
			############################################################
			self.path2 = self.path.replace(self.extension,"")
			os.remove(self.path)
			print('Writing in Your File...')
			newfile = open(self.path2,'wb')
			newfile.write(self.decoded)
			newfile.close()
			print('Done In '+str(time.time() -t))
		else:
			print("The File is Not Encrypted To Decrypted")



		