from django.http import Http404
from django.shortcuts import render
import requests
from rest_framework.generics import GenericAPIView
from .serializers import LinkSerializer
from rest_framework.response import Response


class IGRamDownloadView(GenericAPIView):
    serializer_class = LinkSerializer

    def post(self, request):
        data = LinkSerializer(data=request.POST)
        data.is_valid(raise_exception=True)
        try:
            link = data.validated_data.get('link')
            cookies = {
                '_ga': 'GA1.2.925462583.1683094810',
                '_gid': 'GA1.2.2113720974.1683094810',
                '_gat_gtag_UA_253023977_1': '1',
                '__gads': 'ID=4001b2a1b123992c-22618555badd00a6:T=1683094810:RT=1683094810:S=ALNI_MYr465x7Sjx-6aE1gVYhequeMVIbA',
                '__gpi': 'UID=00000bf4fd873acf:T=1683094810:RT=1683094810:S=ALNI_MbqxlSaQ3r9_WY6Z_wnOO2snhuCTA',
                '_ga_VGQL34VEH8': 'GS1.1.1683094809.1.0.1683094811.0.0.0',
                'PHPSESSID': 'br49250ppssnfc5318k7lqe8g0',
            }

            headers = {

                'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                'content-type': 'application/x-www-form-urlencoded',

                'sec-ch-ua': '"Chromium";v="112", "Microsoft Edge";v="112", "Not:A-Brand";v="99"',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.64',
            }

            data = {
                'url': link,
                'token': '',
            }

            response = requests.post(
                'https://igram.live/wp-json/igram/video-data/', cookies=cookies, headers=headers, data=data)
            return Response({
                'data': response.json()
            })
        except:
            raise Http404
