//监听滚动事件
window.onscroll = function() {
    // 滚动时当前位置距顶部的距离
    var topScroll = document.documentElement.scrollTop;
    console.log(topScroll)
        // 获取导航id
    var nav = document.getElementById("mynavbar");
    // 滚动距离大于多少时执行下面事件
    if (topScroll > 150) {
        // 到了那个距离相当于给了导航定位
        nav.style.position = 'fixed';
        nav.style.top = '0';
        nav.style.zIndex = '99';
        nav.style.width = '100%';
    } else {
        // 小于的时候让他恢复原状
        nav.style = ''
    }
}