import re

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests
from app.api.deps import api_result

router = APIRouter()


class ReqForm(BaseModel):
    img: str


@router.post("/ocr/")
def ocr(req: ReqForm) -> str:
    """
    Test ocr
    """
    token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=zrd9t5c4cnjLHU2S34XkHF3p&client_secret=bj6ZtquEeBfWpBpoRcFPyUHUIOFlqn2D'
    token_rsp = requests.get(token_url)
    if not token_rsp:
        return api_result.error('token response is None')
    json_data = token_rsp.json()
    access_token = json_data['access_token']
    ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_report_detection'
    params = {"image": req.img}
    request_url = ocr_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if not response:
        return api_result.error('ocr response is None')
    json_data = response.json()
    return api_result.ok(data=json_data)


@router.post("/ocr3")
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


@router.post("/ocr2/")
def ocr(req: ReqForm) -> str:
    """
    Test ocr
    """
    token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=zrd9t5c4cnjLHU2S34XkHF3p&client_secret=bj6ZtquEeBfWpBpoRcFPyUHUIOFlqn2D'
    token_rsp = requests.get(token_url)
    if not token_rsp:
        return api_result.error('token response is None')
    json_data = token_rsp.json()
    access_token = json_data['access_token']
    ocr_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/medical_report_detection'
    params = {"image": req.img}
    request_url = ocr_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if not response:
        return api_result.error('ocr response is None')
    json_data = response.json()
    common_data = json_data['words_result']['CommonData']
    item_data = json_data['words_result']['Item']
    items = []
    for item in item_data:
        items.append({
            "enName": get_ename(item[7]['word'], item[6]['word']),
            "cnName": item[7]['word'],
            "result": re.sub('[^0-9,.]', '', item[4]['word']),
            "prob": 0,
            "unit": item[1]['word']
        })
    res = {
        "age": common_data[4]['word'].replace('岁', ''),
        "gender": common_data[6]['word'],
        "items": items
    }
    return api_result.ok(data=res)


def get_ename(cname, ename):
    results = re.findall("[(](.*)[)]", cname)
    if len(results) == 0:
        return ename
    else:
        return results[0]
