### 常用js源码收集

```javascript
$(function () {
    $(".history").hide();
    var focus_lock = false;
    $("#keywords").focus(function () {
        if ($("#keywords").val() != '') return;
        if (focus_lock) return;
        focus_lock = true;
        dot.optionFile = ajaxfile;
        dot.debug = false;
        para = {listtype:'getHistoryKey', id:''};
        dot.ajGetBywhere("",para,function(data){
            focus_lock = false;
            //console.log(data);
            $(".history").html(data.res);
            if ($(".history").css('display') == 'none') {
                $(".history").show()

            } else {
                $(".history").hide()
            }
            $("#list").hide()
        })
    })
    // 绑定委托事件
    $(".history").click(function () {
        var ev = ev || window.event;
        var target = ev.target || ev.srcElement;
        if (target.nodeName.toLowerCase() == 'li') {
            //console.log(target.firstElementChild.innerText)
            var searchKey = target.firstElementChild.innerText;
            $("#keywords").val(searchKey);
        }
        $(".history").hide()
    })
})
```