# Photo-Cropper
Crops a given image in the polygon provided.

### Dependencies needed
Pillow
Numpy

###
URL :  'http://localhost:8000/api/crop_image/'

Payload : JSON

`
{"image": "base_64_image", "coordinates": [[382, 148], [443, 141], [629, 216], [563, 423], [380, 365], [329, 358], [382, 148]]
}

Response : JSON

Cropped image in base 64

`
{"image" : "cropped_base_64_image"}
`
`
