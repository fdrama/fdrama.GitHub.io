---
title: permission
tags: [文件权限,linux]
categories: linux
---

## 文件权限

Linux 文件权限分为三类：

r (read)：可讀取此一檔案的實際內容，如讀取文字檔的文字內容等；
w (write)：可以編輯、新增或者是修改該檔案的內容(但不含刪除該檔案)；
x (eXecute)：該檔案具有可以被系統執行的權限。

文件权限的表示方法：

drwxr-xr-x

第一个字符代表文件类型，d表示目录，-表示文件，l表示链接文件。

接下来的三个字符为一组，分别表示文件所有者、文件所属组、其他用户的权限。

rwxr-xr-x

rwx：文件所有者的权限，可读、可写、可执行。

r-x：文件所属组的权限，可读、不可写、可执行。

r-x：其他用户的权限，可读、不可写、可执行。

文件用户也有三类：文件所有者(owner)、文件所属组(group)、其他用户(others)。

## 文件权限的修改方法

`chgrp` ：改變檔案所屬群組
`chown` ：改變檔案擁有者
`chmod` ：改變檔案的權限, SUID, SGID, SBIT等等的特性

### chgrp

`chgrp [-R] group filename`

`-R` : 递归更改文件属组，就是在更改某个目录文件的属组时，如果加上-R的参数，那么该目录下的所有文件的属组都会更改。

`group` : 指定新的文件属组，必须是已经存在的文件属组名称。 /etc/group

`filename` : 指定要更改属组的文件列表(可以为目录)。

### chown

`chown [-R] user[:group] filename`

`-R` : 递归更改文件属主，就是在更改某个目录文件的属主时，如果加上-R的参数，那么该目录下的所有文件的属主都会更改。

### chmod

`chmod [-R] xyz filename`

`-R` : 递归更改文件权限，就是在更改某个目录文件的权限时，如果加上-R的参数，那么该目录下的所有文件的权限都会更改。

`xyz` : 权限组合，各个权限用数字来表示，r=4，w=2，x=1，所以当要rwx的时候，4+2+1=7，要rw-的时候，4+2=6，要r-x的时候，4+1=5。

<table class="news" style="width: 85%" background-color=yellow>
    <tr style="text-align:center">
    <td>chmod</td><td>u<br>g<br>o<br>a</td>
    <td style="font: 11pt '細明體'">+(加入)<br>-(除去)<br>=(設定)</td>
    <td>r<br>w<br>x</td>
    <td>文件或者目录</td></tr>
</table>

多种方法组合使用，可以单独设置某一类用户的权限，也可以同时设置多个类别的用户权限，可以通过字母或者数字来设置权限，

#### 数字类型修改权限

```bash
chmod 777 filename # 所有用户都有读、写、执行权限 rwxrwxrwx
chmod -R 754 dirname # 递归修改目录下所有文件的权限  rwxr-xr-- 用户：读、写、执行 组：读、执行 其他：读

```

#### 符号类型修改权限

```bash
chmod  u=rwx,go=rx  .bashrc
chmod  a+x  .bashrc
```