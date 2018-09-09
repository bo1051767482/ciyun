# 写词云 导包
import jieba
from os import path
import  matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import pickle


# 笼罩图
backgroud_Image=plt.imread(r'./timg.jpg')

# 读取文件
filename = "./bilibili_danmu.txt"
with open(filename,encoding='utf-8') as f:
 mytext = f.read()

# 词语图
wc=WordCloud(
    background_color='white',  # 设置背景颜色
    # mask=backgroud_Image,  # 设置背景图片
    max_words=100,  # 设置最大现实的字数
    stopwords=STOPWORDS,  # 设置停用词
    width=1000,
    height=800,

    font_path='./ZhengQingKeJingYaTi-ShouBan-2.ttf',  # 设置字体格式，如不设置显示不了中文
    max_font_size=100,  # 设置字体最大值
    random_state=10,  # 设置有多少种随机生成状态，即有多少种配色方案
    margin=2            #边距值
).generate(mytext)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('词云.jpg')



# # <editor-fold desc="Description">
# fr = open('./bilibili_danmu.txt', 'rb')
# text = pickle.load(fr)
#
# backgroud_Image = plt.imread('girl.jpg')
# wc = WordCloud(background_color='white',  # 设置背景颜色
#                 mask=backgroud_Image,  # 设置背景图片
#                 max_words=2000,  # 设置最大现实的字数
#                 stopwords=STOPWORDS,  # 设置停用词
#                 font_path='./ZhengQingKeJingYaTi-ShouBan-2.ttf',  # 设置字体格式，如不设置显示不了中文
#                 max_font_size=50,  # 设置字体最大值
#                 random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
#                 )
# wc.generate(mytext)
# image_colors = ImageColorGenerator(backgroud_Image)
# wc.recolor(color_func=image_colors)
# plt.imshow(wc)
# plt.axis('off')
# plt.show()
# # </editor-fold>




# text_from_file_with_apath = open('./bilibili_danmu.txt',encoding='utf-8').read()
# wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
# print(wordlist_after_jieba)
# wl_space_split = "".join(wordlist_after_jieba)
# my_wordcloud = WordCloud().generate(wl_space_split)
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()