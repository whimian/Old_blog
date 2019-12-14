Title: Anaconda使用mpl_toolkits的方法
Date: 2015-07-03 20:48

<p>matplotlib已经成为使用python进行科学计算绘图的标准装备，而今天在Anaconda发行版下使用matplotlib提供的mpl_toolkits进行三维图形绘制时，却遇到了问题，mpl_toolkits相关py文件明明在目录之下，运行时却还是提示No module named 'mpl_toolkits'的提示，一贯稳定方便的Anaconda下还会出现这样的问题，面对网络中似是而非的解决办法，一时间有些无所适从。</p> 
<p>一些人说问题在于一个namespace package的概念，也就是将同一命名空间内的包分散在不同文件夹下存储时产生的问题，而我按照以下方法查看mpl_toolkits的路径时</p> 
<p>import importlib</p> 
<p>importlib.import_module('mpl_toolkits').__path__</p> 
<p>显示的路径当中已经包含__init__.py文件，却不包含必要函数文件，也就是问题在于没有指向正确的文件夹，这是问题似乎进入了无法解决境地。</p> 
<p>然而有洁癖的我在查看anaconda根目录时发现以前几乎所有版本的packages都保存在目录下面，占用巨大空间，进而想到要用conda clean命令来清理安装目录，或许可以解决连接的混乱。</p> 
<p>没想到，在清理之后，问题真的解决了。。。。。。。</p> 
<p>这时再查看mpl_toolkits的路径，显示出来的就是正确的位置了。</p> 
<p>————————————————————————————————</p> 
<p>之后发现，mpl_toolkits文件夹下的__init__.py文件的确是basemap包&nbsp;创建的。发现过程是这样的：由于basemap包体积巨大，而且目前用不到，因而考虑将其卸载，进而conda uninstall basemap，删除之后，matplotlib又找不到mpl_toolkits了，进入目录发现，真的是没有了__init__.py。</p> 
<p>那就自己添加一个吧！！！</p> 
<p>__init__.py ---------------------------------------------------------------------</p> 
<p>try:</p> 
<p>&nbsp;&nbsp;&nbsp; __import__('pkg_resources').declare_namespace(__name__)</p> 
<p>except ImportError:</p> 
<p>&nbsp;&nbsp;&nbsp; pass # must not have setuptools</p> 
<p>--------------------------------------------------------------------------------</p> 
<p>这样添加之后一切正常了。。。</p> 
<p>Anaconda应该修改一下这个问题。</p>
