function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    var copy = $('#' + data).clone().removeAttr('id');
    var target = $(ev.target);
    var placeholder = target.hasClass('dropBox') ? target : target.parent('.dropBox');
    // console.log(placeholder);
    placeholder.empty().append(copy);
}

function changeImage(target) {
    var parent = $(target).parents('div.card');

    // Target elements
    var targetImg = $(parent).find('img');
    var targetDiagnose = $(parent).find('.diagnose');

    $.post({
        url: '/change-image',
        dataType: 'json',
        success: function (data) {
            targetImg.attr('src', data.img_src);
            targetDiagnose.text(data.img_class);
        }
    });
}

function predictImage(target) {
    // Hide prev result
    var resultPrediction = $('.result');
    resultPrediction.hide();
    // Placeholder
    var targetImgPlaceholder = $(target).parent().find('.dropBox img');

    if (targetImgPlaceholder.length == 0) {
        alert('Please drag and drop cell image!');
    } else {
        var imgPath = targetImgPlaceholder.attr('src');

        $.post({
            url: '/predict',
            data: imgPath,
            success: function (data) {
                // alert(data);
                resultPrediction.text(data).show();
            }
        });
    }
}