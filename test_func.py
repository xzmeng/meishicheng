from xpinyin import Pinyin
pin = Pinyin()
from django.utils.text import slugify
a = '孟祥卓'

b = pin.get_pinyin(a)

print(b)
x = '《fas}'
x = 'chuan-dian-【-yu-tu-】'
print(slugify(x))

# /home/xzmeng/Downloads/Django 2 by Example_Code/Django2byExample_Code/Chapter08/myshop/static/food_images/徽菜/Downloads-Django 2 by Exam
# /home/xzmeng/Downloads/Django 2 by Example_Code/Django2byExample_Code/Chapter08/myshop/static/food_images/徽菜/中爪腐衣.jpg
# ple_Code-Django2byExample_Code-Chapter08-myshop-static-food_images-徽.txt