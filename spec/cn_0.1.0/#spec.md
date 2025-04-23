# Lang124 语言标准 v0.1.0

## 文件扩展名
`.124` 为代码文件扩展名

## 语法
* 每条语句后面必须带分隔符 `;` 或换行符 `\n`

## 关键字

### `import`

描述：

导入 `.124` 模块

-----

语法：

|描述                   |语法                                               |示例
|-                      |-                                                  |-
|导入整个模块           |`import <moduleNameSpace>`                         |`import MyModule::MySubModule`
|导入多个模块           |`import <<moduleNameSpace>,...>`                   |`import MyModule, MyMod2::MySubMod`
|包含模块成员           |`import (<moduleNameSpace>)<member>`               |`import (MyModule)MySubModule`
|包含模块多个成员       |`import (<moduleNameSpace>)<<member>,...>`         |`import (MyModule)member1, member2`
|包含整个模块           |`import (<moduleNameSpace>)*`                      |`import (MyModule)*`
|包含多个模块成员       |`import <(<moduleNameSpace>)<member>,...>`         |
|包含多个模块多个成员   |`import <(<moduleNameSpace>)<<member>,...>,...>`   |
|包含多个整个模块       |`import <(<moduleNameSpace>)*,...>`                |

* 可以给模块或成员改名，如 `import MyModule=MyMod` 或 `import (MyModule)MySubModule=Mod2`
* 推荐一次只导入一个模块，多了乱了可读性会变差。如 `import MyModule` 或 `import (MyModule)member1, member2`


### `importcl`

描述：

导入 C 的 `.h` 头文件

* cc124 需要依赖 C 编译器处理 AST 。支持 `msvc` `gcc` `clang`，推荐 `clang`

-----

语法：

导入 `.h` ：`importcl "<hPath>"` 示例：`importcl "./c/mycfile.h"`

### `importcpp`

描述：

导入 C++ 的 `.h`/`.hh`/`.hpp` 头文件

-----

原理：

在两种语言代码之间夹着一个接口 `.cpp` ，里面加上 `extern "C"` 并把错误转换为 lang124 可以处理的形式

* cc124 需要依赖 C++ 编译器处理 AST 。支持 `msvc` `g++` `clang++`，推荐 `clang++`

-----

语法：

导入 `.hpp` ：`importcpp "<hppPath>"` 示例：`importcpp "./cpp/mycppmodule.hpp"`

