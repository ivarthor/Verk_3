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
		<section><h3>{{frett[0][0]}}</h3></section>
		<section>titill- fréttir</section>
		<section><img src="/static/mynd1.jpeg"></section>
		<section>
			<ul>
				% count = 0;
				% for i in frett:
					<li><a href="/frett/{{count}}">{{i[0]}}</a></li>
					% count += 1
				% end
			</ul>
		</section>
	</div>
	% include('fotur.tpl')
</body>
</html>