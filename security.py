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

		if(not self.verify_formatEmail(email)):
			print("Correo electrónico inválido.")
			return False

		if(not self.verify_formatPassword(password1)):
			print("Clave invalida.")
			return False

		if(password1 != password2):
			print("Las claves no coinciden.")
			return False

		self.dic[ email ] = password1[::-1]

		return True

	def ingresarUsuario(self, email, password):

		if(not self.verify_formatEmail(email)):
			print("Correo electrónico inválido.")
			return False

		if(not self.verify_formatPassword(password)):
			print("Clave invalida.")
			return False

		if( not (email in self.dic) or (self.dic[ email ] != password[::-1])):
			print("Usuario invalido.")
			return False

		print("Usuario aceptado.")
		return True