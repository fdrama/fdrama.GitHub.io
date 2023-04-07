---
title: 计算机中的二进制-文字
tags: [binary, math]
categories: 计算机原理
---


> 由于计算机的硬件决定，任何存储于计算机中的数据，其本质都是以二进制码存储的。

## 如何存储和展示字符

计算机的硬件由许多电子元器件组成，这些元器件都只能处理 0 和 1 这两种信号。因此，计算机中的所有数据都必须以 0 和 1 的形式表示，也就是二进制码。

例如，一个字符串 “hello” 在计算机中的存储形式是一串二进制码，而不是字符串本身。当我们在计算机中输入 “hello” 时，实际上计算机是在存储一串二进制码，而不是字符串本身。

所以，无论是文本数据、图像数据、音频数据还是其他类型的数据，都必须以二进制码的形式存储在计算机中。当我们在计算机中输入、处理或存储数据时，实际上计算机都是在处理二进制码。

计算机可以通过编码和解码的方式，将二进制码转换为我们能够理解的文本、图像、音频等数据。例如，当我们在计算机中输入一个字符串 “hello” 时，计算机会将其转换为相应的二进制码，并将其存储在内存中。当我们在计算机屏幕上看到 “hello” 这个字符串时，实际上计算机是将存储在内存中的二进制码解码为字符串，并将其显示在屏幕上。

### 字符编码

> 为了将文本表示为数字形式，需要构建一种系统来为每一个字母赋予一个唯一的编码。数字和标点符号也算做文本的一种形式，所有它们也必须拥有自己的编码。
> 简而言之，所有由符号所表示的字母和数字都需要编码。具备这种功能的系统被称为字符编码集，系统内每个独立的编码被称为字符编码（Character Codes）。

#### ASCII

计算机最重要的东西就是标准，所有人都遵循并使用的统一编码应运而生。ASCII码（American Standard Code for Information Interchange），从1967年正式公布至今，它一直是计算机产业中的最重要标准。无论何时，在计算机处理文本时，总会不经意间使用到ASCII码。

ASCII 码使用 7 位二进制数来表示每个字符，共计可以表示 128 个字符。

ASCII 码是最常用的字符编码之一，被广泛应用于计算机和通信领域。在计算机中，ASCII 码常用于存储、处理和传输文本数据。查看下表[^1]

其中：

0～31及127(共33个)是控制字符或通信专用字符（其余为可显示字符），如控制符：LF（换行）、CR（回车）、FF（换页）、DEL（删除）、BS（退格)、BEL（响铃）等；通信专用字符：SOH（文头）、EOT（文尾）、ACK（确认）等；ASCII值为8、9、10 和13 分别转换为退格、制表、换行和回车字符。它们并没有特定的图形显示，但会依不同的应用程序，而对文本显示有不同的影响 。

32～126(共95个)是字符（32是空格），其中48～57为0到9十个阿拉伯数字。

65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等。

ASCII 码是目前应用最广泛的字符编码之一，但是它也有一些局限性。在英语中，用128个符号编码便可以表示所有，但是用来表示其他语言，128个符号是不够的。
人们发明了更为先进的字符编码集: **Unicode**。

```diff
- 101101
+ 001111
-------
  0001101
```

#### Unicode

### 字体、字形

## 参考资料

