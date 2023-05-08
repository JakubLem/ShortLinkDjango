from django.shortcuts import redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import BetterLink
from .serializers import BetterLinkSerializer
from .exceptions import BadRequest


class BetterLinkViewSet(viewsets.ModelViewSet):
    serializer_class = BetterLinkSerializer
    queryset = BetterLink.objects.all()
    lookup_field = "short_link"
    lookup_url_kwarg = "short_link"
    http_method_names = ["get", "post"]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise BadRequest(detail=serializer.errors)
        better_link = serializer.save()
        return Response(better_link.view, status=status.HTTP_201_CREATED)

    def retrieve_and_redirect(self, request, short_link=None):
        try:
            better_link = BetterLink.objects.get(short_link=short_link)
            long_link = f"{better_link.get_old_long_link_proto_display()}://{better_link.old_link_url}"
            return redirect(long_link)
        except BetterLink.DoesNotExist:
            return Response({"detail": "Short link not found."}, status=status.HTTP_404_NOT_FOUND)
