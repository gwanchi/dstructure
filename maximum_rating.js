data = [{
    "page": 1,
    "totalPages": 5,
    "data": [{
        "title": "Movie 1",
        "rating": 4.7
    }, {
        "title": "Movie 2",
        "rating": 7.8
    }]
}, {
    "page": 2,
    "totalPages": 5,
    "data": [{
        "title": "Movie 3",
        "rating": 5.1
    }, {
        "title": "Movie 4",
        "rating": 2.4
    }]
}];

ratings = data.map(values => {return values.data.map(v => {return v.rating})});
ratings = ratings.flat();
average = ratings.reduce((a,b) => a + b, 0) / ratings.length;
console.log(`Average rating : ${average}`);
console.log(`Maximum rating : ${Math.max(...ratings)}`);