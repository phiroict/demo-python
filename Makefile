VERSION ?= "004"
build:
	cd demo-app-1 && docker build -t phiroict/demo:20210705.$(VERSION) .
build2:
	cd demo-app-2 && docker build -t phiroict/demo2:20210705.$(VERSION) .

run:  
	-docker rm -f demo-app
	docker run --name demo-app -p 10001:10000 phiroict/demo:20210705.$(VERSION) 
run2:  
	-docker rm -f demo-app2
	docker run --name demo-app2 -p 10011:10010 phiroict/demo2:20210705.$(VERSION) 

release:
	docker push phiroict/demo:20210705.$(VERSION)
	docker push phiroict/demo2:20210705.$(VERSION)