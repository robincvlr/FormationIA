
for %%X in (*.wav) do (
echo Traitement de %%X...
ffmpeg -t 30 -ss 00:00:00.000 -i %%X -acodec copy %%X
)