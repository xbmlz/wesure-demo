from cgi import print_arguments
import json
import requests


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
            return rsp_json['body']['payload']['tabData'][tid]['md_text']
        else:
            return None
    except Exception as e:
        return None


if __name__ == '__main__':
    disease = get_disease_id("布氏杆菌病")
    print(disease)
    # gaishu zhengzhuang bingyin jiuyi zhiliao richang yufang
    info_html = get_disease_info(disease['id'], disease['name'], 'bingyin')
    print(info_html)
