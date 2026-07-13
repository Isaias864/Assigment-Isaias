const colorBtn = document.getElementById('colorBtn');

const colors = [
  '#f0f4f8',
  '#fef3c7',
  '#d1fae5',
  '#dbeafe',
  '#fce7f3',
  '#ede9fe',
  '#ffedd5',
];

let currentIndex = 0;

colorBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % colors.length;
  document.body.style.backgroundColor = colors[currentIndex];
});
