import tempfile
import subprocess

class BuilderStrategyMake:
    @staticmethod
    def build(template: str):
        with tempfile.NamedTemporaryFile(mode="w", delete=True) as temp:
            temp.write(template)
            temp.flush()

            try:
                subprocess.run(['make', '-f', temp.name], check=True)
                print("Build successful")
            except subprocess.CalledProcessError as e:
                print(f"Build error: {e}")
