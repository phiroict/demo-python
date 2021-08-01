VERSION ?= "003"
build:
	docker build -t phiroict/demo:20210705.$(VERSION) .
run:  
	-docker rm -f demo-app
	docker run --name demo-app -p 10001:10000 phiroict/demo:20210705.$(VERSION) 
release:
	docker push phiroict/demo:20210705.$(VERSION)