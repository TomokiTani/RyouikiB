from PIL import Image, ImageDraw

# カラーの画像データ（Imageオブジェクト）の作成
img = Image.new("RGB", (100, 100), "White")
# ImageDrawオブジェクトの作成
draw = ImageDraw.Draw(img)
# 直線の描画
draw.rectangle([(30, 20), (80,30)], fill="Black", outline=None, width=1)
draw.rectangle([(20, 30), (90, 50)], fill="Black", outline=None, width=1)
draw.ellipse([(30, 50), (40,60)], fill="Black", outline=None, width=1)
draw.ellipse([(60, 50), (70,60)], fill="Black", outline=None, width=1)
draw.text((20, 80), 'Tani Tomoki', 'Black')

# 画像の表示
img.show()

class car:
    x = 0
    y = 0

    def set(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        draw.rectangle([(self.x, self.y), (80,30)], fill="Black", outline=None, width=1)
        draw.rectangle([(20, 30), (90, 50)], fill="Black", outline=None, width=1)
        draw.ellipse([(30, 50), (40,60)], fill="Black", outline=None, width=1)
        draw.ellipse([(60, 50), (70,60)], fill="Black", outline=None, width=1)
