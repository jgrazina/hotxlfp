# -*- coding: utf-8 -*-
import unittest
from hotxlfp import Parser


class TestLookupAndReference(unittest.TestCase):

    def test_choose(self):
        p = Parser(debug=True)
        ret = p.parse('CHOOSE(1,1,3)')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('CHOOSE(2,1,3)')
        self.assertEqual(ret['result'], 3)
        self.assertEqual(ret['error'], None)
        ret = p.parse('CHOOSE(255,1,3)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('CHOOSE(3,1,3)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('CHOOSE(1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#N/A')

    def test_match(self):
        p = Parser(debug=True)
        ret = p.parse('MATCH(39,{25,38,40,41},1)')
        self.assertEqual(ret['result'], 2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('MATCH("f?o",{"eee","aaa","foa","foo"},0)')
        self.assertEqual(ret['result'], 4)
        self.assertEqual(ret['error'], None)
        ret = p.parse('MATCH(39,{25,38,40,41},-1)')
        self.assertEqual(ret['result'], 3)
        self.assertEqual(ret['error'], None)

    def test_index(self):
        p = Parser(debug=True)
        ret = p.parse('INDEX({25,38,40,41},1)')
        self.assertEqual(ret['result'], 25)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1\\2\\3\\4;5\\6\\7\\8};2;1)')
        self.assertEqual(ret['result'], 5)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1;2;3;4};2;2)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#REF!')
        ret = p.parse('INDEX({1;2;3;4})')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('INDEX({1,2,3;4,5,6};;2)')
        self.assertEqual(ret['result'], [2, 5])
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1,2,3},,2)')
        self.assertEqual(ret['result'], 2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUM(INDEX({1,2,3;4,5,6};0;2))')
        self.assertEqual(ret['result'], 7)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1;2;3};2;)')
        self.assertEqual(ret['result'], 2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1,2,3},2,)')
        self.assertEqual(ret['result'], 2)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX({1;2;3};;1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')
        ret = p.parse('INDEX({1;2;3};1/0;)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')
        ret = p.parse('INDEX(1,1,1)')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('INDEX(1,1,2)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#REF!')
        ret = p.parse('SUM(INDEX({1,2,3},0,0))')
        self.assertEqual(ret['result'], 6)
        self.assertEqual(ret['error'], None)
