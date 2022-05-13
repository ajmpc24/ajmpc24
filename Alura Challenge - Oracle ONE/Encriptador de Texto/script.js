
const inputTexto= document.querySelector(".form_input");
const mensaje= document.querySelector("#input-text-resultado");
function botonEncriptar(){
    const textoEncriptado = encriptar(inputTexto.value);
    mensaje.value = textoEncriptado;
}
function encriptar(stringParaEncriptar) {
    let matrizEncriptar =[["e", "enter"], ["i", "imes"], ["a", "ai"], ["o", "ober"], ["u", "ufat"]];
    stringParaEncriptar = stringParaEncriptar.toLowerCase();
    for (let i=0; i<matrizEncriptar.length; i++){
        if (stringParaEncriptar.includes(matrizEncriptar[i][0])){
            stringParaEncriptar = stringParaEncriptar.replaceAll(matrizEncriptar[i][0],matrizEncriptar[i][1])
        }
    }
    return stringParaEncriptar;
}

function botonDesencriptar(){
    const textoDesencriptado = encriptar(inputTexto.value);
    mensaje.value = textoDesencriptado;
}
function desencriptar(stringParaDesencriptar) {
    let matrizDesencriptar =[["enter", "e"], ["imes", "i"], ["ai", "a"], ["ober", "o"], ["ufat", "u"]];
    stringParaDesencriptar = stringParaDesencriptar.toLowerCase();
    for (let i=0; i<matrizDesencriptar.length; i++){
        if (stringParaDesencriptar.includes(matrizDesencriptar[i][1])){
            stringParaDesencriptar = stringParaDesencriptar.replaceAll(matrizDesencriptar[i][1],matrizDesencriptar[i][0])
        }
    }
    return stringParaDesencriptar;
}


/*
function copiar() {
    var Copiar = document.getElementById("form_input");

    Copiar.select();
    document.execCommand('copy');
    alert("Copiado con éxito");
    
}
*/