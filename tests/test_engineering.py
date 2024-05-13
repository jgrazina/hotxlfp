# -*- coding: utf-8 -*-
import unittest
import math
from hotxlfp import Parser


class TestEngineering(unittest.TestCase):

    def test_hex2dec(self):
        p = Parser(debug=True)
        ret = p.parse('HEX2DEC("A5")')
        self.assertEqual(ret['result'], 165)
        self.assertEqual(ret['error'], None)
        ret = p.parse('HEX2DEC("FFFFFFFF5B")')
        self.assertEqual(ret['result'], -165)
        self.assertEqual(ret['error'], None)
        ret = p.parse('HEX2DEC("3DA408B9")')
        self.assertEqual(ret['result'], 1034160313)
        self.assertEqual(ret['error'], None)
        ret = p.parse('HEX2DEC("ZZZ")')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')

    def test_dec2hex(self):
        p = Parser(debug=True)
        ret = p.parse('DEC2HEX(100, 4)')
        self.assertEqual(ret['result'], '0064')
        self.assertEqual(ret['error'], None)
        ret = p.parse('DEC2HEX(-54)')
        self.assertEqual(ret['result'], 'FFFFFFFFCA')
        self.assertEqual(ret['error'], None)
        ret = p.parse('DEC2HEX(28)')
        self.assertEqual(ret['result'], '1C')
        self.assertEqual(ret['error'], None)
        ret = p.parse('DEC2HEX(64,1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#NUM!')

    def test_delta(self):
        p = Parser(debug=True)
        ret = p.parse('DELTA(5, 4)')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)
        ret = p.parse('DELTA(5, 5)')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('DELTA(0.5, 0)')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)

    def test_complex(self):
        p = Parser(debug=True)
        ret = p.parse('COMPLEX(3, 5)')
        self.assertEqual(ret['result'], complex(3, 5))
        self.assertEqual(ret['error'], None)


    def test_imaginary(self):
        p = Parser(debug=True)
        ret = p.parse('IMAGINARY("i", "imaginary")')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMAGINARY("1", "imaginary")')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMAGINARY("4i", "imaginary")')
        self.assertEqual(ret['result'], 4)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMAGINARY("2+4i", "imaginary")')
        self.assertEqual(ret['result'], 4)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMAGINARY("5-2i", "imaginary")')
        self.assertEqual(ret['result'], -2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMAGINARY("-5-2i", "imaginary")')
        self.assertEqual(ret['result'], -2)
        self.assertEqual(ret['error'], None)
    
    def test_imreal(self):
        p = Parser(debug=True)
        ret = p.parse('IMREAL("i", "real")')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMREAL("1", "real")')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMREAL("4i", "real")')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMREAL("2+4i", "real")')
        self.assertEqual(ret['result'], 2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMREAL("5-2i", "real")')
        self.assertEqual(ret['result'], 5)
        self.assertEqual(ret['error'], None)
        ret = p.parse('IMREAL("-5-2i", "real")')
        self.assertEqual(ret['result'], -5)
        self.assertEqual(ret['error'], None)