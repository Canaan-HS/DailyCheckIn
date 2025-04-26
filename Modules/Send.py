from .__Lib__ import httpx


class CreateSend:
    def __init__(self):
        self.Client = httpx.Client(http2=True)

    async def async_http_post(self, Name, Url, Headers, Cookies) -> dict:
        async with httpx.AsyncClient(http2=True) as client:
            response = await client.post(Url, headers=Headers, cookies=Cookies)

            try:
                return {"Name": Name} | response.json()
            except:
                return {"Name": Name, "response": response.text}

    def http_get(self, Url, Headers, Cookies):
        Response = self.Client.get(Url, headers=Headers, cookies=Cookies)
        return Response

    def http_post(self, Url, Headers, Cookies, Data={}):
        Response = self.Client.post(Url, headers=Headers, cookies=Cookies, json=Data)
        return Response
