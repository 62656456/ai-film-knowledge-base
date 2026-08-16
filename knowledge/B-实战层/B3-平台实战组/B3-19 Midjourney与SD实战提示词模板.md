# Midjourney与SD实战提示词模板
> 用途（直接复制粘贴）：Midjourney 与 Stable Diffusion 出图时按场景直接复制对应提示词；含MJ通用公式/写实人物/艺术风格/参数速查与SD质量词/公式模板。
> 平台参数/版本为 2026-07 快照，以官方界面为准。
> 版本注（2026-07 已联网确认）：MJ 当前默认版本为 **--v 8.1**（2026-06 起）；**--niji 7**（动漫，2026-01 发布）为真实最新版本。本卡示例多以 `--v 7` 书写，**示例参数可替换为 --v 8.1**。

---

## 第一部分：Midjourney

## 一、MJ 通用公式

> 以下示例中的 `--v 7` 均可替换为当前默认 `--v 8.1`。

### 写实人像公式
```
[年龄/性别] [外貌特征] wearing [服装], [动作/表情], standing in [场景], [光线], [构图], portrait photography, ultra-detailed, 8K --ar 4:5 --v 7
```

填充示例——职场头像：
```
a young professional woman with neat ponytail wearing a navy blazer, confident smile, standing in modern office with soft window light, medium shot, corporate photography, ultra-detailed, 8K --ar 4:5 --v 7
```

填充示例——时尚大片：
```
a fashion model with dramatic makeup wearing avant-garde red dress, walking on rainy street at night, cinematic lighting, full body shot, fashion photography, 8K --ar 2:3 --v 7 --stylize 300
```

### 风景公式
```
[主体地貌] at [时间], [前景] with [细节], [背景], [光线], [风格] landscape, ultra-detailed, 8K --ar 16:9 --v 7
```

填充示例——日落山脉：
```
majestic mountain range at golden hour, colorful clouds in sky, misty valleys below, dramatic lighting, ultra-detailed landscape photography, 8K --ar 16:9 --v 7
```

填充示例——赛博朋克城市：
```
futuristic cyberpunk city at night, neon signs reflecting on wet streets, flying cars between skyscrapers, atmospheric fog, cinematic perspective, ultra-detailed --ar 16:9 --v 7
```

### 产品摄影公式
```
product shot of [产品名称], [材质/颜色], placed on [表面], [光线], clean background, commercial product photography, ultra-detailed, 8K, sharp focus --ar [比例] --v 7
```

填充示例——极简产品：
```
product shot of a minimalist ceramic coffee mug, matte white finish, placed on wooden table with coffee beans, soft studio lighting, clean beige background, commercial photography, ultra-detailed --ar 1:1 --v 7
```

填充示例——奢侈品：
```
luxury watch product photography, gold and leather texture, floating on dark reflective surface, dramatic side lighting, high contrast, macro shot, commercial advertising style, 8K --ar 4:5 --v 7 --stylize 200
```

### 动漫角色公式
```
[角色描述] anime style, [动作], [场景], dramatic lighting, vibrant colors --ar 2:3 --niji 7
```

填充示例：
```
anime warrior character with flowing hair, dynamic action pose, detailed armor, dramatic lighting, vibrant colors, full body shot, ultra-detailed --ar 2:3 --niji 7
```

### FPS第一人称视角
```
A photo from first person POV | while [action] through a [place] at [time] | showing hands like a FPS videogame | from the angle --ar 16:9 --style raw
```

### 卡通肖像
```
isolated [subject], full body, colored, cartoon portrait, bold rounded outlines, animated gifs --style raw
```

---

## 二、MJ 写实人物实战模板

### 梦幻少女森林
```
A 14 year old beautiful Chinese girl playing happily in the forest, a giant Pikachu, smiling, big eyes, princess hair, wearing a Western princess dress, lively, night, dreamlike scenes, fireflies, butterflies, dandelions, flowers and plants, colorful lights, surreal imagination, photo quality, movie lighting effects --ar 3:4 --s 600
```

### 草地阳光女生
```
A charming 30 year old American female, soft wavy blonde hair, crystal clear blue eyes, fair skin. She wears a light blue summer dress with floral patterns, standing in a sunny meadow, tall grass swaying gently in the breeze, a gentle smile on her face, sunlight casting a soft glow on her skin. The background is a distant mountain range and a clear blue sky with a few white clouds. Ultra detailed, photorealistic.
```

### 摩托车沙漠日落
```
A 30 year old American model, long straight black hair, dark brown eyes, olive skin. She wears a stylish black leather jacket and jeans, sitting casually on a motorcycle, background is a desert highway at sunset. The sun hangs low, casting a golden glow over the scene. Every strand of hair and texture of the leather is clearly visible. Photorealistic, cinematic lighting, full body shot.
```

### 雨天窗边特写
```
A realistic close-up portrait depicting a 30 year old American female, freckled face, short red hair, piercing green eyes. She wears a cozy cream-colored sweater, holding a cup of coffee, sitting by a large window with raindrops on the glass. Background softly blurred, showing a rainy cityscape. Ultra detailed, capturing every small freckle and strand of hair.
```

