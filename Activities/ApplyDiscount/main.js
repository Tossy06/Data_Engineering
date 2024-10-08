function discount(precio, porcentaje_descuento) {
    let descuento = precio * (porcentaje_descuento / 100);
    let precio_final = precio - descuento;
    return precio_final;
}

let precio_original = 100;
let porcentaje_descuento = 15;

console.log(`El precio final con descuento es: ${discount(precio_original, porcentaje_descuento)}`);
