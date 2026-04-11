// 6-bob: Taqqoslash va mantiqiy operatorlar

// === Taqqoslash operatorlari ===

// == (qiymat bo'yicha taqqoslash, type coercion)
console.log(5 == "5");       // true (type coercion)
console.log(0 == false);     // true
console.log("" == false);    // true
console.log(null == undefined); // true

// === (qat'iy taqqoslash, tur ham tekshiriladi)
console.log(5 === "5");      // false
console.log(0 === false);    // false
console.log("" === false);   // false
console.log(null === undefined); // false

// != va !==
console.log(5 != "5");       // false (== ning teskarisi)
console.log(5 !== "5");      // true  (=== ning teskarisi)

// >, <, >=, <=
console.log(10 > 5);         // true
console.log(10 < 5);         // false
console.log(5 >= 5);         // true
console.log(5 <= 4);         // false

// === Mantiqiy operatorlar ===

// && (AND — va)
console.log(true && true);    // true
console.log(true && false);   // false
console.log(5 > 3 && 10 > 7); // true

// || (OR — yoki)
console.log(true || false);   // true
console.log(false || false);  // false
console.log(5 > 3 || 10 < 7); // true

// ! (NOT — inkor)
console.log(!true);           // false
console.log(!false);          // true
console.log(!(5 > 3));        // false

// === Ternary operator ===
let yosh = 20;
let holat = yosh >= 18 ? "Katta yoshli" : "Voyaga yetmagan";
console.log(holat); // "Katta yoshli"

// Ternary bilan baho
let ball = 75;
let baho = ball >= 86 ? "A'lo" :
           ball >= 71 ? "Yaxshi" :
           ball >= 56 ? "Qoniqarli" : "Qoniqarsiz";
console.log(`Ball: ${ball}, Baho: ${baho}`); // "Yaxshi"

// === Nullish coalescing (??) ===
let qiymat1 = null ?? "standart";
console.log(qiymat1); // "standart"

let qiymat2 = 0 ?? "standart";
console.log(qiymat2); // 0 (|| dan farqi: 0 va "" ni qabul qiladi)

let qiymat3 = 0 || "standart";
console.log(qiymat3); // "standart" (|| 0 ni falsy deb hisoblaydi)

// === Optional chaining (?.) ===
let user = { ism: "Ali", manzil: { shahar: "Termiz" } };
console.log(user?.manzil?.shahar);  // "Termiz"
console.log(user?.telefon?.raqam);  // undefined (xato bermaydi)
