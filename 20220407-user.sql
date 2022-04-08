/*
 Navicat Premium Data Transfer

 Source Server         : my_db
 Source Server Type    : MySQL
 Source Server Version : 80026
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 80026
 File Encoding         : 65001

 Date: 08/04/2022 09:20:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `type` tinyint(0) NOT NULL COMMENT '0-普通用户 1-视频发布者',
  `username` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
  `user_id` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户24位编码标识',
  `homepage` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '主页链接',
  `subscribers` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '订阅人数-因为很多人的话就不显示具体数目了所以不用int类型',
  `views` int(0) NOT NULL DEFAULT 0 COMMENT '累计观看次数',
  `join_time` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '注册日期',
  `description` varchar(4096) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '描述',
  `details` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '其余细节信息如location',
  `links` varchar(4096) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '' COMMENT '外链-可能多个',
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_id`(`user_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = 'youtube用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (26, 0, 'Terry Simmons TV', 'UCpaxyzNPLQt8m3c9MMJGatg', 'http://www.youtube.com/channel/UCpaxyzNPLQt8m3c9MMJGatg', '148', 34448, '2017年5月12日', 'Official Youtube of Terry Simmons Make sure to Like Comment & Subscribe if your gang and New to the Channel Turn on your post notifications!! & SMASH THE LIKE BUTTON!!! 43VER LIT⚡️ #SimmonsEntertainment', '', '');
INSERT INTO `user` VALUES (27, 0, 'azahra azahra', 'UCdputZFHgLO1EGA7S7indhQ', 'http://www.youtube.com/channel/UCdputZFHgLO1EGA7S7indhQ', '87', 0, '2020年10月23日', '', '', '');
INSERT INTO `user` VALUES (28, 0, 'Rachellouis💞', 'UCmA4vvxHv0aAQM3FChujFkw', 'http://www.youtube.com/channel/UCmA4vvxHv0aAQM3FChujFkw', '711', 0, '2021年7月1日', '', '', '');
INSERT INTO `user` VALUES (29, 0, 'Beautiful Swabi', 'UCoj53901mMAXs5eWXW5KHvA', 'http://www.youtube.com/channel/UCoj53901mMAXs5eWXW5KHvA', '0', 2110907, '2015年6月2日', 'I will try to show you the  beauty of swabi\nIf you like our video.  So share with your friends. Subscribe to our channel and make nice comments.Thank you', '', '');
INSERT INTO `user` VALUES (30, 0, 'shu xi', 'UCR4f3-eWgO64rBYXWV4lvOg', 'http://www.youtube.com/channel/UCR4f3-eWgO64rBYXWV4lvOg', '141', 0, '2021年9月21日', '', '', '');
INSERT INTO `user` VALUES (31, 0, 'Curvy Tv', 'UCkNQ7AobiUzHMgaFNCDAg9Q', 'http://www.youtube.com/channel/UCkNQ7AobiUzHMgaFNCDAg9Q', '5', 379, '2020年10月26日', '', '', '');
INSERT INTO `user` VALUES (32, 0, 'Amjad Laghari', 'UC_dCfxFvC39qEZnylemt44g', 'http://www.youtube.com/channel/UC_dCfxFvC39qEZnylemt44g', '11', 105, '2022年3月16日', 'TikTok lovers kotri', '', '');
INSERT INTO `user` VALUES (33, 0, 'TikTok Big Dude', 'UCd4ygecNWWnvhGdtiCU9rBw', 'http://www.youtube.com/channel/UCd4ygecNWWnvhGdtiCU9rBw', '0', 16388, '2019年12月6日', '#Tiktok#TiktokChallenge#BigBank#TiktokChallengeBigDude\nSubscribe, Like, Share. Thank\'s', '', '');
INSERT INTO `user` VALUES (34, 0, '', 'UC28lwdh7nmDtDOIyMSYaR5w', 'http://www.youtube.com/channel/UC28lwdh7nmDtDOIyMSYaR5w', '0', 0, '', '', '', '');
INSERT INTO `user` VALUES (35, 0, 'kuyzi', 'UCfiPCGzg7_FVYDWVuS9_i6Q', 'http://www.youtube.com/channel/UCfiPCGzg7_FVYDWVuS9_i6Q', '44', 0, '2021年10月7日', '', '', '');
INSERT INTO `user` VALUES (36, 0, 'mycha sasaki🔮', 'UCdVYrr6IdDISBTgv7LcMbzg', 'http://www.youtube.com/channel/UCdVYrr6IdDISBTgv7LcMbzg', '136', 22597, '2015年1月20日', 'I appreciate you help like and subscribe my this sec2 channel☺️\n\n私のsec2チャンネルを気に入って購読していただきありがとうございます☺️', '', '');
INSERT INTO `user` VALUES (37, 0, 'DE MI RANCHITO ASTA TU RANCHO EEEEAAAA', 'UC5aeNQQcpqTpRNZsV4iyRcA', 'http://www.youtube.com/channel/UC5aeNQQcpqTpRNZsV4iyRcA', '117', 5256, '2020年11月9日', '', '', '');
INSERT INTO `user` VALUES (38, 0, 'Wonk Suci', 'UCMRdOkrtNjR_2_f_gLADw9Q', 'http://www.youtube.com/channel/UCMRdOkrtNjR_2_f_gLADw9Q', '1150', 0, '2015年12月19日', '', '', '');
INSERT INTO `user` VALUES (39, 0, 'Nancy Hill', 'UCwTyimw4iS9879HPyE7rslQ', 'http://www.youtube.com/channel/UCwTyimw4iS9879HPyE7rslQ', '1580', 0, '2020年7月10日', '', '', '');
INSERT INTO `user` VALUES (40, 0, 'KYLIE-LUNA', 'UCbd0IJ1OJAVcjjEH4t9VjEw', 'http://www.youtube.com/channel/UCbd0IJ1OJAVcjjEH4t9VjEw', '0', 233906785, '2021年5月8日', 'Hello my name is Kylie😊\nWelcome To My Channel 💖\nThe home of the world’s best relaxing music. Our purpose and passion is to help you relax, unwind and rejuvenate through better sleep, reduced stress, greater concentration and improved mental wellness.\n\nOur world-class composers produce relaxing music with binaural beats and state-enhancing frequencies to help you relax, sleep, focus, meditate and heal. We combine our music with imagery from the world’s most beautiful locations, ensuring that you will feel a sense of deep relaxation whilst watching them. In addition to our own compositions, we also produce music videos from top classical composers such as Mozart and Bach.\n\nThank you for your support!', '', 'https://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqbGdteHpNOTdTNGxXWEdXR0d1SThYVFRpay1RZ3xBQ3Jtc0trc0t6aWRpelNwWUNIcVUtZ0puSXhIbE5LVWNfRTRWUEFBam1xcF9wemZwRmxFUXFNMm1LYjVyU2U4OVdxV05MREp1YS16S0RuUDFfWWNTcGtVRkE2NEphUUxOaElaMkFic1BWejNtZ3N2UUVadlhnQQ&q=https%3A%2F%2Fwww.facebook.com%2FDEEP-SLEEP-102816512205088%2F%3Fref%3Dpages_you_manage\nhttps://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqbmM0WnNyRldrZXdkZWJzOXRvRmIwbi1sN2E2UXxBQ3Jtc0tsektDV0czeldYUmdaUk1Fdm56dHJkaUVScnd0VXM5eHFVVnRYNm1VNi1kQUNWZXFvbGNLMDMtdi10bXdwRTNsaW1xS0szTHVnOWVTblJCM1RMZ3NndXMyZG0zb0dPdUZrcUNfYjlTMy1OVmlLaXBGcw&q=https%3A%2F%2Fwww.instagram.com%2Fdeepsleepkylie%2F\nhttps://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqbS1iWkZZbTl3NG9YUE5EM25ZSVlpNnNTZG0zUXxBQ3Jtc0ttSjVQLVhEd3hhMVdST2VCMzBYQ210aDc0R2g0MER0eE43UzBQc1ZhQ1llVndCS05YWEh2Z3pEWW9CWi16MlZ1U193c1lFd1l2eWViMzhKaWVLRTRROGFhb1ZRZjJvczVlbHlNWngyd0p1RHZlVXU3cw&q=https%3A%2F%2Fshrinke.me%2FSPnTNl6\n');
INSERT INTO `user` VALUES (41, 0, 'Selena Gomes', 'UC7-9dCOEoA1EX40sMKOBpUw', 'http://www.youtube.com/channel/UC7-9dCOEoA1EX40sMKOBpUw', '107', 0, '2021年7月17日', 'Follow me in my link good my Photo and my video', '', '');
INSERT INTO `user` VALUES (42, 0, 'Hesty Ayunda', 'UCUDlcos_10Dxrqe8SgWR7HQ', 'http://www.youtube.com/channel/UCUDlcos_10Dxrqe8SgWR7HQ', '5', 0, '2021年7月25日', '', '', '');
INSERT INTO `user` VALUES (43, 0, '@sahil shorts', 'UCsCqxj4B9N3m1GYO6seEu-A', 'http://www.youtube.com/channel/UCsCqxj4B9N3m1GYO6seEu-A', '0', 525871, '2021年10月16日', '#shortvideo\n#shortvideo\n#Shortvideo\n\n\n👉  All short videos on my channel 😎\n\n👉 new instagram reel videos  on my channel 😍\n\n👉 new instagram All comedy reel videos on my channel 😉\n\n👉 New trending attitude instagram reel video 😈', '', '');
INSERT INTO `user` VALUES (44, 0, 'Happy Place', 'UCYh36J-AstduNVxsJliGYJA', 'http://www.youtube.com/channel/UCYh36J-AstduNVxsJliGYJA', '671', 146506, '2022年2月1日', 'Dance, Sports, Music, Movies and all that good happy fun stuff.', '', '');
INSERT INTO `user` VALUES (45, 0, 'BigAssOnFire', 'UCcNSU6yM_2_usVr5fxvMM7Q', 'http://www.youtube.com/channel/UCcNSU6yM_2_usVr5fxvMM7Q', '3', 143, '2022年3月14日', 'Always seeking for fun 🔞❤️‍🔥\n\nIf you wanna see more, here is my OF page:\nhttps://onlyfans.com/bigassonfire\n\nTwitter: http://twitter.com/bigassonfire ', '', '');
INSERT INTO `user` VALUES (46, 0, 'Nay Cunay', 'UC9v3J3eI7TceweXUeSYsqnQ', 'http://www.youtube.com/channel/UC9v3J3eI7TceweXUeSYsqnQ', '98', 0, '2018年6月24日', '', '', '');
INSERT INTO `user` VALUES (47, 0, 'Mary is not reasonable', 'UCUgv0fmikjILUX1wyV6JKvg', 'http://www.youtube.com/channel/UCUgv0fmikjILUX1wyV6JKvg', '0', 26872145, '2020年9月6日', 'I\'m glad to welcome you to my profile.😊\n                  ❤️My name is Bella.❤️\nI\'m a girl who spends online almost every evening.\n                 Let\'s start with why I\'m here.\nThe answer is simple - I love to be in the spotlight, share my worldview and meet different interesting people and personalities from different parts of the world🌎. It is here that the border between countries is blurred and we are so close to each other.\nI also like to travel around the world and take pictures📸 , that\'s why I also do photography.\n\nIf you would like to support my channel, I will be very grateful, every donation is important to me 😇\n\n🔴 Please Like and Subscribe to my channel and click the bell icon to get new video updates 😀😊\n#shorts\n#Bralcon creating gaming videos and #memes #shorts for a better day\nMy Channel is all about style, outfits, try on and overall fun to watch content.\nIf you enjoy my content consider subscribing and see you on the next video!\n\n♥ SUBSCRIBE US ♥', '', 'https://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqbTVuZzFURUtPRXZvSWRWc051UWoxWFAybFVHZ3xBQ3Jtc0ttRVI2UHZuQW13NlpwWDJreWQyN2kzNUNZb3dmWENBQ2I4cVhLcm4takxqU2EyMnRYaEFpLUdMSUtPdHNHb3Y3Vmw1S2xmVVc0aEhkWXNaZlk3dzMyejRjVmxDc25vMWZKbjA2MkltczhINU5XTS1Fdw&q=https%3A%2F%2Fwww.instagram.com%2Fvnh4885%2F\nhttps://youtube.com/channel/UCk6-_IBxyCl8GGBslBT_BEw\n');
INSERT INTO `user` VALUES (48, 0, 'M э X i z Z z я д🥀', 'UCZIxljyHymrvlF9fkwMXpEA', 'http://www.youtube.com/channel/UCZIxljyHymrvlF9fkwMXpEA', '121', 0, '2021年8月24日', '', '', '');
INSERT INTO `user` VALUES (49, 0, 'YouZaan', 'UCu9nHGlLXwHP2zdgowNT5Wg', 'http://www.youtube.com/channel/UCu9nHGlLXwHP2zdgowNT5Wg', '215', 3418, '2020年11月4日', 'پاکستان خصوصن پاکستان کی شمالی علاقاجاٹ کی خوبصورتی دیکھنے کے لیے ہمارے چنیل کو ضرور سبسکرائب کرے ۔', '', '');
INSERT INTO `user` VALUES (50, 0, 'Música X', 'UCH3uZQXeZ-d9BtW2Cf0qCDw', 'http://www.youtube.com/channel/UCH3uZQXeZ-d9BtW2Cf0qCDw', '0', 38986, '2021年10月12日', 'Músicas para você ouvir e ao mesmo tempo sentir aquele perfume que mais te agrada. ', '', '');
INSERT INTO `user` VALUES (51, 0, 'Virginity', 'UCilI6UqNwd6jqu3KKO-U9vA', 'http://www.youtube.com/channel/UCilI6UqNwd6jqu3KKO-U9vA', '253', 0, '2021年6月26日', '', '', '');
INSERT INTO `user` VALUES (52, 0, 'Ginger Dixon', 'UCBHcG-eHt_d4K25F3KM_9lg', 'http://www.youtube.com/channel/UCBHcG-eHt_d4K25F3KM_9lg', '90', 0, '2020年10月9日', '', '', '');
INSERT INTO `user` VALUES (53, 0, 'Musicadafavola', 'UCYzQdqXGLbdLJO-gg6luPeQ', 'http://www.youtube.com/channel/UCYzQdqXGLbdLJO-gg6luPeQ', '2', 1055, '2022年1月31日', '', '', '');
INSERT INTO `user` VALUES (54, 0, 'Anabel French', 'UClQ1G_hVgM4k-B96amA_s6Q', 'http://www.youtube.com/channel/UClQ1G_hVgM4k-B96amA_s6Q', '276', 0, '2020年7月10日', '', '', '');
INSERT INTO `user` VALUES (55, 0, 'Asim Ali Narela', 'UCXlknAuY--9K_KnhanCir7A', 'http://www.youtube.com/channel/UCXlknAuY--9K_KnhanCir7A', '155', 8658, '2021年11月28日', 'Asim Ali Narela', '', '');
INSERT INTO `user` VALUES (56, 0, 'Mark', 'UCk1K130V7mf5KKb_UdiyGIA', 'http://www.youtube.com/channel/UCk1K130V7mf5KKb_UdiyGIA', '0', 20, '2016年4月16日', '', '', '');
INSERT INTO `user` VALUES (57, 0, 'amd savas', 'UCNHC9kHHZe0HgaCsePiq04w', 'http://www.youtube.com/channel/UCNHC9kHHZe0HgaCsePiq04w', '1', 245, '2020年12月20日', '', '', '');
INSERT INTO `user` VALUES (58, 0, 'bigger grals', 'UCuGTSIe-mZNnqEQ8mEH5rpg', 'http://www.youtube.com/channel/UCuGTSIe-mZNnqEQ8mEH5rpg', '0', 39839, '2020年9月3日', 'Please like ', '', '');
INSERT INTO `user` VALUES (59, 0, 'ジスミ-chan÷', 'UCpe1OuwWisVJTJQPHY5cC9Q', 'http://www.youtube.com/channel/UCpe1OuwWisVJTJQPHY5cC9Q', '95', 0, '2021年4月13日', '', '', '');
INSERT INTO `user` VALUES (60, 0, 'angel', 'UCgm1XJF_bencBq2MfWB6ufg', 'http://www.youtube.com/channel/UCgm1XJF_bencBq2MfWB6ufg', '98', 0, '2021年4月7日', '', '', '');
INSERT INTO `user` VALUES (61, 0, 'ǟզʊɛɛռ ᎰʊƈᏦɢɨʀʟ', 'UCIw1FajeKQSoJt5uOqCTH-w', 'http://www.youtube.com/channel/UCIw1FajeKQSoJt5uOqCTH-w', '1040', 0, '2021年9月2日', '', '', '');
INSERT INTO `user` VALUES (62, 0, 'Nicole Howard', 'UCpKMcYzmEqGjIT1pQmzzt3Q', 'http://www.youtube.com/channel/UCpKMcYzmEqGjIT1pQmzzt3Q', '3', 8, '2022年2月13日', '', '', '');
INSERT INTO `user` VALUES (63, 0, 'Black sweet', 'UCNDnJiRTwmwkDn3ZqZyjb4w', 'http://www.youtube.com/channel/UCNDnJiRTwmwkDn3ZqZyjb4w', '2', 1085, '2020年12月9日', '', '', '');
INSERT INTO `user` VALUES (64, 0, 'ACTIVE MUSIC', 'UCMcL5YCjSNnEgERv-4Z2dHQ', 'http://www.youtube.com/channel/UCMcL5YCjSNnEgERv-4Z2dHQ', '51', 9960, '2011年5月13日', 'Hello dear friends, this channel is only for introducing different types of music styles for you and the entertainment created. Please follow channel. Thank you.\ntrap music,trap nation,trap remix\nhip hop', '', '');
INSERT INTO `user` VALUES (65, 0, 'Dare rapرپ دری', 'UC-q2lT8BsxcsevrsfQ6LExg', 'http://www.youtube.com/channel/UC-q2lT8BsxcsevrsfQ6LExg', '8', 321, '2020年6月4日', '                 ( 💙 💙)\n                      〰️\n                      ❤️\n💚❤️        ', '', '');
INSERT INTO `user` VALUES (66, 0, 'Tv se Bollywood Tak', 'UCmuu1KRbYj-7iPUPvP3DGrw', 'http://www.youtube.com/channel/UCmuu1KRbYj-7iPUPvP3DGrw', '2250', 411364, '2011年12月19日', 'Audition video Acting All talent News channel', '', '');
INSERT INTO `user` VALUES (67, 0, 'Rich Newz High Energy', 'UCbsnKFyb2aO_ISTxLoET2qw', 'http://www.youtube.com/channel/UCbsnKFyb2aO_ISTxLoET2qw', '59', 26485, '2021年1月11日', 'Rich newz High energy is just our thoughts here at rich newz . On many different energy topics. To try to gain a better insight of energy theories. How to make them possible. As well as how to reduce our own emissions that destroy the beautiful earth we live on. Support our tree drive @ Grantaplant.com ', '', '');
INSERT INTO `user` VALUES (68, 0, 'Matthew Camero', 'UCBgs719Y0FHepJbmJ_-hWOg', 'http://www.youtube.com/channel/UCBgs719Y0FHepJbmJ_-hWOg', '1', 0, '2022年2月26日', '', '', '');
INSERT INTO `user` VALUES (69, 0, 'Eriska Smith', 'UCZPzt7Ta3yu3U2UUu9miO3Q', 'http://www.youtube.com/channel/UCZPzt7Ta3yu3U2UUu9miO3Q', '97', 0, '2021年7月16日', '', '', '');
INSERT INTO `user` VALUES (70, 0, 'RICI... 🕊️', 'UCtlrOGqKsygbq3P-R-AGgZQ', 'http://www.youtube.com/channel/UCtlrOGqKsygbq3P-R-AGgZQ', '3', 0, '2021年10月3日', '', '', '');
INSERT INTO `user` VALUES (71, 0, 'Merly nore', 'UCM-4nyhAEcdI8FvjIzG8Jdg', 'http://www.youtube.com/channel/UCM-4nyhAEcdI8FvjIzG8Jdg', '67', 0, '2021年7月27日', '', '', '');
INSERT INTO `user` VALUES (72, 0, 'Gorden termurah channell jatinegara', 'UCRzoHpgjaK6R-JcuMz2waGQ', 'http://www.youtube.com/channel/UCRzoHpgjaK6R-JcuMz2waGQ', '79', 5457, '2021年4月1日', 'Tk.Usaha mandiri jatinegara grosir\n\nhp 085210444416', '', '');
INSERT INTO `user` VALUES (73, 0, 'JCsHORT _ HAUL', 'UCfbXIz5EswMryQR2jE3bmWw', 'http://www.youtube.com/channel/UCfbXIz5EswMryQR2jE3bmWw', '37', 10960, '2012年12月20日', 'Making it HAPPEN!!!!', '', '');
INSERT INTO `user` VALUES (74, 0, 'ASTRIANY 🇫🇷', 'UCw_5Dtc5Q3igltfu51fiDUA', 'http://www.youtube.com/channel/UCw_5Dtc5Q3igltfu51fiDUA', '409', 27818, '2021年8月13日', 'Lets have fun together 😍😍😍', '', '');
INSERT INTO `user` VALUES (75, 0, 'N U R I VOLVO', 'UCAzYP8LCtr5i85NHxSX0aVw', 'http://www.youtube.com/channel/UCAzYP8LCtr5i85NHxSX0aVw', '20', 213, '2018年6月11日', 'Dewasa', '', '');
INSERT INTO `user` VALUES (76, 0, 'Robo Chmel', 'UCmI8mq_DdQWPdFChCAyeLzw', 'http://www.youtube.com/channel/UCmI8mq_DdQWPdFChCAyeLzw', '4', 0, '2020年3月15日', '', '', '');
INSERT INTO `user` VALUES (77, 0, 'Eddy Barzil 31', 'UCAsMOelM-oVIkEFSZf4vz7g', 'http://www.youtube.com/channel/UCAsMOelM-oVIkEFSZf4vz7g', '527', 17284, '2018年10月27日', 'Ich fange wieder neue an mit tanzen ', '', '');
INSERT INTO `user` VALUES (78, 0, 'Dwyne Debi', 'UCJ4VfUv_9R7pKHKRHFAcPMg', 'http://www.youtube.com/channel/UCJ4VfUv_9R7pKHKRHFAcPMg', '25', 0, '2021年10月7日', '', '', '');
INSERT INTO `user` VALUES (79, 0, 'Mae Hunter', 'UC6hBkGRkg9qntzFqrtk0Y-Q', 'http://www.youtube.com/channel/UC6hBkGRkg9qntzFqrtk0Y-Q', '100', 0, '2020年10月25日', '', '', '');
INSERT INTO `user` VALUES (80, 0, 'shienta Bucien', 'UCWWbX_L-zS4SdaeoLB-7FGQ', 'http://www.youtube.com/channel/UCWWbX_L-zS4SdaeoLB-7FGQ', '725', 0, '2021年8月26日', '', '', '');
INSERT INTO `user` VALUES (81, 0, 'Música X', 'UCH3uZQXeZ-d9BtW2Cf0qCDw', 'http://www.youtube.com/channel/UCH3uZQXeZ-d9BtW2Cf0qCDw', '0', 38986, '2021年10月12日', 'Músicas para você ouvir e ao mesmo tempo sentir aquele perfume que mais te agrada. ', '', '');
INSERT INTO `user` VALUES (82, 0, '🧡S༙E༙X༙🔞5⃣6⃣', 'UCaKEvKnQPAmgVEWJNGR4ZyQ', 'http://www.youtube.com/channel/UCaKEvKnQPAmgVEWJNGR4ZyQ', '85', 0, '2021年9月8日', '', '', '');
INSERT INTO `user` VALUES (83, 0, 'Eustacia Parker', 'UCjrFL0tDDaDByTNtC0EhFjA', 'http://www.youtube.com/channel/UCjrFL0tDDaDByTNtC0EhFjA', '423', 0, '2020年7月10日', '', '', '');
INSERT INTO `user` VALUES (84, 0, 'a', 'UCgTz8nnLzKnz4sArIEkEH_A', 'http://www.youtube.com/channel/UCgTz8nnLzKnz4sArIEkEH_A', '0', 0, '2021年11月8日', '', '', '');
INSERT INTO `user` VALUES (85, 0, 'ASHLEY', 'UCPEn2CxXGh-lyVAQLKVWwaQ', 'http://www.youtube.com/channel/UCPEn2CxXGh-lyVAQLKVWwaQ', '118', 0, '2021年6月15日', '', '', '');
INSERT INTO `user` VALUES (86, 0, 'Bella', 'UCX4OhS-i1qlu5FNS6zUaXSw', 'http://www.youtube.com/channel/UCX4OhS-i1qlu5FNS6zUaXSw', '0', 398188783, '2021年9月6日', 'I\'m glad to welcome you to my profile.😊\n                  ❤️My name is Bella.❤️\nI\'m a girl who spends online almost every evening.\n                 Let\'s start with why I\'m here.\nThe answer is simple - I love to be in the spotlight, share my worldview and meet different interesting people and personalities from different parts of the world🌎. It is here that the border between countries is blurred and we are so close to each other.\nI also like to travel around the world and take pictures📸 , that\'s why I also do photography.\n\nIf you would like to support my channel, I will be very grateful, every donation is important to me 😚\nhttps://www.paypal.com/donate/?hosted_button_id=8V8QP43EHZ3M8\n\n🔴 Please Like and Subscribe to my channel and click the bell icon to get new video updates 😀😊\n#shorts', '', 'https://www.youtube.com/redirect?event=channel_description&redir_token=QUFFLUhqbHFackxFNzliYWVtaXJVX3VndnhPR2hXcG5FUXxBQ3Jtc0tsNEN1RjNGUGZxeGhITVlGdlZleWp4Z240Mll1ZWhRcFE1STJ2dHZCSzQxVWM2LUFhYW1tQVRudW9BSUc0ZUJjaWJsQkl4bmZ4VHA4YVNmdktvcUZFWnU0Ukw5YVlVX3VHb29FY1JzbUxkWm9RWi1Ccw&q=https%3A%2F%2Fwww.paypal.com%2Fdonate%2F%3Fhosted_button_id%3D8V8QP43EHZ3M8\nhttps://www.youtube.com/channel/UCX4OhS-i1qlu5FNS6zUaXSw\n');
INSERT INTO `user` VALUES (87, 0, 'Katrece Miller', 'UC21SiGoQQGtwxwcT1tx_mXQ', 'http://www.youtube.com/channel/UC21SiGoQQGtwxwcT1tx_mXQ', '0', 0, '2020年12月7日', '', '', '');
INSERT INTO `user` VALUES (88, 0, 'Poppy Richards', 'UCqRYTDywQymltotrqAf7ydA', 'http://www.youtube.com/channel/UCqRYTDywQymltotrqAf7ydA', '172', 0, '2020年6月23日', '', '', '');
INSERT INTO `user` VALUES (89, 0, 'tasya', 'UCM9uaIM-p2THApPCHiFd6PQ', 'http://www.youtube.com/channel/UCM9uaIM-p2THApPCHiFd6PQ', '98', 0, '2021年10月7日', '', '', '');
INSERT INTO `user` VALUES (90, 0, 'Victor Schimidt', 'UCpEH2EXexdsqPNMHFA1TNBQ', 'http://www.youtube.com/channel/UCpEH2EXexdsqPNMHFA1TNBQ', '5', 0, '2017年4月4日', '', '', '');
INSERT INTO `user` VALUES (91, 0, 'Lili Edward', 'UC2ukvEFYJV2INA5CYhgX_aQ', 'http://www.youtube.com/channel/UC2ukvEFYJV2INA5CYhgX_aQ', '269', 0, '2020年10月22日', '', '', '');
INSERT INTO `user` VALUES (92, 0, 'さず_chan ÷', 'UCVefn6P9Pko8UaNJsoYezgg', 'http://www.youtube.com/channel/UCVefn6P9Pko8UaNJsoYezgg', '130', 0, '2019年10月19日', '', '', '');
INSERT INTO `user` VALUES (93, 0, 'Durex Minz', 'UCWHHx6wCZsbdp2P_l54BEBQ', 'http://www.youtube.com/channel/UCWHHx6wCZsbdp2P_l54BEBQ', '81', 0, '2021年9月1日', 'https://aisuru.tokyo/nomi', '', '');
INSERT INTO `user` VALUES (94, 0, 'ɦɨռǟƭǟ ̽s͓̽', 'UCUvg-19O6lfwQfUh1xjg10w', 'http://www.youtube.com/channel/UCUvg-19O6lfwQfUh1xjg10w', '847', 0, '2021年5月15日', '', '', '');
INSERT INTO `user` VALUES (95, 0, 'Berlin Lovel', 'UCuf4J-dGpoxFLsMCs94DO8Q', 'http://www.youtube.com/channel/UCuf4J-dGpoxFLsMCs94DO8Q', '4', 0, '2021年10月2日', '', '', '');
INSERT INTO `user` VALUES (96, 0, 'Charles Hudson', 'UCUHBkL0cH-q7gm14xs38UbQ', 'http://www.youtube.com/channel/UCUHBkL0cH-q7gm14xs38UbQ', '0', 0, '2021年10月16日', '', '', '');
INSERT INTO `user` VALUES (97, 0, 'MiaMalkova', 'UCau_377ZfO4Cjhm9Gh_zlWQ', 'http://www.youtube.com/channel/UCau_377ZfO4Cjhm9Gh_zlWQ', '35', 0, '2021年9月4日', '', '', '');
INSERT INTO `user` VALUES (98, 0, 'リリ・マルセラ', 'UClxKydi6HVuHF2M7zJQ-3AA', 'http://www.youtube.com/channel/UClxKydi6HVuHF2M7zJQ-3AA', '9', 0, '2021年5月16日', '', '', '');
INSERT INTO `user` VALUES (99, 0, 'Kaycee Tront', 'UCZPwrOlRsLp30ozrGGEZf1g', 'http://www.youtube.com/channel/UCZPwrOlRsLp30ozrGGEZf1g', '2', 10, '2022年3月3日', '', '', '');
INSERT INTO `user` VALUES (100, 0, 'April Moore', 'UCTn-5hVu7HaegZQYqU16Ylw', 'http://www.youtube.com/channel/UCTn-5hVu7HaegZQYqU16Ylw', '177', 0, '2020年4月23日', '', '', '');
INSERT INTO `user` VALUES (101, 0, 'Pakfy Zpgtwk', 'UCGzRYwH9mQRxuQFnIVugQgA', 'http://www.youtube.com/channel/UCGzRYwH9mQRxuQFnIVugQgA', '5', 15, '2021年12月21日', '', '', '');
INSERT INTO `user` VALUES (102, 0, 'Jez Zy', 'UCTbErHrf0d55ZhgHZMNBsHQ', 'http://www.youtube.com/channel/UCTbErHrf0d55ZhgHZMNBsHQ', '86', 0, '2021年10月16日', '', '', '');
INSERT INTO `user` VALUES (103, 0, 'maria vania', 'UCBOsKAPEU5XkqsThd9bKVNA', 'http://www.youtube.com/channel/UCBOsKAPEU5XkqsThd9bKVNA', '201', 0, '2021年6月12日', '', '', '');
INSERT INTO `user` VALUES (104, 0, 'Ariz.', 'UCOsd93PtjR8prKTDSycoccA', 'http://www.youtube.com/channel/UCOsd93PtjR8prKTDSycoccA', '137', 29253, '2020年6月22日', 'Hola bienvenidos es un placer saludarte espero que les guste lo que encuentrén en este canal hay de todo un poco ojala lo disfrutes y se suscriva y lo comparta. Dios. te bendiga', '', '');
INSERT INTO `user` VALUES (105, 0, 'SovereignMan Bryan Trent Turner', 'UCsKAdokcLufQb_MK4BN654Q', 'http://www.youtube.com/channel/UCsKAdokcLufQb_MK4BN654Q', '50', 0, '2017年4月29日', '', '', '');
INSERT INTO `user` VALUES (106, 0, 'Marsela Mitsuki', 'UCJwlkeMf5Ku12x-fySJJv1A', 'http://www.youtube.com/channel/UCJwlkeMf5Ku12x-fySJJv1A', '195', 0, '2021年5月22日', '', '', '');
INSERT INTO `user` VALUES (107, 0, 'Velien 🌷', 'UCNH_6RVXpymcGuoJDw-55hQ', 'http://www.youtube.com/channel/UCNH_6RVXpymcGuoJDw-55hQ', '8', 0, '2021年9月7日', '', '', '');
INSERT INTO `user` VALUES (108, 0, 'Younk LPG', 'UCbgcFj1tPzCb4xiujK-9KhQ', 'http://www.youtube.com/channel/UCbgcFj1tPzCb4xiujK-9KhQ', '46', 10490, '2020年11月1日', 'All for the best ', '', '');
INSERT INTO `user` VALUES (109, 0, 'Xmusic Music', 'UCpSdmmVwlmvFGeNob1KjrGg', 'http://www.youtube.com/channel/UCpSdmmVwlmvFGeNob1KjrGg', '2', 0, '2022年2月12日', '', '', '');
INSERT INTO `user` VALUES (110, 0, 'Limm Lee', 'UCX_Xex5Fjm4k_Gv2msAh92Q', 'http://www.youtube.com/channel/UCX_Xex5Fjm4k_Gv2msAh92Q', '12', 0, '2021年8月24日', '', '', '');
INSERT INTO `user` VALUES (111, 0, 'Dragon of Hateful Retribution', 'UCwgDCft_Cmw69UzqhtzaBZQ', 'http://www.youtube.com/channel/UCwgDCft_Cmw69UzqhtzaBZQ', '0', 0, '2021年12月6日', '', '', '');
INSERT INTO `user` VALUES (112, 0, 'Gaia images', 'UCj5LuOzJgPOe8F-WH0Hbmrw', 'http://www.youtube.com/channel/UCj5LuOzJgPOe8F-WH0Hbmrw', '96', 76855, '2012年10月17日', 'Channel for product photography, videos, tutorials and creative photography artwork.', '', '');
INSERT INTO `user` VALUES (113, 0, 'ㅇ', 'UC3ghWCwWjwU50xk-UNYOKfA', 'http://www.youtube.com/channel/UC3ghWCwWjwU50xk-UNYOKfA', '4', 0, '2022年1月24日', '.', '', '');
INSERT INTO `user` VALUES (114, 0, 'Stewie Griffin 92', 'UCZsxayDO6zaPRsbct4TP5og', 'http://www.youtube.com/channel/UCZsxayDO6zaPRsbct4TP5og', '1', 0, '2022年1月11日', '', '', '');
INSERT INTO `user` VALUES (115, 0, 'SKB Status', 'UCHkmhV9qlgQdRIgLUdmwJLQ', 'http://www.youtube.com/channel/UCHkmhV9qlgQdRIgLUdmwJLQ', '0', 18144, '2021年4月8日', 'Well come to our Youtube Channel  S K B status  we Provide video editing green screen video \nmy name Sabir Khan Baloch', '', '');
INSERT INTO `user` VALUES (116, 0, 'МИА ХАЛИФА', 'UC2HdM8EGY6MSKP708-Aa1pw', 'http://www.youtube.com/channel/UC2HdM8EGY6MSKP708-Aa1pw', '259', 0, '2021年6月18日', '', '', '');
INSERT INTO `user` VALUES (117, 0, 'FAISU GAMING', 'UCerkGRxUINYNrqP-T1MtZIQ', 'http://www.youtube.com/channel/UCerkGRxUINYNrqP-T1MtZIQ', '69', 1152, '2020年3月31日', 'I love free fire . I need your support plzz subscribe and like ', '', '');
INSERT INTO `user` VALUES (118, 0, 'ALICE [[LOVE※dating☆s*x※B🅰️BY', 'UCQDQvXFM1kX1RT5WiVdu9Fg', 'http://www.youtube.com/channel/UCQDQvXFM1kX1RT5WiVdu9Fg', '81', 606, '2021年10月4日', 'don\'t forget to subcribe my chenel. thank you❤❤❤🙏\n\n\nwelcome to our dating site. thank you🙏😘💛💜❤', '', '');
INSERT INTO `user` VALUES (119, 0, 'TU REY DAPIXEAN', 'UCBvOkr_PgUaX8XyRZU3dlFw', 'http://www.youtube.com/channel/UCBvOkr_PgUaX8XyRZU3dlFw', '352', 30999, '2013年4月9日', 'Artist', '', '');
INSERT INTO `user` VALUES (120, 0, 'Blanche Taylor', 'UCagrir_Y7lJmpsZtTzHmNfw', 'http://www.youtube.com/channel/UCagrir_Y7lJmpsZtTzHmNfw', '233', 0, '2020年10月20日', '', '', '');
INSERT INTO `user` VALUES (121, 0, 'A N t h y C H a 🥀', 'UC3x-WVCj-aUesbpPxmo9VVQ', 'http://www.youtube.com/channel/UC3x-WVCj-aUesbpPxmo9VVQ', '714', 23712, '2021年3月2日', '', '', '');
INSERT INTO `user` VALUES (122, 0, '༆𝓐𝓷𝓭𝓻𝓮𝓪 𝓝𝓲𝓬𝓱𝓸𝓵𝓮࿐', 'UCRmtHUH9z5TOO8AfqK6P5LQ', 'http://www.youtube.com/channel/UCRmtHUH9z5TOO8AfqK6P5LQ', '175', 0, '2021年8月28日', '', '', '');

SET FOREIGN_KEY_CHECKS = 1;
