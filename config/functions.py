import requests
from rest_framework.response import Response
from bs4 import BeautifulSoup as bs
from rest_framework.views import APIView
from django.http import Http404
import instaloader
L = instaloader.Instaloader(download_pictures = False, download_videos = False, download_comments= False, compress_json = False)
            
class InstaLoaderDownloadView(APIView):
    def get(self,request):
        try:
            link = request.GET.get('link')
            L.login("myinstauserdown0968", "a905360968")
            print("salom")
            links = link.split("/")
            # print(links)
            shortcode = ""  
            if len(links) > 4:
                shortcode = links[4]
            post = instaloader.Post.from_shortcode(L.context,shortcode)
            if post.is_video:
                video_url = post.video_url
                return Response({"link":video_url})
            raise Http404
        except:
            raise Http404
        

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

class TTDonwloadView(APIView):
    def get(self,request):
        try:
            link = request.GET.get('link')
            cookies = {
                'ad_client': 'ssstik',
                '_ga': 'GA1.2.477926136.1670588441',
                '_gid': 'GA1.2.668062738.1670588441',
                '__gads': 'ID=a5ca8836833bf221-2277609260d80091:T=1670588441:RT=1670588441:S=ALNI_MZwF_yrwE8Alhg6odW5-JXsVI86AA',
                '__cflb': '02DiuEcwseaiqqyPC5qqr6QJm1Rd3cEXq4Zab4soDbKHm',
                '__gpi': 'UID=00000b8fb4606128:T=1670588441:RT=1670652894:S=ALNI_MawD9oTywcuUVhzvBCa-AUqqrHiRw',
                '_gat_UA-3524196-6': '1',
            }

            headers = {
                'authority': 'ssstik.io',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'ad_client=ssstik; _ga=GA1.2.477926136.1670588441; _gid=GA1.2.668062738.1670588441; __gads=ID=a5ca8836833bf221-2277609260d80091:T=1670588441:RT=1670588441:S=ALNI_MZwF_yrwE8Alhg6odW5-JXsVI86AA; __cflb=02DiuEcwseaiqqyPC5qqr6QJm1Rd3cEXq4Zab4soDbKHm; __gpi=UID=00000b8fb4606128:T=1670588441:RT=1670652894:S=ALNI_MawD9oTywcuUVhzvBCa-AUqqrHiRw; _gat_UA-3524196-6=1',
                'hx-current-url': 'https://ssstik.io/en',
                'hx-request': 'true',
                'hx-target': 'target',
                'hx-trigger': '_gcaptcha_pt',
                'origin': 'https://ssstik.io',
                'referer': 'https://ssstik.io/en',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42',
            }

            params = {
                'url': 'dl',
            }

            data = {
                'id': link,
                'locale': 'en',
                'tt': 'SHlFVjQ3',
            }

            response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
            if(response.status_code != 200):
                raise Http404
            downloadsoup = bs(response.text,"lxml")
            downlink = downloadsoup.a["href"]
            print(downlink)
            if 'ssstik' not in downlink:
                raise Http404
            return Response({"link":downlink})
        except :
            raise Http404