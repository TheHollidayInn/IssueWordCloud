import os
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
text = open(path.join(d, 'issues.txt')).read()

wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.show()