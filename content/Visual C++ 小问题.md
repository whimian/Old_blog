Title: Visual C++ 小问题
Date: 2013-04-19 22:40

<p> </p> 
<p>在MFC项目中，使用STL中的valarray模板，会发生一个问题。</p> 
<p> MFC项目需要WinDef.h头文件，其中定义了max()和min()两个函数，这与valarray模板中的成员函数max()和min()发生了冲突，产生了歧义，尝试了使用严格的限定符，没有作用。</p> 
<p>最后在<a target="_blank" rel="nofollow" href="http://social.msdn.microsoft.com/Forums/en-US/vcgeneral/thread/089f654a-bb85-4dd5-ac01-8a72ecf9bdb1/"  >http://social.msdn.microsoft.com/Forums/en-US/vcgeneral/thread/089f654a-bb85-4dd5-ac01-8a72ecf9bdb1/</a>这里找到了答案，原来只要使用在valarray对象前面使用#undef max 和#undef min就能正常使用模板中的成员函数了。</p> 
<p>不过依然不理解为什么WinDef.h 中的函数可以覆盖STL中的函数，且使用限定符也没作用。</p>
