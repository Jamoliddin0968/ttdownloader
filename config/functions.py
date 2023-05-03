import requests
from rest_framework.response import Response
from bs4 import BeautifulSoup as bs
from rest_framework.views import APIView
from django.http import Http404


class IGDownloadView(APIView):
    def get(self, request):
        try:
            link = request.GET.get('link')
            baselink = "https://downloadgram.org"
            data = {
                "url": link
            }
            head = {
                "user-agent": "Chrome"
            }
            ses = requests.Session()
            req = ses.post(baselink, headers=head, data=data)
            soup = [i["href"] for i in bs(req.text, "html.parser").find_all(
                'a', {'href': True, 'rel': 'noopener noreferrer'})]
            if len(soup) > 0:
                return Response({"link": soup[0]})
            raise Http404
        except:
            raise Http404




