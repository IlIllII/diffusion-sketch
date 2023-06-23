import requests
from PIL import Image
from io import BytesIO
import base64
import webuiapi

# import json

server = "http://127.0.0.1:7860/sdapi/v1/txt2img"


def render_image():
    start_image = Image.open("screenshot.png")
    # start_image = start_image.resize((256, 256))
    start_image = start_image.convert("RGB")
    buffered = BytesIO()
    start_image.save(buffered, format="JPEG")
    start_image = base64.b64encode(buffered.getvalue()).decode("utf-8")

    detection_payload = {
        "controlnet_module": "pidinet_scribble",
        "controlnet_input_images": [start_image],
        "controlnet_processor_res": 512,
        "controlnet_threshold_a": 64,
        "controlnet_threshold_b": 64,
    }

    detection_response = requests.post(
        url=f"http://127.0.0.1:7860/sdapi/v1/txt2img", json=detection_payload
    )

    complete_payload = {
        "enable_hr": "false",
        "denoising_strength": 0,
        "firstphase_width": 0,
        "firstphase_height": 0,
        "hr_scale": 2,
        "hr_upscaler": "",
        "hr_second_pass_steps": 0,
        "hr_resize_x": 0,
        "hr_resize_y": 0,
        "prompt": "An airplane flying in the sky",
        "styles": [""],
        "seed": -1,
        "subseed": -1,
        "subseed_strength": 0,
        "seed_resize_from_h": -1,
        "seed_resize_from_w": -1,
        "sampler_name": "DDIM",
        "batch_size": 1,
        "n_iter": 1,
        "steps": 20,
        "cfg_scale": 7,
        "width": 512,
        "height": 512,
        "restore_faces": "false",
        "tiling": "false",
        "do_not_save_samples": "false",
        "do_not_save_grid": "false",
        "negative_prompt": "bad art",
        "eta": 0,
        "s_churn": 0,
        "s_tmax": 0,
        "s_tmin": 0,
        "s_noise": 1,
        "override_settings": {},
        "override_settings_restore_afterwards": "true",
        "script_args": [],
        "sampler_index": "Euler",
        "script_name": "",
        "send_images": "true",
        "save_images": "false",
        "alwayson_scripts": {},
        "controlnet_units": [
            {
                "input_image": [start_image],
                "mask": "",
                "module": "invert",
                "model": "controlnet11Models_scribble [4e6af23e]",
                "weight": 1,
                "resize_mode": "Inner Fit (Scale to Fit)",
                "lowvram": "false",
                "processor_res": 64,
                "threshold_a": 64,
                "threshold_b": 64,
                "guidance": 1,
                "guidance_start": 0,
                "guidance_end": 1,
                "guessmode": "false",
                "rgbbgr_mode": "false",
            }
        ],
    }

    response = requests.post(
        url=f"http://127.0.0.1:7860/sdapi/v1/txt2img", json=complete_payload
    )
    r = response.json()
    print(r["info"])
    print(r["parameters"])
    for j, i in enumerate(r["images"]):
        print(f"j: {j}")
        image2 = Image.open(BytesIO(base64.b64decode(i.split(",", 1)[0])))
        image2.save(f"output_img2img{j}.png")
        print(f"output_img2img{j}.png")
        return i


# for i in r["images"]:
# image = Image.open(BytesIO(base64.b64decode(i.split(",",1)[0])))


# im = render_image()


controlnet_config = {
    "prompt": "a castle",
    "negative_prompt": "(worst quality,low quality,bad quality,normal quality:1.2)",
    "enable_hr": "false",
    "seed": 42,
    "batch_size": 1,
    "steps": 16,
    "quick_steps": 12,
    "cfg_scale": 7,
    "width": 512,
    "height": 512,
    "override_settings": {"CLIP_stop_at_last_layers": 1},
    "override_settings_restore_afterwards": "true",
    "controlnet_units": [
        {
            "weight": 0.6,
            "guidance_start": 0.0,
            "guidance_end": 1.0,
            "module": "none",
            "pixel_perfect": "false",
        }
    ],
}



def generate_image():
    api = webuiapi.WebUIApi()
    img = Image.open("screenshot.png")
    scribble_unit = webuiapi.ControlNetUnit(
        input_image=img,
        module="invert",
        model="controlnet11Models_scribble [4e6af23e]",
        weight=1,
    )

    unit1 = webuiapi.ControlNetUnit(input_image=img, module='canny', model='controlnet11Models_canny [b18e0966]')

    # r = api.img2img(
    #     images=[img],
    #     prompt="beautiful house, awesome scenery, colorful art",
    #     negative_prompt="bad art",
    #     controlnet_units=[scribble_unit],
    #     sampler_name="Euler a",
    #     cfg_scale=10,
    #     steps=40
    # )
    # r.images[0].save("output.png")

    r2 = api.txt2img(
        prompt="beautiful house, awesome scenery, colorful art",
        negative_prompt="bad art",
        controlnet_units=[scribble_unit],
        sampler_name="Euler a",
        cfg_scale=10,
        steps=40
    )
    r2.images[0].save("output.png")
    # r.image.show()
    # r.images[1].show()

# generate_image()