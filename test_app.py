import subprocess

def test_app_runs_successfully():
    try:
        # Run the app.py script using subprocess
        result = subprocess.run(["python", "app.py"], capture_output=True, text=True, check=True)

        # Check if the process returned a zero exit code (indicating success)
        assert result.returncode == 0

        # Check if the expected "pong" message is in the stdout
        assert "pong" in result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # If the app.py script exits with a non-zero code, it's considered a failure
        assert False, f"App execution failed with exit code {e.returncode}:\n{e.stderr}"


