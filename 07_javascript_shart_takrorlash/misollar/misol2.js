// 7-bob: for, while, do...while sikllari

// === for sikli ===
console.log("=== for sikli ===");
for (let i = 1; i <= 5; i++) {
    console.log(`Qator ${i}`);
}

// Teskari hisoblash
console.log("\n=== Teskari hisoblash ===");
for (let i = 10; i >= 1; i--) {
    process.stdout.write(i + " ");
}
console.log();

// === while sikli ===
console.log("\n=== while sikli ===");
let son = 1;
let yigindi = 0;
while (son <= 100) {
    yigindi += son;
    son++;
}
console.log(`1 dan 100 gacha yig'indi: ${yigindi}`); // 5050

// === do...while sikli ===
console.log("\n=== do...while sikli ===");
let x = 1;
do {
    console.log(`x = ${x}`);
    x *= 2;
} while (x <= 16);

// === for...of (massiv elementlari) ===
console.log("\n=== for...of ===");
let mevalar = ["Olma", "Nok", "Uzum", "Anor"];
for (let meva of mevalar) {
    console.log(`Meva: ${meva}`);
}

// === for...in (object kalitlari) ===
console.log("\n=== for...in ===");
let talaba = { ism: "Ali", yosh: 20, fakultet: "Fizmat" };
for (let kalit in talaba) {
    console.log(`${kalit}: ${talaba[kalit]}`);
}

// === break va continue ===
console.log("\n=== break ===");
for (let i = 1; i <= 10; i++) {
    if (i === 6) break; // 6 da to'xtaydi
    console.log(i);
}

console.log("\n=== continue ===");
for (let i = 1; i <= 10; i++) {
    if (i % 2 === 0) continue; // Juft sonlarni o'tkazadi
    console.log(i); // Faqat toq: 1, 3, 5, 7, 9
}

// === Ichma-ich sikllar ===
console.log("\n=== Ko'paytirish jadvali (3x3) ===");
for (let i = 1; i <= 3; i++) {
    let qator = "";
    for (let j = 1; j <= 3; j++) {
        qator += `${i}x${j}=${i*j}\t`;
    }
    console.log(qator);
}
