		// Define the number of questions you want to appear in the quiz
		const numQuestionsToShow = 10; // Change this number as desired

		// Define the questions, answers, and feedback
		const questions = [
			"<h2>Què significa HTML?</h2>",
"<h2>Quina etiqueta HTML s'utilitza per crear un salt de línia?</h2>",
"<h2>Quina és l'etiqueta HTML correcta per inserir una imatge?</h2>",
"<h2>Quin atribut HTML s'utilitza per definir estils en línia?</h2>",
"<h2>En quina secció d'un arxiu HTML s'ha de posar un CSS extern?</h2>",
"<h2>Quina etiqueta HTML s'utilitza per definir un hiperenllaç?</h2>",
"<h2>Quina és l'etiqueta HTML correcta per a l'encapçalament més gran?</h2>",
"<h2>Quin atribut HTML s'utilitza per especificar un text alternatiu per a una imatge?</h2>",
"<h2>Quina és l'etiqueta HTML correcta per crear una llista no ordenada?</h2>",
"<h2>Quina etiqueta HTML s'utilitza per crear una taula?</h2>",
"<h2>Indica quina etiqueta fa servir per escriure un codi JavaScript dins del Codi HTML</h2>",
"<h2>Indica quin codi és fa servir per escrit un codi JavaScript extern dintre del codi HTML</h2>","<h2>Què significa CSS?</h2>",
  "<h2>Quin és el propòsit principal de CSS?</h2>",
  "<h2>Quina propietat de CSS s'utilitza per canviar el color del text?</h2>",
  "<h2>Quina és la manera correcta d'enllaçar un fitxer CSS extern a un document HTML?</h2>",
  "<h2>Quina propietat de CSS s'utilitza per establir l'espai entre els marges d'un element?</h2>",
  "<h2>Quin selector de CSS s'utilitza per seleccionar elements amb un atribut específic?</h2>",
  "<h2>Quin valor de la propietat position de CSS situa un element en la posició relativa al seu contenidor pare?</h2>",
  "<h2>Què fa l'atribut 'box-sizing' en CSS?</h2>",
  "<h2>Què fa la propietat 'display: none' en CSS?</h2>",
  "<h2>Quina propietat de CSS s'utilitza per afegir o canviar l'ombra al voltant d'un element?</h2>",
  "<h2>Quin selector de CSS seleccionarà tots els elements &lt;p&gt; que són fills directes d'un element &lt;div&gt;?</h2>",
  "<h2>Quin és l'operador utilitzat en CSS per seleccionar elements amb classes específiques?</h2>",
  "<h2>Qui, quan i on va iniciar JavaScript?</h2>",
  "<h2>Quin tipus de dades utilitzaries per emmagatzemar un número enter a JavaScript?</h2>",
  "<h2>Què fa l'operador 'typeof' en JavaScript?</h2>",
  "<h2>Quina estructura de control s'utilitza per executar un bloc de codi repetidament mentre una condició és certa?</h2>",
  "<h2>Quin és el mètode utilitzat per afegir un element al final d'un array en JavaScript?</h2>",
  "<h2>Què fa el mètode 'forEach()' en un array de JavaScript?</h2>",
  "<h2>Quin esdeveniment s'utilitza per respondre a l'acció d'un usuari que fa clic en un element HTML?</h2>",
  "<h2>Com es declara una variable en JavaScript utilitzant 'let'?</h2>"
];

  


		const answers = [
			["A. Hyper Text Markup Language", "B. Home Tool Markup Language", "C. Hyperlinks and Text Markup Language", "D. Hypertext Transfer Protocol"],
			["A. <br>", "B. <br />", "C. <line-break>", "D. <break>"],
			["A. <image>", "B. <img>", "C. <picture>", "D. <media>"],
			["A. font", "B. style", "C. class", "D. inline"],
			["A. Al final del document", "B. Dins de <body>", "C. Dins de <head>", "D. Dins de <main>"],
			["A. <hyperlink>", "B. <link>", "C. <a>", "D. <url>"],
			["A. <head>", "B. <heading>", "C. <h1>", "D. <title>"],
			["A. src", "B. href", "C. title", "D. alt"],
			["A. <list>", "B. <ol>", "C. <unorderedlist>", "D. <ul>"],
			["A. <tbl>", "B. <tabular>", "C. <grid>", "D. <table>"],
			["A. <JavaScript>", "B. <js>", "C. <java>", "D. <script>"],
			["A. <script name='myscrypt.js'>", "B.  <script src='myscrypt.js'>", "C.  <script scr='myscrypt.js'>", "D.  <script href='myscrypt.js'>"],
			["A. Cascading Style Sheets", "B. Creative Styling Solutions", "C. Computer Style System", "D. Colorful Styling Styles"],
  ["A. Definir l'estructura d'un document HTML", "B. Definir l'estil i l'aparença d'un document HTML", "C. Definir les funcions interactives d'un document HTML", "D. Definir la interconnexió de documents HTML"],
  ["A. text-color", "B. color-text", "C. font-color", "D. color"],
  ["A. <link rel='stylesheet' href='style.css'>", "B. <style src='style.css'>", "C. <stylesheet>style.css</stylesheet>", "D. <css>style.css</css>"],
  ["A. margin", "B. spacing", "C. padding", "D. border"],
  ["A. #element", "B. .element", "C. element[attribute]", "D. element > p"],
  ["A. relative", "B. absolute", "C. static", "D. fixed"],
  ["A. Determina l'alçada i l'amplada d'un element", "B. Canvia l'ordre dels elements en la pàgina", "C. Defineix el model de caixa d'un element", "D. Estableix la transparència d'un element"],
  ["A. Amaga l'element a la pàgina", "B. Mostra l'element a la pàgina", "C. Desactiva l'estil de l'element", "D. Canvia la posició de l'element"],
  ["A. shadow", "B. border-shadow", "C. box-shadow", "D. element-shadow"],
  ["A. div p", "B. div + p", "C. div ~ p", "D. div > p"],
  ["A. $", "B. .", "C. #", "D. :"],
  ["A. Tim Berners-Lee al 1989 al CERN", "B. Håkon Wium Lie a la seva tesi doctoral el 2006 a la Universitat de Oslo", "C. Brendan Eich al 1995 a Netscape", "D. Guido Van Rossum el 1989 al Centrum Wiskunde & Informatica"],
  ["A. text", "B. boolean", "C. number", "D. string"],
  ["A. Retorna el tipus de dades d'una variable", "B. Comprova si una variable és definida", "C. Comprova si una variable és nul·la", "D. Comprova si una variable és indefinida"],
  ["A. if / else", "B. while", "C. for", "D. switch"],
  ["A. array.push(element)", "B. array.add(element)", "C. array.insert(element)", "D. array.append(element)"],
  ["A. Executa una funció per a cada element de l'array", "B. Ordena els elements de l'array", "C. Filtra els elements de l'array segons un criteri", "D. Retorna la longitud de l'array"],
  ["A. onClick", "B. onHover", "C. onChange", "D. onEvent"],
  ["A. let variableNom;", "B. variableNom = let;", "C. let = variableNom;", "D. let variableNom"]
  
];


		const feedback = [
"Així és! HTML significa Hyper Text Markup Language.",
"Correcte! L'etiqueta <br> s'utilitza per crear un salt de línia",
"Correcte! L'etiqueta <img> s'utilitza per inserir una imatge.",
"Correcte! L'atribut 'style' s'utilitza per definir estils interns.",
"Així és! CSS són les sigles de Cascading Style Sheets",
"Correcte! L'etiqueta <a> s'utilitza per definir un hiperenllaç",
"Així és! L'etiqueta <h1> és l'etiqueta HTML correcta per a l'encapçalament més gran.",
"Correcte! L'atribut alt s'utilitza per especificar text alternatiu per a una imatge.",
"Correcte! L'etiqueta <ul> s'utilitza per crear una llista no ordenada",
"Correcte! L'etiqueta <table> s'utilitza per crear una taula.",
"Així és! L'etiqueta <script> us permet escriure codi JavaScript dins d'HTML.",
"Així és! L'etiqueta src (font) us permet escriure codi JavaScript dins d'HTML",
  "Així és! CSS significa Cascading Style Sheets.",
  "Correcte! El propòsit principal de CSS és definir l'estil i l'aparença d'un document HTML.",
  "Correcte! La propietat de CSS que canvia el color del text és 'color'.",
  "Correcte! Per enllaçar un fitxer CSS extern a un document HTML, fem servir l'etiqueta <link> amb l'atribut 'href'.",
  "Correcte! La propietat de CSS que establirà l'espai entre els marges és 'margin'.",
  "Correcte! El selector de CSS que selecciona elements amb un atribut específic és '[attribute]'.",
  "Correcte! El valor de la propietat 'position' que situa un element en la posició relativa al seu contenidor pare és 'relative'.",
  "Correcte! L'atribut 'box-sizing' en CSS determina el model de caixa d'un element.",
  "Correcte! La propietat 'display: none' en CSS amaga l'element a la pàgina.",
  "Correcte! La propietat de CSS que afegeix o canvia l'ombra al voltant d'un element és 'box-shadow'.",
  "Correcte! El selector de CSS que seleccionarà tots els elements <p> que són fills directes d'un element <div> és 'div > p'.",
  "Correcte! En CSS, utilitzem el símbol '.' per seleccionar elements amb classes específiques.",
   "Correcte! JavaScript significa JavaScript.",
  "Correcte! Per emmagatzemar un número enter a JavaScript, utilitzaries el tipus de dades 'number'.",
  "Correcte! L'operador 'typeof' en JavaScript retorna el tipus de dades d'una variable.",
  "Correcte! La estructura de control que s'utilitza per executar un bloc de codi repetidament mentre una condició és certa és 'while'.",
  "Correcte! Per afegir un element al final d'un array en JavaScript, utilitzaries 'array.push(element)'.",
  "Correcte! El mètode 'forEach()' en un array de JavaScript executa una funció per a cada element de l'array.",
  "Correcte! L'esdeveniment que s'utilitza per respondre a l'acció d'un usuari que fa clic en un element HTML és 'onClick'.",
  "Correcte! Per declarar una variable en JavaScript utilitzant 'let', escriuries 'let variableNom;'"
];


		const correctAnswers = [
			"A", "A", "B", "B", "C", "C", "C", "D", "D", "D","D","B", "A", "B", "D", "A", "C", "C", "A", "C", "A", "C", "D", "B", "C", "C", "A", "B", "A", "A", "A", "A"
];



		
