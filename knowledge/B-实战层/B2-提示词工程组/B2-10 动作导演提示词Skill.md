# 动作导演提示词Skill
> 用途（技能）：动作/战斗类视频的镜头打点逻辑，解决「动作镜头怎么拆」和「怎么让AI生成准确动作」的问题。
> 注：本卡示例中的相机/镜头型号（Arri Alexa、RED V-Raptor、Sony A1、Phantom Flex4K 等）是提示词风格标签而非史实器材配置，照抄出片没问题，当知识引用需谨慎（口径同 B2-09）。

## 核心难点

AI视频生成模型对动作的理解能力有限。一个复杂的动作（如「转身出拳」）通常无法一步到位。必须将动作拆解为若干关键帧（keyframe），每个关键帧只描述一个清晰的姿态。

---

## 动作镜头拆解三原则

### 原则一：一个镜头一个核心动作

错误：`a man running, jumping over a wall, and kicking another man`
正确拆分：
- 镜头A：`a man sprinting toward a wall`
- 镜头B：`a man leaping over a brick wall, mid-air`
- 镜头C：`a man in mid-air delivering a flying kick to another man`

### 原则二：动作镜头优先用侧面角度

AI生成正面动作的准确度远低于侧面。打斗/运动类镜头尽量用侧面（profile）或3/4侧面角度。

推荐角度排序：
1. `side profile angle`（正侧面，最稳定）
2. `three-quarter profile angle`（3/4侧面，兼顾面部和动作）
3. `low angle side view`（低角度侧面，力量感强）
4. `over-the-shoulder`（过肩，适合打斗对峙）

避免：纯正面（`front view`）拍复杂动作。

### 原则三：动作镜头时长要短

| 动作类型 | 单镜头建议时长 |
|---------|-------------|
| 奔跑/移动 | 2-3秒 |
| 跳跃/翻滚 | 1-2秒 |
| 出拳/踢击 | 1-1.5秒 |
| 组合技（2个动作） | 2-3秒 |
| 慢动作特写 | 2-3秒 |
| 动作全貌（远景） | 2-4秒 |

超过4秒的连续动作镜头，AI模型几乎必然出现动作衰减或变形（基于2024代模型经验；可灵2.x/Seedance 2.x 已支持更长连贯动作，按当前模型代际校准）。

---

## 动作场景镜头打点流程

### 第一步：列出动作编舞

用中文先写出完整的动作序列（每个动作用箭头连接）：

```
站立蓄力 → 起身冲刺 → 跳跃腾空 → 空中转身 → 落地出拳 → 对手后退 → 追击
```

### 第二步：按关键帧切镜

每个箭头 = 一个镜头，每镜头描述那个瞬间的姿态：

```
镜头1：蓄力（蹲姿，拳头紧握）→ 镜头2：冲刺（低角度侧面跑步）→ 镜头3：起跳（脚离地瞬间）→ 镜头4：空中转身（侧视图腾空旋转）→ 镜头5：落地出拳（拳头接触瞬间特写）→ 镜头6：对手后退（冲击力反应）→ 镜头7：追击（运动模糊）
```

### 第三步：为每个镜头写提示词

遵循七字段格式（见 B2-01），重点放在 Action 和 Composition 字段。

---

## 动作镜头提示词公式

### 公式一：蓄力/起手式
```
[Character description], [static pose showing preparation: crouching, gripping weapon, winding up], 
[environment], 
[lighting emphasizing tension], 
[shot size], side profile angle, 
[style], [camera/quality]
```

示例：
```
a muscular fighter in black shorts and taped hands, crouching in fighting stance with fists raised to chest level, 
dimly lit underground fight ring, concrete floor with water stains, 
harsh overhead fluorescent light with deep shadows, dramatic contrast, 
medium shot, side profile angle, shallow depth of field, underground fight club cinematic, shot on Arri Alexa 35mm 8K film grain
```

### 公式二：冲刺/移动
```
[Character description], [specific movement: sprinting / leaping / rolling / sliding], 
[environment with motion blur elements], 
[directional lighting with motion], 
[shot size], tracking shot / side angle, 
[style], [camera/quality]
```

示例：
```
a ninja in dark outfit sprinting across rooftop, body leaning forward, 
urban rooftop at night with water towers and vents, city lights blurred in background, 
rim lighting from city glow behind, blue tint, 
medium wide shot, tracking shot from the side matching speed, 
cyberpunk action cinematic, shot on RED V-Raptor 25mm 8K motion sharp
```

