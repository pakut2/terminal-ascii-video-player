Parse video into separate frames:

```shell
ffmpeg -i ./video/bad-apple.mkv -vf fps=24 ./frames/frame%d.png
```

Install dependencies:

```shell
pip install -r requirements.txt
```

Run:

```shell
python3 main.py
```