---
title: Hexo Guide
date: 2022-07-11 17:33:53
tags: [hexo, next]
categories: 指南
---

欢迎来到我的博客!
感谢[GithubPage](https://pages.github.com/) + [Hexo](https://hexo.io/zh-cn/) + [next](https://theme-next.js.org/)。
感谢开源世界，让搭建一个属于自己的博客变的十分便捷。我以后也会在这里分享关于编程和生活的一些东西。

以下是我个人搭建博客的步骤:

## Hexo

[Hexo](https://hexo.io/zh-cn/docs/) 是一个快速、简洁且高效的博客框架

### 安装

#### 前置准备

- 安装nodeJs并配置 (<http://nodejs.cn/learn/introduction-to-nodejs>)

    ```bash
    # 查看是否安装成功
    $ node -v 
    ```

- 安装Git并配置 `https://git-scm.com/`

    ```bash
    # 查看是否安装成功
    $ git --version
    ```

- 安装Hexo

    ```bash
    # 全局安装
    $ npm install -g hexo-cli

    # 局部安装
    $ npm install hexo

    # 命令执行 两种方式
      1. $ npx hexo <command>
    
    # Hexo 所在的目录下的 node_modules 添加到环境变量 直接使用 hexo <command> linux为例
      2. echo 'PATH="$PATH:./node_modules/.bin"' >> ~/.profile
    ```

#### 启动

1. 安装完hexo执行以下命令

    ```bash
    # 初始化 此folder 就是下面文档里的 ${hexo-site}
    $ hexo init <folder>
    $ cd <folder>
    $ npm install
    ```

2. 执行完成后目标文件夹的目录结构

    ```tree
    .
    ├── _config.yml
    ├── package.json
    ├── scaffolds
    ├── source
    |   ├── _drafts
    |   └── _posts
    └── themes
    ```

3. 运行*hexo server*访问 (<http://localhost:4000/>)

### 配置

#### 主题

hexo 有很多主题 这里已Next为例 Next(<https://theme-next.js.org/>)

1. 安装

    ```bash
    # 移动到hexo 安装目录
    $ cd hexo-site
    $ ls
    _config.yml  node_modules  package-lock.json  package.json  scaffolds  source  themes
    ```

   - npm安装

    ```bash
    $ npm install hexo-theme-next
    ```

   - git安装

    ```bash
    $ git clone https://github.com/next-theme/hexo-theme-next themes/next
    ```

2. 配置

    现在有两个配置文件 *_config.yml*， 一个是hexo的配置文件，一个是next主题的配置文件，不同的安装方式，所在的目录不同
    (e.g. thems/next/_config.yml or node_modules/hexo-theme-next/_config.yml.

    不推荐直接修改主题里面的文件, 因为npm升级或者git更新会覆盖文件，hexo建议将主题文件复制到根目录并且修改名称为 ***_config.[theme].yml***

    ```bash
    # Installed through npm
    $ cp node_modules/hexo-theme-next/_config.yml _config.next.yml
    # Installed through Git
    $ cp themes/next/_config.yml _config.next.yml
    ```

3. 修改配置文件 _config.yml

    ```yml
    title: Hexo config file
    theme: next
    ```

4. 启动hexo s 查看页面样式已经发生变化

#### 页面

##### 标签页

1. 生成标签页

    ```bash
    $ cd hexo-site
    $ hexo new page tags

    ```

2. 配置标签页

    修改生成的source/tags/index.md 指定type

    ```yml
    title: Tags
    date: 2014-12-22 12:39:04
    type: tags
    ---
    ```

3. 编辑菜单 *_config.next.yml*

   ```yml
    menu:
       home: / || fa fa-home
       archives: /archives/ || fa fa-archive
       tags: /tags/ || fa fa-tags

    
    tagcloud:
       # 标签的样式
       min: 12 # Minimum font size in px
       max: 30 # Maximum font size in px
       amount: 200 # Total amount of tags
       orderby: name # Order of tags
       order: 1 # Sort order
   ```

4. 在文章里使用标签

    ```yml
    ---
    title: Hexo Guide
    date: 2022-07-11 17:33:53
    tags: [hexo, next]
    ---
    ```

##### 分类页

操作和上面的标签页一样, 只是把 ***tags*** 修改为 ***categories*** ,分类每个文章只支持一个

### 插件

#### 搜索

[hexo-generator-searchdb](https://github.com/theme-next/hexo-generator-searchdb) 用于生成搜索索引文件，其中包含您的文章的所有必要数据。

1. 安装

    ```bash
    $ npm install hexo-generator-searchdb --save
    ```

2. 编辑 ***_config.yml*** 新增配置

   ```yml
    search:
      path: search.xml
      field: post
      content: true
      format: html
   ```

3. 编辑 ***_config_next.yml*** 文件

   ```yml
    local_search:
      enable: true
   ```

#### 评论

hexo-next-utteranc (<https://github.com/theme-next/hexo-next-utteranc>)

next 支持很多评论系统 disqus | disqusjs | changyan | livere | gitalk | utterances  这里以utterances为例

utterance(<https://utteranc.es/>) 原理: 在博客页面上输入评论，utterance拿到这个评论后，自动的提交到上面刚创建仓库的Issues里。

1. 授权

    点击(<https://github.com/apps/utterances>) 安装githubApp 并授权指定仓库

2. 配置 *_config.next.yml*

   ```yml
   comments:
     # Available values: tabs | buttons
     style: tabs
     # 指定评论系统
     active: utterances

    utterance:
       enable: true
       #仓库名字，格式：用户ID/仓库名称
       repo: Molers/BlogComment
       #主题
       theme: github-light
       #映射配置 这里是跳转github后重定向的地址 取的是 url + 当前path名称，所以需要在_config.yml里配置 url为你网站的域名，才能正常跳转
       issue_term: pathname
   ```

3. 让某些页面不支持comments 页头设置false就行

   ```yml
    ---
    title: 404
    date: 2022-07-11 17:38:27
    comments: false
    ---
   ```

#### Rss

hexo-generator-feed (<https://github.com/hexojs/hexo-generator-feed>)

1. 安装

    ```bash 下载 
    $ npm install hexo-generator-feed --save
    ```

2. 配置

   ```yml _config.yml
    feed:
       enable: true 
       type: atom #制定类型
       path: atom.xml  #生成路径
       limit: 20 # 文章数量限制 0/false 表示所有文章
       hub:
       content:
       content_limit: 140 #文章内容限制
       content_limit_delim: ' '
       order_by: -date #排序
       icon: icon.png
       autodiscovery: true
       template:
   ```

3. 展示

    两种展示位置, 一个在文章底部, 一个在菜单栏

    ```yml _config.next.yml
    follow_me:
        # 文章底部
       RSS: /atom.xml || fa fa-rss
    
    menu:
        # 菜单栏
       RSS: /atom.xml || fa fa-rs
    ```

#### 字体统计

hexo-word-counter (<https://github.com/next-theme/hexo-word-counter>)

1. 安装

   ```bash
   $ npm install hexo-word-counter
   ```

2. 配置 *_config.yml*

   ```yml
    symbols_count_time:
       symbols: true
       time: true
       total_symbols: true
       total_time: true
       exclude_codeblock: false
       awl: 4
       wpm: 275
       suffix: "mins."
   ```

3. 配置 *_config.next.yml

   ```yml
    symbols_count_time:
       separated_meta: true
       item_text_total: false
       symbols: true
   ```

### 部署

#### Git

##### git管理源码

推荐使用 ***${username}.github.io*** 仓库管理源代码，两个分支 一个hexo保存源码信息， 一个main保存生成的静态文件用于部署。

1. 在你的hexo 目录下执行 *git init*
2. git checout ${branchname}
3. git remote add ${name} `https://github.com/username/username.github.io`
4. git add .
5. git commit -m "init hexo";
6. git push

##### 部署静态文件

Hexo 提供了快速方便的一键部署功能，让您只需一条命令就能将网站部署到服务器上。 这里推荐git部署

1. 安装 hexo-deployer-git
  
    ```bash
    # 安装
    $ npm install hexo-deployer-git
    ```

2. 修改**_config.yml**文件里的deploy值

    ```yml
    deploy:
       type: git
       repo: https://github.com/{$username}/{$username}.github.io # Repository
       branch: main #[branch]
       message: update Hexo Static Content #commit message
    ```

3. 生成站点文件并推送至远程库执行

    ```bash
    # 清理并发布
    $ hexo clean && hexo deploy
    ```

4. 登入Github，请在库设置（Repository Settings）中将默认分支设置为*步骤2* _config.yml配置中的分支名称。
5. 稍等片刻，您的站点就会显示在您的Github Pages中 `https://${username}.github.io`

##### 这一切是如何发生的

当执行 hexo deploy 时，Hexo 会将 public 目录中的文件和目录推送至 _config.yml 中指定的远端仓库和分支中，并且完全覆盖该分支下的已有内容。

#### 疑难解答

1. Spawn failed

    ```log 问题
        fatal: unable to access 'https://github.com/${username}/${username}.github.io/': OpenSSL SSL_read: Connection was reset, errno 10054
        FATAL {
        err: Error: Spawn failed
            at ChildProcess.<anonymous> (E:\develop\hello\node_modules\hexo-util\lib\spawn.js:51:21)
            at ChildProcess.emit (node:events:527:28)
            at ChildProcess.cp.emit (E:\develop\hello\node_modules\cross-spawn\lib\enoent.js:34:29)
            at Process.ChildProcess._handle.onexit (node:internal/child_process:291:12) {
            code: 128
        }
        } Something's wrong. Maybe you can find the solution here: %s https://hexo.io/docs/troubleshooting.html

    ```

    ```bash 解决
    # 切换到博客根目录
    cd hexo-site
    # 删除此文件
    rm -rf .deploy_git/
    # git 配置换行符转换
    git config --global core.autocrlf false
    # 部署
    hexo clean && hexo g && hexo d
    ```