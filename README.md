# Connected Car Demo
### Prerequisites & Technologies used:
- JDK 7 or 8
- Python 3
- SSH
- Hadoop 3
- Spring XD 
- Redis
- NodeJS 10

### Steps:
- To make this project up and running - *I'm assuming you followed the steps in spring xd docs to install hadoop*- do the following:
	1) **Setup you ssh connection to the localhost**:
	```bash
		>>> ssh localhost
		>>> ssh 0.0.0.0
		>>> source /usr/local/hadoop-working/hadoop-evn
	```
	**NOTE**: Make sure to replace the above path to yours.

	2) **Run Hadoop**:
	```bash
		>>> start-dfs.sh
		>>> start-yarn.sh
		>>> jps
	```
	3) **Run Redis**:
	```bash
		>>> redis-server
	```
	- And in different terminal, run the following:
	```bash
		>>> redis-cli
	```
	4) **Run Spring XD**:
		- To run Spring XD, go the folder where you downloaded it, and do the following and keep it running:
		```bash
			>>> xd/bin> ./xd-singlenode
		```
		- In another terminal, do the following:
		```bash
			>>> shell/bin> ./xd-shell
		```
	5) **Create a Stream**:
		- Now, we need to create a stream that takes an HTTP request (POST) from the `Simulator`, and save the data into `Hadoop` hdfs, and send the same data to redis.
		- In the terminal where you performed ` ./xd-shell `, write the following command:
		```bash
		>>> xd:>stream create --name car --definition "http --port=8000 | hdfs --rollover=20 --idleTimeout=10000" --deploy
		Created and deployed new stream 'car'
		```
		```bash
		>>> xd:>hadoop config fs --namenode hdfs://localhost:8020
		>>> xd:>stream create --name car-tap --definition "tap:stream:car > redis --queue=myList2" --deploy
		Created and deployed new stream 'car-tap'
		```
	6) **Run the Simulator**:
		- You can run the simulator to send the data, or you can do the same function with the following command:
		```bash
		>>> xd:>http post --target http://localhost:8000 --data "spring"
		> POST (text/plain;Charset=UTF-8) http://localhost:8000 spring
		> 200 OK
		```
	7) **Check Hadoop**:
		- You can check if the data was sent successfully, by performing the following command:
		```bash
		>>> hadoop fs ls /xd/
		Found 10 items
		drwxr-xr-x   - mosaab supergroup          0 2019-03-09 17:58 /xd/car
		drwxr-xr-x   - mosaab supergroup          0 2019-03-07 12:13 /xd/myhdfsstream1
		drwxr-xr-x   - mosaab supergroup          0 2019-03-07 13:08 /xd/new_1
		drwxr-xr-x   - mosaab supergroup          0 2019-03-07 13:44 /xd/new_2
		drwxr-xr-x   - mosaab supergroup          0 2019-03-09 17:20 /xd/test
		drwxr-xr-x   - mosaab supergroup          0 2019-03-07 12:53 /xd/tmp
		```
		```bash
		>>> xd:>hadoop fs cat /xd/car/car-0.txt
		spring
		```
	8) **Check Redis**:
		- Now, It is the time to see our data in Redis server, first, go to the terminal where you typed `redis-cli`, and write the following command:
		```bash
		>>> lrange myList2 0 -1
		1) spring
		```
	9) **Open the dashboard**:
		- And allow socket.io to communicate with Redis to collect the cars' data.
		- You can start NodeJS server as follows:
		```bash
		>>> node index.js
	10) **Open the dashboard**:
		- Now, you can open the dashboard via this URL `http://localhost:8001/index.html` and you can see the position of each car in Google map.

### Video
[![]()]("Connected Car (Mosaab).mkv")
