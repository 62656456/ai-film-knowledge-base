# A2-07 电影风格／题材视觉图鉴资产清单 v0.2

> 用途：记录 A2-07 已采用的 8 张原创视觉图鉴资产、图注边界、最终提示词与 QA 结论。2026-08-03 全库巡检确认：8 图均已嵌入 A2-07 正文，本清单是附属证据，不是独立知识卡。

## 总体边界

- 共 8 张原创 PNG，统一尺寸 `1672 × 941`，横向四栏，无栏内标题、Logo、品牌、水印或影视 IP 角色。
- 栏位标签与图注应放在 Markdown 正文中，不写进图片。
- 这些图展示的是**可观察的最终画面机制**，不能反向证明真实生产管线。例如“看起来符合 PBR 材质和光照规律”不等于已经核实它由真实 PBR 三维软件流程制作。
- 所有大众口语风格均已转译为天空、光线、构图、材质、造型、空间和运动痕迹等通用机制；提示词未点名或模仿任何在世创作者。
- 06、07 各做过一次定向修正；其余图片首轮通过。所有最终图已实际目视检查。

---

## 01｜制作外观入口

- **文件名**：`01_production_appearances.png`
- **四栏标签（左→右）**：数字 2D 赛璐璐式平涂｜摄影写实／写实三维外观｜3D Cel Shading｜黏土定格材料感
- **建议嵌入章节**：媒介与制作外观入口；适合作为图鉴开场。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：第一栏靠清晰线稿、平涂色块和硬边两级阴影成立；第二栏靠湿混凝土、布料粗糙度、金属反射和自然接触阴影形成摄影写实感；第三栏保留三维几何，但将光照压缩成有限色阶并加轮廓；第四栏出现指纹、手工塑形、微缩景深与实体接触感。
- **判定边界**：第二栏可以安全标注为“摄影写实／写实三维外观候选”。单张生成图无法证明其真实使用了 PBR 材质节点、能量守恒或具体三维渲染管线；主卡若使用“PBR”一词，图注应写“呈现 PBR 式材质与光照外观”，不要把视觉结果冒充工艺证据。
- **QA**：通过。四栏、人物、站姿、自行车、包裹、机位和天气基本稳定；无可读文字、Logo、IP、明显肢体问题或栏位串扰。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape teaching comparison image for a Markdown film-style knowledge card
Primary request: Create one original four-panel comparison board showing the exact same cinematic scene in four different production appearances. The scene is a young adult bicycle courier in an ochre raincoat, standing beside a red cargo bicycle under a simple concrete bus shelter, one hand holding the bicycle handlebar and the other checking a small blank parcel. A puddle, one bench, and a distant apartment block remain in exactly the same positions in every panel.
Panel structure: four equal vertical panels in one wide landscape image, subtle clean dividers, no labels.
Critical invariant: same person identity, same body pose, same clothing design and colors, same bicycle, same parcel, same camera height, same 35mm-equivalent framing, same object placement, same overcast lighting direction. Change only the production appearance.
Panel 1 appearance: digitally hand-drawn 2D animation with cel-style flat color, clean ink outline, two-tone hard-edged shadows, painted flat background.
Panel 2 appearance: high-quality 3D CGI with physically based materials, realistic wet concrete, fabric roughness, metal reflections, natural contact shadows, coherent PBR lighting.
Panel 3 appearance: 3D CGI with cel shading, clearly three-dimensional geometry but compressed light into two hard tonal bands, controlled dark outlines, graphic highlights.
Panel 4 appearance: real handcrafted clay stop-motion miniature appearance, visible fingerprints and slight sculpting marks, physical clay figure and clay bicycle, miniature set, real contact shadows and shallow depth of field.
Composition/framing: wide 16:9 teaching board, four equal vertical panels, medium-wide full-body scene, subject centered identically in each panel.
Lighting/mood: neutral overcast daylight, identical direction and value structure in all panels so medium differences remain teachable.
Constraints: exactly four panels; no written words, no letters, no numbers, no captions, no signs, no logos, no brands, no watermark; original generic character; no resemblance to any existing film character; no extra people; no change of story, pose, camera, weather, or palette between panels.
```

---

## 02｜二维画面家族

- **文件名**：`02_2d_image_families.png`
- **四栏标签（左→右）**：数字赛璐璐式平涂｜水彩逐帧绘画感｜中国水墨动画语言｜几何矢量与剪纸拼贴
- **建议嵌入章节**：二维画面家族／手绘与平面动画。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：同一青年、桥栏、列车和黄昏视点不变；四栏分别依靠硬边色块、透明水彩湿边、墨线／留白／墨色密度、几何纸片与层叠纸影构成画面。
- **QA**：通过。角色身份、站姿和城市构图稳定；水墨不是简单黑白滤镜，剪纸栏有真实纸层；无文字伪影、明显手部畸形或风格串扰。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board for film-style browsing
Primary request: Show the same original young adult commuter at a city pedestrian overpass during sunset in four distinct 2D image families. The commuter wears a teal jacket, cream trousers, and a small rust-red shoulder bag, stands in three-quarter profile with both hands resting on the railing, looking toward a distant train and layered low-rise city blocks.
Panel structure: exactly four equal vertical panels in one wide landscape image, clean pale dividers, no labels.
Critical invariant: same character identity, hairstyle, outfit colors, body pose, railing, distant train, skyline silhouette, camera height, medium-wide framing, sunset direction, and basic composition in all four panels. Change only the final 2D visual construction.
Panel 1: digital 2D cel-style flat color, precise clean linework, controlled flat color shapes, two hard-edged shadow steps, stable painted background, crisp animation keyframe finish.
Panel 2: frame-by-frame watercolor painting appearance, translucent washes, visible cold-press paper grain, wet edges, pigment blooms, soft lost-and-found contours, luminous sunset preserved through paper white.
Panel 3: Chinese ink-animation visual language translated through observable mechanisms: expressive varying ink line, dry-brush city silhouettes, layered ink washes, generous breathing negative space, drifting diluted pigment, selective muted mineral teal and rust accents, spatial depth created by ink density rather than Western volumetric modeling.
Panel 4: geometric vector and cut-paper collage, simplified angular shapes, visibly layered colored paper, cut fibers and slight paper shadows, flat graphic perspective, restrained geometric pattern.
Composition/framing: wide 16:9 comparison board, each panel a self-contained vertical crop of the same medium-wide view.
Lighting/mood: clear youth-oriented urban dusk, coral horizon and cool blue upper sky, identical light direction across panels.
Constraints: exactly four panels; entirely original generic scene; no text, no letters, no numbers, no captions, no signs, no logos, no watermarks, no UI, no existing film characters, no recognizable franchise imagery, no additional people, no change of pose or camera between panels.
```