### 秋天纽约街头
```
A 30 year old American female, medium-length brown hair, lightly tanned skin, hazel eyes. She stands confidently on a busy New York City street, wearing a stylish trench coat and boots, surrounded by orange and red falling autumn leaves. The city skyline is visible in the distance, soft sunlight filtering through skyscrapers. Photorealistic, ultra detailed.
```

---

## 三、MJ 艺术风格模板

### 艺术家风格场景
```
A futuristic cityscape in the style of Syd Mead
```
```
A steampunk airship in the style of Jules Verne
```
```
A whimsical forest scene in the style of Tim Burton
```
```
A surreal underwater world in the style of Salvador Dali
```
```
A magical, dreamlike world in the style of Hayao Miyazaki
```
```
A futuristic, dystopian world in the style of Blade Runner
```
```
A snowy mountain landscape with a hidden castle, in the style of Hayao Miyazaki
```
```
A cityscape with towering, interconnected treehouses, in the style of Studio Ghibli
```

### 波普艺术
```
A pop art illustration of a hamburger made of pearls, diamonds, and gold
```
```
A vibrant abstract expressionist painting of the Nike swoosh logo, with bold strokes of color and movement
```

---

## 四、MJ 参数速查

| 参数 | 作用 | 常用值 |
|---|---|---|
| `--ar` | 画面比例 | 16:9 / 9:16 / 1:1 / 4:5 / 3:4 |
| `--v` | 版本 | 8.1 (当前默认，2026-06起) / 7 / 6.1 / niji 7 (动漫) |
| `--stylize / --s` | 艺术化程度 | 100-250适中 / 250-500艺术感强 |
| `--chaos / --c` | 变化程度 | 0稳定 / 50-80探索 |
| `--no` | 排除内容 | `--no text, watermark` |
| `--style raw` | 减少MJ默认美化 | 适合卡通/写实 |

---

## 第二部分：Stable Diffusion

## 五、SD 通用质量词

### 正向质量前缀
```
masterpiece, best quality, high resolution, 8k, ultra-detailed
```

### 反向提示词（完整版）
```
((nsfw)),sketches,(worst quality:2),(low quality:2),(normal quality:2),lowers,normal quality,((monochrome)),((grayscale)),facing away,looking away,text,error,extra digit,fewer digits,cropped,jpeg art|acts,signature,watermark,username,blurry,skin spots,acnes,skin blemishes,bad anatomy,fat,bad feet,cropped,poorly drawn hands,poorly drawn faces,mutation,deformed,tilted head,bad anatomy,bad hands,extra fingers,fewer digits,extra limbs,extra arms,extra legs,malformed limbs,fused fingers,too many fingers,long neck,cross-eyed,mutated hands,bad body,bad proportions,gross proportions,text,error,missing fingers,missing arms,missing legs,extra digit,extra arms,extra leg,extra foot,missing fingers
```

### 反向提示词（精简版）
```
nsfw, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, jpeg artifacts, signature, watermark, blurry, deformed
```

---

## 六、SD 高调摄影公式

```
High-key photography portrait of a [Subject/description], wearing [attire], in a [location], [pose], high exposure, soft-focus lens, bright ambient lighting, subtle shadows, high-key color palette
```

填充示例——画廊女孩：
```
High-key photography portrait of a young beautiful Chinese girl, wearing a flowing silk gown, in a minimalist art gallery, standing serenely eye level angle, high exposure, soft-focus lens, bright ambient lighting, subtle shadows, high-key color palette
```

填充示例——屋顶酒吧：
```
High-key photography portrait of a super beautiful Chinese girl, wearing a shimmering sequin dress, in a chic rooftop bar, laughing, low angle, high exposure, soft-focus lens, bright ambient lighting, subtle shadows, high-key color palette
```

填充示例——旗袍试衣间：
```
High-key photography portrait of a fashion Chinese model, wearing a red cheongsam, in the fitting room with lots of Hanfu clothes, angled from High angle, high exposure, soft-focus lens, bright ambient lighting, subtle shadows, high-key color palette
```

参数设置：大模型用 LiblibAI"万享超写实"模型线（资料线为 SD1.5 底模；确切模型名与底模以平台页面实际为准）| 采样器 Euler a | 步数25 | CFG 3 | 开启After Details脸部修复

---

## 七、SD 3D等距视角模板

```
3D isometric cute Chinese ancient style architecture, yellow in color, warm lighting night 3d, Diorama, c4d, Unreal Engine, 8k, OC renderer, blind box, best quality, cinematic lighting, chiaroscuro, detail, solid background, clean background, artistic, award winning, light color, UHD, 3d rendering, best quality
```

反向提示词同上方完整版。

---

## 八、SD 通用公式
```
(主体描述), (风格) style, (光照), (视角), masterpiece, best quality, 8k, ultra-detailed
```
