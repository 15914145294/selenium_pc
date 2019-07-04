# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     xpath
   Description :
   Author :       Administrator
   date：          2019/7/4 0004
-------------------------------------------------
"""
"""
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>

/ 从根节点选择
// 从匹配节点的当前节点选择文档中的节点，而不考虑他们的位置
. 当前节点
.. 当前节点的父节点
@ 选择属性
谓语：谓语用来查找某个特定的节点或者包含某个指定的值的节点。
/bookstore/book[1]  选择bookstore的第一个子元素
/bookstore/book[last()] 选择bookstore的最后子元素
/bookstore/book[last()-1] 选择bookstore的倒数第二个子元素
/bookstore/book[position()<3] 选择bookstore的最前面两个子元素
//title[@lang] 选择所有属性为lang的title节点
/bookstore/book[price>35]  选择bookstore的book子元素 其中price 大于35
//title[@lang='eng'] 选择所有属性lang的值为eng的title元素
/bookstore/book[price>35]/title 选择bookstore的title子元素 其中price 大于35

选择未知节点
* 匹配任何元素节点
	/bookstore/* 选择bookstore的所有子元素
	//* 选择文档中的所有元素
*@ 匹配任何属性节点
	//title[*@] 选取所有带有属性的 title 元素
node() 匹配任何节点类型

选取若干路径
/bookstore/book/title | //price  ：选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素

***********************xpath轴*********************************
ancestor 选择当前节点的所有先辈
ancestor-or-self 选择当前节点的所有先辈及节点本身
attribute 当前节点的属性
child 当前节点的所有子元素
descendant 选取当前节点的所有后代元素（子、孙等）
descendant-or-self 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 选取文档中当前节点的结束标签之后的所有节点。
namespace  选取当前节点的所有命名空间节点
parent  选取当前节点的父节点。
preceding  选取文档中当前节点的开始标签之前的所有节点
preceding-sibling 选取当前节点之前的所有同级节点
self  选取当前节点

位置路径表达式
绝对路径位置：/step/step/...
相对位置路径：step/step/...

child::book 当前元素的子元素book
attribute:lang 选取当前节点的 lang 属性。
child::* 当前节点的所有子元素
attribute::*当前节点的所有属性
child::test() 选取当前节点的所有文本子节点。
child::node() 当前元素的所有子节点
descendant::book	选取当前节点的所有 book 后代。
ancestor::book	选择当前节点的所有 book 先辈。
ancestor-or-self::book	选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
child::*/child::price	选取当前节点的所有 price 孙节点。

XPath 运算符
下面列出了可用在 XPath 表达式中的运算符：

运算符	描述	实例	返回值
|	计算两个节点集	//book | //cd	返回所有拥有 book 和 cd 元素的节点集
+	加法	6 + 4	10
-	减法	6 - 4	2
*	乘法	6 * 4	24
div	除法	8 div 4	2
=	等于	price=9.80	如果 price 是 9.80，则返回 true。如果 price 是 9.90，则返回 false。

!=	不等于	price!=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。

<	小于	price<9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。

<=	小于或等于	price<=9.80	如果 price 是 9.00，则返回 true。如果 price 是 9.90，则返回 false。

>	大于	price>9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.80，则返回 false。

>=	大于或等于	price>=9.80	如果 price 是 9.90，则返回 true。如果 price 是 9.70，则返回 false。

or	或	price=9.80 or price=9.70	如果 price 是 9.80，则返回 true。如果 price 是 9.50，则返回 false。

and	与	price>9.00 and price<9.90	如果 price 是 9.80，则返回 true。如果 price 是 8.50，则返回 false。

mod	计算除法的余数	5 mod 2	1

# element =driver.find_element_by_xpath("//input[@id='kw']/preceding-sibling::span")
# element =driver.find_element_by_xpath("//input[@id='kw']/parent::*/parent::*")
# elements =driver.find_elements_by_xpath("//input[@id='kw']/ancestor::*")
element =driver.find_element_by_xpath("//*[@id='form']/")
print(element)
# for x in element:
# 	print(x.tag_name)
# driver.find_element_by_xpath("//*[@id='su']").click()
# driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()

"""
