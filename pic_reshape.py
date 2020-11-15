# 统一图片
import os
from PIL import Image

BDF_PATH = './0_bdf/'
CBC_PATH = './1_cbc/'
CQC_PATH = './2_cqc/'
FQCD_PATH = './3_fqcd/'

RE_BDF_PATH = './ready_dish_data/0_bdf/'
RE_CBC_PATH = './ready_dish_data/1_cbc/'
RE_CQC_PATH = './ready_dish_data/2_cqc/'
RE_FQCD_PATH = './ready_dish_data/3_fqcd/'
# 改图片名
def renamesJPG(filepath, kind):
    images = os.listdir(filepath)
    i = 0
    for name in images:
        os.rename(filepath+name, filepath+kind+'_'+name.split('.')[0]+'.jpg')
        i = i + 1
        print(name, "更名完成")

# 改尺寸
def converJPG(jpgfile, file_path, outdir, width=224, height=224):
    img = Image.open(file_path+jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

# renamesJPG(BDF_PATH, '0')
# renamesJPG(CBC_PATH, '1')
# renamesJPG(CQC_PATH, '2')
# renamesJPG('./ready_dish_data/4_cdf/', '4')

# # 改BDF尺寸
# for jpgfile in os.listdir(BDF_PATH):
#     print(jpgfile, "更改尺寸完成")
#     converJPG(jpgfile, BDF_PATH, "./ready_dish_data/0_bdf")


TRAIN_PATH = './ready_dish_data/train_data/'
TEST_PATH = './ready_dish_data/test_data/'
# # 改TRAIN尺寸
# for jpgfile in os.listdir(TRAIN_PATH):
#     print(jpgfile, "更改尺寸完成")
#     converJPG(jpgfile, TRAIN_PATH, TRAIN_PATH)

#改TEST尺寸
for jpgfile in os.listdir(TEST_PATH):
    print(jpgfile, "更改尺寸完成")
    converJPG(jpgfile, TEST_PATH, TEST_PATH)
