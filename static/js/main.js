$(document).ready(function () {

    $('#image_upload').on('submit', function (e) {
        e.preventDefault();
        var form = $(this);
        var data = new FormData(form.get(0));
        var url = form.attr('action');

        $.ajax({
            url: url,
            method:'POST',
            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                if (data['result'] === true) {
                    form[0].reset()
                    $('.message-box').text('Фотография успешно загружена')
                } else {
                    $('.message-box').text(data['errors']['image'])
                }
            }
        });
    });

});