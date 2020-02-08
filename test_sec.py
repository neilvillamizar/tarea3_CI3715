import unittest
from security import *



class securityTester( unittest.TestCase ):
    
    def exist():
        """ por implementar """

    def setUp(self):
        """Call before every test case."""
        self.sec = security()

    def testEmailAndPasswordOK( self ):
        self.assertTrue( self.sec.registrarUsuario("correo@gmail.com","Clave1234","Clave1234") , "True" )
        self.assertTrue( self.exist(self.sec.dic, "correo@gmail.com", "Clave1234"), "True")



if __name__ == "__main__":
    unittest.main() # run all test 