### 公式三：空中动作
```
[Character description], [specific mid-air pose: spinning / kicking / flipping / diving], 
[environment below and around], 
[dramatic backlighting or rim light emphasizing silhouette], 
[shot size], low angle looking up, 
[style], [camera/quality]
```

示例：
```
a martial artist in white gi performing a spinning roundhouse kick mid-air, 
traditional wooden dojo interior with tatami floor, shoji screens, 
dramatic backlight from windows behind creating a glowing silhouette, dust particles catching light, 
medium wide shot, low angle looking up at the jumping figure, 
martial arts action cinematic, high contrast, shot on Arri Alexa anamorphic 8K
```

### 公式四：冲击/接触瞬间
```
[Character description], [exact moment of impact: fist connecting / sword hitting / body crashing], 
[environment], 
[harsh flash lighting or impact lighting], 
[close-up or extreme close-up], [angle emphasizing force], 
[style], [camera/quality]
```

示例：
```
a boxer's gloved fist connecting with opponent's jaw, sweat droplets flying from impact, 
boxing ring under bright ring lights, ropes slightly visible at edge, 
harsh direct flash of ring light freezing the moment, high contrast, 
extreme close-up, side angle, ultra-fast shutter freeze frame, 
sports action photography, gritty dramatic, shot on Sony A1 400mm 8K
```

### 公式五：慢动作特写
```
[Subject detail: fist / foot / weapon / sweat / debris], [frozen mid-air or slow-motion], 
[environment slightly blurred], 
[dramatic lighting highlighting the subject detail], 
[extreme close-up], macro perspective, 
[style], [camera/quality with slow motion tag]
```

示例：
```
water droplets and sweat frozen in mid-air around a fighter's fist during a punch, 
out of focus gym background, 
harsh side lighting catching each water droplet individually, crystalline highlights, 
extreme close-up, 1000fps slow motion simulation, 
action cinematography, hyper-detailed, shot on Phantom Flex4K macro lens 8K
```

### 公式六：反应/冲击波
```
[Character reacting: stumbling / falling / crashing through], 
[environment with destruction/debris], 
[dynamic lighting: sparks / explosion flash / dust cloud light], 
[shot size], [angle showing impact scale], 
[style], [camera/quality]
```

示例：
```
a man thrown backward through a market stall, wooden crates shattering, vegetables flying, 
busy Asian night market with stalls and lanterns, 
orange flash light from impact mixing with red lantern glow, debris illuminated, 
wide shot, eye level, showing full body trajectory and destruction path, 
action movie cinematic, high energy, shot on Arri Alexa 24mm 8K
```

---

## 动作序列编排模板

将多个动作镜头组合成完整序列时，遵循以下节奏模式：

### 节奏模式A：蓄势 - 爆发 - 收尾（3镜头）

```
镜头1：蓄力（2-3s，静态/慢）→ 镜头2：爆发（1-2s，快/冲击）→ 镜头3：收尾（2-3s，反应/余韵）
```

### 节奏模式B：远-中-近-远（4镜头）

```
镜头1：远景交代（2s，环境+人物）→ 镜头2：中景动作（2s，侧面全身）→ 镜头3：特写冲击（1s，拳头/接触点）→ 镜头4：远景反应（2s，余波/环境变化）
```

### 节奏模式C：慢-快-慢（3镜头）

```
镜头1：慢动作铺垫（3s，慢速蓄力）→ 镜头2：正常速度爆发（1.5s，快速连击）→ 镜头3：慢动作收尾（3s，最后一击的冲击波）
```

---

## 动作提示词的禁区

| 禁止写 | 原因 | 替代方案 |
|--------|------|---------|
| 两个以上连续动作 | AI无法连贯执行 | 拆成多个镜头 |
| 具体武术招式名称（如"旋风腿"） | AI不一定理解 | 用姿态描述：`spinning kick mid-air` |
| 正面拍高速动作 | 动作模糊/变形 | 用侧面角度 |
| 超过4秒的动态镜头 | 动作衰减 | 切成短镜头 |
| 复杂武器操作（如"换弹匣+瞄准+射击"） | 步骤太多 | 每步一个镜头 |
| 群体混战（超过3人同时打斗） | 人体混乱/穿模 | 用远景简化，或聚焦1v1 |
