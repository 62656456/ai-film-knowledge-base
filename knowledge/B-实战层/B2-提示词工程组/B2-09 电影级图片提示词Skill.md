# 电影级图片提示词Skill
> 用途（技能）：电影感英文提示词的固定格式参数，直接套用即可生成电影级画面的提示词。
> 注：本卡设备组合是提示词风格标签而非史实（如 Arriflex 416 实为 Super 16mm 机型不配35mm胶片、"35mm TV news camera"不存在），照抄出片没问题，当知识引用需谨慎。
> 定位：本卡为电影感参数母表——B1 分镜模板、B3 图片模板的 Camera/Style 字段以本卡为单一事实源。

## 使用方式

选择需要的参数组合，填入七字段的对应位置。电影感提示词的核心在于：具体设备 + 光线描述 + 色调控制 + 质感标签。不是简单地加一个 `cinematic` 就够了。

---

## 电影感固定参数表

### 设备参数（Camera 字段用）

根据想要的"电影年代感"选择设备组合：

#### 现代数字电影摄影机
```
shot on Arri Alexa 65, Panavision Ultra Vista anamorphic lens, 8K, cinematic color grading
```
效果：顶级电影质感，色彩准确，宽银幕比例感，适合所有现代电影风格

```
shot on RED V-Raptor XL, Cooke S7/i Full Frame Plus lens, 8K, REDWideGamutRGB color space
```
效果：高动态范围，适合高对比度/夜景/赛博朋克场景

```
shot on Sony Venice 2, Zeiss Supreme Prime lens, 8K, dual native ISO, S-Cinetone color
```
效果：肤色还原优秀，适合人物为主的电影场景

#### 经典胶片模拟
```
shot on 35mm Kodak Vision3 500T film stock, Arriflex 416 camera, tungsten balanced, warm grain
```
效果：经典电影胶片质感，暖色调颗粒，适合70-90年代怀旧风格

```
shot on 16mm Kodak Vision3 250D film stock, Bolex camera, daylight balanced, heavy grain
```
效果：粗颗粒独立电影感，适合纪录片/低成本/艺术风格

```
shot on 65mm IMAX film stock, Panavision System 65 camera, ultra-wide format, immense detail
```
效果：超大画幅沉浸感，适合史诗/自然/太空类场景

#### 电视/老电影模拟
```
shot on 35mm TV news camera, vintage 1970s broadcast lens, CCD sensor look, interlaced scan lines, warm faded color
```
效果：70-80年代电视新闻质感，适合复古/怀旧/伪纪录片风格

---

### 镜头参数（Camera 字段用）

根据想要的画面特征选择镜头：

| 镜头类型 | 效果 | 参数写法 |
|---------|------|---------|
| 变形宽银幕 | 经典宽银幕电影感、水平拉丝光晕 | `anamorphic lens, 2.39:1 aspect ratio, horizontal lens flare` |
| 球面镜头 | 写实、无变形、清晰锐利 | `spherical lens, sharp focus, no distortion` |
| 长焦压缩 | 空间压缩感、背景放大拉近 | `200mm telephoto lens, compressed perspective, thin depth of field` |
| 广角透视 | 空间纵深感、夸张透视 | `18mm wide-angle lens, deep perspective, barrel distortion at edges` |
| 微距镜头 | 极致细节、极浅景深 | `100mm macro lens, extreme close-up, paper-thin depth of field` |
| 老旧镜头 | 光斑/色散/暗角/模糊边缘 | `vintage uncoated lens, heavy vignetting, chromatic aberration, soft corners` |

---

### 色调参数（Style 字段用）

电影调色是电影感的灵魂。根据想要的氛围选择色调组合：

#### Teal & Orange（最经典的电影调色）
```
teal and orange color grade, skin tones warm orange, shadows cool teal, complementary contrast
```
适用：动作片、冒险片、好莱坞大片

#### Desaturated Cold（冷调去饱和）
```
desaturated color grade, cool blue-grey tones, muted greens, low saturation, cold atmosphere
```
适用：科幻片、惊悚片、战争片、反乌托邦

#### Warm Golden（暖金调）
```
warm golden color grade, honey-toned highlights, amber shadows, rich warm palette
```
适用：怀旧片、爱情片、西部片、家庭故事

#### Bleach Bypass（漂白旁路）
```
bleach bypass look, high contrast desaturated, crushed blacks, metallic sheen on highlights
```
适用：战争片（如《拯救大兵瑞恩》）、 gritty写实现代片

#### Cross-Processed（交叉冲洗）
```
cross-processed color shift, green shadows, yellow highlights, unnatural color cast, nostalgic
```
适用：独立电影、音乐视频、艺术实验

#### Day for Night（日拍夜）
```
day-for-night look, deep blue cast over daylight scene, darkened exposure, moonlit illusion
```
适用：夜景模拟、低成本夜间拍摄、悬疑片

---

### 质感标签（Camera 字段用）

电影画面必须有质感，不能"太干净"：

```
film grain, subtle noise texture, natural skin texture, visible pores, micro-contrast, cinematic sharpness, slight halation on highlights
```

根据风格增减：
- 写实电影：保留 `film grain` + `natural skin texture` + `micro-contrast`
- 梦幻浪漫：去掉 grain，加 `soft glow` + `halation`
- 粗糙写意：加重 grain，加 `heavy noise` + `soft focus areas`

---

## 完整电影感提示词组装示例

### 示例1：现代动作片

```
a muscular man in tactical gear sprinting through a narrow alley, 
leaping over a concrete barrier, intense determined expression, 
rain-soaked urban alley at night, concrete walls with graffiti, fire escape stairs, puddles splashing, 
harsh rim lighting from overhead neon signs in blue and orange, wet reflective surfaces, 
medium wide shot, tracking shot following alongside, shallow depth of field, 
teal and orange color grade, high contrast gritty action, 
shot on Arri Alexa 65, Panavision anamorphic lens, 8K, film grain, cinematic sharpness
```

### 示例2：70年代怀旧电影

```
a woman in a floral maxi dress standing at a desert gas station, 
looking back over her shoulder with a wistful expression, wind blowing her hair, 
vast American Southwest desert, a single retro gas pump, faded sign, dusty road stretching to horizon, 
warm golden hour sunlight from behind, long shadows, dust particles floating in air, 
medium full shot, eye level, 2.39:1 aspect ratio framing, 
warm golden color grade, 1970s road movie aesthetic, 
shot on 35mm Kodak Vision3 500T, vintage anamorphic lens, warm grain, slight vignetting
```

### 示例3：科幻悬疑

```
an astronaut floating alone inside a dark spacecraft corridor, 
reaching toward a flickering control panel, face half illuminated by screen glow, 
interior of abandoned space station, floating debris, emergency lights pulsing red, 
cold blue light from distant window contrasting with warm amber control panel glow, single source lighting, 
medium shot, slow dolly backward, wide angle perspective showing corridor depth, 
desaturated cold sci-fi tone, deep shadows, sterile metallic atmosphere, 
shot on Sony Venice 2, 18mm wide-angle, 8K, subtle blue shift, film grain, micro-contrast
```

---

## 电影感提示词避坑指南

| 错误做法 | 正确做法 |
|---------|---------|
| 只写 `cinematic` | 写具体设备+镜头+调色 |
| 同时写多种风格 | 只选一个主导电影风格 |
| 忘了写光线方向 | 必须有明确光源方向和质感 |
| 画质太干净（不加grain） | 根据风格加film grain或texture |
| 没有景深控制 | 明确写shallow/deep depth of field |
| 镜头/景别没写 | 至少写shot size和一个camera参数 |
