$( document ).ready(function() {
	var js = document.createElement("script");

	js.type = "text/javascript";
	js.src = "../static/assets/javascript/app/dashboard.js";

	document.body.appendChild(js);

	setTimeout(	function()	{
		dashboard.init_map();
		dashboard.fixMapHeiight();
	}, 200);
});

$( window ).resize(	function ()	{
	dashboard.fixMapHeiight();
});