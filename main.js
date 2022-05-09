const flag = true;

const myPromise = new Promise((resolve, reject) => {
  if (flag) {
    resolve("Успешное выполнение promise");
  } else {
    reject("Неуспешное выполнение promise");
  }
});