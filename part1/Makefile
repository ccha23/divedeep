# =====================================================================
# For one-time setup/fix
# ---------------------------------------------------------------------

setup: dev fix

# Install and configure clangd a debugger extension for Coder Server
# See:
# - CodeLLDB manual: https://github.com/vadimcn/codelldb/blob/master/MANUAL.md#expressions
# - VSCode clangd: https://github.com/clangd/vscode-clangd
# - VSCode debug: https://code.visualstudio.com/docs/debugtest/debugging
# - clangd config: https://clangd.llvm.org/config
dev:
	@echo "Setting up clangd for Code Server..." && \
	code-server --install-extension llvm-vs-code-extensions.vscode-clangd && \
	code-server --install-extension vadimcn.vscode-lldb && \
	mkdir -p ~/.config/clangd/ && cp -f clangd_config.yaml ~/.config/clangd/config.yaml && \
	echo "Done! Restart Jupyter server for changes to take effect."

# Restore link color
# See https://github.com/jupyter-book/jupyterlab-myst/issues/248
fix:
	@echo "Apply fix..." && \
	mkdir -p ~/.jupyter/custom/ && cp -f custom.css ~/.jupyter/custom/custom.css && \
	echo "Done! Restart Jupyter server for changes to take effect."