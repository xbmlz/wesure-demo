import json
import time
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import requests

from app.api.deps import api_result

router = APIRouter()


@router.get("/yd/")
def yd(disease: str) -> str:
    """
    腾讯医典
    https://h5.baike.qq.com/api/access/json/cmd/GetDiseaseTabList?timestamp=1653979782124
    post

    """
    disease = get_disease_id(disease)
    if not disease:
        return api_result.error('未找到对应疾病')
    # gaishu zhengzhuang bingyin jiuyi zhiliao richang yufang
    gaishu = get_disease_info(disease['id'], disease['name'], 'gaishu')
    zhengzhuang = get_disease_info(disease['id'], disease['name'], 'zhengzhuang')
    bingyin = get_disease_info(disease['id'], disease['name'], 'bingyin')
    zhiliao = get_disease_info(disease['id'], disease['name'], 'zhiliao')
    jiuyi = get_disease_info(disease['id'], disease['name'], 'jiuyi')
    richang = get_disease_info(disease['id'], disease['name'], 'richang')
    yufang = get_disease_info(disease['id'], disease['name'], 'yufang')
    return api_result.ok(data={
        'gaishu': gaishu,
        'zhengzhuang': zhengzhuang,
        'zhiliao': zhiliao,
        'bingyin': bingyin,
        'jiuyi': jiuyi,
        'richang': richang,
        'yufang': yufang
    })


def get_disease_id(name: str):
    """
    获取疾病id
    """
    req_url = 'https://h5.baike.qq.com/api/access/json/cmd/SearchForInner'
    req_data = {
        "header": {
            "version": 2,
            "flag": 0
        },
        "body": {
            "seq": 143,
            "cmd": "SearchForInner",
            "token": "fb351713-d63d-4307-bdfb-1e5df6ccc3a8-yk",
            "payload": {
                "query": name
            }
        }
    }
    rsp = requests.post(req_url, data=json.dumps(req_data))
    rsp_json = rsp.json()
    try:
        if rsp.status_code == 200:

            return rsp_json['body']['payload']['diseases'][0]
        else:
            return None
    except Exception as e:
        return None


def get_disease_info(disease_id: str, disease_name: str, tab: str) -> str:
    """
    获取疾病id
    """
    req_url = 'https://h5.baike.qq.com/api/access/json/cmd/GetDiseaseTabList'
    req_data = {
        "header": {
            "version": 2,
            "flag": 0
        },
        "body": {
            "seq": 49,
            "cmd": "GetDiseaseTabList",
            "token": "fb351713-d63d-4307-bdfb-1e5df6ccc3a8-yk",
            "payload": {
                "disease": disease_name,
                "tab": tab,
                "id": disease_id
            }
        }
    }
    rsp = requests.post(req_url, data=json.dumps(req_data))
    rsp_json = rsp.json()
    try:
        if rsp.status_code == 200:
            tid = 'tid' + str(rsp_json['body']['payload']['tabData']['tid'])
            if tab == 'gaishu':
                return rsp_json['body']['payload']['tabData'][tid]['md_definition']
            else:
                return rsp_json['body']['payload']['tabData'][tid]['md_text']
        else:
            return None
    except Exception as e:
        return None
