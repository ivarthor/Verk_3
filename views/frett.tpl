<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hasarfréttir</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
	% include('haus.tpl')
	<div class="row">
		<section>{{frett[0]}}</section>
		<section>titill- fréttir</section>
		<section> <img src="/static/mynd{{nr}}.jpeg"> </section>
		<section class="pd2"> 
			<p>{{frett[1]}}</p>
			<p>{{frett[2]}}</p>
		</section>
	</div>
	% include('fotur.tpl')
</body>
</html>