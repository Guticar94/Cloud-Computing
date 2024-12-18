function(doc){
    if(doc.created_at && doc.geo){
        let len = Object.keys(doc.geo).length;
        const dateString = doc.created_at;
        let date = new Date(dateString);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const result = [year, month, day];
        if (len >0){
          emit(result,doc.geo['place_id'])
        }
    }
}