---

## 03｜三维渲染家族

- **文件名**：`03_3d_rendering_families.png`
- **四栏标签（左→右）**：摄影写实 PBR 式外观｜圆润风格化 3D｜Cel Shaded 3D｜Low-poly 3D
- **建议嵌入章节**：三维渲染家族。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：写实栏用皮肤、织物、木纹、玻璃与砖面的连续材质响应；圆润栏简化比例和形体；Cel 栏有轮廓线、硬色阶与图形高光；Low-poly 栏在人物、树木和建筑上均保留清晰面片。
- **QA**：通过。人物、吉他、琴盒和街角视点稳定，四种三维体块与表面差异清楚；持握关系可读，无文字、Logo 或明显肢体错误。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board for film-style browsing
Primary request: Show the same original young adult street musician at the same compact neighborhood corner in four distinct 3D rendering families. The character wears a burnt-orange hooded jacket, charcoal trousers, and white sneakers, stands beside a closed dark-blue guitar case, and adjusts the strap of a small acoustic guitar. Behind them are one rounded corner shop window with blank glass, one street tree, one bicycle rack, and brick paving.
Panel structure: exactly four equal vertical panels in one wide landscape image, clean neutral dividers, no labels.
Critical invariant: same character identity, hairstyle, clothing colors, body proportions, pose, guitar, guitar case, street corner geometry, object positions, camera height, medium-wide full-body framing, focal length, and soft late-afternoon light direction. Change only the 3D visual design and rendering family.
Panel 1: photorealistic high-end 3D CGI appearance with physically credible PBR materials, realistic skin and fabric microtexture, wood grain, glass reflections, rough brick, coherent global illumination and contact shadows; it must read like a photographed real street while remaining an original synthetic scene.
Panel 2: rounded stylized 3D, appealing simplified anatomy, broad soft shapes, gently exaggerated head and hands, smooth matte materials, soft sculpted hair clumps, clean cinematic global illumination; polished stylization, not toy plastic.
Panel 3: cel-shaded 3D with clearly modeled three-dimensional forms, precise dark contour lines, two or three hard tonal bands, graphic shaped highlights, compressed gradients, crisp anime-independent generic design.
Panel 4: low-poly 3D with intentionally reduced geometry, clean visible polygon facets on face, clothes, guitar, tree and architecture, flat-shaded planes, high-resolution clean output, strong readable silhouette; low-poly by design, not low quality.
Composition/framing: wide 16:9 comparison board; each panel uses the same medium-wide street-corner view.
Lighting/mood: calm late-afternoon neighborhood light, same warm key and cool sky fill across panels.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no readable signs, no logos, no brands, no watermarks, no UI; entirely original generic character; no existing film or game character resemblance; no extra people; no change of pose, camera, props, or scene layout between panels.
```

---

## 04｜实体与混合媒介

- **文件名**：`04_physical_mixed_media.png`
- **四栏标签（左→右）**：木偶定格｜黏土定格｜纸片剪纸定格｜真人材质＋绘画纸张＋摄影碎片混合拼贴
- **建议嵌入章节**：实体材料与混合媒介。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：木偶栏有可见关节、雕刻头手和真实针织服装；黏土栏有指纹、塑形和替换面痕迹；纸片栏是平面关节与纸层阴影；混合栏将真人皮肤和织物、绘画墙面、撕贴窗景与摄影物件并置。
- **QA**：通过。四栏动作、苹果、木碗和房间关系清楚；材料来源可辨，无文字、Logo、明显手部错误或构图失控。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board for film-style browsing
Primary request: Show the exact same quiet interior action in four distinct physical or mixed-media image families. An original young adult woman with a short black bob, mustard cardigan, blue shirt, and dark green skirt stands at a small wooden kitchen table, placing one red apple into a shallow wooden bowl with her right hand while her left hand steadies the bowl. The room has one square window, one simple chair, one cream table lamp, and a checked cloth.
Panel structure: exactly four equal vertical panels in one wide landscape image, clean neutral dividers, no labels.
Critical invariant: same character identity and hairstyle, same outfit colors, same body pose and hand action, same apple and bowl, same table, window, chair, lamp and cloth positions, same eye-level camera, medium-wide framing, and same soft window-light direction. Change only the material medium and construction.
Panel 1: handcrafted puppet stop-motion set, articulated fabric-and-wood puppet with discreet joints, tailored miniature clothes, carved wooden hands and head, real miniature furniture, physical textiles, authentic contact shadows and shallow miniature depth of field.
Panel 2: clay stop-motion set, fully sculpted clay character and props, visible fingerprints, subtle kneading and replacement-face seams, softly compressed clay edges, physical miniature lighting and real contact.
Panel 3: paper cut-out stop-motion, flat articulated paper character with visible pinned or layered joints, cut paper furniture and window, fibrous torn and scissor-cut edges, stacked paper shadows, clearly planar side-facing construction while preserving the same action.
Panel 4: deliberate mixed-media collage combining realistic photographic skin and cloth fragments for the person, hand-painted gouache paper for walls and furniture, torn photographic fragments for the window and apple, visible paper fibers, pasted seams, mismatched but intentional grain and perspective; coherent composition built from multiple material sources.
Composition/framing: wide 16:9 comparison board; each panel repeats the same medium-wide kitchen-table composition.
Lighting/mood: calm morning window light from the same side in all panels, tactile and observational.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no logos, no brands, no watermarks, no UI, no readable packaging; entirely original character; no existing film or franchise imagery; no extra people; anatomically understandable hands with exactly five fingers where dimensional; no change of action, camera, or room layout between panels.
```

