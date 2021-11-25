/*Declare script*/
function pop_bulle() {
    $(".search_item").on('click', function() {
        var item_searched = $("#item_searched").val();
        if (item_searched == ''){
            window.alert("PUT THE POTO LA BAS!!");
            return 0
        }
        var url = "/item/" + item_searched + "/1";
        window.alert(url);
        window.location.href = url;
    })
}

/* Start script*/
$(document).ready(function() {
    pop_bulle();
});