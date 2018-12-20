import re

# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*	匹配0个或多个的表达式。
# re+	匹配1个或多个的表达式。
# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}
# re{ n,}	精确匹配n个前面表达式。
# re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	匹配a或b
# (re)	G匹配括号内的表达式，也表示一个组
# (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)	类似 (...), 但是不表示一个组
# (?imx: re)	在括号中使用i, m, 或 x 可选标志
# (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
# (?#...)	注释.
# (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。
# 但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
# (?> re)	匹配的独立模式，省去回溯。
# \w	匹配字母数字
# \W	匹配非字母数字
# \s	匹配任意空白字符，等价于 [\t\n\r\f].
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9].
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置。
# \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等.	匹配一个换行符。匹配一个制表符。等
# \1...\9	匹配第n个分组的内容。
# \10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。


# +表示必须至少匹配到一个*表示不匹配到也可以，后边？表示懒惰模式

# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
line = "Cats are smarter than dogs"
matchObj = re.match( '(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
print('-----------------------------------------')

matchObj = re.match( 'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
matchObj = re.search( 'dogs', line, re.M|re.I)
if matchObj:
   print ("search --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")
print('-----------------------------------------')

# re.search扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
print('-----------------------------------------')

# d+表示数字结尾
# Python中字符串前面加上 r 表示原生字符串
content = "Extra things hello 123455 World_this is 899 a regex Demo extra things"
content = re.sub('(\d+)',r'\1 8',content)
print(content)
print('-----------------------------------------')

html = ''''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))
print('-----------------------------------------')

result = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result.group(1),result.group(2))
print('-----------------------------------------')

result = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print('-----------------------------------------')

# 匹配出全部歌名
# \s意味后边有换行符，*表示一个或者多个
partten = re.compile('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',re.S)
result = re.findall(partten,html)
print(result)
print('-----------------------------------------')
for a in result:
   print(a[1])

print('-----------------------------------------')
result = re.sub('<a.*?>|</a>','',html)
print(result)
print('-----------------------------------------')
result = re.findall('<li.*?>(.*?)</li>',result,re.S)
print(result)
print('-----------------------------------------')
for a in result:
   # s.strip(rm)删除s字符串中开头、结尾处，位于rm删除序列的字符,
   # 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')
   print(a.strip())
print('-----------------------------------------')
