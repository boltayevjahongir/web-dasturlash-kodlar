// 8-bob: Massivlar va massiv metodlari

// === Massiv yaratish ===
let mevalar = ["Olma", "Nok", "Uzum", "Anor", "Banan"];
console.log("Massiv:", mevalar);
console.log("Uzunlik:", mevalar.length);  // 5
console.log("Birinchi:", mevalar[0]);     // "Olma"
console.log("Oxirgi:", mevalar[mevalar.length - 1]); // "Banan"

// === push, pop, shift, unshift ===
mevalar.push("Gilos");       // Oxiriga qo'shish
console.log("push:", mevalar);

mevalar.pop();                // Oxirgisini olib tashlash
console.log("pop:", mevalar);

mevalar.unshift("Shaftoli");  // Boshiga qo'shish
console.log("unshift:", mevalar);

mevalar.shift();              // Birinchisini olib tashlash
console.log("shift:", mevalar);

// === splice va slice ===
let sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

let kesilgan = sonlar.slice(2, 5); // [3, 4, 5] — asl massiv o'zgarmaydi
console.log("slice(2,5):", kesilgan);

sonlar.splice(3, 2); // index 3 dan 2 ta element o'chiradi
console.log("splice(3,2):", sonlar); // [1, 2, 3, 6, 7, 8, 9, 10]

// === forEach ===
console.log("\n=== forEach ===");
mevalar.forEach((meva, index) => {
    console.log(`${index + 1}. ${meva}`);
});

// === map — yangi massiv yaratish ===
let baholar = [85, 92, 78, 95, 68];
let oshirilgan = baholar.map(b => b + 5);
console.log("\nmap (+5):", oshirilgan);

// === filter — filtrlash ===
let yuqori = baholar.filter(b => b >= 80);
console.log("filter (>=80):", yuqori); // [85, 92, 95]

// === find — birinchi mos elementni topish ===
let birinchi90 = baholar.find(b => b >= 90);
console.log("find (>=90):", birinchi90); // 92

// === reduce — yig'ish ===
let jami = baholar.reduce((yigindi, b) => yigindi + b, 0);
let ortacha = jami / baholar.length;
console.log(`reduce (o'rtacha): ${ortacha.toFixed(1)}`); // 83.6

// === sort ===
let tartibsiz = [34, 7, 23, 32, 5, 62];
tartibsiz.sort((a, b) => a - b); // O'sish tartibida
console.log("\nsort (o'sish):", tartibsiz);

tartibsiz.sort((a, b) => b - a); // Kamayish tartibida
console.log("sort (kamayish):", tartibsiz);

// === includes, indexOf ===
console.log("\nincludes 'Nok':", mevalar.includes("Nok")); // true
console.log("indexOf 'Uzum':", mevalar.indexOf("Uzum"));  // 2

// === Spread operatori ===
let a = [1, 2, 3];
let b = [4, 5, 6];
let birlashgan = [...a, ...b];
console.log("\nspread:", birlashgan); // [1, 2, 3, 4, 5, 6]
