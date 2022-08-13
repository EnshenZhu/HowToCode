// this solution is right but be very slow when n is a large number
// we say this solution is in a recursive method

const fib = (n) => {
    if (n <= 2) {
        return 1;
    }

    return fib(n - 1) + fib(n - 2)
}

// console.log(fib(6))
// console.log(fib(7))
console.log(fib(50))

// time complexity O(2^n) check the following link for explanation
// https://syedtousifahmed.medium.com/fibonacci-iterative-vs-recursive-5182d7783055#:~:text=Time%20Complexity%3A&text=Hence%20the%20time%20taken%20by,2%5En)%20or%20exponential.

// space complexity O(n)