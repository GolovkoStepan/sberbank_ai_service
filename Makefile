.PHONY: run_dev_server
run_dev_server:
	uvicorn main:app --reload

.PHONY: run_server
run_server:
	uvicorn main:app