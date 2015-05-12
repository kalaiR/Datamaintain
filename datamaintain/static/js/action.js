

 $(document).ready( function ()
 {
  // alert("test");
  $( "#datepicker" ).datepicker({
   
      dateFormat: "yy-mm-dd",
      changeDate:true, 
      changeMonth: true,//this option for allowing user to select month
      changeYear: true //this option for allowing user to select from year range
    });
  $('#datepicker').change(function () {
      
      
      date=$(this).val();
      alert(date);
      get_absent_list(date);
      // $('.get_absent_list').show();
   });
});


var response_cache = {};
function get_absent_list(date) {
  alert("get_absent_list");
if (response_cache[date]) {
    $(".absent_list").html(response_cache[date]);
    alert("response_cache");
  } 
else {
  // alert("else");
  $.getJSON("/get_absent_list/", {date: date},
      function(ret, textStatus) {
        // alert("else1");
        // alert(JSON.stringify(ret));
        var id = '';
        var name = '';       
        for(var i in ret){
          id += ret[i].id
          name += ret[i].name
        }
        // alert(id);
        // alert(name);
        // alert(date);
        newid = id.split(",");
        newname= name.split(",");
        // for(i=0;i<newname.length;i++)
        // alert(newname[i]);  
        // for(i=0;i<newid.length;i++)
        // alert(newid[i]);  
        $('#absent_list_name').html(newname);
        $('#absent_list_id').html(newid);

      }); 

}


}



  