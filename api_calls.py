import webuiapi
from PIL import Image

api = webuiapi.WebUIApi()

result1 = api.txt2img(
    prompt="cute squirrel",
    negative_prompt="ugly, out of frame",
    seed=1003,
    # styles=["anime"],
    cfg_scale=7,
)

# image = Image.open(result1.image)
# result1.image.show()
result1.image.save("result1.png")

print(result1.info)
print(result1.parameters)

# normal txt2img
r = api.txt2img(prompt="photo of a beautiful girl with blonde hair", height=512, seed=100)
img = r.image
# img.show()

print(api.controlnet_model_list())

# txt2img with ControlNet (used 1.0 but also supports 1.1)
unit1 = webuiapi.ControlNetUnit(input_image=img, module='canny', model='controlnet11Models_canny [b18e0966]')

r = api.txt2img(prompt="photo of a beautiful girl", controlnet_units=[unit1])
# r.image.show()

img = Image.open("screenshot.png")

unit1 = webuiapi.ControlNetUnit(input_image=img, module='canny', model='controlnet11Models_canny [b18e0966]')
unit2 = webuiapi.ControlNetUnit(input_image=img, module='invert', model='controlnet11Models_scribble [4e6af23e]', weight=1)

r2 = api.img2img(prompt="airplane",
            images=[img],
            width=512,
            height=512,
            controlnet_units=[unit2, unit1],
            sampler_name="Euler a",
            cfg_scale=7,
           )

print(len(r2.images))
# r2.image.show()
r2.images[0].show()
r2.images[1].show()

r = api.controlnet_detect(images=[img], module='canny')
# r.image.show()