1. [Ascii](https://ascii.org.cn/)
2. &laquo;隐匿在计算机软硬件背后的语言&raquo;

[^1]:
<table>
    <tr>
        <td>Bin
(二进制)
</td>
        <td>Oct
(八进制)
</td>
        <td>Dec
(十进制)
</td>
        <td>Hex
(十六进制)
</td>
        <td>缩写/字符
</td>
        <td>解释
</td>
    </tr>
    <tr>
        <td>0000 0000</td>
        <td>00</td>
        <td>0</td>
        <td>0x00</td>
        <td>NUL(null)</td>
        <td>空字符</td>
    </tr>
    <tr>
        <td>0000 0001</td>
        <td>01</td>
        <td>1</td>
        <td>0x01</td>
        <td>SOH(start of headline)</td>
        <td>标题开始</td>
    </tr>
    <tr>
        <td>0000 0010</td>
        <td>02</td>
        <td>2</td>
        <td>0x02</td>
        <td>STX (start of text)</td>
        <td>正文开始</td>
    </tr>
    <tr>
        <td>0000 0011</td>
        <td>03</td>
        <td>3</td>
        <td>0x03</td>
        <td>ETX (end of text)</td>
        <td>正文结束</td>
    </tr>
    <tr>
        <td>0000 0100</td>
        <td>04</td>
        <td>4</td>
        <td>0x04</td>
        <td>EOT (end of transmission)</td>
        <td>传输结束</td>
    </tr>
    <tr>
        <td>0000 0101</td>
        <td>05</td>
        <td>5</td>
        <td>0x05</td>
        <td>ENQ (enquiry)</td>
        <td>请求</td>
    </tr>
    <tr>
        <td>0000 0110</td>
        <td>06</td>
        <td>6</td>
        <td>0x06</td>
        <td>ACK (acknowledge)</td>
        <td>收到通知</td>
    </tr>
    <tr>
        <td>0000 0111</td>
        <td>07</td>
        <td>7</td>
        <td>0x07</td>
        <td>BEL (bell)</td>
        <td>响铃</td>
    </tr>
    <tr>
        <td>0000 1000</td>
        <td>010</td>
        <td>8</td>
        <td>0x08</td>
        <td>BS (backspace)</td>
        <td>退格</td>
    </tr>
    <tr>
        <td>0000 1001</td>
        <td>011</td>
        <td>9</td>
        <td>0x09</td>
        <td>HT (horizontal tab)</td>
        <td>水平制表符</td>
    </tr>
    <tr>
        <td>0000 1010</td>
        <td>012</td>
        <td>10</td>
        <td>0x0A</td>
        <td>LF (NL line feed, new line)</td>
        <td>换行键</td>
    </tr>
    <tr>
        <td>0000 1011</td>
        <td>013</td>
        <td>11</td>
        <td>0x0B</td>
        <td>VT (vertical tab)</td>
        <td>垂直制表符</td>
    </tr>
    <tr>
        <td>0000 1100</td>
        <td>014</td>
        <td>12</td>
        <td>0x0C</td>
        <td>FF (NP form feed, new page)</td>
        <td>换页键</td>
    </tr>
    <tr>
        <td>0000 1101</td>
        <td>015</td>
        <td>13</td>
        <td>0x0D</td>
        <td>CR (carriage return)</td>
        <td>回车键</td>
    </tr>
    <tr>
        <td>0000 1110</td>
        <td>016</td>
        <td>14</td>
        <td>0x0E</td>
        <td>SO (shift out)</td>
        <td>不用切换</td>
    </tr>
    <tr>
        <td>0000 1111</td>
        <td>017</td>
        <td>15</td>
        <td>0x0F</td>
        <td>SI (shift in)</td>
        <td>启用切换</td>
    </tr>
    <tr>
        <td>0001 0000</td>
        <td>020</td>
        <td>16</td>
        <td>0x10</td>
        <td>DLE (data link escape)</td>
        <td>数据链路转义</td>
    </tr>
    <tr>
        <td>0001 0001</td>
        <td>021</td>
        <td>17</td>
        <td>0x11</td>
        <td>DC1 (device control 1)</td>
        <td>设备控制1</td>
    </tr>
    <tr>
        <td>0001 0010</td>
        <td>022</td>
        <td>18</td>
        <td>0x12</td>
        <td>DC2 (device control 2)</td>
        <td>设备控制2</td>
    </tr>
    <tr>
        <td>0001 0011</td>
        <td>023</td>
        <td>19</td>
        <td>0x13</td>
        <td>DC3 (device control 3)</td>
        <td>设备控制3</td>
    </tr>
    <tr>
        <td>0001 0100</td>
        <td>024</td>
        <td>20</td>
        <td>0x14</td>
        <td>DC4 (device control 4)</td>
        <td>设备控制4</td>
    </tr>
    <tr>
        <td>0001 0101</td>
        <td>025</td>
        <td>21</td>
        <td>0x15</td>
        <td>NAK (negative acknowledge)</td>
        <td>拒绝接收</td>
    </tr>
    <tr>
        <td>0001 0110</td>
        <td>026</td>
        <td>22</td>
        <td>0x16</td>
        <td>SYN (synchronous idle)</td>
        <td>同步空闲</td>
    </tr>
    <tr>
        <td>0001 0111</td>
        <td>027</td>
        <td>23</td>
        <td>0x17</td>
        <td>ETB (end of trans. block)</td>
        <td>结束传输块</td>
    </tr>
    <tr>
        <td>0001 1000</td>
        <td>030</td>
        <td>24</td>
        <td>0x18</td>
        <td>CAN (cancel)</td>
        <td>取消</td>
    </tr>
    <tr>
        <td>0001 1001</td>
        <td>031</td>
        <td>25</td>
        <td>0x19</td>
        <td>EM (end of medium)</td>
        <td>媒介结束</td>
    </tr>
    <tr>
        <td>0001 1010</td>
        <td>032</td>
        <td>26</td>
        <td>0x1A</td>
        <td>SUB (substitute)</td>
        <td>代替</td>
    </tr>
    <tr>
        <td>0001 1011</td>
        <td>033</td>
        <td>27</td>
        <td>0x1B</td>
        <td>ESC (escape)</td>
        <td>换码(溢出)</td>
    </tr>
    <tr>
        <td>0001 1100</td>
        <td>034</td>
        <td>28</td>
        <td>0x1C</td>
        <td>FS (file separator)</td>
        <td>文件分隔符</td>
    </tr>
    <tr>
        <td>0001 1101</td>
        <td>035</td>
        <td>29</td>
        <td>0x1D</td>
        <td>GS (group separator)</td>
        <td>分组符</td>
    </tr>
    <tr>
        <td>0001 1110</td>
        <td>036</td>
        <td>30</td>
        <td>0x1E</td>
        <td>RS (record separator)</td>
        <td>记录分隔符</td>
    </tr>
    <tr>
        <td>0001 1111</td>
        <td>037</td>
        <td>31</td>
        <td>0x1F</td>
        <td>US (unit separator)</td>
        <td>单元分隔符</td>
    </tr>
    <tr>
        <td>0010 0000</td>
        <td>040</td>
        <td>32</td>
        <td>0x20</td>
        <td>(space)</td>
        <td>空格</td>
    </tr>
    <tr>
        <td>0010 0001</td>
        <td>041</td>
        <td>33</td>
        <td>0x21</td>
        <td>!</td>
        <td>叹号</td>
    </tr>
    <tr>
        <td>0010 0010</td>
        <td>042</td>
        <td>34</td>
        <td>0x22</td>
        <td>"</td>
        <td>双引号</td>
    </tr>
    <tr>
        <td>0010 0011</td>
        <td>043</td>
        <td>35</td>
        <td>0x23</td>
        <td>#</td>
        <td>井号</td>
    </tr>
    <tr>
        <td>0010 0100</td>
        <td>044</td>
        <td>36</td>
        <td>0x24</td>
        <td>$</td>
        <td>美元符</td>
    </tr>
    <tr>
        <td>0010 0101</td>
        <td>045</td>
        <td>37</td>
        <td>0x25</td>
        <td>%</td>
        <td>百分号</td>
    </tr>
    <tr>
        <td>0010 0110</td>
        <td>046</td>
        <td>38</td>
        <td>0x26</td>
        <td>&amp;amp;</td>
        <td>和号</td>
    </tr>
    <tr>
        <td>0010 0111</td>
        <td>047</td>
        <td>39</td>
        <td>0x27</td>
        <td>'</td>
        <td>闭单引号</td>
    </tr>
    <tr>
        <td>0010 1000</td>
        <td>050</td>
        <td>40</td>
        <td>0x28</td>
        <td>(</td>
        <td>开括号</td>
    </tr>
    <tr>
        <td>0010 1001</td>
        <td>051</td>
        <td>41</td>
        <td>0x29</td>
        <td>)</td>
        <td>闭括号</td>
    </tr>
    <tr>
        <td>0010 1010</td>
        <td>052</td>
        <td>42</td>
        <td>0x2A</td>
        <td>*</td>
        <td>星号</td>
    </tr>
    <tr>
        <td>0010 1011</td>
        <td>053</td>
        <td>43</td>
        <td>0x2B</td>
        <td>+</td>
        <td>加号</td>
    </tr>
    <tr>
        <td>0010 1100</td>
        <td>054</td>
        <td>44</td>
        <td>0x2C</td>
        <td>,</td>
        <td>逗号</td>
    </tr>
    <tr>
        <td>0010 1101</td>
        <td>055</td>
        <td>45</td>
        <td>0x2D</td>
        <td>-</td>
        <td>减号/破折号</td>
    </tr>
    <tr>
        <td>0010 1110</td>
        <td>056</td>
        <td>46</td>
        <td>0x2E</td>
        <td>.</td>
        <td>句号</td>
    </tr>
    <tr>
        <td>0010 1111</td>
        <td>057</td>
        <td>47</td>
        <td>0x2F</td>
        <td>/</td>
        <td>斜杠</td>
    </tr>
    <tr>
        <td>0011 0000</td>
        <td>060</td>
        <td>48</td>
        <td>0x30</td>
        <td>0</td>
        <td>字符0</td>
    </tr>
    <tr>
        <td>0011 0001</td>
        <td>061</td>
        <td>49</td>
        <td>0x31</td>
        <td>1</td>
        <td>字符1</td>
    </tr>
    <tr>
        <td>0011 0010</td>
        <td>062</td>
        <td>50</td>
        <td>0x32</td>
        <td>2</td>
        <td>字符2</td>
    </tr>
    <tr>
        <td>0011 0011</td>
        <td>063</td>
        <td>51</td>
        <td>0x33</td>
        <td>3</td>
        <td>字符3</td>
    </tr>
    <tr>
        <td>0011 0100</td>
        <td>064</td>
        <td>52</td>
        <td>0x34</td>
        <td>4</td>
        <td>字符4</td>
    </tr>
    <tr>
        <td>0011 0101</td>
        <td>065</td>
        <td>53</td>
        <td>0x35</td>
        <td>5</td>
        <td>字符5</td>
    </tr>
    <tr>
        <td>0011 0110</td>
        <td>066</td>
        <td>54</td>
        <td>0x36</td>
        <td>6</td>
        <td>字符6</td>
    </tr>
    <tr>
        <td>0011 0111</td>
        <td>067</td>
        <td>55</td>
        <td>0x37</td>
        <td>7</td>
        <td>字符7</td>
    </tr>
    <tr>
        <td>0011 1000</td>
        <td>070</td>
        <td>56</td>
        <td>0x38</td>
        <td>8</td>
        <td>字符8</td>
    </tr>
    <tr>
        <td>0011 1001</td>
        <td>071</td>
        <td>57</td>
        <td>0x39</td>
        <td>9</td>
        <td>字符9</td>
    </tr>
    <tr>
        <td>0011 1010</td>
        <td>072</td>
        <td>58</td>
        <td>0x3A</td>
        <td>:</td>
        <td>冒号</td>
    </tr>
    <tr>
        <td>0011 1011</td>
        <td>073</td>
        <td>59</td>
        <td>0x3B</td>
        <td>;</td>
        <td>分号</td>
    </tr>
    <tr>
        <td>0011 1100</td>
        <td>074</td>
        <td>60</td>
        <td>0x3C</td>
        <td>&amp;lt;</td>
        <td>小于</td>
    </tr>
    <tr>
        <td>0011 1101</td>
        <td>075</td>
        <td>61</td>
        <td>0x3D</td>
        <td>=</td>
        <td>等号</td>
    </tr>
    <tr>
        <td>0011 1110</td>
        <td>076</td>
        <td>62</td>
        <td>0x3E</td>
        <td>&amp;gt;</td>
        <td>大于</td>
    </tr>
    <tr>
        <td>0011 1111</td>
        <td>077</td>
        <td>63</td>
        <td>0x3F</td>
        <td>?</td>
        <td>问号</td>
    </tr>
    <tr>
        <td>0100 0000</td>
        <td>0100</td>
        <td>64</td>
        <td>0x40</td>
        <td>@</td>
        <td>电子邮件符号</td>
    </tr>
    <tr>
        <td>0100 0001</td>
        <td>0101</td>
        <td>65</td>
        <td>0x41</td>
        <td>A</td>
        <td>大写字母A</td>
    </tr>
    <tr>
        <td>0100 0010</td>
        <td>0102</td>
        <td>66</td>
        <td>0x42</td>
        <td>B</td>
        <td>大写字母B</td>
    </tr>
    <tr>
        <td>0100 0011</td>
        <td>0103</td>
        <td>67</td>
        <td>0x43</td>
        <td>C</td>
        <td>大写字母C</td>
    </tr>
    <tr>
        <td>0100 0100</td>
        <td>0104</td>
        <td>68</td>
        <td>0x44</td>
        <td>D</td>
        <td>大写字母D</td>
    </tr>
    <tr>
        <td>0100 0101</td>
        <td>0105</td>
        <td>69</td>
        <td>0x45</td>
        <td>E</td>
        <td>大写字母E</td>
    </tr>
    <tr>
        <td>0100 0110</td>
        <td>0106</td>
        <td>70</td>
        <td>0x46</td>
        <td>F</td>
        <td>大写字母F</td>
    </tr>
    <tr>
        <td>0100 0111</td>
        <td>0107</td>
        <td>71</td>
        <td>0x47</td>
        <td>G</td>
        <td>大写字母G</td>
    </tr>
    <tr>
        <td>0100 1000</td>
        <td>0110</td>
        <td>72</td>
        <td>0x48</td>
        <td>H</td>
        <td>大写字母H</td>
    </tr>
    <tr>
        <td>0100 1001</td>
        <td>0111</td>
        <td>73</td>
        <td>0x49</td>
        <td>I</td>
        <td>大写字母I</td>
    </tr>
    <tr>
        <td>01001010</td>
        <td>0112</td>
        <td>74</td>
        <td>0x4A</td>
        <td>J</td>
        <td>大写字母J</td>
    </tr>
    <tr>
        <td>0100 1011</td>
        <td>0113</td>
        <td>75</td>
        <td>0x4B</td>
        <td>K</td>
        <td>大写字母K</td>
    </tr>
    <tr>
        <td>0100 1100</td>
        <td>0114</td>
        <td>76</td>
        <td>0x4C</td>
        <td>L</td>
        <td>大写字母L</td>
    </tr>
    <tr>
        <td>0100 1101</td>
        <td>0115</td>
        <td>77</td>
        <td>0x4D</td>
        <td>M</td>
        <td>大写字母M</td>
    </tr>
    <tr>
        <td>0100 1110</td>
        <td>0116</td>
        <td>78</td>
        <td>0x4E</td>
        <td>N</td>
        <td>大写字母N</td>
    </tr>
    <tr>
        <td>0100 1111</td>
        <td>0117</td>
        <td>79</td>
        <td>0x4F</td>
        <td>O</td>
        <td>大写字母O</td>
    </tr>
    <tr>
        <td>0101 0000</td>
        <td>0120</td>
        <td>80</td>
        <td>0x50</td>
        <td>P</td>
        <td>大写字母P</td>
    </tr>
    <tr>
        <td>0101 0001</td>
        <td>0121</td>
        <td>81</td>
        <td>0x51</td>
        <td>Q</td>
        <td>大写字母Q</td>
    </tr>
    <tr>
        <td>0101 0010</td>
        <td>0122</td>
        <td>82</td>
        <td>0x52</td>
        <td>R</td>
        <td>大写字母R</td>
    </tr>
    <tr>
        <td>0101 0011</td>
        <td>0123</td>
        <td>83</td>
        <td>0x53</td>
        <td>S</td>
        <td>大写字母S</td>
    </tr>
    <tr>
        <td>0101 0100</td>
        <td>0124</td>
        <td>84</td>
        <td>0x54</td>
        <td>T</td>
        <td>大写字母T</td>
    </tr>
    <tr>
        <td>0101 0101</td>
        <td>0125</td>
        <td>85</td>
        <td>0x55</td>
        <td>U</td>
        <td>大写字母U</td>
    </tr>
    <tr>
        <td>0101 0110</td>
        <td>0126</td>
        <td>86</td>
        <td>0x56</td>
        <td>V</td>
        <td>大写字母V</td>
    </tr>
    <tr>
        <td>0101 0111</td>
        <td>0127</td>
        <td>87</td>
        <td>0x57</td>
        <td>W</td>
        <td>大写字母W</td>
    </tr>
    <tr>
        <td>0101 1000</td>
        <td>0130</td>
        <td>88</td>
        <td>0x58</td>
        <td>X</td>
        <td>大写字母X</td>
    </tr>
    <tr>
        <td>0101 1001</td>
        <td>0131</td>
        <td>89</td>
        <td>0x59</td>
        <td>Y</td>
        <td>大写字母Y</td>
    </tr>
    <tr>
        <td>0101 1010</td>
        <td>0132</td>
        <td>90</td>
        <td>0x5A</td>
        <td>Z</td>
        <td>大写字母Z</td>
    </tr>
    <tr>
        <td>0101 1011</td>
        <td>0133</td>
        <td>91</td>
        <td>0x5B</td>
        <td>[</td>
        <td>开方括号</td>
    </tr>
    <tr>
        <td>0101 1100</td>
        <td>0134</td>
        <td>92</td>
        <td>0x5C</td>
        <td>\</td>
        <td>反斜杠</td>
    </tr>
    <tr>
        <td>0101 1101</td>
        <td>0135</td>
        <td>93</td>
        <td>0x5D</td>
        <td>]</td>
        <td>闭方括号</td>
    </tr>
    <tr>
        <td>0101 1110</td>
        <td>0136</td>
        <td>94</td>
        <td>0x5E</td>
        <td>^</td>
        <td>脱字符</td>
    </tr>
    <tr>
        <td>0101 1111</td>
        <td>0137</td>
        <td>95</td>
        <td>0x5F</td>
        <td>_</td>
        <td>下划线</td>
    </tr>
    <tr>
        <td>0110 0000</td>
        <td>0140</td>
        <td>96</td>
        <td>0x60</td>
        <td>`</td>
        <td>开单引号</td>
    </tr>
    <tr>
        <td>0110 0001</td>
        <td>0141</td>
        <td>97</td>
        <td>0x61</td>
        <td>a</td>
        <td>小写字母a</td>
    </tr>
    <tr>
        <td>0110 0010</td>
        <td>0142</td>
        <td>98</td>
        <td>0x62</td>
        <td>b</td>
        <td>小写字母b</td>
    </tr>
    <tr>
        <td>0110 0011</td>
        <td>0143</td>
        <td>99</td>
        <td>0x63</td>
        <td>c</td>
        <td>小写字母c</td>
    </tr>
    <tr>
        <td>0110 0100</td>
        <td>0144</td>
        <td>100</td>
        <td>0x64</td>
        <td>d</td>
        <td>小写字母d</td>
    </tr>
    <tr>
        <td>0110 0101</td>
        <td>0145</td>
        <td>101</td>
        <td>0x65</td>
        <td>e</td>
        <td>小写字母e</td>
    </tr>
    <tr>
        <td>0110 0110</td>
        <td>0146</td>
        <td>102</td>
        <td>0x66</td>
        <td>f</td>
        <td>小写字母f</td>
    </tr>
    <tr>
        <td>0110 0111</td>
        <td>0147</td>
        <td>103</td>
        <td>0x67</td>
        <td>g</td>
        <td>小写字母g</td>
    </tr>
    <tr>
        <td>0110 1000</td>
        <td>0150</td>
        <td>104</td>
        <td>0x68</td>
        <td>h</td>
        <td>小写字母h</td>
    </tr>
    <tr>
        <td>0110 1001</td>
        <td>0151</td>
        <td>105</td>
        <td>0x69</td>
        <td>i</td>
        <td>小写字母i</td>
    </tr>
    <tr>
        <td>0110 1010</td>
        <td>0152</td>
        <td>106</td>
        <td>0x6A</td>
        <td>j</td>
        <td>小写字母j</td>
    </tr>
    <tr>
        <td>0110 1011</td>
        <td>0153</td>
        <td>107</td>
        <td>0x6B</td>
        <td>k</td>
        <td>小写字母k</td>
    </tr>
    <tr>
        <td>0110 1100</td>
        <td>0154</td>
        <td>108</td>
        <td>0x6C</td>
        <td>l</td>
        <td>小写字母l</td>
    </tr>
    <tr>
        <td>0110 1101</td>
        <td>0155</td>
        <td>109</td>
        <td>0x6D</td>
        <td>m</td>
        <td>小写字母m</td>
    </tr>
    <tr>
        <td>0110 1110</td>
        <td>0156</td>
        <td>110</td>
        <td>0x6E</td>
        <td>n</td>
        <td>小写字母n</td>
    </tr>
    <tr>
        <td>0110 1111</td>
        <td>0157</td>
        <td>111</td>
        <td>0x6F</td>
        <td>o</td>
        <td>小写字母o</td>
    </tr>
    <tr>
        <td>0111 0000</td>
        <td>0160</td>
        <td>112</td>
        <td>0x70</td>
        <td>p</td>
        <td>小写字母p</td>
    </tr>
    <tr>
        <td>0111 0001</td>
        <td>0161</td>
        <td>113</td>
        <td>0x71</td>
        <td>q</td>
        <td>小写字母q</td>
    </tr>
    <tr>
        <td>0111 0010</td>
        <td>0162</td>
        <td>114</td>
        <td>0x72</td>
        <td>r</td>
        <td>小写字母r</td>
    </tr>
    <tr>
        <td>0111 0011</td>
        <td>0163</td>
        <td>115</td>
        <td>0x73</td>
        <td>s</td>
        <td>小写字母s</td>
    </tr>
    <tr>
        <td>0111 0100</td>
        <td>0164</td>
        <td>116</td>
        <td>0x74</td>
        <td>t</td>
        <td>小写字母t</td>
    </tr>
    <tr>
        <td>0111 0101</td>
        <td>0165</td>
        <td>117</td>
        <td>0x75</td>
        <td>u</td>
        <td>小写字母u</td>
    </tr>
    <tr>
        <td>0111 0110</td>
        <td>0166</td>
        <td>118</td>
        <td>0x76</td>
        <td>v</td>
        <td>小写字母v</td>
    </tr>
    <tr>
        <td>0111 0111</td>
        <td>0167</td>
        <td>119</td>
        <td>0x77</td>
        <td>w</td>
        <td>小写字母w</td>
    </tr>
    <tr>
        <td>0111 1000</td>
        <td>0170</td>
        <td>120</td>
        <td>0x78</td>
        <td>x</td>
        <td>小写字母x</td>
    </tr>
    <tr>
        <td>0111 1001</td>
        <td>0171</td>
        <td>121</td>
        <td>0x79</td>
        <td>y</td>
        <td>小写字母y</td>
    </tr>
    <tr>
        <td>0111 1010</td>
        <td>0172</td>
        <td>122</td>
        <td>0x7A</td>
        <td>z</td>
        <td>小写字母z</td>
    </tr>
    <tr>
        <td>0111 1011</td>
        <td>0173</td>
        <td>123</td>
        <td>0x7B</td>
        <td>{</td>
        <td>开花括号</td>
    </tr>
    <tr>
        <td>0111 1100</td>
        <td>0174</td>
        <td>124</td>
        <td>0x7C</td>
        <td>|</td>
        <td>垂线</td>
    </tr>
    <tr>
        <td>0111 1101</td>
        <td>0175</td>
        <td>125</td>
        <td>0x7D</td>
        <td>}</td>
        <td>闭花括号</td>
    </tr>
    <tr>
        <td>0111 1110</td>
        <td>0176</td>
        <td>126</td>
        <td>0x7E</td>
        <td>~</td>
        <td>波浪号</td>
    </tr>
    <tr>
        <td>0111 1111</td>
        <td>0177</td>
        <td>127</td>
        <td>0x7F</td>
        <td>DEL (delete)</td>
        <td>删除</td>
    </tr>
</table>