import sys
import nbformat

def fix_widgets_metadata(ipynb_path):
    nb = nbformat.read(ipynb_path, as_version=nbformat.NO_CONVERT)
    if "widgets" in nb.metadata:
        print(f"Removing 'widgets' from metadata in {ipynb_path}...")
        del nb.metadata["widgets"]
        nbformat.write(nb, ipynb_path)
        print("✅ Fixed notebook. You can reopen it now.")
    else:
        print("No 'widgets' key found in notebook metadata. Nothing to fix.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_notebook_widgets.py <notebook.ipynb>")
        sys.exit(1)
    fix_widgets_metadata(sys.argv[1])