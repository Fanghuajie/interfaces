from wordcloud import WordCloud
import matplotlib.pyplot as plt
filename = "yes-minister.txt"
with open(filename) as f:
    mytext = f.read()
wordcloud = WordCloud().generate(mytext)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
