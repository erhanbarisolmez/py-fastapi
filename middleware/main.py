from unicorn import UnicornMiddleware
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware



app = FastAPI()

"""
httpsGelen tüm isteklerin ya da olması gerektiğini zorunlu kılar wss.
Gelen istekler httpbunun wsyerine güvenli şemaya yönlendirilecektir.
"""
app.add_middleware(HTTPSRedirectMiddleware)

app.add_middleware(UnicornMiddleware, some_config= "rainbow")


"""
HostHTTP Ana Bilgisayar Başlığı saldırılarına karşı koruma sağlamak için, gelen tüm isteklerin
doğru ayarlanmış bir başlığa sahip olmasını zorunlu kılar .
"""
app.add_middleware(
TrustedHostMiddleware, allowed_hosts=["example.com", "*.example.com"]
)

@app.get("/")
async def main():
  return {"message": "Hello World"}
