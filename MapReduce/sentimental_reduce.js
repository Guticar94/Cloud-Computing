function(keys,values,rereduce){
    let posNum = 0;
    let total = 0;
    for (let i =0;i<values.length;i++){

        if(rereduce){
            total += values[i][1]
            posNum +=values[i][0]
        }else{
            total++;
            if(values[i] === 1){
                posNum++;
            }
        }
    }
    //[postive num, total num]
    return [posNum,total]

}