function set(percent){;
    var $bar = $('.progress');

    if (percent >= 100) {
        $bar.removeClass('active');
        percent = 100
    }
    $bar.width(percent+ "%");
    $bar.text(percent + "%");
}