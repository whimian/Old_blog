Title: FFTW应用于Visual Studio 2010项目中
Date: 2013-04-07 17:13

<p> </p> 
<p>FFTW官方网站上提供编译好的<a target="_blank" rel="nofollow" href="http://www.fftw.org/install/windows.html"  >DLL</a>文件。</p> 
<p>下载解压后，在Visual Studio 2010中打开Tools &gt; Visual Studio Command Prompt ，转到解压后的文件夹中（比如D:\fftw），使用VS2010自带的lib.exe软件生成LIB文件：</p> 
<p>32位：</p> 
<p> </p> 
<p>lib /machine:ix86 /def:libfftw3-3.def</p> 
<p>lib /machine:ix86 /def:libfftw3f-3.def</p> 
<p>lib /machine:ix86 /def:libfftw3l-3.def</p> 
<p>64位：</p> 
<p> </p> 
<p>lib /machine:x64 /def:libfftw3-3.def</p> 
<p>lib /machine:x64 /def:libfftw3f-3.def</p> 
<p>lib /machine:x64 /def:libfftw3l-3.def</p> 
<p> 这样对应文件夹下便生成了libfftw3-3.lib、libfftw3l-3.lib、libfftw3f-3.lib三个LIB文件。</p> 
<p> 该文件夹下还包括原有的fftw3.h和三个DLL文件libfftw3-3.dll、libfftw3l-3.dll、libfftw3f-3.dll。</p> 
<p>新建一个Project后，我们可以选择Project &gt; Properties打开项目属性。把D:\fftw添加到VC++ Directories项目下的Include Directories栏（头文件搜索路径）和Library Directories栏（lib文件搜索路径）中。同时打开Linker&gt;Input 将上面3个LIB文件名添加在Additional Dependencies 栏目中。</p> 
<p>这样便设置好了路径，使得编译器可以找到我们上面生成的LIB文件。</p> 
<p> 之后，我们只要把前面提到的三个DLL文件放在建立的Project文件夹下，这样程序运行时便可以使用了。网络上有人说把DLL放在System32中，这当然可以使用，不过个人认为修改windows文件夹是一大忌讳。</p> 
<p>以上只是简单的安装方法，想要彻底理解整个过程，需要windows编程的许多知识。</p>
