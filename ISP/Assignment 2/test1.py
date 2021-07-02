import unittest
from aes import AES


class AES_TEST(unittest.TestCase):
    def setUp(self):
        master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
        self.AES = AES(master_key)

    def test_encryption(self):
        plain_text = 0x3243f6a8885a308d313198a2e0370734
        encrypted = self.AES.encrypt(plain_text)
        self.assertEqual(encrypted, 0x3925841d02dc09fbdc118597196a0b32)

    def test_decryption(self):
        cipher_text = 0x3925841D02DC09FBDC118597196A0B32
        decrypted = self.AES.decrypt(cipher_text)
        self.assertEqual(decrypted, 0x3243f6a8885a308d313198a2e0370734)


if __name__ == "__main__":
    unittest.main()
