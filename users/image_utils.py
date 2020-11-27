class CenterAndCrop(object):
    def process(self, image):
        # Code for adding the watermark goes here.
        dim = min(image.width, image.height)
        left = (image.width - dim) // 2
        top = (image.height - dim) // 2
        right = (image.width + dim) // 2
        bottom = (image.height + dim) // 2
        image = image.crop((left, top, right, bottom))
        return image