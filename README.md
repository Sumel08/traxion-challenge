# Traxion Challenge

Author: Oscar Lemus

## Challenge

Create a URL Shortener service

## Instructions

This project was created with serverless framework, and it is ready to be
deployed, if you want to run this locally, you need to follow the next steps

* Create a new environment and install the required packages
* Run ```sls offline``` command in order to raise a new server in offline mode
* An api key will be given in prompt in order to test locally
* The default url is ```http://localhost:3000```
* Note: in order to be functional, first you need to deploy the project in your AWS account in order to create the
  infrastructure DynamoDB and you need to configure your default profile credentials, or you can put your credentials
  in ```src/dao/shortcode.py``` file, on ```boto3.client('dynamodb')``` method
  as ```boto3.client('dynamodb', aws_access_key_id={your key}, aws_secret_access_key={your secret key})```

### Deploy

In order to deploy the service you just need to configure in serverless.yml your aws account profile and
run ```sls deploy```

## API Contract

### Create a new shortcode

<table>
<thead>
<tr>
<th>Use Case</th>
<th>Create a Shortcode</th>
</tr>
</thead>
<tbody>
<tr>
<td>Path</td>
<td>/</td>
</tr>
<tr>
<td>Method</td>
<td>POST</td>
</tr>
<tr>
<td>Preconditions</td>
<td>Have an api Key</td>
</tr>
<tr>
<td colspan="2">Headers</td>
</tr>
<tr>
<td>Content-Type</td>
<td>application/json</td>
</tr>
<tr>
<td>x-api-key</td>
<td>{{apiKey}}</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td>Body Example</td>
<td>

```json
{
  "url": "https://oscar.lemus.app",
  "name": "Personal Web"
}
```

</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td>Code</td>
<td>Response</td>
</tr>
<tr>
<td>201</td>
<td>

```json
{
  "url": "https://some-domain.com/tx3Df"
}
```

</td>
</tr>
<tr><td>400</td><td>Bad Request</td></tr>
<tr><td>403</td><td>Not Allowed</td></tr>
<tr><td>500</td><td>Internal Server Error</td></tr>
</tbody>
</table>

### Create a new shortcode

<table>
<thead>
<tr>
<th>Use Case</th>
<th>Get Original URL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Path</td>
<td>/{code}</td>
</tr>
<tr>
<td>Method</td>
<td>GET</td>
</tr>
<tr><td colspan="2"></td></tr>
<tr>
<td>Code</td>
<td>Response</td>
</tr>
<tr>
<td>302</td>
<td>
Redirect to original URL
</td>
</tr>
<tr><td>400</td><td>Bad Request</td></tr>
<tr><td>404</td><td>Shortcode not found</td></tr>
<tr><td>403</td><td>Not Allowed</td></tr>
<tr><td>500</td><td>Internal Server Error</td></tr>
</tbody>
</table>

## Tasks to follow

| TXC-1 | Define Infrastructure in serverless framework |
|-------|-----------------------------------------------|
| TXC-2 | Create code structure                         |
| TXC-3 | Implement functionality                       |
| TXC-4 | Write Tests                                   |
| TXC-5 | Complete Documentation                        |