const inputMensaje = document.querySelector(".form_input");
const inputResultado = document.querySelector(".input-text-resultado");

const botonEncriptar = document.querySelector("#boton1");
const botonDesencriptar = document.querySelector("#boton2");
const botonDesencriptar = (textoEncriptado);


function encriptar(palabraParaEncriptar) {
    let matrizCodigo = [
        ["e", "enter"],
        ["i", "imes"],
        ["a", "ai"],
        ["u", "ufat"]
    ]
    palabraParaEncriptar = palabraParaEncriptar.toLowerCase();

    for (let i = 0; i <= matrizCodigo.length; i++) {

        if (palabraParaEncriptar.includes(matrizCodigo[i][0])) {
            palabraParaEncriptar = palabraParaEncriptar.replaceAll(matrizCodigo[i][0], matrizCodigo[i][1])
        }
    }

}



// botonDesencriptar()