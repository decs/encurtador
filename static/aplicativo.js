$(document).ready(function() {
	var desativaEnvio = function(val){
		$('#encurtador input[type=submit]').attr('disabled', val);
	};
	
	$('#encurtador').ajaxSend(function(){
		$('#mensagem').html('Carregando...').fadeIn();
	});
	
    $('#encurtador').ajaxForm({
		dataType: 'json',
		beforeSubmit: function(){
			desativaEnvio(true);
		},
		success: function(json){
			desativaEnvio(false);
			if (json.erro) {
				$('#mensagem').html('Deu errado! :(<br />Verifique se o link é válido ou tente usar outro código...').fadeIn('slow');
			} else {
				$('#mensagem').html('Pronto! :)<br />Agora você pode compartilhar seu novo link: <a href="' + json.codigo + '">' + json.codigo + '</a>').fadeIn('slow');
				$('#urls').append('<li><a href="' + json.codigo + '">' + json.codigo + '</a> <a href="' + json.codigo + '+">+</a> ' + json.destino + '</li>');
				$('#encurtador').clearForm();
			}
		}
	});
});
