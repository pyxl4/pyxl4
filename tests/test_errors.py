# coding: pyxl
import pytest

from pyxl.codec.register import pyxl_decode
from pyxl.codec.parser import ParseError
from pyxl.codec.html_tokenizer import BadCharError

def test_malformed_if():
    with pytest.raises(ParseError):
        pyxl_decode(b"""
            <frag>
                <if cond="{true}">foo</if>
                this is incorrect!
                <else>bar</else>
            </frag>""")

def test_multiple_else():
    with pytest.raises(ParseError):
        pyxl_decode(b"""
            <frag>
                <if cond="{true}">foo</if>
                <else>bar</else>
                <else>baz</else>
             </frag>""")

def test_nested_else():
    with pytest.raises(ParseError):
        pyxl_decode(b"""
            <frag>
                <if cond="{true}">foo</if>
                <else><else>bar</else></else>
            </frag>""")

def test_bad_char1():
    with pytest.raises(BadCharError):
        pyxl_decode(b'<_bad_element></lm>')

def test_bad_char2():
    with pytest.raises(BadCharError):
        pyxl_decode(b'<div class="foo"=></div>')
