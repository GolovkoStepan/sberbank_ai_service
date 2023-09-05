.PHONY: run_env
run_env:
	. ./venv/bin/activate

.PHONY: run_dev_server
run_dev_server: run_env
	uvicorn main:app --reload

.PHONY: run_server
run_server: run_env
	uvicorn main:app