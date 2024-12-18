function(doc){
    if(doc.created_at && doc.sentiment_analysis){
        const dateString = doc.created_at;
        let date = new Date(dateString);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const result = [year, month, day];
        let flg = 0;

        if (doc.sentiment_analysis ==="POSITIVE"){
            flg = 1
        }
        emit(result,flg)

    }
}