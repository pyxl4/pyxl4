# coding: pyxl

from pyxl import html

def test_no_filter():
    children = <div><p>One</p><p>Two</p></div>.children()
    assert len(children) == 2
    assert str(children[0]) == '<p>One</p>'
    assert str(children[1]) == '<p>Two</p>'

def test_class_filter():
    div = <div><p class="yo">Hi</p><p>No</p><p class="yo">ho</p></div>
    children = div.children(selector='.yo')
    assert len(children) == 2
    assert str(children[0]) == '<p class="yo">Hi</p>'
    assert str(children[1]) == '<p class="yo">ho</p>'

def test_id_filter():
    div = <div><p id="yo">Hi</p><p>No</p><p id="ho">ho</p></div>
    children = div.children(selector='#yo')
    assert len(children) == 1
    assert str(children[0]) == '<p id="yo">Hi</p>'

def test_tag_filter():
    div = <div><div><p>Yo</p></div><p>Hi</p></div>
    children = div.children('p')
    assert len(children) == 1
    assert str(children[0]) == '<p>Hi</p>'

def test_filter_negation():
    div = <div><p class="yo">Hi</p><p>No</p><p class="ho">ho</p></div>
    children = div.children(selector='.yo', exclude=True)
    assert len(children) == 2
    assert str(children[0]) == '<p>No</p>'
    assert str(children[1]) == '<p class="ho">ho</p>'
