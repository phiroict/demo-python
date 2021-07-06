build:
	docker build -t phiroict/demo:20210705.001 .
run:  
	-docker rm -f demo-app
	docker run --name demo-app -p 10001:10000 phiroict/demo:20210705.001 
release:
	docker push phiroict/demo:20210705.001  