---

## 05｜未来世界题材

- **文件名**：`05_future_world_genres.png`
- **四栏标签（左→右）**：Cyberpunk｜Solarpunk｜Steampunk｜Dieselpunk
- **建议嵌入章节**：未来世界／Punk 家族图鉴。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：四栏不是调色变化。赛博朋克栏显示封闭企业塔、监控、改造线缆和拥挤维修层；Solarpunk 栏显示太阳能、雨水系统、花园、公共交通与共同维护；Steampunk 栏显示蒸汽管网、锅炉、铆接铁件和机械维修；Dieselpunk 栏显示装饰艺术体量、柴油交通、工业烟气与中世纪机器文化。
- **QA**：通过。同一街口、推车配送员和机位稳定；四套技术制度、材料与生活方式清楚，背景人物均在维修、通行或劳动；无可读文字、Logo、IP 或明显结构错误。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board for film-style browsing
Primary request: Create an original four-panel comparison of the same street-level city block and camera composition rebuilt as four different future or alternate-history world systems. In every panel, a generic adult utility courier pushes a compact handcart across the same foreground crosswalk; a four-story corner building occupies the left, a transit stop sits center-right, and residents actively work in the middle distance.
Panel structure: exactly four equal vertical panels in one wide landscape image, clear neutral dividers, no labels.
Critical invariant: same street footprint, same camera height and wide three-quarter street view, same courier position and cart silhouette, same approximate building massing, same time of day. The world design, materials, infrastructure, power relations and everyday activity must change per panel; differences must not be mere color grading.
Panel 1 — cyberpunk: dense vertical class separation, aging stacked housing beneath a sealed corporate tower, biometric access chokepoint without readable UI, surveillance hardware, tangled retrofit cables, crowded street repair stalls, prosthetic maintenance, delivery labor and residents moving through cramped public space; technology is powerful but unevenly owned. Neon is sparse and functional, not a purple-pink wallpaper.
Panel 2 — solarpunk: community-operated neighborhood with visible rooftop solar thermal and photovoltaic systems, shaded public tram, rainwater channels, passive ventilation, food gardens integrated with housing, shared repair workshop, cargo bicycles, residents maintaining infrastructure together; biodiversity and labor are visible, not simply plants on glass towers.
Panel 3 — steampunk alternate history: steam-powered municipal tram, elevated insulated steam pipes, riveted iron and brick workshops, belt-driven repair machinery visible through open bays, pneumatic parcel tubes, soot-managed boilers, era-consistent tailored workwear and active mechanics; brass is used functionally, not as decoration everywhere.
Panel 4 — dieselpunk: interwar-to-mid-century machine culture, reinforced concrete block with Art Deco geometry, diesel trolley-bus or utility truck, aviation-inspired metal canopies, heavy riveted machinery, public fuel depot and maintenance crews, period work coats and industrial civic order; smoky diesel infrastructure and geometric propaganda-era massing without any text or symbols.
Composition/framing: wide 16:9 teaching board, four equal vertical panels, each a complete street-block view with clear foreground, working middle ground and architecture background.
Lighting/mood: neutral late-afternoon side light shared across panels so world-system differences remain legible.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no readable signs, no logos, no brands, no watermarks, no national or political emblems, no existing franchise designs or characters; original worldbuilding; background people must be engaged in purposeful continuous actions, not standing motionless; avoid style differences based only on palette.
```

---

## 06｜大众口语风格译码

- **文件名**：`06_popular_style_decoding.png`
- **四栏标签（左→右）**：澄澈高细节都市天空与天气光的青春 2D｜温暖有生活痕迹的手绘自然幻想 2D｜正面居中、粉彩、平面调度的故事书真人美术｜细长轮廓、扭曲建筑、黑白＋单一强调色的哥特童话定格感
- **建议嵌入章节**：大众口语风格称呼如何转译为通用画面机制。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：第一栏以大尺度高细节天空、云缘光和湿地反射建立青春天气感；第二栏靠旧木、藤蔓、补丁、生活器物与手绘线条建立自然幻想；第三栏靠正面居中、严格对称、粉彩块面与浅舞台空间形成真人故事书美术；第四栏靠细长木偶轮廓、扭曲站台、硬斜光和黑白中的红鞋单色强调成立。
- **QA**：修正后通过。首轮第四栏旅行包残留绿色，破坏“单一强调色”；唯一一次修正将第四栏除红鞋外全部转为灰阶，前三栏、站位和构图保持稳定。无文字、Logo、IP 或明显肢体问题。

### 基础生成提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board translating popular informal style descriptions into observable visual mechanisms
Primary request: Show the same original young adult waiting alone on the same suburban commuter platform in four broadly recognizable but fully generic final visual styles. The person has short dark hair, wears a pale cream windbreaker, navy trousers, red canvas shoes, and carries a small green duffel bag. They stand beside one bench, looking down the tracks; a small shelter, overhead wires, distant low buildings and a broad sky remain the basic scene.
Panel structure: exactly four equal vertical panels in one wide landscape image, clear neutral dividers, no labels.
Critical invariant: same character identity, outfit colors, waiting pose, green bag position, bench and track direction, eye-level medium-wide camera, and narrative moment. Change the final visual mechanisms, production design and atmospheric treatment per panel.
Panel 1: youth-oriented digital 2D animation with exceptionally clear high-detail urban sky and weather light; precise clean linework, luminous cloud layers, atmospheric perspective, sunlit cloud edges, subtle wet-platform reflections, tiny everyday city details, crisp color separation, emotional contrast between small waiting figure and vast changing sky. No imitation of any named creator or studio.
Panel 2: warm hand-drawn natural-fantasy 2D with lived-in material detail; soft irregular pencil and paint lines, weathered timber shelter, moss and vines integrated with practical drainage, patched cushions, old enamel objects, wind moving leaves, warm window light and layered greenery; gentle everyday magic suggested by small natural motion, not by franchise creatures. No imitation of any named creator or studio.
Panel 3: live-action storybook production design with frontal centered camera, rigorous symmetry, pastel color blocks, shallow theatrical space, carefully arranged bench and shelter, matte painted surfaces, deliberately flat staging, restrained deadpan pose, practical set and costume textures; whimsical yet controlled. No imitation of any named director.
Panel 4: gothic fairy-tale stop-motion-like material appearance with a slender elongated puppet silhouette, twisted but readable station architecture, crooked overhead poles, black-and-white palette with only the red shoes as a single accent color, carved and fabric materials, hard raking shadows, miniature fog and slightly stepped pose; elegant melancholy rather than horror gore. No imitation of any named creator.
Composition/framing: wide 16:9 teaching board, four equal vertical panels, each showing the same complete platform waiting moment.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no readable station signs, no logos, no brands, no watermarks, no UI, no existing film characters, no franchise imagery, no creator names represented visually, no extra foreground people; no grotesque anatomy; clear hands and feet; no cross-contamination of the four visual mechanisms.
```

