/* Project specific Javascript goes here. */

$(window).load(function() {
   $('div.media').each(function(i) {
      $(this).delay((i + 1) * 5).fadeIn(600);
   });
});
