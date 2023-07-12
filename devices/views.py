from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3
from .serializers import DeviceSerializer


db = boto3.resource("dynamodb")
table = db.Table("devices")


# -- creating a new device by post request --#


@api_view(["POST"])
def store(request):
    try:
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            table.put_item(Item=data)

            return Response(
                status=status.HTTP_201_CREATED,
                data={"message": "Device created successfully"},
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    except Exception as e:
        return Response(
            {"error", e},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# -- show existing device information by get request -- #


@api_view(["GET"])
def show(request, id):
    try:
        device = table.get_item(Key={"id": f"/devices/id{id}"})
        if device.get("Item") is not None:
            return Response(
                device,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "device Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )
    except Exception as e:
        return Response(
            {"error", "something failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def index(request):
    try:
        devices = table.scan()
        return Response(
            devices,
            status=status.HTTP_200_OK,
        )
    except Exception as e:
        return Response(
            {"error", "something failed"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
