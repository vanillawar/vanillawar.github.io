const TIMER_HAS_ENDED = "Time is up!";

function setText(elementId, text) {
    document.getElementById(elementId).innerText = text;
}

function timerText(targetDate) {
    var now = new Date().getTime();

    var distance = targetDate.getTime() - now;

    if (distance < 0) {
        return TIMER_HAS_ENDED;
    }

    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    text = "";
    if (days > 0) {
        text += days + "d ";
    }
    if (hours > 0 || days > 0) {
        text += hours + "h ";
    }
    if (minutes > 0 || days > 0 || hours > 0) {
        text += minutes + "m ";
    }
    text += seconds + "s";

    return text;
}

function setTimer(targetDate, elementId, prefix = "", suffix = "") {
    setText(elementId, prefix + timerText(targetDate) + suffix);

    var timer = setInterval(function () {
        var text = timerText(targetDate);
        setText(elementId, prefix + text + suffix);

        if (text === TIMER_HAS_ENDED) {
            clearInterval(timer);
        }
    }, 1000);
}
