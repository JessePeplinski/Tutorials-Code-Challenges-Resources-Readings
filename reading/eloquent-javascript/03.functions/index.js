// Minimum
function min(num1, num2) {
    if(num1 > num2) {
        return num2;
    }
    else if(num1 < num2) {
        return num1;
    }
    else {
        return 0;
    }
}

console.log(min(2, 1));

// Recursion
function isEven(num) {
    if(num === 0) return true;
    else if (n === 1) return false;
    else return isEven(n - 2);
}

// Bean Counting 
function countChars(string, character) {
    let result = string.split('');
    let count = 0;

    for (let i = 0; i < result.length; i++) {   
        if (result[i] === character) {
            count++;
        }
    }

    return count;
}

console.log(countChars("kakkerlak", "k"));