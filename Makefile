
.PHONY: help
help: ### Display this help screen.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

SRC := $(shell find . -type f -name '*.py' -not -path "./venv/*")

.PHONY: deps
deps: ### Package the runtime requirements.
	@pip freeze > requirements.txt

.PHONY: lint
lint: ### Lint the source code.
	@echo "Running import sort..."
	@isort --atomic --multi-line=VERTICAL_HANGING_INDENT ${SRC}
	@echo "Running static code analysis..."
	@pyflakes ${SRC}
	@echo "Running code style check..."
	@pycodestyle ${SRC} --ignore=W293,E121,E125,E402,E501

test: ### Run the test suite.
	@echo "Running tests..."
	@python -m unittest discover -s tests
