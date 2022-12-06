import treepoem
from treepoem import TreepoemError
from PIL import EpsImagePlugin
from io import BytesIO

__options = {
    "eclevel": "Q",
    "width": 1.2,
    "height": 1.2,
    "includetext": True,
    "compress_level": 0,
    "textfont": "Arial",
}


def __to_file(image: EpsImagePlugin.EpsImageFile) -> BytesIO:
    img_io = BytesIO()
    image.convert("RGBA").save(fp=img_io, format="PNG")
    img_io.seek(0)
    return img_io


def generate_code(type: str, data: str) -> EpsImagePlugin.EpsImageFile:
    try:
        EpsImagePlugin.gs_windows_binary = "C:\Program Files (x86)\gs\gs10.00.0\\bin\gswin32c.exe"
        return __to_file(treepoem.generate_barcode(barcode_type=type, data=data, options=__options))
    except TreepoemError as err:
        print(err)
