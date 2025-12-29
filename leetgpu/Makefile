# LeetGPU Local Test Runner
# Usage: make <problem>  (e.g., make vector_addition)

NVCC := nvcc
NVCC_FLAGS := -g -G -O2 -arch=sm_52 -Wno-deprecated-gpu-targets
BIN_DIR := bin

# Auto-discover all test files and derive problem names
TEST_FILES := $(wildcard tests/test_*.cu)
PROBLEMS := $(patsubst tests/test_%.cu,%,$(TEST_FILES))

# Default target: list available problems
.PHONY: help
help:
	@echo "Usage: make <problem>"
	@echo ""
	@echo "Available problems:"
	@for p in $(PROBLEMS); do echo "  $$p"; done
	@echo ""
	@echo "Other targets:"
	@echo "  make all    - Run all tests"
	@echo "  make clean  - Remove compiled binaries"

# Ensure bin directory exists
$(BIN_DIR):
	mkdir -p $(BIN_DIR)

# Pattern rule: make <problem> compiles and runs
.PHONY: $(PROBLEMS)
$(PROBLEMS): %: $(BIN_DIR)/% | $(BIN_DIR)
	@echo "Running $@..."
	@./$(BIN_DIR)/$@

# Pattern rule: compile solution + test into binary
$(BIN_DIR)/%: %.cu tests/test_%.cu | $(BIN_DIR)
	$(NVCC) $(NVCC_FLAGS) -o $@ $< tests/test_$*.cu

# Run all tests
.PHONY: all
all: $(PROBLEMS)

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf $(BIN_DIR)
