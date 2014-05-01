$(document).ready(function() {

  window.pane = function() {
    $(".pane").height($(window).height());
  }

  $(window).resize(function(){
    return pane();
  });

  pane();

});
