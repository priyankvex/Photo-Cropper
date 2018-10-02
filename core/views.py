from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import CreateAPIView

from core.crop_utils import crop_image


class CropView(CreateAPIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):

        input_base64_image = request.data.get("image")
        coordinates = request.data.get("coordinates")

        coordinate_tuples = self.create_coordinates(coordinates)

        cropped_image = crop_image(input_base64_image, coordinate_tuples)

        cropped_image = cropped_image.decode('utf-8')

        return JsonResponse(
            {"image": cropped_image}
        )

    def create_coordinates(self, coordinates):

        coordinate_tuples = []

        for c in coordinates:
            coordinate_tuples.append((c[0], c[1]))

        return coordinate_tuples
