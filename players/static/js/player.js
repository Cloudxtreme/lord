activity_log_container = $('#activity_log_container');
other_player_container = $('ul#other-players');

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
		
		// only run if the activity isn't displayed.
		if ($(item_id).length == 0) {
			var new_activity = $(item.activity_html).hide();
			activity_log_container.prepend(new_activity);
			new_activity.slideDown();
			if (item.activity_type == 'arrival') {
				$('#other-players-blurb').html(item.other_players_blurb);
				other_player_container.append(item.other_players_html);
			} else if (item.activity_type == 'departure') {
				$('#other-players-blurb').html(item.other_players_blurb);
				$('#oplayer_' + item.from_player).remove();
			} else if (item.activity_type == 'pvp_defender' || item.activity_type == 'pvp_attacker') {
				$('#my_hitpoints').css('width', item.percent_hp_remaining + '%');
				$('#my_hitpoints').parent().removeClass().addClass('progress progress-striped progress-' + item.hp_class);
			}
		}
	});
}