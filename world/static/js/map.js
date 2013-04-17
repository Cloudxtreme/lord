function move(direction) {
	$('input#direction').val(direction);
	$('form#direction_form').submit();
}

$(document).keydown(function(e){
    if (e.keyCode == 37) {  // left arrow
       move('W');
       return false;
    }
    if (e.keyCode == 38) { // up arrow
       move('N');
       return false;
    }
    if (e.keyCode == 39) { // right arrow
       move('E');
       return false;
    }
    if (e.keyCode == 40) { // down arrow
       move('S');
       return false;
    }
});