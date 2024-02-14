#!/usr/bin/node
const args = process.argv;
arglen = args.length - 2;

if (arglen === 0)
{
    console.log('NO argument');
}else{
    console.log(args[2]);
}
