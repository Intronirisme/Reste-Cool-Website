$(function () {
    let target = 0;
    let allHome = $('[id^=accueil-]');
    let allShop = $('[id^=collec-]');
    let depth = +$(allHome[target]).data('depth');
    $(document.body).css('--d', depth+'px');
    $('#hall').empty().html(allHome[target].content.cloneNode(true)).attr({
        stop: depth,
        to: depth
    });
    $('#shop').empty().html(allShop[target].content.cloneNode(true));
});