# Cheat Sheet

## 1. Generate Alpha Video

Use `main.py` to generate alpha video.

## 2. Converting equirectangular VR footage into Fisheye

```sh
ffmpeg -i input.mp4 -filter_complex "[0:v]split=2[left][right]; [left]crop=3630:3630:0:0[left_crop]; [right]crop=3630:3630:3630:0[right_crop]; [left_crop]v360=hequirect:fisheye:iv_fov=180:ih_fov=180:v_fov=180:h_fov=180[leftfisheye]; [right_crop]v360=hequirect:fisheye:iv_fov=180:ih_fov=180:v_fov=180:h_fov=180[rightfisheye]; [leftfisheye][rightfisheye]hstack[stacked]; [stacked]scale=7260:3630[v]" -map '[v]' -c:a copy -crf 15 output_fisheye_video.mp4
```

or without resize:

```sh
ffmpeg -i input.mp4 -filter_complex "[0:v]split=2[left][right]; [left]crop=3630:3630:0:0[left_crop]; [right]crop=3630:3630:3630:0[right_crop]; [left_crop]v360=hequirect:fisheye:iv_fov=180:ih_fov=180:v_fov=180:h_fov=180[leftfisheye]; [right_crop]v360=hequirect:fisheye:iv_fov=180:ih_fov=180:v_fov=180:h_fov=180[rightfisheye]; [leftfisheye][rightfisheye]hstack[v]" -map '[v]' -c:a copy -crf 15 output_fisheye_video.mp4
```

Note: You can use the same comand to convert the alpha channel video to an fisheye format.

## 3. Merge Fisheye with Alpha

```sh
ffmpeg -i "fisheye.mp4" -i "alpha.mp4" -i "mask.png" -filter_complex "[1]scale=iw*0.4:-1[alpha];[2][alpha]scale2ref[mask][alpha];[alpha][mask]alphamerge,split=2[masked_alpha1][masked_alpha2]; [masked_alpha1]crop=iw/2:ih:0:0,split=2[masked_alpha_l1][masked_alpha_l2]; [masked_alpha2]crop=iw/2:ih:iw/2:0,split=4[masked_alpha_r1][masked_alpha_r2][masked_alpha_r3][masked_alpha_r4]; [0][masked_alpha_l1]overlay=W*0.5-w*0.5:-0.5*h[out_lt];[out_lt][masked_alpha_l2]overlay=W*0.5-w*0.5:H-0.5*h[out_tb]; [out_tb][masked_alpha_r1]overlay=0-w*0.5:-0.5*h[out_l_lt];[out_l_lt][masked_alpha_r2]overlay=0-w*0.5:H-0.5*h[out_tb_ltb]; [out_tb_ltb][masked_alpha_r3]overlay=W-w*0.5:-0.5*h[out_r_lt];[out_r_lt][masked_alpha_r4]overlay=W-w*0.5:H-0.5*h" -c:v libx265 -crf 18 -preset veryfast -map 0:a:? -c:a copy "final.mp4" -y
```
