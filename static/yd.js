layui.use(["upload", "element", "layer", "code"], function () {
    var $ = layui.jquery,
        upload = layui.upload,
        element = layui.element,
        layer = layui.layer,
        code = layui.code;

    $('#search_btn').click(function () {
        disease_name = $("#disease_name").val();
        if (disease_name == "") {
            layer.msg("请输入疾病名称");
            return false;
        }
        var loading = layer.load(1, {
            shade: [0.1, '#fff']
        });
        var tabs = ['gaishu', 'zhengzhuang', 'bingyin', 'jiuyi', 'zhiliao', 'richang', 'yufang'];
        $.get("/api/v1/yd?disease=" + disease_name, function (res) {
            for (var i = 0; i < tabs.length; i++) {
                $("#" + tabs[i]).empty();
            }
            layer.close(loading);
            if (res.code == 0) {
                console.log(res.data)
                for (var i = 0; i < tabs.length; i++) {
                    $("#" + tabs[i]).html(res.data[tabs[i]]);
                }
            } else {
                layer.msg(res.msg);
            }
        })
    })
});