// const jeah = 'threerznlrhtkjp23mtflmbrzq395three'

// const value = jeah[0];

// const charcodetest = '0123456789';

// const isNumber = (character) => {
//     if(character.charCodeAt(0) >= 48 && character.charCodeAt(0) <= 57){
//         return true
//     }

//     return false
// }




// for(let i = 0; i < charcodetest.length; i++){
//     console.log(`${charcodetest[i]} --> ${charcodetest.charCodeAt(i)}`)
// }

// console.log('isNumber(charcodetest[0]): ', isNumber(charcodetest[0]));
// console.log('isNumber(jeah[0]): ', isNumber(jeah[0]));

// return;

// let testing = '';

// for(let i = 0; i < jeah.length; i++){

//     co
//     console.log(jeah[i]);
//     console.log(typeof Number(jeah[i]));
// }


// console.log(typeof Number('9'));
// return;


const fs = require('fs');

const idk = fs.readFileSync('./input.txt', 'utf-8');

const array = idk.split('\r\n');

const isNumber = (character) => {
    if(character.charCodeAt(0) >= 48 && character.charCodeAt(0) <= 57){
        return true
    }

    return false
}

// console.log(array);

let answer = 0;

let index = 0; 


for(const line of array){

    let lp = 0;
    let rp = line.length - 1;

    let leftValue, rightValue;

    do{
        if(lp >= rp)break;

        // console.log(`lp: ${line[lp]}`);
        // console.log(`rp: ${line[rp]}`);

        if(!leftValue && isNumber(line[lp])){
            // console.log(`selecting left value at lp(index): ${lp}`);
            leftValue = line[lp];
        } 
        if(!rightValue && isNumber(line[rp])){
            // console.log(`selecting right value at rp(index): ${rp}`);
            rightValue = line[lp]
        } 

        lp++;
        rp--;



    }while(!leftValue || !rightValue)

    const numString = leftValue + rightValue;
    console.log('numString: ', numString);

    const numVersion = Number(numString);

    // console.log(numVersion);
    answer += numVersion;
    
    // for(let i = 0; i < line.length; i++){
    //     if(typeof Number(line[i]) === 'number'){
    //         leftValue = line[i];
    //         break;
    //     } 

    // }

    // for(let i = line.length - 1; i >= 0; i--){
    //     if( isNumber(line[i])){
    //         rightValue = line[i];
    //         break;
    //     }
    // }

    // const valueString = leftValue + rightValue;
    // console.log('valueString: ', valueString);
    // const valueNumber = Number(valueString);
    // // console.log('valueNumber: ', valueNumber);

    // answer += valueNumber;


}

console.log('answer: ', answer);