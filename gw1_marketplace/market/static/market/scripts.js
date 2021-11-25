//  window.addEventListener("resize", function() {
//    "use strict"; window.location.reload(); 
//  });


  document.addEventListener("DOMContentLoaded", function(){
        

      /////// Prevent closing from click inside dropdown
    document.querySelectorAll('.dropdown-menu').forEach(function(element){
      element.addEventListener('click', function (e) {
        e.stopPropagation();
      });
    })



    // make it as accordion for smaller screens
    if (window.innerWidth < 992) {

      // close all inner dropdowns when parent is closed
      document.querySelectorAll('.navbar .dropdown').forEach(function(everydropdown){
        everydropdown.addEventListener('hidden.bs.dropdown', function () {
          // after dropdown is hidden, then find all submenus
            this.querySelectorAll('.submenu').forEach(function(everysubmenu){
              // hide every submenu as well
              everysubmenu.style.display = 'none';
            });
        })
      });
      
      document.querySelectorAll('.dropdown-menu a').forEach(function(element){
        element.addEventListener('click', function (e) {
    
            let nextEl = this.nextElementSibling;
            if(nextEl && nextEl.classList.contains('submenu')) {  
              // prevent opening link if link needs to open dropdown
              e.preventDefault();
              console.log(nextEl);
              if(nextEl.style.display == 'block'){
                nextEl.style.display = 'none';
              } else {
                nextEl.style.display = 'block';
              }

            }
        });
      })
    }
    // end if innerWidth

  }); 
  // DOMContentLoaded  end

// Seach value in url > get url
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



$("#id_group").change(function () {
  var url = $("#orderForm").attr("data-category-url");
  var groupId = $(this).val();
  
  $.ajax({
    url: url,
    data: {
      'group': groupId
    },
    success: function (data) {
      $("#id_category").html(data);
    }
  });

});
