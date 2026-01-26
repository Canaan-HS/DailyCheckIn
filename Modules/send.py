from .libs import curl, CurlAsyncSession


class CreateSend:
    def __init__(self):
        self.session = curl.Session(impersonate="chrome120")

    async def async_curl_post(self, name, url, headers, cookies) -> dict:
        async with CurlAsyncSession(impersonate="chrome120") as session:
            response = await session.post(url, headers=headers, cookies=cookies)

            try:
                return {"Name": name} | response.json()
            except:
                return {"Name": name, "response": response.text}

    def curl_get(self, url, headers, cookies):
        response = self.session.get(url, headers=headers, cookies=cookies)
        return response

    def curl_post(self, url, headers, cookies, Data={}):
        response = self.session.post(url, headers=headers, cookies=cookies, json=Data)
        return response
