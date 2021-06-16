from PIL import Image
import os,sys
mw=100
ms=40
mysize=mw*ms
#选择画布
toImage=Image.new('rgba',(2000,2000))
for y in range(1,22):
    for x in range(1,22):
        try:
#选取照片，按照想要的方式，依次选取
    fromImage=Image.open(r"C://Users/Administrator/Desktop/BS/soccer/%s.jpg" %str(ms*(y-1)+x))
#黏贴照片
        fromImage=fromImage.resize((100,100),Image.ANTIALIAS)
        toImage.paste(fromImage,((x-1)*mw,(y-1)*mw))
        except IOError:
        pass

toImage.show()
toImage.save('C:/Users/Administrator/Desktop/CAI.png')

