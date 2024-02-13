#!/usr/bin/node
const args = process.args;
len = args.length

if (len == 1){
    console.log('NO argument');
}
else if (len == 3)
{
    console.log('Argument found');
}else{
    console.log('Arguments found');
}
