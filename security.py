import re 

class security():

	def __init__(self):
		self.dic = {}
		self.usr_number = 0

	def verify_formatEmail(self, email):
		regex = r'^\w+([!#\$%&\'\*\+-\/=\^_`\{\|\}~\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
		if(re.search(regex,email)): 
			return True
		return False

	def verify_formatPassword(self, password):
		regex = r'[a-zA-Z0-9]+'

		if(not re.search(regex, password)):
			return False
		
		if(len(password) < 8 or len(password) > 16):
			return False

		counter = 0
		existsMin = False
		existsMax = False
		existsDig = False

		for c in password:			
			if(re.search(r'[a-z]', c)):
				existsMin = True
			
			if(re.search(r'[A-Z]', c)):
				existsMax = True
			
			if(re.search(r'[0-9]', c)):
				existsDig = True

			if(re.search(r'[a-zA-Z]', c)):
				counter += 1
		
		if(not existsDig or not existsMax or not existsMin):
			return False

		if(counter < 3):
			return False
		
		return True

	def registrarUsuario(self, email, password1, password2):

		if(not self.verify_formatEmail(email) or not self.verify_formatPassword(password1)):
			print("Correo electrónico inválido y/o Clave inválida")
			return False

		return True