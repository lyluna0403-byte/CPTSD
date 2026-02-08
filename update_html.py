import re
import os

# Define the new HTML content for the sections
# Using the content from CPTSD.md

part3_html = """
            <!-- 第三部分 -->
            <section id="part3" class="mb-12">
                <div class="section-header">
                    <div class="header-line"></div>
                    <div class="header-box">第三部分：社交疗愈 (缩减外在批判者)</div>
                    <div class="header-line"></div>
                </div>
                <div class="content-section">
                    <p class="text-sm text-gray-500 mb-6 leading-relaxed">外在批判者让你把周围的人都视为危险、有缺陷或不可信的，表现为被动攻击性、批评他人、需要控制一切，会导致社交孤立或破裂。</p>
                    
                    <div class="mb-8">
                        <h4 class="font-bold mb-4 text-[#DE95BA]">1. 视角转换练习</h4>
                        <ul class="text-xs text-gray-500 space-y-4 list-dot">
                            <li><strong>识破投射：</strong>当你强烈地批判某人时，问自己：“这是否是我对自己不满的投射？”或者“这是否是我过去施虐者特质的重现？”</li>
                            <li><strong>打破二元对立：</strong>
                                <div class="mt-2 pl-2 border-l-2 border-pink-100">
                                    <p class="mb-1"><strong>练习：</strong>列出这个人的3个优点和3个缺点。</p>
                                    <p><strong>提醒：</strong>“人是复杂的混合体。某人有一个缺点，并不代表他完全不可信。”</p>
                                </div>
                            </li>
                            <li><strong>区分“危险”与“不完美”：</strong>
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-2">
                                    <div class="bg-red-50 p-3 rounded text-gray-600">
                                        <strong>危险的人：</strong>虐待狂、无同理心、只索取 (需远离)。
                                    </div>
                                    <div class="bg-green-50 p-3 rounded text-gray-600">
                                        <strong>不完美的人：</strong>偶尔犯错但本质善良、愿意沟通 (可建立关系)。我们可以对“不完美”的人感到失望，但不必因此切断关系。
                                    </div>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="font-bold mb-4 text-[#DE95BA]">2. 冲突解决工具</h4>
                        <ul class="text-xs text-gray-500 space-y-3 list-dot">
                            <li><strong>暂停技术：</strong>当对话变得激烈或感到被触发时，要求暂停 (1分钟到24小时)，直到情绪回归平稳。</li>
                            <li><strong>"我"字句：</strong>避免说“你总是...”，改用“当...发生时，我感到...”。</li>
                            <li><strong>先肯定：</strong>在抱怨前，先肯定对方和这段关系的价值。</li>
                            <li><strong>去理想化：</strong>接受冲突是关系的一部分，不是关系的终结。</li>
                        </ul>
                    </div>
                </div>
            </section>
"""

part4_html = """
            <!-- 第四部分 -->
            <section id="part4" class="mb-12">
                <div class="section-header">
                    <div class="header-line"></div>
                    <div class="header-box">第四部分：情绪释放 (哀悼工作)</div>
                    <div class="header-line"></div>
                </div>
                <div class="content-section">
                    <p class="text-sm text-gray-500 mb-6 leading-relaxed">未被表达的悲伤是CPTSD的核心。通过“哀悼”将积压的创伤能量排出体外。</p>
                    
                    <h4 class="font-bold mb-6 text-center">四种关键的哀悼形式</h4>
                    
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div class="step-item">
                            <h5 class="font-bold text-[#DE95BA] mb-2 text-lg">1. 愤怒</h5>
                            <ul class="text-xs text-gray-500 space-y-2">
                                <li><strong>目的：</strong>减少恐惧，重建边界，将内化的羞耻转化为自我保护。</li>
                                <li><strong>方法：</strong>独自一人时，对过去的施虐者大声表达愤怒：“这不公平！”“你不该那样对我！”</li>
                            </ul>
                        </div>
                        <div class="step-item">
                            <h5 class="font-bold text-[#DE95BA] mb-2 text-lg">2. 哭泣</h5>
                            <ul class="text-xs text-gray-500 space-y-2">
                                <li><strong>目的：</strong>释放悲伤，切断交感神经的过度兴奋。</li>
                                <li><strong>方法：</strong>不要压抑眼泪。为那个曾经受苦的小孩而哭，这是一种深度的自我怜悯。可以找一个安全舒适的地方，播放音乐或者看一部感人的电影，回忆被人善待的记忆等。</li>
                            </ul>
                        </div>
                        <div class="step-item">
                            <h5 class="font-bold text-[#DE95BA] mb-2 text-lg">3. 口头宣泄</h5>
                            <ul class="text-xs text-gray-500 space-y-2">
                                <li><strong>目的：</strong>认知重组，打破孤立。</li>
                                <li><strong>方法：</strong>找一个安全的人倾诉，或写日记/录音。把混乱的痛苦变成有逻辑的语言。</li>
                            </ul>
                        </div>
                        <div class="step-item">
                            <h5 class="font-bold text-[#DE95BA] mb-2 text-lg">4. 感受</h5>
                            <ul class="text-xs text-gray-500 space-y-2">
                                <li><strong>目的：</strong>瓦解解离，从身体层面释放压力。</li>
                                <li><strong>方法：</strong>被动地关注身体的紧张部位 (如胸口的紧绷)，不试图改变它，只是通过觉察与这种不适共存，直到它自然消解。</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
"""

