# AuroSrc

一个轻量级、多线程、支持管道的自动化互联网漏洞挖掘框架。


## 简介

本项目是模仿[POC-T](https://github.com/Xyntax/POC-T)写的一个脚本调用框架，最终目的是实现自动化漏洞挖掘。

设计思路参考了[POC-T](https://github.com/Xyntax/POC-T)，有很多脚本直接来自此项目，还有一些脚本来自于[boy-hack](https://github.com/boy-hack)的[POC-T](https://github.com/boy-hack/POC-T)。


## 目录结构

这是一个很轻量级（很简单）的项目，目录结构如下：

* auto\_src.py    入口程序
* libs/          框架代码
* scripts/       可调用的脚本


## 参数

* -h 显示帮助
* -q 安静模式，不输出提示信息
* -t 指定线程数
* -s 指定要执行的脚本
* -i 指定要执行脚本的参数，可以出现多次


## 使用

### 单脚本单目标：

```
python auto_src.py -s test -i target
```

这将调用scripts/目录下的test.py脚本。参数中可以写test，也可以写test.py。

### 单脚本多目标：

```
python auto_src.py -s test -i target1 -i target2 -i target3
```

或使用管道：

```
echo -e 'target1\ntarget2\ntarget3' | python auto_src.py -s test
```

注：在使用管道输入的同时也可以使用-i参数输入。

### 多脚本：

要同时调用多个脚本，需要将多个脚本放在scripts/下同一目录中，如：

```
scripts/
├── muli
│   ├── s1.py
│   └── s2.py
└── test.py
```

然后使用如下命令：

```
python auto_src.py -s muli -i target
```

这样就会同时加载muli/s1.py和muli/s2.py。
如果muli/中还有多级目录，则多级目录中后缀为.py和.pyc的脚本都会被调用。

多脚本多目标时，会对每个脚本执行每个目标。如：

```
python auto_src.py -s muli -i target1 -i target2
```

会执行四种组合：

* muli/s1.py    target1
* muli/s1.py    target2
* muli/s2.py    target1
* muli/s2.py    target2

### 级连不同脚本

```
python auto_src.py -s test1 -i target | python auto_scr.py -s test2
```

会将test1.py的输出做为test2.py的输入。

在使用管道时，可以加上-q参数使框架不输出提示信息。
但这是没有必要的，提示信息会直接输出到屏幕，不会进入管道。


## 编写脚本

脚本命名随意，但其中必须有函数poc，该函数只接受一个字符串类型的参数。
用-s参数指定脚本，框架实际上会调用该脚本中的poc函数。
该函数的返回值可以有多种，框架的输出取决于函数的返回值：

* 返回False或None：没有任何输出
* 返回True：输出输入的参数
* 返回集合或列表：逐行输出集合或列表中各个元素
* 其他情况：直接打印返回值


## 特别声明

本程序含有一定的破坏性，请遵守当地法律后使用。不可用于非法用途！


## 联系作者

[Werner](me@werner.wiki)


## 参考

* [https://github.com/Xyntax/POC-T](https://github.com/Xyntax/POC-T)
* [https://github.com/Xyntax/POC-T/wiki](https://github.com/Xyntax/POC-T/wiki)
* [https://github.com/boy-hack/POC-T](https://github.com/boy-hack/POC-T)
* [http://www.freebuf.com/sectool/176562.html](http://www.freebuf.com/sectool/176562.html)

