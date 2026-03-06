//different types of literals present
//Object {}
//Boolean true, false
//String '' , ""
//Template literal ``

//below is the string literal example
const message='this is my \n first message';
console.log(message);
const message1=
'this is my\n'+ 
'\'first\' message';
console.log(message1);

//Template literal example
const message3 = `this is 
'JavaScript' example`;
console.log(message3);

const emailMessage = 
`Hello Team,
    Thank you for the joining the session.
    
Thanks & Regards,
Abc`;
console.log(emailMessage);

//another use of template literal is adding the dynamic values in the 
//message 

const name1='Techspiration';
const message4 = 'Welcome to the'+" "+name1;
console.log(message4);

const message5 = `welcome to the ${name1} office at ${5+5} am`;
console.log(message5);
