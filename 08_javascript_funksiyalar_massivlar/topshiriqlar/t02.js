// Topshiriq 2 (O'rta): Massiv metodlari bilan talabalar statistikasi

// Berilgan ma'lumotlar:
const talabalar = [
    { ism: "Ali", ball: 92, guruh: "A" },
    { ism: "Vali", ball: 78, guruh: "B" },
    { ism: "Guli", ball: 65, guruh: "A" },
    { ism: "Dildora", ball: 88, guruh: "B" },
    { ism: "Eldor", ball: 45, guruh: "A" },
    { ism: "Farida", ball: 95, guruh: "B" },
    { ism: "Ganisher", ball: 71, guruh: "A" },
    { ism: "Hulkar", ball: 83, guruh: "B" },
];

// 1. map bilan: Har bir talabaga "baho" xususiyati qo'shing
//    (86+ = "A'lo", 71+ = "Yaxshi", 56+ = "Qoniqarli", boshqa = "Qoniqarsiz")

// 2. filter bilan: Faqat "A" guruh talabalarini ajratib oling

// 3. reduce bilan: Barcha talabalarning o'rtacha ballini hisoblang

// 4. sort bilan: Talabalarni ball bo'yicha kamayish tartibida saralang

// 5. find bilan: Balli 90 dan yuqori birinchi talabani toping

// 6. every va some bilan:
//    - Barcha talabalar o'tganmi (ball >= 56)?
//    - Kamida bitta a'lochi bormi (ball >= 86)?
