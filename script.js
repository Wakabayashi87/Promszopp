const promos = [
  {shop:'Biedronka', product:'Pierś z kurczaka 1 kg', price:9.99, discount:-33},
  {shop:'Lidl', product:'Czekolada Milka 100 g', price:2.99, discount:-40},
  {shop:'Kaufland', product:'Jogurt naturalny 400 g', price:1.69, discount:-32},
  {shop:'Aldi', product:'Pomidory malinowe 500 g', price:4.99, discount:-29},
  {shop:'Netto', product:'Mleko UHT 3,2 % 1 l', price:2.49, discount:-22},
  {shop:'Dino', product:'Płatki owsiane 500 g', price:2.99, discount:-30},
  {shop:'Biedronka', product:'Ser Gouda 200 g', price:4.49, discount:-25},
  {shop:'Lidl', product:'Pomidory koktajlowe 250 g', price:3.99, discount:-35},
  {shop:'Kaufland', product:'Chleb pszenny 500 g', price:1.99, discount:-20},
  {shop:'Aldi', product:'Makaron świderki 500 g', price:2.49, discount:-38},
  {shop:'Netto', product:'Jajka M 10 szt.', price:4.99, discount:-28},
  {shop:'Dino', product:'Serek wiejski 150 g', price:1.19, discount:-26},
  {shop:'Biedronka', product:'Kanapki serowe 4 szt.', price:3.49, discount:-30},
  {shop:'Lidl', product:'Sok pomarańczowy 1 l', price:2.99, discount:-33},
  {shop:'Kaufland', product:'Ogórki kiszone 900 g', price:3.99, discount:-27},
  {shop:'Aldi', product:'Cukier trzcinowy 1 kg', price:3.29, discount:-25},
  {shop:'Netto', product:'Kawa mielona 250 g', price:8.99, discount:-31},
  {shop:'Dino', product:'Kanapki z szynką 4 szt.', price:3.99, discount:-28},
  {shop:'Biedronka', product:'Herbata czarna 50 g', price:2.19, discount:-35},
  {shop:'Lidl', product:'Ser Mozzarella 125 g', price:3.49, discount:-30},
  {shop:'Kaufland', product:'Masło 200 g', price:4.29, discount:-32},
  {shop:'Aldi', product:'Przyprawa gyros 50 g', price:1.99, discount:-20},
  {shop:'Netto', product:'Żel pod prysznic 250 ml', price:2.79, discount:-24},
  {shop:'Dino', product:'Ser feta 150 g', price:3.79, discount:-26}
];

// aktualna data
const todaySpan = document.getElementById('today');
todaySpan.textContent = new Date().toLocaleDateString('pl-PL', {day:'numeric', month:'long', year:'numeric'});
document.getElementById('lastUpdate').textContent = new Date().toLocaleString('pl-PL');

const shopNav = document.getElementById('shopNav');
const promoGrid = document.getElementById('promoGrid');

const shops = [...new Set(promos.map(p => p.shop))].sort();

// przyciski sklepów
shops.forEach(shop => {
  const btn = document.createElement('a');
  btn.className = 'btn btn-outline-light btn-sm';
  btn.href = `#${shop.toLowerCase()}`;
  btn.textContent = shop;
  shopNav.appendChild(btn);
});

// sekcje promocji
shops.forEach(shop => {
  const section = document.createElement('section');
  section.className = 'col-12';
  section.id = shop.toLowerCase();
  section.innerHTML = `<h3 class="mt-4">${shop}</h3>`;

  const row = document.createElement('div');
  row.className = 'row g-3';

  promos.filter(p => p.shop === shop).forEach(p => {
    const card = document.createElement('div');
    card.className = 'col-6 col-md-4 col-lg-3';
    card.innerHTML = `
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h6 class="card-title">${p.product}</h6>
          <p class="mb-1"><strong>${p.price.toFixed(2)} zł</strong></p>
          <span class="badge bg-danger">${p.discount}%</span>
        </div>
      </div>`;
    row.appendChild(card);
  });
  section.appendChild(row);
  promoGrid.appendChild(section);
});

document.getElementById('count').textContent = promos.length;
