

function check() {
	var p = 0;

	var q1 = document.getElementsByName('q1');

for (var i = 0, length = q1.length; i < length; i++)
{
 if (q1[i].checked)
 {

 	if (q1[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg1").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg1").innerHTML = "Resposta Incorrecta! La resposta correcta es 192, perqué 15 Minuts x 4 Viatjes donen 1 hora en total que es igual a 192. 48 Pasatgers x 4 Viatjes= 192 Pasatgers";
 		
 		document.getElementById("msg1").innerHTML = "Resposta Incorrecta! La resposta correcta es 192, perqué 15 Minuts x 4 Viatjes donen 1 hora en total que es igual a 192. 48 Pasatgers x 4 Viatjes= 192 Pasatgers"};

  break;
 }
}

var q2 = document.getElementsByName('q2');

for (var i = 0, length = q2.length; i < length; i++)
{
 if (q2[i].checked)
 {

 	if (q2[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg2").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg2").innerHTML = "Resposta Incorrecta! La resposta correcta es (4,4 ± 0,22) kΩ, perqué si fem 1,1 + 3,3 x 0,05 = (4,4 ± 0,22) kΩ"};

  break;
 }
}

var q3 = document.getElementsByName('q3');

for (var i = 0, length = q3.length; i < length; i++)
{
 if (q3[i].checked)
 {

 	if (q3[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg3").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg3").innerHTML = "Resposta Incorrecta! La resposta correcta es 10 mm2 perqué 750/75 = 10mm2"};

  break;
 }
}

var q4 = document.getElementsByName('q4');

for (var i = 0, length = q4.length; i < length; i++)
{
 if (q4[i].checked)
 {

 	if (q4[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg4").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg4").innerHTML = "Resposta Incorrecta! La resposta correcta es 160,9 kg perqué 2,45kG CO2 x 7,1L x 925km = 160,9 kg "};

  break;
 }
}

var q5 = document.getElementsByName('q5');

for (var i = 0, length = q5.length; i < length; i++)
{
 if (q5[i].checked)
 {

 	if (q5[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg5").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg5").innerHTML = "Resposta Incorrecta! La resposta correcta es 1288 perqué 0,92 x 1400u = 1288"};

  break;
 }
}

var q6 = document.getElementsByName('q6');

for (var i = 0, length = q6.length; i < length; i++)
{
 if (q6[i].checked)
 {

 	if (q6[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg6").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg6").innerHTML = "Resposta Incorrecta! La resposta correcta es la b perqué la taula de la veritat mai pot tindre lletres. l'apartat b hem d'escriure totes les possibles variables. A l'últim apartat, el c, Hem de dibuixar be les lletres i no confondre-les."};

  break;
 }
}

var q7 = document.getElementsByName('q7');

for (var i = 0, length = q7.length; i < length; i++)
{
 if (q7[i].checked)
 {

 	if (q7[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg7").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg7").innerHTML = "Resposta Incorrecta! La resposta correcta es la a perque hem de utilitzar les formules adients a el que ens demana, i no confundir els signes + - i les unitats com en aquest cas el rendiment, les forces verticals per energies, etc"};

  break;
 }
}

var q8 = document.getElementsByName('q8');

for (var i = 0, length = q8.length; i < length; i++)
{
 if (q8[i].checked)
 {

 	if (q8[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg8").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg8").innerHTML = "Resposta Incorrecta! La resposta correcta es la d perque hem de utilitzar les formules adients a el que ens demana, i no confundir els signes + - i les unitats com en aquest cas el rendiment, el parell, les energies i les forces verticals, etc"};

  break;
 }
}

var q9 = document.getElementsByName('q9');

for (var i = 0, length = q9.length; i < length; i++)
{
 if (q9[i].checked)
 {

 	if (q9[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg9").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg9").innerHTML = "Resposta Incorrecta! La resposta correcta es la a perque hem de utilitzar les formules adients a el que ens demana, i no confundir els signes + - i les unitats com en aquest cas la potencia electrica posarla en W i no en J, el parell , etc"};

  break;
 }
}

var q10 = document.getElementsByName('q10');

for (var i = 0, length = q10.length; i < length; i++)
{
 if (q10[i].checked)
 {

 	if (q10[i].value == "true") {
 		p = p+1 
 		document.getElementById("msg10").innerHTML = "Correcte!"} 
 		else {document.getElementById("msg10").innerHTML = "Resposta Incorrecta! La resposta correcta es la a perque hem de utilitzar les formules adients a el que ens demana, i no confundir els signes + - i les unitats com en aquest cas les energies i les formules amb la V i la G, etc"};

  break;
 }
}
console.log(p)
var txt = document.getElementById('txt')

if (p == 10) {
	txt.innerHTML = "Enhorabona! Has obtingut 10/10!"
} else if (p < 10 && p > 6) {
	txt.innerHTML = "Ben fet. Has obtingut " + p + "/10!"
} else if (p <= 6 && p > 3) {
	txt.innerHTML = "Pots millorar. Has obtingut " + p + "/10!"
} else if (p <= 3) {
  txt.innerHTML =	"Has d'estudiar molt! Has obtingut" + p + "/10!"
}

}