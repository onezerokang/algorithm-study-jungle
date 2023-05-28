{
  const n: string | null = prompt("숫자의 개수를 입력해주세요.");
  const N: number = n ? parseInt(n) : 0;
  if (N >= 1 && N <= 1000000) {
    const numbers: string | null = prompt(
      "숫자들을 빈칸을 사이에 두고 입력해주세요."
    );
    const nums: Array<number> = numbers
      ? numbers.split(" ").map((v) => parseInt(v))
      : [];
    if (nums.length === N) {
      const dict = new Map();
      const numsCopy: Array<number> = [];
      nums.map((v) => (numsCopy.includes(v) ? numsCopy : numsCopy.push(v)));
      numsCopy.sort();
      numsCopy.map((item, idx) => dict.set(item, idx));
      nums.map((v) => console.log(dict.get(v)));
    } else {
      console.log("입력한 숫자의 개수가 불일치합니다.");
    }
  } else {
    console.log("숫자 N의 개수가 부적절합니다. (1 ≤ N ≤ 1,000,000)");
  }
}

/**
   * test1
   * 
   * input
  5
  2 4 -10 4 -9
   * output
  2 3 0 3 1
   * 
   * test2
  6
  1000 999 1000 999 1000 999
  * output
  1 0 1 0 1 0
  
   */
