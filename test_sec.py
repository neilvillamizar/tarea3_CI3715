import unittest
from security import *



class securityRegistrarUsuarioTester( unittest.TestCase ):
    
    def exist(self, email, password):
        return email in self.sec.dic and self.sec.dic[email] == password[::-1]

    def setUp(self):
        """Call before every test case."""
        self.sec = security()

    # Caso interior
    def testEmailAndPasswordOK( self ):
        self.assertTrue( self.sec.registrarUsuario("correo@gmail.com","Clave1234","Clave1234"))
        self.assertTrue( self.exist("correo@gmail.com", "Clave1234"))
    
    # Caso interior
    def testEmailWithLotOfDots(self):
        self.assertTrue(self.sec.registrarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234", "Clave1234"))

    # Caso interior
    def testEmailWithSpecialCharacters(self):
        self.assertTrue(self.sec.registrarUsuario("user%example.com@example.org", "Clave1234", "Clave1234"))

    # Caso Malicioso
    def testEmailNotOK1( self ):
        self.assertFalse( self.sec.registrarUsuario("correogmail.com","Clave1234","Clave1234"))

    # Caso interior
    def testEmailNotOK2( self ):
        self.assertFalse( self.sec.registrarUsuario("correo..gmail@gmail.com","Clave1234","Clave1234"))

    # Caso frontera
    def testEmailNotOK3( self ):
        self.assertFalse( self.sec.registrarUsuario(".correo.gmail@gmail.com","Clave1234","Clave1234"))

    # Caso interior
    def testEmailNotOK4( self ):
        self.assertFalse( self.sec.registrarUsuario("correo.gmail.@gmail.com","Clave1234","Clave1234"))
    
    # Caso interior
    def testEmailOkNotPasswordNotLetter(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "123456789", "123456789"))
    
    # Caso interior
    def testEmailOkNotPasswordNoDigit(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Claveyeah", "Claveyeah"))
    
    # Caso frontera
    def testEmailOkNotPasswordNotUppercase(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "claveyeah123", "claveyeah123"))
    
    # Caso Esquina
    def testEmailOkNotPasswordTooLong(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Claveyeahimmaw123", "Claveyeahimmaw123"))
    
    # Caso Frontera
    def testEmailOkNotPasswordLessThan3Letters(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Cl12345678", "Cl12345678"))

    # Caso interior
    def testPasswordsNotEqual(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Cla2345678", "Clb2345678"))

class securityIngresarUsuarioTester( unittest.TestCase ):
    
    def exist(self, email, password):
        return email in self.sec.dic and self.sec.dic[email] == password[::-1]

    def setUp(self):
        """Call before every test case."""
        self.sec = security()
        
    # Caso interior
    def testEmailAndPasswordOK( self ):
        self.sec.registrarUsuario("correo@gmail.com", "Clave123", "Clave123")
        self.assertTrue( self.sec.ingresarUsuario("correo@gmail.com", "Clave123"))

    # Caso malicioso
    def testUserDoesntExists( self ):
        self.sec.registrarUsuario("correo@gmail.com", "Clavee123", "Clave123")
        self.assertFalse( self.sec.ingresarUsuario("correo@gmail.com", "Clavee123"))
    
    # Caso interior
    def testEmailWithLotOfDots(self):
        self.sec.registrarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234", "Clave1234")
        self.assertTrue(self.sec.ingresarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234"))

    # Caso interior
    def testEmailWithSpecialCharacters(self):
        self.sec.registrarUsuario("user%example.com@example.org", "Clave1234", "Clave1234")
        self.assertTrue(self.sec.ingresarUsuario("user%example.com@example.org","Clave1234"))

    # Caso malicioso
    def testEmailNotOK1( self ):
        self.assertFalse( self.sec.ingresarUsuario("correogmail.com", "Clave1234"))

    # Caso interior
    def testEmailNotOK2( self ):
        self.assertFalse( self.sec.ingresarUsuario("correo..gmail@gmail.com","Clave1234"))

    # Caso frontera
    def testEmailNotOK3( self ):
        self.assertFalse( self.sec.ingresarUsuario(".correo.gmail@gmail.com","Clave1234"))

    # Caso interior
    def testEmailNotOK4( self ):
        self.assertFalse( self.sec.ingresarUsuario("correo.gmail.@gmail.com","Clave1234"))
    
    # Caso interior
    def testEmailOkNotPasswordNotLetter(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "123456789"))
    
    # Caso interior
    def testEmailOkNotPasswordNoDigit(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Claveyeah"))
    
    # Caso interior
    def testEmailOkNotPasswordNotUppercase(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "claveyeah123"))
    
    # Caso interior
    def testEmailOkNotPasswordTooLong(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Claveyeahimmaw123"))
    
    # Caso interior
    def testEmailOkNotPasswordLessThan3Letters(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Cl12345678"))



if __name__ == "__main__":
    unittest.main() # run all test 