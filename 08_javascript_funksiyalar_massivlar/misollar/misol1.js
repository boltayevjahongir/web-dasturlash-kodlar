// 8-bob: Funksiyalar — declaration, expression, arrow

// === Function Declaration ===
function salom(ism) {
    return `Salom, ${ism}!`;
}
console.log(salom("Ali")); // "Salom, Ali!"

// === Function Expression ===
const kvadrat = function(n) {
    return n * n;
};
console.log(kvadrat(5)); // 25

// === Arrow Function ===
const kub = (n) => n ** 3;
console.log(kub(3)); // 27

// Bir necha qatorli arrow function
const faktorial = (n) => {
    if (n <= 1) return 1;
    return n * faktorial(n - 1);
};
console.log(`5! = ${faktorial(5)}`); // 120

// === Default parametrlar ===
function salamla(ism = "Mehmon", vaqt = "kun") {
    return `Xayrli ${vaqt}, ${ism}!`;
}
console.log(salamla());             // "Xayrli kun, Mehmon!"
console.log(salamla("Ali", "tong")); // "Xayrli tong, Ali!"

// === Rest parametr (...) ===
function yigindi(...sonlar) {
    return sonlar.reduce((s, n) => s + n, 0);
}
console.log(yigindi(1, 2, 3, 4, 5)); // 15

// === Callback funksiya ===
function amalBajar(a, b, amal) {
    return amal(a, b);
}
console.log(amalBajar(10, 5, (a, b) => a + b)); // 15
console.log(amalBajar(10, 5, (a, b) => a * b)); // 50

// === Objectlar ===
const talaba = {
    ism: "Ali",
    familiya: "Valiyev",
    yosh: 20,
    fanlar: ["Matematika", "Fizika", "Informatika"],
    toliqIsm() {
        return `${this.ism} ${this.familiya}`;
    }
};

console.log(talaba.toliqIsm()); // "Ali Valiyev"
console.log(talaba.fanlar[2]);  // "Informatika"

// Destructuring
const { ism, yosh, fanlar } = talaba;
console.log(`${ism}, ${yosh} yosh, ${fanlar.length} ta fan`);
