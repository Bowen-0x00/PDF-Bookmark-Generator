# PDF-Bookmark-Generator
PDF-Bookmark-Generator 是一个 Python 工具，用于用目录信息为PDF文件生成书签。方便扫描版的 PDF 文件生成可跳转的书签，提升文档的可导航性和用户体验。这些目录信息可以从网上（数字图书馆、出版社或京东等渠道）或者OCR识别得到。

# 用法
`python PDF-Bookmark-Generator.py input.pdf toc.txt output.pdf --offset 0`

- input.pdf 是输入的 PDF 文件路径。
- toc.txt 是包含目录的文本文件路径。
- output.pdf 是输出的带书签的 PDF 文件路径。
- --offset 是可选参数，用于调整页码偏移（默认为 0）。


## toc
用缩进来标示目录层级，类似

```
第4章　函数调用规范与栈 67
    4.1　函数调用规范 67
    4.2　入栈与出栈 70
    4.3　RISC-V栈的布局 72
        4.3.1　不使用FP的栈布局 72
        4.3.2　使用FP的栈布局 74
        4.3.3　栈回溯 76
    4.4　实验 78
        4.4.1　实验4-1：观察栈布局 78
        4.4.2　实验4-2：观察栈回溯 78
```

## offset
目录信息对应的页数和pdf实际的页数有偏差，比如目录得到第1章的页数为1，而实际中的页数为23，那么offset就可以设置为22，以设置正确的跳转页数