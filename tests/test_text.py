# -*- coding: utf-8 -*-
import unittest
import math
from hotxlfp import Parser
from hotxlfp.formulas.error import XLError


class TestText(unittest.TestCase):

    def test_char(self):
        p = Parser(debug=True)
        ret = p.parse('CHAR(65)')
        self.assertEqual(ret['result'], 'A')
        self.assertEqual(ret['error'], None)
        ret = p.parse('CHAR(33)')
        self.assertEqual(ret['result'], '!')
        self.assertEqual(ret['error'], None)
        ret = p.parse('CHAR(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')

    def test_code(self):
        p = Parser(debug=True)
        ret = p.parse('CODE("A")')
        self.assertEqual(ret['result'], 65)
        self.assertEqual(ret['error'], None)
        ret = p.parse('CODE("!")')
        self.assertEqual(ret['result'], 33)
        self.assertEqual(ret['error'], None)

    def test_clean(self):
        p = Parser(debug=True)
        ret = p.parse('CLEAN(CHAR(9)&"Monthly report"&CHAR(10))')
        self.assertEqual(ret['result'], 'Monthly report')
        self.assertEqual(ret['error'], None)
        ret = p.parse('CLEAN(B3)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('CLEAN(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')
        ret = p.parse('CLEAN(223)')
        self.assertEqual(ret['result'], '223')
        self.assertEqual(ret['error'], None)

    def test_concatenate(self):
        p = Parser(debug=True)
        ret = p.parse('CONCAT("The"," ","sun"," ","will"," ","come"," ","up"," ","tomorrow.")')
        self.assertEqual(ret['result'], 'The sun will come up tomorrow.')
        self.assertEqual(ret['error'], None)
        ret = p.parse('CONCAT(1/0, 14,"sun")')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')

    def test_len(self):
        p = Parser(debug=True)
        ret = p.parse('LEN("Phoenix, AZ")')
        self.assertEqual(ret['result'], 11)
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEN("     One   ")')
        self.assertEqual(ret['result'], 11)
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEN(B3)')
        self.assertEqual(ret['result'], 0)
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEN(3)')
        self.assertEqual(ret['result'], 1)
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEN(223)')
        self.assertEqual(ret['result'], 3)
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEN(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')


    def test_lower(self):
        p = Parser(debug=True)
        ret = p.parse('LOWER("aBcDe")')
        self.assertEqual(ret['result'], 'abcde')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LOWER(B3)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LOWER(223)')
        self.assertEqual(ret['result'], '223')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LOWER(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')

    def test_upper(self):
        p = Parser(debug=True)
        ret = p.parse('UPPER("aBcDe")')
        self.assertEqual(ret['result'], 'ABCDE')
        self.assertEqual(ret['error'], None)
        ret = p.parse('UPPER(B3)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('UPPER(223)')
        self.assertEqual(ret['result'], '223')
        self.assertEqual(ret['error'], None)
        ret = p.parse('UPPER(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')

    def test_proper(self):
        p = Parser(debug=True)
        ret = p.parse('PROPER("aBcDe")')
        self.assertEqual(ret['result'], 'Abcde')
        self.assertEqual(ret['error'], None)
        ret = p.parse('PROPER("76budGet")')
        self.assertEqual(ret['result'], '76Budget')
        self.assertEqual(ret['error'], None)
        ret = p.parse('PROPER(B3)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('PROPER(223)')
        self.assertEqual(ret['result'], '223')
        self.assertEqual(ret['error'], None)
        ret = p.parse('PROPER(1/0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#DIV/0!')

    def test_substitute(self):
        p = Parser(debug=True)
        ret = p.parse('SUBSTITUTE("ccc", "a", "b")')
        self.assertEqual(ret['result'], 'ccc')
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ccc", "a", "b", 2)')
        self.assertEqual(ret['result'], 'ccc')
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "a", "b")')
        self.assertEqual(ret['result'], "olb b todos e todbs bs meninbs e os meninos")
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "a", "b", 2)')
        self.assertEqual(ret['result'], "ola b todos e todas as meninas e os meninos")
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "a", "b", 0)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "os", "a", 3)')
        self.assertEqual(ret['result'], "ola a todos e todas as meninas e os menina")
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "os", "a", 2)')
        self.assertEqual(ret['result'], "ola a todos e todas as meninas e a meninos")
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE("ola a todos e todas as meninas e os meninos", "a", "b", "a")')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('SUBSTITUTE(, "a", "b", "a")')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('SUBSTITUTE(;;)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], None)
        ret = p.parse('SUBSTITUTE(;;;)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')

    def test_textjoin(self):
        p = Parser(debug=True)
        ret = p.parse('TEXTJOIN(";", TRUE, {"1";"2";"3"})')
        self.assertEqual(ret['result'], '1;2;3')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXTJOIN(";", TRUE, {"1",,"2","3"})')
        self.assertEqual(ret['result'], '1;2;3')
        ret = p.parse('TEXTJOIN(";", FALSE, {"1",,"2","3"})')
        self.assertEqual(ret['result'], '1;;2;3')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXTJOIN(1, FALSE, {"1",,"2","3"})')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')

    def test_left(self):
        p = Parser(debug=True)
        ret = p.parse('LEFT("Sale Price", 4)')
        self.assertEqual(ret['result'], 'Sale')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFT("Sweeden")')
        self.assertEqual(ret['result'], 'S')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFT("Sale Price", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('LEFT("Sale Price", 400)')
        self.assertEqual(ret['result'], 'Sale Price')
        self.assertEqual(ret['error'], None)

    def test_right(self):
        p = Parser(debug=True)
        ret = p.parse('RIGHT("Sale Price", 5)')
        self.assertEqual(ret['result'], 'Price')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHT("Stock Number")')
        self.assertEqual(ret['result'], 'r')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHT("Sale Price", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('RIGHT("Sale Price", 400)')
        self.assertEqual(ret['result'], 'Sale Price')
        self.assertEqual(ret['error'], None)

    def test_mid(self):
        p = Parser(debug=True)
        ret = p.parse('MID("Fluid Flow", 1, 5)')
        self.assertEqual(ret['result'], 'Fluid')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MID("Fluid Flow", 7, 20)')
        self.assertEqual(ret['result'], 'Flow')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MID("Fluid Flow", 20, 5)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MID("Fluid Flow", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')


    def test_leftb(self):
        p = Parser(debug=True)
        ret = p.parse('LEFTB("Sale Price", 4)')
        self.assertEqual(ret['result'], 'Sale')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFTB("Sweeden")')
        self.assertEqual(ret['result'], 'S')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFTB("Sale Price", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('LEFTB("Sale Price", 400)')
        self.assertEqual(ret['result'], 'Sale Price')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFTB("ㅍa", 1)')
        self.assertEqual(ret['result'], 'ㅍ')
        self.assertEqual(ret['error'], None)
        ret = p.parse('LEFTB("aㅍ", 1)')
        self.assertEqual(ret['result'], 'a')
        self.assertEqual(ret['error'], None)

    def test_rightb(self):
        p = Parser(debug=True)
        ret = p.parse('RIGHTB("Sale Price", 5)')
        self.assertEqual(ret['result'], 'Price')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHTB("Stock Number")')
        self.assertEqual(ret['result'], 'r')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHTB("Sale Price", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('RIGHTB("Sale Price", 400)')
        self.assertEqual(ret['result'], 'Sale Price')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHTB("aㅍ", 1)')
        self.assertEqual(ret['result'], 'ㅍ')
        self.assertEqual(ret['error'], None)
        ret = p.parse('RIGHTB("ㅍa", 1)')
        self.assertEqual(ret['result'], 'a')
        self.assertEqual(ret['error'], None)

    def test_midb(self):
        p = Parser(debug=True)
        ret = p.parse('MIDB("Fluid Flow", 1, 5)')
        self.assertEqual(ret['result'], 'Fluid')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MIDB("Fluid Flow", 7, 20)')
        self.assertEqual(ret['result'], 'Flow')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MIDB("Fluid Flow", 20, 5)')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MIDB("Fluid Flow", -1)')
        self.assertEqual(ret['result'], None)
        self.assertEqual(ret['error'], '#VALUE!')
        ret = p.parse('MIDB("aㅍa", 2, 2)')
        self.assertEqual(ret['result'], 'ㅍa')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MIDB("aㅍa", 1, 2)')
        self.assertEqual(ret['result'], 'aㅍ')
        self.assertEqual(ret['error'], None)
        ret = p.parse('MIDB("aㅍa", 2, 1)')
        self.assertEqual(ret['result'], 'ㅍ')
        self.assertEqual(ret['error'], None)

    def test_text(self):
        p = Parser(debug=True)
        ret = p.parse('TEXT(100.25,"???/???")')
        self.assertEqual(ret['result'], '401/4')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2024,4,3),"yyyy")')
        self.assertEqual(ret['result'], '2024')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"yy")')
        self.assertEqual(ret['result'], '04')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"mmmmm")')
        self.assertEqual(ret['result'], 'A')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"mmmm")')
        self.assertEqual(ret['result'], 'April')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"mmm")')
        self.assertEqual(ret['result'], 'Apr')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"mm")')
        self.assertEqual(ret['result'], '04')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"m")')
        self.assertEqual(ret['result'], '4')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"dddd")')
        self.assertEqual(ret['result'], 'Saturday')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"ddd")')
        self.assertEqual(ret['result'], 'Sat')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"dd")')
        self.assertEqual(ret['result'], '03')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"d")')
        self.assertEqual(ret['result'], '3')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"dd-mm-yyy")')
        self.assertEqual(ret['result'], '03-04-2004')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"dddd, mmmm dd")')
        self.assertEqual(ret['result'], 'Saturday, April 03')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"ddd, mmm d")')
        self.assertEqual(ret['result'], 'Sat, Apr 3')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(DATE(2004,4,3),"mmmmm yy")')
        self.assertEqual(ret['result'], 'A 04')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(100,"$#,##0")')
        self.assertEqual(ret['result'], '$100')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(100,"#,##0€")')
        self.assertEqual(ret['result'], '100€')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(0.85,"0%")')
        self.assertEqual(ret['result'], '85%')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(0.85,"0")')
        self.assertEqual(ret['result'], '1')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(0.5,"0")')
        self.assertEqual(ret['result'], '1')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(0.4,"0")')
        self.assertEqual(ret['result'], '0')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(3.141592654,"0.000")')
        self.assertEqual(ret['result'], '3.142')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(25000000000,"0.0E+00")')
        self.assertEqual(ret['result'], '2.5E+10')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(8.9,"#.000")')
        self.assertEqual(ret['result'], '8.900')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(.631,"0.#")')
        self.assertEqual(ret['result'], '0.6')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(1234.568,"#.0#")')
        self.assertEqual(ret['result'], '1234.57')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(1234.59,"####.#")')
        self.assertEqual(ret['result'], '1234.6')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(8.9, "#.000")')
        self.assertEqual(ret['result'], "8.900")
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(.631, "0.#")')
        self.assertEqual(ret['result'], "0.6")
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(1234.568, "#.0#")')
        self.assertEqual(ret['result'], "1234.57")
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(12, "#.0#")')
        self.assertEqual(ret['result'], "12.00")
        self.assertEqual(ret['error'], None)
        ret = p.parse('TEXT(5.25, "# ???/???")')
        self.assertEqual(ret['result'], "5 1/4")
        self.assertEqual(ret['error'], None)

    def test_trim(self):
        p = Parser(debug=True)
        ret = p.parse('TRIM(" test ")')
        self.assertEqual(ret['result'], 'test')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TRIM(" test   3 spaces later")')
        self.assertEqual(ret['result'], 'test 3 spaces later')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TRIM("     ")')
        self.assertEqual(ret['result'], '')
        self.assertEqual(ret['error'], None)
        ret = p.parse('TRIM(3.14)')
        self.assertEqual(ret['result'], 3.14)
        self.assertEqual(ret['error'], None)
