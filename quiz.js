function check() {
	var p = 0;

	var q1 = document.getElementsByName('q1');

for (var i = 0, length = q1.length; i < length; i++)
{
 if (q1[i].checked)
 {

 	if (q1[i].value == "true") {
 		p = p+0.5;  
 		document.getElementById("msg1").innerHTML = "Genial"} 
 		else {document.getElementById("msg1").innerHTML = "Resposta incorrecte. La resposta correcte Ã©s la c). PerquÃ¨ el que hem si dividim la inversiÃ³ feta per les carreteres que Ã©s de 3800M entre el total de la inversiÃ³ que Ã©s 10200M i ho multipliquem per 100 ens dona aproximadament el 37,25%. El que hem de fer desprÃ©s Ã©s restar 100-37,25 i ens dons 62,75% que Ã©s el que sâ€™inverteix a la Xarxa ferroviÃ ria."};

  break;
 }
}

var q2 = document.getElementsByName('q2');

for (var i = 0, length = q2.length; i < length; i++)
{
 if (q2[i].checked)
 {

 	if (q2[i].value == "true") {
 		p = p+0.5;  
 		document.getElementById("msg2").innerHTML = "Genial!"} 
 		else {document.getElementById("msg2").innerHTML = "Malament!! La resposta correcte Ã©s la a). Primer, hem de passar les 340 tonelades a 340Â·10^6 grams i dividir-ho entre la multiplicaciÃ³ del nombre de passatgers i els quilÃ³metres recorreguts. Per tant ens quedarÃ  340Â·10^6/(325Â·8000) = 130,7 g."};

  break;
 }
}

var q3 = document.getElementsByName('q3');

for (var i = 0, length = q3.length; i < length; i++)
{
 if (q3[i].checked)
 {

 	if (q3[i].value == "true") {
 		p = p+0.5;  
 		document.getElementById("msg3").innerHTML = "Genial!"} 
 		else {document.getElementById("msg3").innerHTML = "Malament! 3.	La resposta correcte Ã©s la a)."};

  break;
 }
}

var q4 = document.getElementsByName('q4');

for (var i = 0, length = q4.length; i < length; i++)
{
 if (q4[i].checked)
 {

 	if (q4[i].value == "true") {
 		p = p+0.5;  
 		document.getElementById("msg4").innerHTML = "Genial!"} 
 		else {document.getElementById("msg4").innerHTML = "Malament! La resposta correcte Ã©s la b). El valor nominal Ã©s sempre el valor teÃ²ric, sense tenir en compte las tolerÃ ncies."};

  break;
 }
}

var q5 = document.getElementsByName('q5');

for (var i = 0, length = q5.length; i < length; i++)
{
 if (q5[i].checked)
 {

 	if (q5[i].value == "true") {
 		p = p+0.5; 
 		document.getElementById("msg5").innerHTML = "Genial!"} 
 		else {document.getElementById("msg5").innerHTML = "Malament! La resposta correcte Ã©s la b). Primer hem de calcular la secciÃ³ de la barra massissa fent 25 mm Â· 300 mm = 0,0075 m^2. DesprÃ©s hem de dividir la forÃ§a axial mÃ xima entre la secciÃ³ calculada fent 360Â·10^3 N / 0,0075 m^2= 48Â·10^6 Pa = 48 MPa"};

  break;
 }
}

var q6 = document.getElementsByName('q6');

for (var i = 0, length = q6.length; i < length; i++)
{
 if (q6[i].checked)
 {

 	if (q6[i].value == "true") {
 		p = p+2.5; 
 		document.getElementById("msg6").innerHTML = "Genial!"} 
 		else {document.getElementById("msg6").innerHTML =  "<img src= respostaex2.png> "};

  break;
 }
}

var q7 = document.getElementsByName('q7');

for (var i = 0, length = q7.length; i < length; i++)
{
 if (q7[i].checked)
 {

 	if (q7[i].value == "true") {
 		p = p+2.5; 
 		document.getElementById("msg7").innerHTML = "Genial!"} 
 		else {document.getElementById("msg7").innerHTML = " <img src= respostaex3a.png>"};

  break;
 }
}

var q8 = document.getElementsByName('q8');

for (var i = 0, length = q8.length; i < length; i++)
{
 if (q8[i].checked)
 {

 	if (q8[i].value == "true") {
 		p = p+2.5; 
 		document.getElementById("msg8").innerHTML = "Genial!"} 
 		else {document.getElementById("msg8").innerHTML = "<img src= respostaex4a.png>"};

  break;
 }
}

var q9 = document.getElementsByName('q9');

for (var i = 0, length = q9.length; i < length; i++)
{
 if (q9[i].checked)
 {

 	if (q9[i].value == "true") {
 		p = p+2.5;
 		document.getElementById("msg9").innerHTML = "Genial!"} 
 		else {document.getElementById("msg9").innerHTML = "<img src= respostaex3b.png>"};

  break;
 }
}

var q10 = document.getElementsByName('q10');

for (var i = 0, length = q10.length; i < length; i++)
{
 if (q10[i].checked)
 {

 	if (q10[i].value == "true") {
 		p = p+2.5; 
 		document.getElementById("msg10").innerHTML = "Genial!"} 
 		else {document.getElementById("msg10").innerHTML = "<img src= respostaex4b.png>"};

  break;
 }
}
console.log(p)
var txt = document.getElementById('txt')

if (p == 15) {
	txt.innerHTML = "Enhorabona! Has obtingut 15/15!"
} else if (p < 15 && p > 10) {
	txt.innerHTML = "Ben fet. Has obtingut " + p + "/15!"
} else if (p <= 10 && p > 5) {
	txt.innerHTML = "Pots millorar. Has obtingut " + p + "/15!"
} else if (p <= 5) {
  txt.innerHTML =	"Has d'estudiar molt! Has obtingut" + p + "/15!"
}

}