part5_html = """
            <!-- 第五部分 -->
            <section id="part5" class="mb-12">
                <div class="section-header">
                    <div class="header-line"></div>
                    <div class="header-box">第五部分：管理“遗弃抑郁”</div>
                    <div class="header-line"></div>
                </div>
                <div class="content-section">
                    
                    <div class="mb-10">
                        <h4 class="font-bold mb-4 text-[#DE95BA]">1. 理解反应循环</h4>
                        <p class="text-xs text-gray-500 mb-3">了解这个恶性循环，有助于你从中跳脱出来：</p>
                        <div class="bg-[#fffbf7] p-4 rounded-lg border border-pink-100">
                            <ul class="text-xs text-gray-500 space-y-2 list-dot">
                                <li><strong>触发：</strong>遗弃抑郁发作 (感到渺小、绝望、空虚)。</li>
                                <li><strong>情绪反应：</strong>引发剧烈的恐惧和羞耻 (“我是个错误”、“我没人要”)。</li>
                                <li><strong>认知反应：</strong>内在批判者被激活 (“如果你够好，就不会发生这种事”)。</li>
                                <li><strong>行为反应：</strong>启动4F反应 (战、逃、僵、讨好) 作为防御机制。</li>
                            </ul>
                        </div>
                    </div>

                    <div class="mb-10">
                        <h4 class="font-bold mb-4 text-[#DE95BA]">2. 识别闪回的迹象</h4>
                        <p class="text-xs text-gray-500 mb-3">当出现以下迹象时，请告诉自己：“我正在经历遗弃抑郁的闪回。”</p>
                        <ul class="text-xs text-gray-500 space-y-3 list-dot">
                            <li><strong>情绪迹象：</strong>感到极度渺小、无助、绝望；羞耻感爆棚，不敢见人；自我价值感瞬间蒸发。</li>
                            <li><strong>认知迹象：</strong>内在/外在批判者声音变大；思维极端化 (非黑即白)；灾难化思维 (觉得一切都完了)。</li>
                            <li><strong>行为迹象：</strong>情绪反应与当下的触发事件不成比例；增加自我药疗行为 (成瘾、暴食等)；极度回避或过度黏人。</li>
                        </ul>
                    </div>

                    <div class="mb-10">
                        <h4 class="font-bold mb-4 text-[#DE95BA]">3. 穿越遗弃抑郁的路线图</h4>
                        <div class="quote-bubble mb-4">不要试图抵抗，而是像冲浪一样等待浪潮过去。</div>
                        <ul class="text-xs text-gray-500 space-y-3 list-dot">
                            <li><strong>识别下坠感：</strong>当内心突然出现巨大空洞时，标记它：“这是遗弃抑郁，是旧伤复发。”</li>
                            <li><strong>理解本质：</strong>这不是你现在的性格缺陷，这是童年被忽视、被拒绝的“记忆情绪”回放。</li>
                            <li><strong>接纳而非抵抗：</strong>告诉自己：“我现在感觉很糟糕，这很正常，因为我正在处理过去的旧伤。”不要试图立刻“修好”它 (那是批判者的要求)。</li>
                            <li><strong>保持联结：</strong>想象自己抱着那个被遗弃的婴儿 (你自己的内在小孩)。</li>
                            <li><strong>等待浪潮过去：</strong>这种绝望感是波浪状的。如果你不惊慌、不自我攻击，它最终会消退。</li>
                        </ul>
                    </div>

                    <div>
                        <h4 class="font-bold mb-4 text-[#DE95BA]">4. 三大管理策略</h4>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <div class="p-3 border border-pink-100 rounded bg-white">
                                <strong class="block text-pink-400 text-xs mb-2">区分痛苦</strong>
                                <p class="text-[11px] text-gray-500">区分“必要的痛苦”(正常的悲伤、恐惧) 和“不必要的痛苦”(自我遗弃、毒性羞耻、批判者的攻击)。</p>
                            </div>
                            <div class="p-3 border border-pink-100 rounded bg-white">
                                <strong class="block text-pink-400 text-xs mb-2">身体正念</strong>
                                <p class="text-[11px] text-gray-500">觉察身体哪里紧张？通过系统化拉伸缓解肌肉的“盔甲化”，通过身体感受来释放冻结的记忆。</p>
                            </div>
                            <div class="p-3 border border-pink-100 rounded bg-white">
                                <strong class="block text-pink-400 text-xs mb-2">正念代谢抑郁</strong>
                                <p class="text-[11px] text-gray-500">像消化食物一样消化情绪。允许抑郁流经你的意识，不加评判地观察它，发展对自己的深度同情。</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

part6_html = """
            <!-- 第六部分 -->
            <section id="part6" class="mb-12">
                <div class="section-header">
                    <div class="header-line"></div>
                    <div class="header-box">第六部分：通过关系治愈创伤</div>
                    <div class="header-line"></div>
                </div>
                <div class="content-section">
                    <p class="text-sm text-gray-500 mb-8 text-center italic font-bold">核心原则：关系造成的创伤，最终需要在关系中治愈。</p>
                    
                    <div class="mb-10">
                        <h4 class="font-bold mb-4 text-[#DE95BA]">1. 关系疗愈的阶梯</h4>
                        <p class="text-xs text-gray-500 mb-4">如果你暂时无法信任他人，可以按照这个阶梯循序渐进：</p>
                        
                        <div class="space-y-4">
                            <div class="flex items-start gap-3">
                                <div class="bg-pink-100 text-pink-500 font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 text-xs">1</div>
                                <div>
                                    <strong class="text-xs text-gray-700 block">阅读疗愈</strong>
                                    <p class="text-[11px] text-gray-500">与书本建立关系。当你感到被作者理解时，这是一种低风险的联结。</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-3">
                                <div class="bg-pink-100 text-pink-500 font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 text-xs">2</div>
                                <div>
                                    <strong class="text-xs text-gray-700 block">寻找“足够好”的人</strong>
                                    <p class="text-[11px] text-gray-500">放弃寻找完美的父母替代品。寻找那些有同理心、愿意倾听、能为自己的错误道歉的人。</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-3">
                                <div class="bg-pink-100 text-pink-500 font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 text-xs">3</div>
                                <div>
                                    <strong class="text-xs text-gray-700 block">治疗性关系</strong>
                                    <p class="text-[11px] text-gray-500">好的心理咨询师可以作为“替代性父母”，提供无条件的积极关注，让你体验安全的依恋。</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-3">
                                <div class="bg-pink-100 text-pink-500 font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 text-xs">4</div>
                                <div>
                                    <strong class="text-xs text-gray-700 block">脆弱性练习</strong>
                                    <p class="text-[11px] text-gray-500">在安全的关系中，尝试暴露一点点脆弱 (如承认恐惧)。如果对方反应良好，再多暴露一点。这是重建信任的重要途径。</p>
                                </div>
                            </div>
                            <div class="flex items-start gap-3">
                                <div class="bg-pink-100 text-pink-500 font-bold rounded-full w-6 h-6 flex items-center justify-center flex-shrink-0 text-xs">5</div>
                                <div>
                                    <strong class="text-xs text-gray-700 block">通过哀悼修复</strong>
                                    <p class="text-[11px] text-gray-500">当在关系中感到失望时，与其攻击或断联，不如表达受伤 (“你那样说时，我感到很难过”)。</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div>
                        <h4 class="font-bold mb-4 text-[#DE95BA]">2. 疗愈性关系的四个关键品质</h4>
                        <p class="text-xs text-gray-500 mb-4">在寻找伴侣、朋友或治疗师时，寻找具备这些品质的关系：</p>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <div class="glass-card p-4 rounded-xl">
                                <strong class="text-pink-400 text-xs block mb-1">共情</strong>
                                <p class="text-[11px] text-gray-500">对方能通过感受进入你的体验，能仔细倾听并镜像你的感受。</p>
                            </div>
                            <div class="glass-card p-4 rounded-xl">
                                <strong class="text-pink-400 text-xs block mb-1">真诚的脆弱性</strong>
                                <p class="text-[11px] text-gray-500">真实的关系造就健康的关系。适度的自我表露能打破羞耻感。</p>
                            </div>
                            <div class="glass-card p-4 rounded-xl">
                                <strong class="text-pink-400 text-xs block mb-1">对话性</strong>
                                <p class="text-[11px] text-gray-500">关系是互动的，能提供创伤知识，减少羞耻，增加控制感。</p>
                            </div>
                            <div class="glass-card p-4 rounded-xl">
                                <strong class="text-pink-400 text-xs block mb-1">协作关系修复</strong>
                                <p class="text-[11px] text-gray-500">能够承认伤害，承担责任，并共同修复关系。这比从不犯错更重要。</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
