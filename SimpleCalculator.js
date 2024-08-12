function calc(){

const a=parseFloat(document.getElementById("num1").value);
const b=parseFloat(document.getElementById("num2").value);

const add=a+b;
const sub=a-b;
const mult=a*b;
const div=a/b;

console.log(a,b,add,sub,mult,div)

document.getElementById("Result").innerHTML=`Addition: ${add}<br>
                Subtraction: ${sub}<br>
                Multiplication: ${mult}<br>
                Division: ${div}`;

}
