import win32com.client

# 启动 Word 应用
word = win32com.client.Dispatch("Word.Application")
word.Visible = True  # 让 Word 可见（调试时使用）

# 创建一个新文档
doc = word.Documents.Add()

# 向文档中添加文本
paragraph = doc.Paragraphs.Add()
paragraph.Range.Text = "Hello, this is a test document."

# 保存文档
doc.SaveAs(r"c:/p/py/tools/document.docx")  # 修改为你的路径
doc.Close()

# 退出 Word
word.Quit()
