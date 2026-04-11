// 7-bob: if/else va switch misollari

// === if / else if / else ===
let ball = 82;

if (ball >= 86) {
    console.log("A'lo");
} else if (ball >= 71) {
    console.log("Yaxshi");  // Bu ishlaydi
} else if (ball >= 56) {
    console.log("Qoniqarli");
} else {
    console.log("Qoniqarsiz");
}

// === Ichma-ich if ===
let yosh = 20;
let guvohnoma = true;

if (yosh >= 18) {
    if (guvohnoma) {
        console.log("Haydash mumkin");
    } else {
        console.log("Guvohnoma oling");
    }
} else {
    console.log("Yoshingiz yetmaydi");
}

// === switch operatori ===
let kun = 3;

switch (kun) {
    case 1:
        console.log("Dushanba");
        break;
    case 2:
        console.log("Seshanba");
        break;
    case 3:
        console.log("Chorshanba"); // Bu ishlaydi
        break;
    case 4:
        console.log("Payshanba");
        break;
    case 5:
        console.log("Juma");
        break;
    case 6:
    case 7:
        console.log("Dam olish kuni");
        break;
    default:
        console.log("Noto'g'ri kun raqami");
}

// === switch bilan fasl aniqlash ===
let oy = "Aprel";

switch (oy) {
    case "Dekabr":
    case "Yanvar":
    case "Fevral":
        console.log("Qish");
        break;
    case "Mart":
    case "Aprel":
    case "May":
        console.log("Bahor"); // Bu ishlaydi
        break;
    case "Iyun":
    case "Iyul":
    case "Avgust":
        console.log("Yoz");
        break;
    default:
        console.log("Kuz");
}
