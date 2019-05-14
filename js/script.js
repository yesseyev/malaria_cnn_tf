function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  var copy = $('#' + data).clone();
  var target = $(ev.target);
  var placeholder = target.hasClass('dropBox') ? target : target.parent('.dropBox');
  console.log(placeholder);
  placeholder.empty().append(copy);
}