### 唯一修正提示词

```text
Edit the most recently generated four-panel image.
Change only the fourth (far-right) panel: make every element strictly grayscale except the character's red canvas shoes, which remain the only colored accent. Specifically remove all green from the duffel bag and render the bag in grayscale; remove any other residual color in the fourth panel.
Preserve the first three panels exactly as they are. Preserve all four panel widths, dividers, character identity, pose, clothing, bag shape, station architecture, camera, lighting and composition. Do not add or remove objects.
No text, letters, numbers, logos, signs, watermarks or UI.
```

---

## 07｜完整组合效果 A

- **文件名**：`07_complete_combinations_a.png`
- **四栏标签（左→右）**：3D Cel Shading＋Cyberpunk＋Neo-noir＋Art Deco／Brutalism｜2D 水彩＋Solarpunk＋青春爱情＋高调天气光｜真人写实＋硬科幻＋Brutalism＋纪录观察｜木偶定格＋Gothic Romance＋德国表现主义影响＋低调光
- **建议嵌入章节**：跨层完整组合示范 A。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：四栏保持“两人在建筑入口交换重要小物件”的基本动作。第一栏用三维 Cel 体块、企业门槛、低调功能光和装饰艺术／粗野主义入口建立技术权力；第二栏用水彩、共治能源设施、雨后高调光和羞涩身体关系建立青春爱情；第三栏用月面气闸、磨损、尘控和观察机位建立硬科幻；第四栏用实体木偶、扭曲门洞、斜影和腐朽材质建立哥特关系。
- **QA**：修正后通过。首轮第一栏的赛博朋克与 Neo-noir 成立，但 Cel Shading 不够明显；唯一一次修正增强第一栏轮廓线、硬边两三级阴影和图形高光，保留后三栏与原有构图。无文字、Logo、IP 或明显手部错误。

