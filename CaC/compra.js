const precioTicket = 200;

function resumir(){
    var cantidadTicket = document.getElementById("inputCantidad").value;
    var descuento = document.getElementById("inputCategoria").value;
    
    var precioConDescuento = precioTicket-((precioTicket*descuento) / 100);
    var precioFinal = cantidadTicket * precioConDescuento;

    document.getElementById("compraTotal").value; = "Total a pagar: $" + precioFinal;
}