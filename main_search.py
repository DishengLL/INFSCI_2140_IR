# import IndexingWithWhoosh.MyIndexReader as MyIndexReader
import Search.QueryRetreivalModel as QueryRetreivalModel
import Search.ExtractQuery as ExtractQuery
import datetime
import Indexing.MyIndexReader as MyIndexReader

startTime = datetime.datetime.now()

index = MyIndexReader.MyIndexReader()

search = QueryRetreivalModel.QueryRetrievalModel(index)
s = input('input query: ')
extractor = ExtractQuery.ExtractQuery(s)

queries= extractor.getQuries()
for query in queries:
    ##print(query.topicId,"\t",query.queryContent)
    results = search.retrieveQuery(query, 20)
    rank = 1
    for result in results:
        print(result.getDocNo(),' ',rank," ",result.getScore())
        rank = rank +1

endTime = datetime.datetime.now()
print ("load index & retrieve the token running time: ", endTime - startTime)