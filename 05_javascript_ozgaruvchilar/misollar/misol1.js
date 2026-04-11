// 5-bob: var, let, const farqlari
// Bu faylni Node.js yoki brauzer konsolida ishga tushiring

// === var — eski usul, function scope ===
var ism = "Ali";
var ism = "Vali"; // Qayta e'lon qilish mumkin
console.log("var:", ism); // Vali

// === let — zamonaviy, block scope ===
let yosh = 20;
// let yosh = 25; // Xato! Qayta e'lon qilib bo'lmaydi
yosh = 25; // Qiymatni o'zgartirish mumkin
console.log("let:", yosh); // 25

// === const — o'zgarmas, block scope ===
const PI = 3.14159;
// PI = 3.14; // Xato! Qiymatni o'zgartirib bo'lmaydi
console.log("const:", PI);

// === Scope farqlari ===
// var — function scope
function varScope() {
    if (true) {
        var x = 10;
    }
    console.log("var scope:", x); // 10 — if blokidan tashqarida ham ishlaydi
}
varScope();

// let — block scope
function letScope() {
    if (true) {
        let y = 20;
        console.log("let ichida:", y); // 20
    }
    // console.log(y); // Xato! y faqat if bloki ichida mavjud
}
letScope();

// === Hoisting ===
console.log(a); // undefined (var hoisting)
var a = 5;

// console.log(b); // Xato! (let hoisting bo'lmaydi)
let b = 10;

// === const bilan object ===
const talaba = { ism: "Ali", yosh: 20 };
talaba.yosh = 21; // Xususiyatni o'zgartirish mumkin
console.log("const object:", talaba);
// talaba = {}; // Xato! O'zgaruvchini qayta tayinlab bo'lmaydi
