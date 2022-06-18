
from fastapi import APIRouter
import requests
from app.api.api_v1.endpoints.report import ReqForm
from app.api.deps import api_result

router = APIRouter()


@router.post("/ocr")
def ocr_common(req: ReqForm) -> str:
    token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=zrd9t5c4cnjLHU2S34XkHF3p&client_secret=bj6ZtquEeBfWpBpoRcFPyUHUIOFlqn2D'
    token_rsp = requests.get(token_url)
    if not token_rsp:
        return api_result.error('token response is None')
    json_data = token_rsp.json()
    access_token = json_data['access_token']
    ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate'
    params = {"image": req.img}
    request_url = ocr_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if not response:
        return api_result.error('ocr response is None')
    json_data = response.json()
    return api_result.ok(data=json_data)
