$(function(){
    $(".gallery-item a").fancybox({
        padding: 0
    });

    $(".main-photos").fancybox({
        padding: 0
    });

    $("#bottom-form-id").submit(function(){
        if($("#id_email").val() == ''){
            $("#id_email").addClass('error');
            setTimeout(function(){
                $("#id_email").removeClass('error')
            }, 3000);
        }
        if($("#id_comment").val() == ''){
            $("#id_comment").addClass('error');
            setTimeout(function(){
                $("#id_comment").removeClass('error')
            }, 3000);
        }
        if($("#id_email").val() != '' && $("#id_comment").val() != ''){
            $.ajax({
                type: 'POST',
                url: '/order/',
                data: $(this).serializeArray(),
                success: function(){
                    $.fancybox($(".message-send-modal"));
                    $("#id_email").val('');
                    $("#id_comment").val('');
                }
            });
        }
        return false;
    });
});