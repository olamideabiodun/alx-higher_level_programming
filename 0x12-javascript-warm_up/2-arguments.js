#!/usr/bin/node
const args = process.argv;
len = args.length - 2;

if (len === 0){
    console.log('NO argument');
}
else if (len === 1)
{
    console.log('Argument found');
}else{
    console.log('Arguments found');
}
