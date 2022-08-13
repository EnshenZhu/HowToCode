const fib2 = (n) => {
    if (n <= 2) {
        return 1
    }
    else {
        num1 = num2 = 1
        for (let idx = 3; idx <= n; idx++) {
            result = num1 + num2
            num1 = num2
            num2 = result
        }
        return result
    }
}

console.log(fib2(50))