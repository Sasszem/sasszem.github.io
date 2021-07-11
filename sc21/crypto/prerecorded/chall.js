#!/usr/bin/env node

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
rl.on("close", () => {
  yellow("These horoscopes are real!");
  process.exit(1);
});

const ask = (q) => new Promise((resolve) => rl.question(q, (s) => resolve(s)));

const flag = process.env["FLAG"];
if (flag === undefined) {
  console.log("Missing flag, please contact admin"); process.exit(2);
}

const horoscopes = require('fs').readFileSync('horoscopes.txt', 'ascii', function (err,data) {
  if (err) {
    return console.log(err);
  }
}).split("\n"); 

setTimeout(() => {
  console.log("I don't have all day! I have to Look out for a succulent that sings near a moonstone.");
  process.exit(3);
}, 30 * 1000);

const H = 14;
const S = 7;

const main = async () => {
  console.log(`Node version ${process.version}`);
  console.log(`Here are the first two weeks of horoscopes I got from the trial version of Horoscopist.`);
  
  for (let i = 0; i < H; i++) {
    console.log(horoscopes[Math.floor(Math.random()*horoscopes.length)]);
  }

  console.log("Tell me the 3rd week's horoscopes!")
  
  for (let i = 0; i < S; i++) {
    const h = horoscopes[Math.floor(Math.random()*horoscopes.length)];
    const s = await ask(`Horoscope ${i + 1}? `);
    if (s !== h) {
      console.log("Don't waste my time! These horoscopes are always accurate!");
      process.exit(0);
    }
  }

  console.log("How? They are always super accurate for me. Don't tell me, are you a sage?", flag);
  process.exit(0);
};

main().finally(() => process.exit(6));
