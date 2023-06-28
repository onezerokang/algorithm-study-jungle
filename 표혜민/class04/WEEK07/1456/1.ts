{
  const input = prompt("숫자 A B를 입력해주세요.") as string;
  if (!input) {
    console.log("입력값이 부적절합니다.");
  } else {
    const [A, B]: Array<number> = input.split(" ").map((v) => parseInt(v));
    const dv: number = Math.ceil(Math.sqrt(B));
    const primes: Array<boolean> = new Array(dv + 1).fill(true);
    primes[1] = false; //1은 소수가 아니다.
    for (let i = 2; i < dv + 1; i++) {
      //소수 계산
      if (primes[i]) {
        if (i * i > dv) {
          break;
        }
        for (let j = Math.pow(i, 2); j < dv + 1; j += i) {
          primes[j] = false;
        }
      }
    }

    let cnt: number = 0;
    for (let i = 1; i < primes.length; i++) {
      if (primes[i]) {
        let result = i * i;
        while (true) {
          if (result < A) {
            result *= i;
            continue;
          }
          if (result > B) {
            break;
          }
          result *= i;
          cnt += 1;
        }
      }
    }
    console.log(cnt);
  }
}
