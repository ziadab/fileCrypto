import os
import platform 
import base64

class fileOnBase64():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	from fileCrypto import Base64
	myfile = fileOnBase64("exemple.jpg")
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path):
		self.path = str(path)
		
	def encrypt(self):
		"""To give the Order To Encrypt The File"""

		if '.cry' not in self.path:
			file = open(self.path,"rb")
			file_data = file.read()
			file.close()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path = self.path.split('/')[-1]
			#End Checking Wich Platform
			print('Encryption of '+str(self.path)+'...')
			######################### Base 64 ##########################
			self.encoded = base64.b64encode(file_data)
			############################################################
			print('writing in you file ...')
			print("It's will Take a Will ")
			os.remove(self.path)
			newfile = open(str(self.path) + '.cry',"wb")
			newfile.write(self.encoded)
			newfile.close()
			print('Done.')
		else:
			print("The File is already encrypt")

	def decrypt(self):
		"""To Give The Order To Decrypt The File"""

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
			self.decoded = base64.b64decode(file_data)
			############################################################
			self.path2 = self.path.replace('.cry',"")
			os.remove(self.path)
			print('Writing in Your File...')
			newfile = open(self.path2,'wb')
			newfile.write(self.decoded)
			newfile.close()
		else:
			print("The File is Not Encrypted To Decrypted")



		