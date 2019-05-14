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
    console.log(placeholder);
    placeholder.empty().append(copy);
}

function changeImage(target) {
    console.log('image-change');
    var parent = $(target).parents('div.card');
    // console.log(parent, parent.parents('div.card'));
    var targetImg = $(parent).find('img');
    console.log(targetImg);

    $.post('/change-image', function (img_src) {
        console.log(img_src);

        targetImg.attr('src', img_src);
    });
}