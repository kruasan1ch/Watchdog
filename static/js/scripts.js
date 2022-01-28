function SendPageData(){
    var link = $("#link").val();
    var type = parseInt($("#type").val());

    $.ajax({
        url: '/add_page',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            "link": link,
            "type": type
        }),
        success: function(result) {
            window.location.reload();
        },
    });
}
function DeletePage(id){
    var ID = parseInt(id)
    $.ajax({
        url: '/del_page',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            "id": ID,
        }),
        success: function(result) {
            window.location.reload();
        },
    });
}
function CheckForUpdates(){
    $.ajax({
        url: '/check',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            "message": "ok"
        }),
        success: function(result) {
            window.location.reload();
        },
    });
}