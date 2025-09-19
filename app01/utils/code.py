import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def check_code(width=120, height=40):
    # 创建图片
    image = Image.new('RGB', (width, height), (240, 240, 240))
    draw = ImageDraw.Draw(image)

    # 生成验证码
    characters = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))

    # 设置字体
    try:
        font = ImageFont.truetype('arial.ttf', 24)
    except:
        font = ImageFont.load_default()

    # 绘制验证码
    for i, char in enumerate(characters):
        color = (random.randint(50, 150), random.randint(50, 150), random.randint(50, 150))
        x = 10 + i * (width // 4) + random.randint(-3, 3)
        y = random.randint(5, 15)
        draw.text((x, y), char, fill=color, font=font)

    # 添加干扰
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=(random.randint(100, 200), random.randint(100, 200), random.randint(100, 200)))

    # 保存到内存流
    stream = BytesIO()
    image.save(stream, 'png')
    stream.seek(0)

    # 返回图片数据和验证码字符串
    return stream.getvalue(), characters