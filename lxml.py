"""
在指定div元素后插入div
"""
import lxml.etree as ET

content='''\
<div id="contents">
    <div id="content_nav">
        something goes here
    </div>
    <p>
        some contents
    </p>   
</div>
'''
tree = ET.fromstring(content, parser=ET.HTMLParser())
contentnav = tree.find(".//div[@id='content_nav']")
contentdiv = contentnav.getparent()
contentdiv.insert(contentdiv.index(contentnav)+1,
                  ET.XML("<div style='clear: both'></div>"))
print(ET.tostring(tree))


'''
An etree element has two methods: addprevious and addnext for doing exactly what you want.
'''
import lxml.etree as ET

content='''\
<div id="contents">
    <div id="content_nav">
        something goes here
    </div>
    <p>
        some contents
    </p>   
</div>
'''
tree = ET.fromstring(content, parser=ET.HTMLParser())
contentnav = tree.find(".//div[@id='content_nav']")
contentnav.addnext(ET.XML("<div style='clear: both'></div>"))
print(ET.tostring(tree))

def insert_after(element, new_element):
    parent = element.getparent()
    parent.insert(parent.index(element)+1, new_element)
