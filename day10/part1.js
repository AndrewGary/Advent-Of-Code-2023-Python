const fs = require('fs');

const input = fs.readFileSync('./input.txt').toString()

grid = input.split('\r\n').map(item => {
    const ra = []

    for(i = 0; i < item.length; i++){
        ra.push(item[i])
    }

    return ra
});

const findStartCords = (matrix) => {

    for(let i = 0; i < matrix.length; i++){
        if(matrix[i].includes('S')){
            const columnNumber = matrix[i].indexOf('S')

            return [i, columnNumber];
        }
    }
}

const part1 = (grid) => {

    path = []
    const startCords = findStartCords(grid);
    path.push(startCords)


    let startCount = 0;

    const pathSet = []

    let count = 0;
    while(true){


        count++
        currentNode = path[path.length - 1]
        currentLine = currentNode[0]
        currentColumn = currentNode[1]
        currentValue = grid[currentLine][currentColumn]
        prevLine = currentValue === 'S' ? 'NA' : path[path.length - 2][0]
        prevColumn = currentValue === 'S' ? 'NA' : path[path.length -2][1]

        // if(currentValue == 'S'){
        //     startCount++
        // }
        // if(currentValue === 'S' && startCount > 1){
        //     console.log('YES');
        // }
        // console.log(`Current Value: ${currentValue} -- Line: ${currentLine} -- Column: ${currentColumn}`)


        // console.log('startCount: ', startCount);

        if(currentValue === 'S'){
            startCount++
            if(startCount === 2){
                break;
            }
        }

        if(currentValue === 'S'){
            if(grid[currentLine - 1][currentColumn] === '|' || grid[currentLine - 1][currentColumn] === 'F' || grid[currentLine - 1][currentColumn] === '7'){
                path.push([currentLine - 1, currentColumn])
                const idk = `${currentLine -1}-${currentColumn}`
                if(pathSet.includes(idk)){
                    console.log('OUTTTTT')
                    return
                }else{
                    pathSet.push(idk)
                }
                continue;
            }
        }


        let option1, option2;

        if(currentValue === '-'){
            option1 = [currentLine, currentColumn - 1]
            option2 = [currentLine, currentColumn + 1]
        }else if(currentValue === '|'){
            option1 = [currentLine - 1, currentColumn]
            option2 = [currentLine + 1, currentColumn]
        }else if(currentValue === 'F'){
            option1 = [currentLine + 1, currentColumn]
            option2 = [currentLine, currentColumn + 1]
        }else if(currentValue === '7'){
            option1 = [currentLine + 1, currentColumn]
            option2 = [currentLine, currentColumn - 1]
        }else if(currentValue === 'J'){
            option1 = [currentLine - 1, currentColumn]
            option2 = [currentLine, currentColumn - 1]
        }else if(currentValue === 'L'){
            option1 = [currentLine - 1, currentColumn]
            option2 = [currentLine, currentColumn + 1]
        }

        option1Value = grid[option1[0]][option1[1]]
        option2Value = grid[option2[0]][option2[1]]

        if(option1Value === 'S'){
            path.push(option2)
            const idk = `${option2[0]}-${option2[1]}`
            if(pathSet.includes(idk)){
                console.log('OUTTAHERE')
                return;
            }else{
                pathSet.push(idk)
            }
            continue;
        }

        if(option2Value === 'S'){
            path.push(option1)
            const idk = `${option1[0]}-${option1[1]}`
            if(pathSet.includes(idk)){
                console.log(currentLine)
                console.log(currentColumn)
                console.log(currentValue)

                console.log(count)

                console.log(path[0])
                console.log(path[1])
                console.log('OUTTAAAAAAA')
                return;
            }else{
                pathSet.push(idk)
            }
            continue;
        }

        if(option1[0] == prevLine && option1[1] === prevColumn){
            path.push(option2)
            const idk = `${option2[0]}-${option2[1]}`
            if(pathSet.includes(idk)){
                console.log('OUTTAHERE')
                return;
            }else{
                pathSet.push(idk)
            }
            continue;
        }

        if(option2[0] === prevLine && option2[1] === prevColumn){
            path.push(option1)
            const idk = `${option1[0]}-${option1[1]}`
            if(pathSet.includes(idk)){

                
                console.log('OUTTAAAAAAA2')
                return
            }else{
                pathSet.push(idk)
            }
            continue;
        }


        // console.log('currentValue: ', currentValue);
        // console.log('option1: ', option1);
        // console.log('option2: ', option2);

        // if(option1[0] === prevLine && option1[2] === prevColumn){
        //     console.log(`selecting option2`)
        //     path.push(option2)
        // }else{
        //     console.log(`selecting option1`)
        //     path.push(option1)
        // }



    }

    // console.log(path.length)
    

}

const part2 = (grid) => {
}

console.log('Part 1: ', part1(grid))
console.log('Part 2: ', part2(grid))




