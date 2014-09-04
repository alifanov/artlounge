$(function(){
    $(".gallery-item a").fancybox({
        padding: 0
    });

    $("#bottom-form-id").submit(function(){
        if($("#id_email").val() == ''){
            $("#id_email").addClass('error');
            setTimeout(function(){
                $("#id_email").removeClass('error')
            }, 3000);
            return false;
        }
        if($("#id_comment").val() == ''){
            $("#id_comment").addClass('error');
            setTimeout(function(){
                $("#id_comment").removeClass('error')
            }, 3000);
            return false;
        }
        return false;
    });
});