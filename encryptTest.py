import unittest
import encrypt

class Test(unittest.TestCase):
    
    def test_sh256(self):
        result1 = encrypt.encrypt_pass('lumpenproleterya')
        result2 = encrypt.encrypt_pass('lalala123')
        result3 = encrypt.encrypt_pass('123124565432134567898765432214252435123`231234252341312312415124')

        ch_result1 = 'e5d1b30b67a39e1ec076ae9ea12049e0253fdec41eb525862f9346f1038aa05f'
        ch_result2 = '273259472544c038bdf860d1b3aba5afb2ad0257c9a840da3822e77a80cd6fdc'
        ch_result3 = 'cd905d7164920bcba91dfc61540a0b42daf2accb155b4304995244db35191944'

        self.assertEqual(result1, ch_result1)
        self.assertEqual(result2, ch_result2)
        self.assertEqual(result3, ch_result3)

    def test_salting(self):
        result1 = encrypt.salting_pass(encrypt.encrypt_pass('lumpenproleterya'))
        result2 = encrypt.salting_pass(encrypt.encrypt_pass('lalala123'))
        result3 = encrypt.salting_pass(encrypt.encrypt_pass('123124565432134567898765432214252435123`231234252341312312415124'))

        _hashed1, salt = result1.split(':')
        _hashed2, salt = result2.split(':')
        _hashed3, salt = result3.split(':')

        ch_result1 = 'e5d1b30b67a39e1ec076ae9ea12049e0253fdec41eb525862f9346f1038aa05f'
        ch_result2 = '273259472544c038bdf860d1b3aba5afb2ad0257c9a840da3822e77a80cd6fdc'
        ch_result3 = 'cd905d7164920bcba91dfc61540a0b42daf2accb155b4304995244db35191944'

        self.assertEqual(_hashed1, ch_result1)
        self.assertEqual(_hashed2, ch_result2)
        self.assertEqual(_hashed3, ch_result3)
