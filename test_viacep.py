
import unittest
import viacep

class TestCase(unittest.TestCase):

    def test(self):
    	test = viacep.ViaCEP('78048000')
    	self.assertEqual(test.retorna_uf(), 'MT')

if __name__ == '__main__':
    unittest.main()
