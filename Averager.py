from io import BytesIO
import numpy
from PIL import Image


class ImageAverager(object):
    def averager(self, list_of_img_data, add_noise=False, raw=False):
        N = len(list_of_img_data)
        ws = set()
        hs = set()
        for i in list_of_img_data:
            if raw:
                img = Image.open(BytesIO(i))
            else:
                img = i
            w, h = img.size
            ws.add(w)
            hs.add(h)
        w = max(ws)
        h = max(hs)
        if len(ws) > 1 and len(hs) > 1:
            for i in list_of_img_data:
                if raw:
                    Image.open(BytesIO(i)).resize(w, h)
                else:
                    i.resize(w, h)

        # Create a numpy array of floats to store the average (assume RGB images)
        arr = numpy.zeros((h, w, 3), numpy.float)

        # Build up average pixel intensities, casting each image as an array of floats
        for im in list_of_img_data:
            if raw:
                img = Image.open(BytesIO(im))
            else:
                img = im
            imarr = numpy.array(img, dtype=numpy.float)
            arr = arr + imarr / N

        ## add some random noise
        if add_noise:
            rand_arr = numpy.random.rand(h, w, 3) * 255
            N = N + 1
            arr = arr + rand_arr / N

        # Round values in array and cast as 8-bit integer
        arr = numpy.array(numpy.round(arr), dtype=numpy.uint8)

        # Generate, save and preview final image
        out = Image.fromarray(arr, mode="RGB")
        return out
