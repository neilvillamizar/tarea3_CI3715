import unittest
from security import *



class securityRegistrarUsuarioTester( unittest.TestCase ):
    
    def exist(self, email, password):
        return self.sec.dic[email] == password[::-1]
        """ por implementar """

    def setUp(self):
        """Call before every test case."""
        self.sec = security()

    def testEmailAndPasswordOK( self ):
        self.assertTrue( self.sec.registrarUsuario("correo@gmail.com","Clave1234","Clave1234"))
        self.assertTrue( self.exist("correo@gmail.com", "Clave1234"))
    
    def testEmailWithLotOfDots(self):
        self.assertTrue(self.sec.registrarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234", "Clave1234"))

    def testEmailWithSpecialCharacters(self):
        self.assertTrue(self.sec.registrarUsuario("user%example.com@example.org", "Clave1234", "Clave1234"))

    def testEmailNotOK1( self ):
        self.assertFalse( self.sec.registrarUsuario("correogmail.com","Clave1234","Clave1234"))

    def testEmailNotOK2( self ):
        self.assertFalse( self.sec.registrarUsuario("correo..gmail@gmail.com","Clave1234","Clave1234"))

    def testEmailNotOK3( self ):
        self.assertFalse( self.sec.registrarUsuario(".correo.gmail@gmail.com","Clave1234","Clave1234"))

    def testEmailNotOK4( self ):
        self.assertFalse( self.sec.registrarUsuario("correo.gmail.@gmail.com","Clave1234","Clave1234"))
    
    def testEmailOkNotPasswordNotLetter(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "123456789", "123456789"))
    
    def testEmailOkNotPasswordNoDigit(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Claveyeah", "Claveyeah"))
    
    def testEmailOkNotPasswordNotUppercase(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "claveyeah123", "claveyeah123"))
    
    def testEmailOkNotPasswordTooLong(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Claveyeahimmaw123", "Claveyeahimmaw123"))
    
    def testEmailOkNotPasswordLessThan3Letters(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Cl12345678", "Cl12345678"))

    def testPasswordsNotEqual(self):
        self.assertFalse(self.sec.registrarUsuario("correo@gmail.com", "Cla2345678", "Clb2345678"))

class securityIngresarUsuarioTester( unittest.TestCase ):
    
    def exist(self, email, password):
        return self.sec.dic[email] == password[::-1]
        """ por implementar """

    def setUp(self):
        """Call before every test case."""
        self.sec = security()
        

    def testEmailAndPasswordOK( self ):
        self.sec.registrarUsuario("correo@gmail.com", "Clave123", "Clave123")
        self.assertTrue( self.sec.ingresarUsuario("correo@gmail.com", "Clave123"))

    def testUserDoesntExists( self ):
        self.sec.registrarUsuario("correo@gmail.com", "Clavee123", "Clave123")
        self.assertFalse( self.sec.ingresarUsuario("correo@gmail.com", "Clavee123"))
    
    def testEmailWithLotOfDots(self):
        self.sec.registrarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234", "Clave1234")
        self.assertTrue(self.sec.ingresarUsuario("disposable.style.email.with+symbol@example.com", "Clave1234"))

    def testEmailWithSpecialCharacters(self):
        self.sec.registrarUsuario("user%example.com@example.org", "Clave1234", "Clave1234")
        self.assertTrue(self.sec.ingresarUsuario("user%example.com@example.org","Clave1234"))

    def testEmailNotOK1( self ):
        self.assertFalse( self.sec.ingresarUsuario("correogmail.com", "Clave1234"))

    def testEmailNotOK2( self ):
        self.assertFalse( self.sec.ingresarUsuario("correo..gmail@gmail.com","Clave1234"))

    def testEmailNotOK3( self ):
        self.assertFalse( self.sec.ingresarUsuario(".correo.gmail@gmail.com","Clave1234"))

    def testEmailNotOK4( self ):
        self.assertFalse( self.sec.ingresarUsuario("correo.gmail.@gmail.com","Clave1234"))
    
    def testEmailOkNotPasswordNotLetter(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "123456789"))
    
    def testEmailOkNotPasswordNoDigit(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Claveyeah"))
    
    def testEmailOkNotPasswordNotUppercase(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "claveyeah123"))
    
    def testEmailOkNotPasswordTooLong(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Claveyeahimmaw123"))
    
    def testEmailOkNotPasswordLessThan3Letters(self):
        self.assertFalse(self.sec.ingresarUsuario("correo@gmail.com", "Cl12345678"))



if __name__ == "__main__":
    unittest.main() # run all test 