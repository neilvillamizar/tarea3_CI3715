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
        self.assertTrue( self.sec.registrarUsuario("correo@gmail.com","Clave1234","Clave1234") , "True" )
        self.assertTrue( self.exist(self.sec.dic, "correo@gmail.com", "Clave1234"), "True")

    def testEmailNotOK1( self ):
        self.assertFalse( self.sec.registrarUsuario("correogmail.com","Clave1234","Clave1234") , "False" )

    def testEmailNotOK2( self ):
        self.assertFalse( self.sec.registrarUsuario("correo..gmail@gmail.com","Clave1234","Clave1234") , "False" )

    def testEmailNotOK3( self ):
        self.assertFalse( self.sec.registrarUsuario(".correo.gmail@gmail.com","Clave1234","Clave1234") , "False" )

    def testEmailNotOK4( self ):
        self.assertFalse( self.sec.registrarUsuario("correo.gmail.@gmail.com","Clave1234","Clave1234") , "False" )

if __name__ == "__main__":
    unittest.main() # run all test 