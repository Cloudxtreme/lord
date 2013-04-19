activity_log_container = $('#activity_log_container');

(function poll_activity_log() {
	setTimeout(function() {
		$.ajax({
			url: "/api/players/activity_log/",
			type: "GET",
			success: function(data) {
				update_activity_log(data);
			},
			dataType: "json",
			complete: poll_activity_log,
			timeout: 2000
		})
	}, 2000);
})();

function update_activity_log(data) {
	data.objects.map(function(item) {
		item_id = '#activity_log_' + item.id;
		if ($(item_id).length == 0) {
			var new_activity = $(item.html).hide();
			activity_log_container.prepend(new_activity);
			new_activity.slideDown();
		}
	});
}