// 6-bob: Arifmetik va tayinlash operatorlari

// === Arifmetik operatorlar ===
let a = 15;
let b = 4;

console.log("Qo'shish:    ", a + b);   // 19
console.log("Ayirish:     ", a - b);   // 11
console.log("Ko'paytirish:", a * b);   // 60
console.log("Bo'lish:     ", a / b);   // 3.75
console.log("Qoldiq:      ", a % b);   // 3
console.log("Daraja:      ", a ** 2);  // 225

// Increment va decrement
let son = 5;
console.log("son++:", son++); // 5 (avval qiymat, keyin oshadi)
console.log("son:  ", son);   // 6
console.log("++son:", ++son); // 7 (avval oshadi, keyin qiymat)

let son2 = 10;
console.log("son2--:", son2--); // 10
console.log("--son2:", --son2); // 8

// === Tayinlash operatorlari ===
let x = 100;
console.log("x =  ", x);      // 100

x += 10;
console.log("x += 10:", x);   // 110

x -= 20;
console.log("x -= 20:", x);   // 90

x *= 2;
console.log("x *= 2: ", x);   // 180

x /= 3;
console.log("x /= 3: ", x);   // 60

x %= 7;
console.log("x %= 7: ", x);   // 4

x **= 3;
console.log("x **= 3:", x);   // 64

// === String bilan + operatori ===
let ism = "Ali";
let familiya = "Valiyev";
let toliqIsm = ism + " " + familiya;
console.log("To'liq ism:", toliqIsm); // "Ali Valiyev"

// Son + String = String
console.log("5" + 3);       // "53" (string concatenation)
console.log(5 + "3");       // "53"
console.log(5 + 3 + "px");  // "8px" (avval 5+3=8, keyin 8+"px")
console.log("Son: " + 5 + 3); // "Son: 53"
