(function(){
	var extenxionJS = '.js';
	var sourceScripts = '../../static/assets/';
	var scriptsList =	[
							'javascript/libraries/jquery-3.1.1.min',
							'templates/semantic/dist/semantic.min',
							'javascript/app/dashboard'
						];
	for(var i = 0; i < scriptsList.length; i++){
		var scriptTagHTML = document.createElement('script');
		scriptTagHTML.type ='text/javascript';
		scriptTagHTML.async = false;
		scriptTagHTML.src = sourceScripts + scriptsList[i] + extenxionJS;
		(document.getElementsByTagName('HEAD')[0]||document.body).appendChild(scriptTagHTML);
	};

	setTimeout(	function(){
		app.init();
		dashboard.init_map();
		dashboard.fixMapHeiight();
	}, 200);
})();

var app = {
	init : function() {
		$('#editProfile').click( function(){
			$('.ui.modal').modal('show');
		});

		$('.message .close').on('click', function(){
			$(this).closest('.message').transition('fade');
		});

		$(window).resize(	function (){
			dashboard.fixMapHeiight();
		});
	}
}
