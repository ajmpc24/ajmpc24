
const form_input = document.querySelector(".form_input");
const mensaje = document.querySelector("input-text-resultado");

function botonEncriptar(){
    const textoEncriptado = encriptar(form_input.value);
    mensaje.value = textoEncriptado;
}

function encriptar(palabraParaEncriptar){
    let matrizCodigo = [["e", "enter"], ["i", "imes"], ["a", "ai"], ["u", "ufat"]]
    palabraParaEncriptar = palabraParaEncriptar.toLowerCase();
    for (let i=0; i<=matrizCodigo.length; i++){
        if(palabraParaEncriptar.includes(matrizCodigo[i][0])){
            palabraParaEncriptar = palabraParaEncriptar.replaceAll(matrizCodigo[i][0], matrizCodigo[i][1])
        }
    }

}



    // botonDesencriptar()