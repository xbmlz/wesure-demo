from fastapi.encoders import jsonable_encoder


def ok(msg=None, data=None):
    if data is None and msg is None:
        res = {
            'code': 0,
            'msg': '操作成功',
            'data': ''
        }
    elif msg is None:
        res = {
            'code': 0,
            'msg': '操作成功',
            'data': data
        }
    elif data is None:
        res = {
            'code': 0,
            'msg': msg,
            'data': ''
        }
    else:
        res = {
            'code': 0,
            'msg': msg,
            'data': data
        }

    return jsonable_encoder(res)


def error(msg=None, data=None):
    if data is None and msg is None:
        res = {
            'code': 500,
            'msg': '操作失败'
        }
    elif msg is None:
        res = {
            'code': 500,
            'msg': '操作失败',
            'data': data
        }
    elif data is None:
        res = {
            'code': 500,
            'msg': msg,
            'data': ''
        }
    else:
        res = {
            'code': 500,
            'msg': msg,
            'data': data
        }
    return jsonable_encoder(res)