"""

part7_html = """
            <!-- 附录部分 -->
            <section id="part7" class="mb-20">
                <div class="section-header">
                    <div class="header-line"></div>
                    <div class="header-box">附录：幸存者工具箱</div>
                    <div class="header-line"></div>
                </div>

                <!-- 康复意图 -->
                <div class="content-section">
                    <h4 class="font-bold mb-4 text-[#DE95BA]">1. CPTSD 康复意图</h4>
                    <p class="text-xs text-gray-400 mb-3">每天朗读这些意图，重塑你的潜意识：</p>
                    <ul class="text-xs text-gray-500 space-y-2 list-dot">
                        <li>我想要与我自己发展更持续的、充满爱和接纳的关系。</li>
                        <li>我想要学会成为自己最好的朋友。</li>
                        <li>我想要吸引基于爱、尊重、公平和相互支持的关系。</li>
                        <li>我想要从毒性羞耻感中获得越来越多的自由。</li>
                        <li>我想要发现完整、不受抑制的自我表达。</li>
                        <li>我想要工作、休息和娱乐的平衡；稳定和变化的平衡。</li>
                        <li>我想要找到有效和非虐待的方式来处理愤怒。</li>
                        <li>我想要获得最佳的身体健康，培养活力与平静的平衡。</li>
                        <li>我想要在我的生活中为美和自然留出充足的空间。</li>
                    </ul>
                </div>

                <!-- 权利法案 -->
                <div class="content-section">
                    <h4 class="font-bold mb-4 text-[#DE95BA]">2. 人类权利法案</h4>
                    <p class="text-xs text-gray-400 mb-3">你是成年人，你拥有以下不可剥夺的权利：</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">1. 我有权得到尊重的对待。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">2. 我有权说“不”。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">3. 我有权犯错。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">4. 我有权拥有自己的感受、信念、观点和偏好。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">5. 我有权拒绝未经请求的建议或反馈。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">6. 我有权改变主意、计划或行动方案。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">7. 我有权抗议讽刺、破坏性批评或不公平待遇。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">8. 我有权感到愤怒并以非虐待方式表达它。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">9. 我有权拒绝为任何其他人的问题或不良行为承担责任。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">10. 我有权偶尔幼稚、不成熟、矛盾或不一致。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">11. 我有权玩耍、浪费时间并不总是富有成效。</div>
                        <div class="text-[11px] p-2 border border-pink-50 rounded bg-white hover:bg-pink-50 transition-colors">12. 我有权向朋友寻求情感支持，适度抱怨和宣泄。</div>
                    </div>
                </div>

                <!-- 沟通工具 -->
                <div class="content-section">
                    <h4 class="font-bold mb-4 text-[#DE95BA]">3. 冲突解决与沟通工具</h4>
                    <div class="space-y-6">
                        <div class="step-item">
                            <span class="text-sm font-bold text-pink-400 block mb-2">3.1 健康沟通准则</span>
                            <ul class="text-xs text-gray-500 space-y-1 list-dot">
                                <li><strong>目标：</strong>是告知和协商改变，而不是惩罚。</li>
                                <li><strong>前提：</strong>在抱怨前，先肯定对方和关系的价值。</li>
                                <li><strong>禁忌：</strong>不辱骂、不讽刺、不人身攻击、不读心(猜测动机)、不打断。</li>
                                <li><strong>技巧：</strong>使用“我”陈述(“我感到......”)，避免“你”陈述(“你总是......”)。一次只处理一个具体问题。保持对话简洁。</li>
                                <li><strong>正常化冲突：</strong>两个人都可以是对的，只是观点不同。</li>
                            </ul>
                        </div>
                        <div class="step-item">
                            <span class="text-sm font-bold text-pink-400 block mb-2">3.2 “暂停”技术</span>
                            <ul class="text-xs text-gray-500 space-y-1 list-dot">
                                <li><strong>何时使用：</strong>当讨论变得激烈、任何一方感到过度触发、或遭遇对方过度攻击时。</li>
                                <li><strong>如何做：</strong>约定一个暂停手势或暗号。立即停止互动。</li>
                                <li><strong>时长：</strong>1分钟到24小时不等，取决于恢复平静需要多久。</li>
                            </ul>
                        </div>
                        <div class="step-item">
                            <span class="text-sm font-bold text-pink-400 block mb-2">3.3 移情工作</span>
                            <ul class="text-xs text-gray-500 space-y-1 list-dot">
                                <li><strong>警惕：</strong>当你对伴侣的轻微错误产生剧烈的愤怒或恐惧时，这通常是移情(将对父母的反应投射到了伴侣身上)。</li>
                                <li><strong>识别：</strong>伴侣的一个眼神、一句话触发了你数十年的痛苦。</li>
                                <li><strong>处理：</strong>意识到这是“过去在入侵现在”，通过沟通澄清事实，而非陷入投射性认同。</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </section>
