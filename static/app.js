layui.use(["upload", "element", "layer"], function () {
    var $ = layui.jquery,
        upload = layui.upload,
        element = layui.element,
        layer = layui.layer;

    $('#upimg').change(function (e) {
        var files = this.files;
        if (files.length) {
            if (!/image\/\w+/.test(files[0].type)) {
                alert("请确保文件为图像类型")
                return false;
            }
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#preimg').attr('src', e.target.result);

                do_ocr(e.target.result);
            };
            reader.readAsDataURL(files[0]);
        }
    });

    function do_ocr(img_str) {
        var loading = layer.load(1, {
            shade: [0.1, '#fff']
        });
        $.ajax({
            url: "/api/v1/ocr/",
            type: "POST",
            dataType: "json",
            contentType: "application/json",
            data: JSON.stringify({
                img: img_str,
            }),
            success: function (res) {
                console.log(res.data);
                renderCommonData(res.data.words_result.CommonData);
                renderItemData(res.data.words_result.Item);
                layer.close(loading);
            },
        });
    }

    layer.photos({
        photos: '#upload_box' // 图片预览容器
        , zIndex: 99999999 // 弹出层级
        , shade: 0.2// 背景虚化
        , shift: 0 //0-6的选择，指定弹出图片动画类型，默认随机
    });

    function renderCommonData(commonData) {
        $("#common_result").empty();
        for (item in commonData) {
            $("#common_result").append(`<tr><td>${commonData[item].word_name}</td><td>${commonData[item].word}</td></tr>`)
        }
    }

    function renderItemData(itemData) {
        $("#item_result").empty();
        for (item in itemData) {
            //$("#item_result").append(`<tr>
            //  <td>${itemData[item][7].word}</td>
            //  <td>${itemData[item][6].word}</td>
            //  <td>${itemData[item][4].word}</td>
            //  <td>${itemData[item][5].word}</td>
            //  <td>${itemData[item][2].word}</td>
            //  <td>${itemData[item][1].word}</td>
            //  <td>${itemData[item][3].word}</td>
            // <td>${itemData[item][0].word}</td>
            //</tr>`)
            $("#item_result").append(`<tr>
              <td>${itemData[item][7].word}</td>
              <td>${itemData[item][6].word}</td>
              <td>${itemData[item][4].word}</td>
              <td>${itemData[item][5].word}</td>
              <td>${itemData[item][2].word}</td>
              <td>${itemData[item][1].word}</td>
            </tr>`)
        }
    }
});