

use reqwest;

// tokio let's us use "async" on our main function
#[tokio::main] 
async fn main() {
    // chaining .await will yield our query result
    let result = reqwest::get("http://127.0.0.1:5000/").await;
    println!("{:?}", result); 

    let params = [("data", "Post Request success")];
    let client = reqwest::Client::new();
    let res = client.post("http://127.0.0.1:5000/")
        .form(&params)
        .send()
        .await; 

        

}