"""

# Read existing HTML
file_path = '/Users/lisansui/12-AI使用/CPTSD/疗愈指南.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Helper function to replace section by ID
def replace_section(content, section_id, new_html):
    pattern = re.compile(f'<section id="{section_id}".*?</section>', re.DOTALL)
    if pattern.search(content):
        return pattern.sub(new_html.strip(), content)
    else:
        print(f"Warning: Section {section_id} not found!")
        return content

# Perform replacements
# Note: For Part 3, we replace the existing 'part3' with BOTH part3_html and part4_html
# We construct a combined string for the replacement
combined_part34 = part3_html + "\n\n" + part4_html
content = replace_section(content, 'part3', combined_part34)
content = replace_section(content, 'part5', part5_html)
content = replace_section(content, 'part6', part6_html)
content = replace_section(content, 'part7', part7_html)

# Clean up CPTSD.md artifacts in the file if any leaked (unlikely with this method but good practice)
# Also clean up the actual CPTSD.md file
md_path = '/Users/lisansui/12-AI使用/CPTSD/CPTSD.md'
if os.path.exists(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Regex cleanup for MD
    md_content = re.sub(r'\\resizebox\{.*?\}\{.*?\}\{(.*?)\}', r'\1', md_content)
    md_content = re.sub(r'\}\s*\[0.3cm\]', '', md_content)
    md_content = re.sub(r'\{自我疗愈指南\}', '自我疗愈指南', md_content)
    md_content = re.sub(r'% .*', '', md_content)
    md_content = re.sub(r'\\setlength.*?', '', md_content)
    md_content = re.sub(r'\{\|.*?\|\}', '', md_content)
    md_content = re.sub(r'\*\*\}\s*&', '', md_content)
    md_content = re.sub(r'\*\*\}\s*\\\\', '', md_content)
    
    # Fix table structure if broken
    # (This is a best-effort cleanup)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

# Write updated HTML
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated 疗愈指南.html and cleaned CPTSD.md")
