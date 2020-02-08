import unittest
from security import *



class securityTester( unittest.TestCase ):
    
    def exist(self, dic, email, password):
        return True
        """ por implementar """

    def setUp(self):
        """Call before every test case."""
        self.sec = security()

    def testEmailAndPasswordOK( self ):
        self.assertTrue( self.sec.registrarUsuario("correo@gmail.com","Clave1234","Clave1234"))
        self.assertTrue( self.exist(self.sec.dic, "correo@gmail.com", "Clave1234"))
    
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

if __name__ == "__main__":
    unittest.main() # run all test 