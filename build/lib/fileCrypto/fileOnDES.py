try:
	from Crypto.Cipher import DES
	from Crypto import Random
	from Crypto.Util import Counter
except:
	import sys
	sys.exit("You Need To Download First pycrypto Module.\nusing the following command : 'pip3 install pycrypto'")

import time
import platform
import base64
import hashlib
import os

class fileOnDES():
	"""This Class Is To Encrypt And Decrypt Your File In Easy Way No Complaxy
	Is Just Like That :
	import fileCrypto
	key = "123456789"  #Hir You Can Say Key Is Like Password For Your File
	myfile = fileCrypto.fileOnDES("exemple.jpg", key)
	myfile.encrypt() #This Methode To Encrypt The File
	myfile.decrypt() #This Methode To Decrypt the File
	#Encryption And Decryption of File Was Never Easy Than Before
	:)"""

	def __init__(self,path,key,extension='.cry'):
		self.path = str(path)
		tmp = int(hashlib.sha1(key.encode('utf8')).hexdigest(), 16) % (10 ** 8)
		tmp = str(tmp)
		self.key = str.encode(tmp) 
		self.extension = str(extension)

	def encrypt(self):
		"""To give the Order To Encrypt The File"""

		t = time.time() 
		if self.extension not in self.path:
			with open(self.path,"rb") as infile:
				file_data = infile.read()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path_dir = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path_dir = self.path.split('/')[-1]
			#End Checking Wich Platform
			print('Encryption of '+self.path_dir+'...')
			print('It\'s may take a will')
			############################ DES Encryption #################
			bs = DES.block_size
			iv = Random.new().read(int(bs/2))
			ctr = Counter.new(int(bs*8/2), prefix=iv)
			c = DES.new(self.key, DES.MODE_CTR, counter= ctr)
			encrypt_data = iv + c.encrypt(file_data)
			self.encrypt = base64.b64encode(encrypt_data)
			########################### END Encryption ###################
			print('writing your file...')
			os.remove(self.path)
			with open(self.path + self.extension ,"wb") as outfile:
				outfile.write(self.encrypt)
			print("Done In "+str(time.time() -t))
		else:
			print('The file is Already encrypt.')

	def decrypt(self):
		"""To Give The Order To Decrypt The File"""
		t = time.time()
		if self.extension in self.path:
			with open(self.path,'rb') as file:
				file_data = file.read()
			#Start To CHecking The PlatForm
			if platform.system() == "Windows":
				self.path = self.path.split("\\")[-1]
			elif platform.system() == "Linux":
				self.path = self.path.split('/')[-1]
			#End Checking Wich Platform
			print("Decrypting of "+str(self.path)+"...")
			######################### Des Decryption ###################################
			bs = DES.block_size
			iv = base64.b64decode(file_data)[:4]
			encMsg = base64.b64decode(file_data)[4:]
			ctr = Counter.new(int(bs*8/2) , prefix = iv)
			d = DES.new(self.key,DES.MODE_CTR,counter = ctr)
			self.decrypt = d.decrypt(encMsg)
			############################################################################
			self.path2 = self.path.replace(self.extension,"")
			os.remove(self.path)
			print('Writing in Your File...')
			with open(self.path2,'wb') as outfile:
				outfile.write(self.decrypt)
			print('Done In '+str(time.time() -t) +' secondes')
		else:
			print("The File is Not Encrypted To Decrypted")





