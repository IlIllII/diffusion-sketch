import queue
import threading

import webuiapi
from PIL import Image


def generate_image():
    api = webuiapi.WebUIApi()
    img = Image.open("screenshot.png")
    scribble_unit = webuiapi.ControlNetUnit(
        input_image=img,
        module="invert",
        model="controlnet11Models_scribble [4e6af23e]",
        weight=1,
    )
    result = api.txt2img(
        prompt="beautiful house, awesome scenery, colorful art",
        negative_prompt="bad art",
        controlnet_units=[scribble_unit],
        sampler_name="Euler a",
        cfg_scale=10,
        steps=40,
    )
    result.images[0].save("output.png")


result_queue = queue.Queue()


def make_network_request():
    counter = 0
    while counter < 10:
        success = True
        try:
            generate_image()
            result = "Network request complete!"
            result_queue.put(result)
        except Exception as e:
            success = False
            result = "Network request failed!"
            print(e)
            result_queue.put(result)

        if success:
            break
        counter += 1


def send_screenshot_to_sd():
    threading.Thread(target=make_network_request).start()


def check_for_result():
    if not result_queue.empty():
        result = result_queue.get()
        print(result)
