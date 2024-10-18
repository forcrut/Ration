$(document).ready(function() {
	$("#target").val("");
	$('table.ration select#nutrition').val("");
	for (var i = 1; i < FIELDS_LEN + 1; i++) {
		$("tr#target-norm").append('<td>0</td>');
		$("tr#target-ration").append('<td>0</td>');
		$("tr#target-diff").append('<td>0</td>');
	}
	function calculate(nutr = undefined) {
		console.log(1);
		var ration = $("tr#target-ration td");
		if (nutr) {
			for (var i = 1; i < FIELDS_LEN + 1; i++) {
				$(ration[i]).text((parseFloat($(ration[i]).text()) + parseFloat(nutr[i - 1])).toFixed(2));
			}
		}
		var diff = $("tr#target-diff td");
		var norm = $("tr#target-norm td");
		for (var i = 1; i < FIELDS_LEN + 1; i++) {
			$(diff[i]).text((parseFloat($(ration[i]).text()) - parseFloat($(norm[i]).text())).toFixed(2));
		}
	};
	$("#target").change(function() {
		var selected = $(this).val();
		var norm = $("tr#target-norm td");
		if (selected != "") {
			$.ajax({
				url: `${GET_NORM_URL}${selected}`,
				type: "GET",
				success: function(data) {
					if (data.norm.length) {
						for (var i = 1; i < FIELDS_LEN + 1; i++) {
							$(norm[i]).text(data.norm[i - 1]);
						}
					} else {
						for (var i = 1; i < FIELDS_LEN + 1; i++) {
							$(norm[i]).text(0);
						}
					};
					calculate();
				}
			});
		} else {
			for (var i = 1; i < FIELDS_LEN; i++) {
				$(norm[i]).text(0);
			};
			calculate();
		}
	});
	function handleChangeRation() {
		var selected = $(this).val();
		var target = "table.ration tr#add-component";
		if (selected != "") {
			var tag_select = this;
			$.ajax({
				url: `${GET_NUTR_URL}${selected}`,
				type: "GET",
				success: function(data) {
					if (data.nutr.length) {
						var nutr = `<td value=${$(tag_select).val()}>${$(tag_select).find('option:selected').text()}</td>`;
						$(tag_select).val("");
						var tag = $(tag_select);
						tag_select = null;
						$(target).empty();
						$(target).append(nutr);
						nutr = null;
						data.nutr.forEach(function(component) {
							$(target).append(`<td>${component}</td>`);
						});
						calculate(data.nutr);
						$(target).removeAttr('id');
						$("table.ration tbody").append('<tr id="add-component"><td></td></tr>');
						$(target).find('td').append(tag)
						$('table.ration select#nutrition').change(handleChangeRation);
					} else {
						$(tag_select).val("");
					}
				}
			});
		}
	};
	$('table.ration select#nutrition').change(handleChangeRation);
	$('#target').trigger('change');
});