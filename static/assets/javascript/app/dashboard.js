var dashboard = {
	test: function ()	{
		console.log("Entra al dashboard");
	},
	init_map: function ()	{
		var myOptions = {
			zoom:14,
			center:	new google.maps.LatLng(21.8852562,-102.29156769999997),
			mapTypeId:	google.maps.MapTypeId.ROADMAP};
						map = new google.maps.Map(document.getElementById("map"), myOptions);
						marker = new google.maps.Marker({
								map: map,
								position: new google.maps.LatLng(21.8852562, -102.29156769999997)
							},
							{
								map: map,
								position: new google.maps.LatLng(22.8852554	, -103.29156769999955)
							}

						);
			//			infowindow = new google.maps.InfoWindow({content:"Aguascalientes" });
			//			google.maps.event.addListener(	marker, 
			//											"click", function()	{
			//											infowindow.open(map,marker);
			//			});
			//			infowindow.open(map,marker);
	},
	fixMapHeiight: function	()	{
		var menuHeight	=	$("#menu").height(),
			windowsHeight = $( window ).height(),
			finalHeight = windowsHeight - menuHeight;
			console.log(	finalHeight);
		$("#map").css(	"height",	finalHeight);
	}
};