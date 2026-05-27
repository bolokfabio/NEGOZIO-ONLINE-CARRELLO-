
// =========================
// 🔵 AGGIUNGI
// =========================
async function aggiungi() {

    const prodotto = document.getElementById("prodotto").value;
    const prezzo = document.getElementById("prezzo").value;
    const quantita = document.getElementById("quantita").value;

    await fetch("/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `prodotto=${prodotto}&prezzo=${prezzo}&quantita=${quantita}`
    });

    const res = await fetch("/lista");
    const data = await res.json();

    document.getElementById("out").innerText =
        "Prodotti: " + data.length;
}


// =========================
// 🔵 LISTA
// =========================
async function lista() {

    await fetch("/lista", { method: "POST" });

    const res = await fetch("/lista");
    const data = await res.json();

    let text = "";

    data.forEach(p => {
        text += p.prodotto + " - " + p.prezzo + "€ x " + p.quantita + "\n";
    });

    document.getElementById("out").innerText = text;
}


// =========================
// 🔵 TOTALE
// =========================
async function totale() {

    await fetch("/totale", { method: "POST" });

    const res = await fetch("/totale");
    const data = await res.json();

    document.getElementById("out").innerText =
        "Totale carrello: " + data.totale + "€";
}


// =========================
// 🔵 COSTOSI
// =========================
async function costosi() {

    await fetch("/costosi", { method: "POST" });

    const res = await fetch("/costosi");
    const data = await res.json();

    let text = "";

    data.forEach(p => {
        text += p.prodotto + " - totale: " + (p.prezzo * p.quantita) + "€\n";
    });

    document.getElementById("out").innerText = text;
}
