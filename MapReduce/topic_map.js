
function(doc){
    if(doc.created_at && doc.topics){
        const dateString = doc.created_at;
        const date = new Date(dateString);
        const year = date.getFullYear();
        const month = date.getMonth() + 1;
        const day = date.getDate();
        const result = [year, month, day];
        for (let i =0;i<doc.topics.length;i++){
            emit(result,doc.topics[i]);
        }

    }
}