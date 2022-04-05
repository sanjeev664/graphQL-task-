import aspose.words as aw
import pytest



doc = aw.Document("test.pdf")

assert doc.save("word.docx")






