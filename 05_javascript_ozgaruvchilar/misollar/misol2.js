// 5-bob: Ma'lumot turlari va type conversion

// === Asosiy ma'lumot turlari ===

// String
let ism = "Boltayev Jahongir";
console.log(typeof ism); // "string"

// Number
let yosh = 25;
let narx = 99.99;
console.log(typeof yosh);  // "number"
console.log(typeof narx);  // "number"

// Boolean
let aktiv = true;
console.log(typeof aktiv); // "boolean"

// Undefined
let noaniq;
console.log(typeof noaniq); // "undefined"

// Null
let bosh = null;
console.log(typeof bosh); // "object" (bu JS ning tarixiy xatosi)

// Object
let talaba = { ism: "Ali", yosh: 20 };
console.log(typeof talaba); // "object"

// Array (aslida object)
let fanlar = ["Matematika", "Fizika", "Informatika"];
console.log(typeof fanlar);          // "object"
console.log(Array.isArray(fanlar));   // true

// === Type Conversion ===

// Stringga o'tkazish
let son = 42;
console.log(String(son));       // "42"
console.log(son.toString());    // "42"
console.log(son + "");          // "42"

// Songa o'tkazish
let matn = "123";
console.log(Number(matn));      // 123
console.log(parseInt(matn));    // 123
console.log(parseFloat("3.14")); // 3.14
console.log(+"456");            // 456 (unary plus)

// Booleanga o'tkazish
console.log(Boolean(1));        // true
console.log(Boolean(0));        // false
console.log(Boolean(""));       // false
console.log(Boolean("salom"));  // true
console.log(Boolean(null));     // false
console.log(Boolean(undefined)); // false

// === Template Literals ===
let studentIsm = "Ali";
let studentYosh = 20;
let xabar = `Salom, mening ismim ${studentIsm}, yoshim ${studentYosh} da.`;
console.log(xabar);

// Ko'p qatorli matn
let html = `
<div>
    <h1>${studentIsm}</h1>
    <p>Yoshi: ${studentYosh}</p>
</div>
`;
console.log(html);
