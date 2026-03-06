const { textSpanOverlapsWith, NewLineKind } = require("typescript");

const message="this is my first message";//primitive type
console.log(typeof message);
const message1 = new String("hello");//object type
console.log(typeof message1);
//primitive type automatically converts into object wherenever required
//example
console.log(message.toLowerCase);
console.log(message.length);
//object consumes more memory to store 
//primitive takes the less memory
message[0];
message[1];
message.includes('my');
message.includes('not');
message.startsWith('my');
message.endsWith('message');
message.indexOf('my');
message.replace('first','second'); //this is my second message
//it creates the new string doesnot modify the original message
console.log(message);//this is my first message
message.trim();
message.trimLeft();
message.trimRight();
//use the string documentation from the google for the escape notation
 /* \0 the null Character
\' single quote
\" double quote
\\ backslash
\n NewLine
\r carriagereturn 
\v vertical tab 
\t tab
*/
const message2= ' this is mine\'s ';
console.log(message2);
const message3 = "welcome to \n javascript class";
message.split(" ");