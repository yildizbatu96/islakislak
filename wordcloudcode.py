from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


STOPWORDS.add('bu')
STOPWORDS.add('mi')
STOPWORDS/add('bir')
text = open('sozler.txt', 'r').read()
foto = np.array(Image.open('barisabi.png'))
wc = WordCloud(background_color='white', collocations=False, mask=foto, width= 1000, height=1000, stopwords=STOPWORDS)
wc.generate(text)

plt.figure(figsize=(20,10))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.to_file('barisabimiz.png')
