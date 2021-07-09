# Building an API with the Serverless Framework

This is a companion project to my blog post [building an api with the serverless framework](https://rhythmandbinary.com/post/2021-07-09-building-an-api-with-the-serverless-framework).

Check out my post and the [serverless getting started page](https://www.serverless.com/framework/docs/getting-started/) for more.

This API has basic endpoints for Create, Read, Update, and Delete (CRUD) operations. Its a very simple meal planning API.

If you follow along in my post, the body that is returned from the API generally looks like this:

```json
[
  {
    "updatedAt": 1625837107257,
    "username": "1234",
    "meals": [
      {
        "lunch": "sandwhich",
        "breakfast": "cereal",
        "day": "0",
        "dinner": "chicken"
      },
      {
        "lunch": "",
        "breakfast": "",
        "day": "1",
        "dinner": ""
      },
      {
        "lunch": "",
        "breakfast": "",
        "day": "2",
        "dinner": ""
      },
      {
        "lunch": "",
        "breakfast": "",
        "day": "3",
        "dinner": ""
      },
      {
        "lunch": "",
        "breakfast": "",
        "day": "4",
        "dinner": ""
      },
      {
        "lunch": "",
        "breakfast": "",
        "day": "5",
        "dinner": ""
      },
      {
        "lunch": "pizza",
        "breakfast": "oatmeal",
        "day": "6",
        "dinner": "lasagna"
      }
    ]
  }
]
```

When you call the `create` endpoint it will create a blank set of values to start with. Just make sure to pass a `username` as that will be how the data is keyed in DyanmoDB. Here is a sample body for the `create` endpoint:

```json
{
  "username": "1234"
}
```
