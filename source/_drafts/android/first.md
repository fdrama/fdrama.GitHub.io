# Android从零开始学习

## 1. 为什么要写这个教程

我是一个Java开发者，经常做一些后台的数据方面的工作，但是我对Android开发也有一定的兴趣，所以我想写一个从零开始学习Android的教程，希望能够帮助到一些和我一样的人。

## 2. 为什么要从零开始

我觉得从零开始学习Android，可以让我们更好的理解Android的开发过程，而不是直接使用一些框架，这样我们才能更好的理解Android的开发过程。

## 3. 开始学习

### 3.1. 准备工作

#### 3.1.1. 安装JDK

首先我们需要安装JDK，这个就不多说了，网上有很多教程，这里就不多说了。

#### 3.1.2. 安装Android Studio

Android Studio是Android官方推荐的开发工具，我们可以在[这里](https://developer.android.com/studio/index.html)下载到最新的Android Studio。

#### 3.1.3. 安装Android SDK

Android SDK是Android开发所需要的一些工具，我们可以在Android Studio中安装。这个的作用后续会讲到。

#### 3.1.4. 安装Android模拟器

Android模拟器是Android开发所需要的一些工具，我们可以在Android Studio中安装。安装HAXM加速器可以加快模拟器的运行速度。可以放在运行项目的时候再安装。

安装HAXM加速器的时候，可能会遇到以下问题：可以查看日志解决对应问题，比如我的就是VMX enabled - No，需要在BIOS中开启虚拟化技术。

```bash
Version: 7.6.5
Output folder: C:\Program Files\Intel\HAXM
Extract: checktool.exe... 100%
Execute: C:\Program Files\Intel\HAXM\checktool.exe --verbose
CPU vendor          *  GenuineIntel
Intel64 supported   *  Yes
VMX supported       *  Yes
VMX enabled         -  No
EPT supported       *  Yes
NX supported        *  Yes
NX enabled          *  Yes
Hyper-V disabled    *  Yes
OS version          *  Windows 10.0.19045
OS architecture     *  x86_64
Guest unoccupied    *  Yes. 0 guest(s)
The system requirements are not satisfied.
```

### 3.2. 创建第一个Android项目

#### 3.2.1. 创建项目

惯例，我们先创建一个HelloWorld项目，这个项目的作用是打印HelloWorld。

创建一个`Empty Activity`的项目，然后点击Finish，就可以创建一个项目了。 Activity是Android中的一个概念，我们后续会讲到。

输入项目名称，然后点击Next，其他的都默认就可以了。后续会讲到这些内容。

#### 3.2.2. 运行项目

项目创建好后，会加载一些依赖，这个过程可能会比较慢，需要耐心等待。

其中会去下载Gradle，这个是一个构建工具，可能会失败。

```log
STDOUT - Downloading https://services.gradle.org/distributions/gradle-8.2-bin.zip
2024-01-12 14:05:23,995 [1583280]   WARN - #com.android.tools.idea.whatsnew.assistant.WhatsNewBundleCreator - Connect timed out
java.net.SocketTimeoutException: Connect timed out
at java.base/sun.nio.ch.NioSocketImpl.timedFinishConnect(NioSocketImpl.java:546)
.............
```

有两种解决方案：

第一种：

1. 使用代理，打开`File`->`Settings`->`Appearance & Behavior`->`System Settings`->`HTTP Proxy`，
2. 然后选择`Auto-detect proxy settings`，输入国内的代理地址。也可以选择`Manual proxy configuration`，输入代理地址和端口号。
3. 然后点击`Check connection`，输入超时的资源地址， 如果成功，就可以点击`OK`了。

第二种：

1. 在网上下载资源，然后放到对应的目录下，比如我的是`C:\Users\Administrator\.gradle\wrapper\dists\gradle-8.2-bin\bbg7u40eoinfdyxsxr3z4i7ta`，然后解压，然后重启Android Studio。

然后就可以运行项目了。运行项目的时候看到模拟器的界面，出现了HelloWorld，说明我们的项目运行成功了。

### 3.3. 项目结构

#### 3.3.1. 项目结构

可以参考[官方文档](https://developer.android.google.cn/studio/projects)。

大致可以分为以下几个部分：

- `app`：代码
- `Gradle Scripts`：Gradle脚本
- `res`：资源文件

可以参考[官方文档](https://developer.android.google.cn/guide/topics/resources/providing-resources?hl=zh-cn#ResourceTypes)。

*表格*

| 资源类型 | 说明 |
| --- | --- |
| anim | 动画 |
| animator | 属性动画 |
| color | 颜色 |
| drawable | 可绘制资源 |
| mipmaps | 文件夹管理启动器图标 |
| layout | 布局 |
| raw | 需以原始形式保存的任意文件 |
| values | 包含字符串、整数和颜色等简单值的 XML 文件。 |
| xml | XML 文件 |
| font | 字体文件 |

### 3.4. 运行和发布项目

#### 3.4.1. 运行项目

可以参考[官方文档](https://developer.android.google.cn/studio/run)。

有可能运行项目的时候没有问题，但是发布项目的时候会报错，这个时候需要检查一下项目的依赖，是否有问题。

每次改了Build.gradle文件后，都需要点击`Sync Now`，同步一下项目。

#### 3.4.2  版本管理

可以参考[官方文档](https://developer.android.google.cn/studio/projects/android-library)。

Gradle版本、JDK版本，Android Gradle Plugin版本都需要注意版本对应。我们可以在[这里](https://developer.android.google.cn/studio/releases/gradle-plugin)查看对应的版本。

我遇到的问题是JDK版本不对应，我使用的是JDK 8，但是Android Gradle Plugin 8.2.1不支持JDK 8，需要使用JDK 17。

可以在构建的时候指定JDK版本，比如：

```bash
./gradlew build -Dorg.gradle.java.home="F:\Programs\jdk-17.0.9"
```

当然也可以在.gradle/gradle.properties 文件中指定：

```properties
org.gradle.java.home=F:/Programs/jdk-17.0.9
```

#### 3.4.3 打包APK

点击`Build`-> `Generate Signed Bundle / APK`，
然后选择`APK`，然后点击`Next`，填入一些信息，
然后选择`release`，然后点击`Next`,
然后点击`Finish`，然后就可以在`app\release`目录下看到生成的APK文件了。
可以将APK文件安装到手机上，看看效果