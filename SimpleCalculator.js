function calc(){

const x=parseFloat(document.getElementById("num1").value);
const y=parseFloat(document.getElementById("num2").value);
const operation = document.querySelector('input[name="operation"]:checked').value;

let result;
console.log(x,y,operation)
switch(operation) {
    case 'addition':
        result = `Addition: ${x + y}`;
        break;
    case 'subtraction':
        result = `Subtraction: ${x - y}`;
        break;
    case 'multiplication':
        result = `Multiplication: ${x * y}`;
        break;
    case 'division':
        result = y !== 0 ? `Division: ${x / y}` : 'Cannot divide by zero';
        break;
    default:
        result = 'Please select an operation.';
}

document.getElementById("Result").innerHTML = result;

}
