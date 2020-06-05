// carousel follow navbar bottom
var onResize = function() {
    $('body').css('padding-top',$('.fixed-top').height()+28);
};
$(window).resize(onResize);
$(function() {
    onResize();
});