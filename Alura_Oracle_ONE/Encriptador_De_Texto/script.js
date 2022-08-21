const inputTexto = document.querySelector(".form_input");
const mensaje = document.querySelector("#input-text-resultado");
//Metodo Encriptar
function botonEncriptar() {
    const textoEncriptado = encriptar(inputTexto.value);
    mensaje.value = textoEncriptado;
}

function encriptar(stringParaEncriptar) {
    let matrizEncriptar = [
        ["e", "enter"],
        ["i", "imes"],
        ["a", "ai"],
        ["o", "ober"],
        ["u", "ufat"]
    ];
    stringParaEncriptar = stringParaEncriptar.toLowerCase();
    for (let i = 0; i < matrizEncriptar.length; i++) {
        if (stringParaEncriptar.includes(matrizEncriptar[i][0])) {
            stringParaEncriptar = stringParaEncriptar.replaceAll(matrizEncriptar[i][0], matrizEncriptar[i][1])
        }
    }
    return stringParaEncriptar;
}

//Metodo Desemcriptar
function botonDesencriptar() {
    const textoDesencriptado = desencriptar(inputTexto.value);
    mensaje.value = textoDesencriptado;
}

function desencriptar(stringParaDesencriptar) {
    let matrizDesencriptar = [
        ["e", "enter"],
        ["i", "imes"],
        ["a", "ai"],
        ["o", "ober"],
        ["u", "ufat"]
    ];
    stringParaDesencriptar = stringParaDesencriptar.toLowerCase();
    for (let i = 0; i < matrizDesencriptar.length; i++) {
        if (stringParaDesencriptar.includes(matrizDesencriptar[i][1])) {
            stringParaDesencriptar = stringParaDesencriptar.replaceAll(matrizDesencriptar[i][1], matrizDesencriptar[i][0])
        }
    }
    return stringParaDesencriptar;
}

//Metodo Copiar
/*
function botonCopiaTexto() {
    var contenido = document.querySelector("#input-text-resultado");
    contenido.select();
    document.execCommandnd("copy");
    alert("Texto copiado! ");

}
*/
function botonCopiaTexto() {

    var texto = document.querySelector("#input-text-resultado");
    
    texto.select();
    document.execCommand("copy");

    alert("Texto Copiado con exito!");
    entradaTexto.focus();
    respuesta.value = "";
}
