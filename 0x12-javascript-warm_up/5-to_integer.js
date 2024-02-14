#!/usr/local/bin/node
const args = process.argv;



arglen = args.length - 2;
if (arglen === 0){
    console.log('NO argument');
}
for (i = 2; i < args.length; i++)
{
    arguments = args[i];
    console.log(arguments);
}
