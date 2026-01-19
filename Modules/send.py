from .libs import httpx


class CreateSend:
    def __init__(self):
        self.Client = httpx.Client(http2=True)

    async def async_http_post(self, name, url, headers, cookies) -> dict:
        async with httpx.AsyncClient(http2=True) as client:
            response = await client.post(url, headers=headers, cookies=cookies)

            try:
                return {"Name": name} | response.json()
            except:
                return {"Name": name, "response": response.text}

    def http_get(self, url, headers, cookies):
        response = self.Client.get(url, headers=headers, cookies=cookies)
        return response

    def http_post(self, url, headers, cookies, Data={}):
        response = self.Client.post(url, headers=headers, cookies=cookies, json=Data)
        return response
