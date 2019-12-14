Title: Cygwin rebaseall 和 pango文件夹
Date: 2013-04-22 19:33

<p> </p> 
<p>今天安装配置cygwin时遇到了两个奇怪的问题。</p> 
<p>其一，是安装新的软件包时，cygwin的setup.exe程序会显示一个奇怪的错误，其中包含pango.sh。</p> 
<p>解决方法更奇怪，只要自己建立etc/pango 目录即可。</p> 
<p>其二，是在安装了xorg-server、xinit、gnuplot以后，用来画图会显示一个有fork() 的错误，这里就要用到rebaseall工具。</p> 
<p>下面是wiki条目：</p> 
<p> </p> 
<p>Rebasing 表示的是指建立一个<a title="&#20849;&#20139;&#24211;&#65288;&#39029;&#38754;&#19981;&#23384;&#22312;&#65289;" target="_blank" rel="nofollow" href="http://zh.wikipedia.org/w/index.php?title=%E5%85%B1%E4%BA%AB%E5%BA%93&amp;action=edit&amp;redlink=1"  >共享库</a><a title="&#26144;&#20687;&#65288;&#39029;&#38754;&#19981;&#23384;&#22312;&#65289;" target="_blank" rel="nofollow" href="http://zh.wikipedia.org/w/index.php?title=%E6%98%A0%E5%83%8F&amp;action=edit&amp;redlink=1"  >映像</a>的过程，这种方式可以保证在使用虚拟内存的时候不会与系统中其他以装载的共享库冲突。</p> 
<p>这个技术广被泛地使用在&nbsp;<a title="Win32" target="_blank" rel="nofollow" href="http://zh.wikipedia.org/wiki/Win32"  >Win32</a>&nbsp;平台上，用于避免系统DLL文件<a title="&#37325;&#36617;" target="_blank" rel="nofollow" href="http://zh.wikipedia.org/wiki/%E9%87%8D%E8%BC%89"  >重载</a>造成的地址溢出。</p> 
<p>一些在Linux/x86系统上的安全方面的扩展部分使用Rebasing 技术。 为了把地址0x00作为所有编码的指针，用它限制能够使用的代码地址在0x00ffffff以下；这可以消除一些安全方面的内存溢出问题， 这些问题往往涉及了错误的零点校验结束字符串，一般在C程序语言中。</p> 
<p>&nbsp;</p> 
<p>在win7下只要：</p> 
<p> </p> 
<p>/usr/bin/rebaseall -v</p> 
<p>exit</p> 
<p>一切就完成了。</p>
