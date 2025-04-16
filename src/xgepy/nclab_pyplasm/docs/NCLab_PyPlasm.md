# NCLab PyPlasm

## Docker Container Adjustments

Since we are using our own Docker container, several adjustments were made to the build process:

### Core Modifications

1. **GUI Initialization**
   - Modified `xge/xge.cpp` to return nothing when attempting to initialize the GUI
   - This prevents unnecessary GUI-related operations in our containerized environment

2. **Dependencies**
   - PyPlasm uses Juce, which must be included in `libs/CMakeLists.txt`
   - This ensures proper dependency management in the container

3. **Logging**
   - Reduced verbosity by modifying `xge/log.cpp`
   - Logger now returns nothing when creating objects
   - This minimizes unnecessary output

### Modular Architecture

1. **Module Integration**
   - Added nclab_pyplasm module to `xgepy/CMakeLists.txt`
   - This enables proper module loading

2. **Import Structure**
   - Implemented one-way imports from `fenvs.py`
   - No imports from our module to `fenvs.py`
   - This prevents circular import errors

3. **Code Organization**
   - Replaced monolithic `fenvs.py` (12,000+ lines) with modular structure
   - Each module is self-contained and self-explanatory
   - Functions are exposed through `nclab_pyplasm/__init__.py`

### Best Practices

1. **Function Naming**
   - Use complete function names instead of shortcuts
   - Examples:
     - Use `MOVE` instead of `M` or `T`
     - Use `DIFFERENCE` instead of `DIFF`
   - This improves code readability and maintainability

2. **Module Control**
   - **Import Structure**
     - `xgepy/__init__.py` uses `from nclab_pyplasm import *` for controlled exposure
     - Submodules avoid importing from each other to prevent circular dependencies

   - **Function Exposure**
     - Each module file defines an `__all__` list to explicitly control which functions are exposed
     - Example:
       ```python
       __all__ = [
           'MOVE',       # Main function
           'M',          # Shortcut (if needed)
           'T',          # Alternative name
       ]
       ```
     - This provides clear documentation of the public API
     - Prevents accidental exposure of internal function

3. **Pre-commit Hooks**
   - The project uses pre-commit hooks.
   - Current hooks include:
     - `trailing-whitespace`: Removes trailing whitespace
     - `end-of-file-fixer`: Ensures files end with a newline
     - `check-yaml`: Validates YAML files
     - `black`: Python code formatter

   - To install the hooks:
     ```bash
     # Install pre-commit if not already installed
     pip install pre-commit

     # Install the hooks
     pre-commit install
     ```
**Note**
- The old fenvs.py is for now included. In case we need some reference.
- Feel free to make any adjustments.
