import re 

class security():

	def __init__(self):
		self.dic = {}
		self.usr_number = 0

	def verify_format(self, email):
		regex = r'^\w+([!#\$%&\'\*\+-\/=\^_`\{\|\}~\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
		if(re.search(regex,email)): 
			return True
		return False

	def registrarUsuario(self, email, password1, password2):

		if(not self.verify_format(email)):
			print("Correo electrónico inválido y/o Clave inválida")
			return False

		return True