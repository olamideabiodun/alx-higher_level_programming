#!/usr/bin/node
const args = process.argv;
arglen = args.length - 3;
if (arglen === 0){
    console.log(`${args[arglen]} is ${args[arglen]}`);
}else{
    console.log(`${args[2]} is ${args[3]}`);
}
