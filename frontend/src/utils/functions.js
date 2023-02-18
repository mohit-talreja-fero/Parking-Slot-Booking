export function getToday() {
  return new Date().toISOString().slice(0, 10);
}

export function dateTimeConstructor(date, time) {
  /* 
    INPUT:      date: "2023-01-26"
    INPUT:      time: "13:59"
    OUTPUT:     date_time: "2023-01-26 13:59",
  */
  return `${date} ${time}`;
}

export async function waitForNSeconds(n) {
  await new Promise((resolve) => {
    return setTimeout(resolve, n * 1000);
  });
}
