
# COLORS
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
RESET  := $(shell tput -Txterm sgr0)

TARGET_MAX_CHAR_NUM=20

## Show help with `make help`
help:
	@echo ''
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)


.PHONY: run docker
## Builds the base Docker image and runs the container
run docker:
	@echo "Building Docker image and spinning up container..."
	@docker compose up --build --remove-orphans -d --force-recreate
	@echo "Docker container deployed successfully! Check the status of the running containers in the Docker Desktop."
	@echo "Streamlit app running at http://localhost:8501/"

.PHONY: down
## Shuts down the Docker container
down: 
	@echo "Shutting down and removing Docker containers..."
	@docker compose down --remove-orphans
	@echo "Containers removed."

.PHONY: restart
## Restarts Docker containers
restart: down up

.PHONY: run local
run local:
	python3 -m venv .venv && \
	source .venv/bin/activate && \
	pip install -r requirements-streamlit.txt --no-cache-dir && \
	streamlit run streamlit_app.py