### 基础生成提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board showing complete cross-layer film-style combinations
Primary request: Create four fully realized, independent cinematic style combinations around the same basic blocking: one adult stands in the left foreground and returns a small important object to a second adult waiting inside a large architectural threshold on the right. The handoff and two-person relationship remain readable, while each panel rebuilds the characters, object, world and final image according to its complete combination.
Panel structure: exactly four equal vertical panels in one wide landscape image, clean neutral dividers, no labels.
Panel 1: 3D CGI with precise cel shading; science fiction > cyberpunk world where access and infrastructure are controlled by a powerful corporation; Neo-noir moral tension; monumental Brutalist concrete transit gate with restrained Art Deco bronze geometry; low-key night image illuminated only by motivated ticket-machine strips, maintenance lamps and distant vehicle light; two or three hard tonal bands, controlled outlines, wet surfaces, clear 3D depth. A courier returns a stolen access token to a maintenance worker. Sparse functional cyan and amber, not generic purple-pink neon.
Panel 2: hand-painted 2D watercolor; Solarpunk neighborhood where renewable infrastructure is maintained collectively; youth romance; high-key weather light just after a summer shower; translucent pigment, paper grain, luminous clouds, solar canopy, rain garden and shared bicycle workshop. One young adult returns a pressed-leaf keepsake to another at a garden tram shelter; shy, hopeful body language.
Panel 3: photorealistic live-action appearance; hard science fiction; exposed Brutalist lunar research habitat; observational documentary camera at human height; functional white work light and harsh reflected lunar daylight; credible pressure seals, dust control, repair wear and resource constraints. A suited technician returns a sealed sample cartridge to a habitat engineer at an airlock threshold. Natural restrained performance, physically plausible equipment, no decorative sci-fi UI.
Panel 4: real handcrafted puppet stop-motion appearance; Gothic Romance with forbidden memory and decaying family space; influenced by observable German Expressionist mechanisms: distorted doorway, impossible angled walls, elongated shadows and subjective architecture; low-key candle and moonlight. A slender fabric-and-wood puppet returns a small locket to another puppet inside a warped mansion entrance; tactile miniature materials, articulated joints, melancholy intimacy, black charcoal and faded burgundy.
Composition/framing: wide 16:9 teaching board; four equal vertical panels; similar two-person diagonal blocking and architectural threshold scale in every panel, each panel a polished final film frame.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no signs, no logos, no brands, no watermarks, no UI text, no national symbols, no existing film characters or franchise designs; original generic characters; clear hands and object exchange; no style spill between panels.
```

### 唯一修正提示词

```text
Edit the most recently generated four-panel image.
Change only the first (far-left) panel. Preserve its cyberpunk Neo-noir scene, two-person handoff, Art Deco and Brutalist doorway, camera, composition, objects, wet ground, functional cyan and amber lights, and low-key mood. Make the rendering unmistakably 3D cel-shaded: add controlled dark contour lines around character silhouettes and major architecture edges, compress all form lighting into two or three clearly hard-edged tonal bands, use crisp graphic shaped highlights, remove smooth photorealistic skin and fabric gradients while keeping modeled 3D depth and coherent perspective.
Preserve panels 2, 3 and 4 exactly as they are. Do not change panel widths or dividers.
No text, letters, numbers, logos, signs, watermarks or UI.
```

---

## 08｜完整组合效果 B

- **文件名**：`08_complete_combinations_b.png`
- **四栏标签（左→右）**：3D 水墨 NPR＋武侠＋长镜空间感｜2D Pixel Art＋后末日生存＋有限色板｜真人摄影＋2D 拼贴＋超现实散文电影｜Low-poly 3D＋Cozy Fantasy＋Pastel＋柔和环境光
- **建议嵌入章节**：跨层完整组合示范 B。
- **正文嵌入**：`[Image omitted from the public edition pending source and reuse-rights verification.]`
- **可观察差异**：四栏保持“旅人提灯沿路径走向庇护所”的基本关系。水墨栏用三维连续山路、亭子、墨线、干笔和留白承载武侠空间；Pixel 栏用统一像素尺度、有限色板、废弃设施和资源物件建立生存；真人拼贴栏以摄影道路为现实层，叠加撕纸天空、照片碎片和非现实物件联想；Low-poly 栏用清晰面片、柔和粉彩、菜园、柴堆、面包与暖窗建立低威胁照料感。
- **QA**：通过。四栏媒介和完整组合边界清晰；灯笼持握与路径关系可读；无可读文字、Logo、IP、栏位串扰或明显人体错误。未修正。

### 最终提示词

```text
Use case: scientific-educational
Asset type: landscape four-panel visual atlas board showing complete cross-layer film-style combinations
Primary request: Create four fully realized cinematic combinations around one shared narrative image: a lone traveler carrying a small lantern follows a path from the left foreground toward a shelter on the right middle distance. Keep the traveler-path-shelter relationship and wide spatial composition readable in all panels, while changing medium, world and final visual language.
Panel structure: exactly four equal vertical panels in one wide landscape image, clean neutral dividers, no labels.
Panel 1: 3D CGI environment and character rendered through Chinese ink-inspired NPR; wuxia world; long-take spatial feeling expressed in one deep continuous mountain-path composition with multiple navigable depth planes, clear entrances and exits, and a distant covered pavilion. Expressive varying ink contours, dry-brush rock textures, layered wash density, breathing negative space and restrained mineral-red lantern accent; three-dimensional perspective remains coherent, not a flat ink filter. A wandering swordswoman in simple travel robes carries the lantern, no fantasy magic effects.
Panel 2: hand-designed 2D pixel art; post-apocalyptic survival; limited palette of dusty ochre, charcoal, muted olive and one pale lamp tone; deliberate pixel clusters, consistent pixel scale, crisp nearest-neighbor edges, side-oblique ruined service road, salvaged metal shelter, water containers and repaired gear. Survivor carries the lantern toward safety; clear environmental resource story, not merely ruins.
Panel 3: photorealistic live-action photography combined with deliberate 2D collage for a surreal essay-film image; an ordinary traveler walks toward a roadside bus shelter while torn painted paper sky layers, photographic memory fragments, hand-drawn arrows without text, and mismatched-scale household object silhouettes intrude into the real landscape. Visible paper seams, archival grain differences and nonliteral spatial associations suggest memory and thought; the live-action person and road remain photographically grounded. No recognizable archival source or copyrighted image.
Panel 4: low-poly 3D; cozy fantasy; pastel palette and soft ambient light; clean visible polygon facets, simplified traveler with lantern, gently curved path, small welcoming stone-and-timber cottage shelter, kitchen garden, stacked firewood, bread basket and tiny warm windows; low threat, everyday care and safety communicated through useful objects and open posture, not just yellow lighting.
Composition/framing: wide 16:9 teaching board, four equal vertical panels, each a complete wide shot with traveler left foreground, path through center, shelter right middle distance and layered background.
Constraints: exactly four panels; no text, no letters, no numbers, no captions, no signs, no logos, no brands, no watermarks, no UI, no existing film or game characters, no franchise imagery; original scenes; no extra foreground people; no style spill between panels; preserve clear anatomy and readable lantern grip.
```

---

## 主任务合并前建议复核

1. 由主任务决定 8 张图在 A2-07 中的最终排序、外部中文标题和图注，不在图片内部追加文字。
2. 01、03 的“PBR”只作为外观描述；若正文讨论真实工艺，必须继续保留“最终视觉不能证明生产管线”的边界。
3. 05 的 Punk 四栏适合与正文的世界规则定义并读，避免读者把图像当作唯一标准样貌。
4. 06 的四栏故意不出现作者或工作室名称；正文若解释大众口语称呼，仍应优先使用可观察机制而非个人风格模仿指令。
5. 当前资产状态为“已生成并经 Codex 目视 QA，待主任务／用户审美验收”，不等于已经合入正式知识卡。
