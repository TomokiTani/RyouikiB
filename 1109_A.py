from PIL import Image, ImageDraw

# カラーの画像データ（Imageオブジェクト）の作成
img = Image.new("RGB", (500, 500), "Black")
# ImageDrawオブジェクトの作成
draw = ImageDraw.Draw(img)
# 直線の描画
draw.rectangle([(120, 130), (200, 150)], fill="White", outline=None, width=1)

# 画像の表示
img.show()