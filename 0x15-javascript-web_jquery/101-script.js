// remove an item onclick
$(document).ready(function () {
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  $('#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });

  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
