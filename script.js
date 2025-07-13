const promos = [
  {shop:'Biedronka', product:'Pierś z kurczaka 1 kg', price:'9,99 zł', discount:'-33 %'},
  {shop:'Lidl', product:'Czekolada Milka 100 g', price:'2,99 zł', discount:'-40 %'},
  {shop:'Kaufland', product:'Jogurt naturalny 400 g', price:'1,69 zł', discount:'-32 %'},
  {shop:'Aldi', product:'Pomidory malinowe 500 g', price:'4,99 zł', discount:'-29 %'},
  {shop:'Netto', product:'Mleko UHT 1 l', price:'2,49 zł', discount:'-22 %'},
  {shop:'Dino', product:'Płatki owsiane 500 g', price:'2,99 zł', discount:'-30 %'},
  {shop:'Biedronka', product:'Ser Gouda 200 g', price:'4,49 zł', discount:'-25 %'},
  {shop:'Lidl', product:'Pomidory koktajlowe 250 g', price:'3,99 zł', discount:'-35 %'},
  {shop:'Kaufland', product:'Chleb pszenny 500 g', price:'1,99 zł', discount:'-20 %'},
  {shop:'Aldi', product:'Makaron świderki 500 g', price:'2,49 zł', discount:'-38 %'},
  {shop:'Netto', product:'Jajka M 10 szt.', price:'4,99 zł', discount:'-28 %'},
  {shop:'Dino', product:'Serek wiejski 150 g', price:'1,19 zł', discount:'-26 %'},
  {shop:'Biedronka', product:'Kanapki serowe 4 szt.', price:'3,49 zł', discount:'-30 %'},
  {shop:'Lidl', product:'Sok pomarańczowy 1 l', price:'2,99 zł', discount:'-33 %'},
  {shop:'Kaufland', product:'Ogórki kiszone 900 g', price:'3,99 zł', discount:'-27 %'},
  {shop:'Aldi', product:'Cukier trzcinowy 1 kg', price:'3,29 zł', discount:'-25 %'},
  {shop:'Netto', product:'Kawa mielona 250 g', price:'8,99 zł', discount:'-31 %'},
  {shop:'Dino', product:'Kanapki z szynką 4 szt.', price:'3,99 zł', discount:'-28 %'},
  {shop:'Biedronka', product:'Herbata czarna 50 g', price:'2,19 zł', discount:'-35 %'},
  {shop:'Lidl', product:'Ser Mozzarella 125 g', price:'3,49 zł', discount:'-30 %'},
  {shop:'Kaufland', product:'Masło 200 g', price:'4,29 zł', discount:'-32 %'},
  {shop:'Aldi', product:'Przyprawa gyros 50 g', price:'1,99 zł', discount:'-20 %'},
  {shop:'Netto', product:'Żel pod prysznic 250 ml', price:'2,79 zł', discount:'-24 %'},
  {shop:'Dino', product:'Ser feta 150 g', price:'3,79 zł', discount:'-26 %'}
];

promos.sort((a,b)=>parseInt(b.discount)-parseInt(a.discount));

const grid = document.getElementById('promoGrid');
const search = document.getElementById('search');
const shopNav = document.getElementById('shopNav');

const shops = [...new Set(promos.map(p=>p.shop))];

shops.forEach(s=>{
  shopNav.insertAdjacentHTML('beforeend', `<button class="btn btn-sm btn-outline-light" data-shop="${s}">${s}</button>`);
});

function render(list){
  grid.innerHTML = '';
  shops.forEach(shop=>{
    const items = list.filter(p=>p.shop===shop);
    if(!items.length) return;
    grid.insertAdjacentHTML('beforeend', `<div class="col-12 section-header">${shop}</div>`);
    items.forEach(p=>{
      grid.insertAdjacentHTML('beforeend', `
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
          <div class="card card-promo h-100">
            <div class="card-header d-flex justify-content-between">
              <span class="shop-badge ${shop.toLowerCase()}">${shop}</span>
              <span class="badge bg-danger">${p.discount}</span>
            </div>
            <div class="card-body">
              <h6 class="card-title">${p.product}</h6>
              <p class="fw-bold text-success mb-0">${p.price}</p>
            </div>
          </div>
        </div>
      `);
    });
  });
  document.getElementById('count').textContent = list.length;
}

render(promos);

search.addEventListener('input', ()=>{
  const v = search.value.toLowerCase();
  render(promos.filter(p=>p.product.toLowerCase().includes(v) || p.shop.toLowerCase().includes(v)));
});

shopNav.addEventListener('click', e=>{
  if(e.target.dataset.shop){
    const shop = e.target.dataset.shop;
    render(promos.filter(p=>p.shop===shop));
  }
});

const today = new Date().toLocaleDateString('pl-PL');
document.getElementById('today').textContent = `(${today})`;
document.getElementById('lastUpdate').textContent =
  new Date().toLocaleString('pl-PL', {day:'2-digit', month:'2-digit', year:'numeric', hour:'2-digit', minute:'2-digit'});
