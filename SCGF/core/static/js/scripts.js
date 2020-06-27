
var receita = document.getElementById("corpo").getAttribute("data-receita");
var despesa = document.getElementById("corpo").getAttribute("data-despesa");

var saldo = parseFloat(receita) - parseFloat(despesa);
parseFloat(saldo)

elem = document.getElementById('saldo');
elem.innerHTML = '<h1>Saldo R$ '+saldo+'</h1>';