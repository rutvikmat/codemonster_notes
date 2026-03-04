const prices = [10, 20, 30];
const taxRate = 0.1;

// Adding 10% tax to each price
const pricesWithTax = prices.map(price => price + (price * taxRate));

console.log(pricesWithTax);