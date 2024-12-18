function(keys,values,rereduce){
    let map = new Map();
    if (rereduce){
        for(let i =0;i<values.length;i++){
            for (let j =0;j<values[i].length;j++){
                let num  = (map.get(values[i][j][0]) || 0)+values[i][j][1];
                map.set(values[i][j][0],num)
            }

        }
    }else{
        for (let i=0;i<values.length;i++){
            let num  = (map.get(values[i]) || 0)+1;
            map.set(values[i],num);
        }

    }
    return Array.from(map)
}