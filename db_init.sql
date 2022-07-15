CREATE TABLE IF NOT EXISTS `video`
(
    `id`             bigint(20) auto_increment NOT NULL COMMENT 'id',
    `title`          varchar(100)              NOT NULL DEFAULT '' COMMENT '视频标题',
    `video_id`       varchar(24)               NOT NULL DEFAULT '' COMMENT '视频唯一标识',
    `publisher`      varchar(64)               NOT NULL DEFAULT '' COMMENT '视频发布者',
    `publisher_link` varchar(256)              NOT NULL DEFAULT '' COMMENT '视频发布者主页链接',
    `video_link`     varchar(256)              NOT NULL DEFAULT '' COMMENT '视频链接',
    `date`           varchar(20)               NOT NULL DEFAULT '' COMMENT '视频发布日期',
    `views`          int                       NOT NULL DEFAULT 0 COMMENT '视频观看次数',
    `description`    varchar(10000)            NOT NULL DEFAULT '' COMMENT '视频描述',
    `comments_count` int                       NOT NULL DEFAULT 0 COMMENT '视频评论数量',
    `create_time`    bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`),
    KEY `publisher` (`publisher`),
    KEY `video_id` (`video_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='Youtube视频表';


CREATE TABLE IF NOT EXISTS `comment`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `video_id`    varchar(24)               NOT NULL DEFAULT '' COMMENT '视频id',
    `user`        varchar(64)               NOT NULL DEFAULT '' COMMENT '评论者',
    `user_link`   varchar(256)              NOT NULL DEFAULT '' COMMENT '评论者主页链接',
    `content`     varchar(15000)            NOT NULL DEFAULT '' COMMENT '评论内容',
    `date`        varchar(20)               NOT NULL DEFAULT '' COMMENT '发布日期',
    `type`        smallint                  NOT NULL DEFAULT 0 COMMENT '-1-占位 0-正常评论 1-包含色情链接的评论 2-包含其他链接的评论',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`),
    KEY `video_id` (`video_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='视频评论表';


CREATE TABLE IF NOT EXISTS `user`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `type`        tinyint                   NOT NULL DEFAULT 0 COMMENT '0-普通用户 1-垃圾评论用户',
    `username`    varchar(64)               NOT NULL DEFAULT '' COMMENT '用户名',
    `user_id`     varchar(24)               NOT NULL DEFAULT '' COMMENT '用户24位编码标识',
    `homepage`    varchar(256)              NOT NULL DEFAULT '' COMMENT '主页链接',
    `subscribers` varchar(10)               NOT NULL DEFAULT '' COMMENT '订阅人数-因为很多人的话就不显示具体数目了所以不用int类型',
    `views`       int                       NOT NULL DEFAULT 0 COMMENT '累计观看次数',
    `join_time`   varchar(30)               NOT NULL DEFAULT '' COMMENT '注册日期',
    `description` varchar(4096)             NOT NULL DEFAULT '' COMMENT '描述',
    `details`     varchar(1024)             NOT NULL DEFAULT '' COMMENT '其余细节信息如location',
    `links`       varchar(4096)             NOT NULL DEFAULT '' COMMENT '外链-可能多个',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`),
    KEY `user_id` (`user_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='youtube用户表';


CREATE TABLE IF NOT EXISTS `site`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `comment_id`  bigint(20)                NOT NULL DEFAULT 0 COMMENT '来源评论在comment表中的id',
    `user_id`     varchar(24)               NOT NULL DEFAULT '' COMMENT '来自于哪一位用户',
    `url`         varchar(256)              NOT NULL DEFAULT '' COMMENT '评论中发布的网址',
    `land_page`   varchar(2048)             NOT NULL DEFAULT '' COMMENT '色情网站落地页链接',
    `page_title`  varchar(256)              NOT NULL DEFAULT '' COMMENT '网站标题',
    `screenshot`  varchar(256)              NOT NULL DEFAULT '' COMMENT '网站截图',
    `type`        tinyint                   NOT NULL DEFAULT 2 COMMENT '0-普通网站 1-色情网站 2-未分类',
    `detail`      varchar(24)               NOT NULL DEFAULT '' COMMENT '细分',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`),
    KEY `comment_id` (`comment_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='色情网站信息';


CREATE TABLE IF NOT EXISTS `domain`
(
    `id`                      bigint(20) auto_increment NOT NULL COMMENT 'id',
    `domain_name`             varchar(100)              NOT NULL DEFAULT '' COMMENT '域名',
    `registrant_id`           varchar(100)              NOT NULL DEFAULT '' COMMENT 'registrant id',
    `registrant_name`         varchar(100)              NOT NULL DEFAULT '' COMMENT 'registrant name',
    `registrant_organization` varchar(100)              NOT NULL DEFAULT '' COMMENT 'registrant org',
    `registrant_street`       varchar(100)              NOT NULL DEFAULT '' COMMENT 'registrant street',
    `registrant_city`         varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant city',
    `registrant_province`     varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant province',
    `registrant_postal_code`  varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant postal code',
    `registrant_country`      varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant country',
    `registrant_phone`        varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant phone',
    `registrant_phone_ext`    varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant phone ext',
    `registrant_fax`          varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant fax',
    `registrant_fax_ext`      varchar(30)               NOT NULL DEFAULT '' COMMENT 'registrant fax ext',
    `registrant_email`        varchar(200)              NOT NULL DEFAULT '' COMMENT 'registrant email',
    `raw_data`                varchar(15000)            NOT NULL DEFAULT '' COMMENT 'whois raw data',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='域名信息';


CREATE TABLE IF NOT EXISTS `tt_cover`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `file_name`   varchar(200)              NOT NULL DEFAULT '' COMMENT '截图文件名',
    `user_id`     varchar(32)               NOT NULL DEFAULT '' COMMENT '用户名的MD5值 用于建立人脸库注册人脸时的useid参数',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='tiktok cover';


CREATE TABLE IF NOT EXISTS `affpay_offer`
(
    `id`                bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`               varchar(1024)             NOT NULL COMMENT 'offer自身网址',
    `title`             varchar(600)              NOT NULL DEFAULT '' COMMENT 'offer标题',
    `payout`            varchar(32)               NOT NULL DEFAULT '' COMMENT '酬金',
    `status`            varchar(24)               NOT NULL DEFAULT '' COMMENT 'offer状态',
    `offer_create_time` varchar(32)               NOT NULL DEFAULT 0 COMMENT 'offer创建时间',
    `offer_update_time` varchar(32)               NOT NULL DEFAULT '' COMMENT 'offer更新时间',
    `category`          varchar(256)              NOT NULL DEFAULT '' COMMENT 'offer类别',
    `geo`               VARCHAR(2048)             NOT NULL DEFAULT '' COMMENT '国家地区',
    `network`           VARCHAR(32)               NOT NULL DEFAULT '' COMMENT '营销网络',
    `description`       VARCHAR(10000)            NOT NULL DEFAULT '' COMMENT 'offer描述',
    `land_page`         VARCHAR(1024)             NOT NULL DEFAULT '' COMMENT '落地页链接',
    `land_page_img`     VARCHAR(256)              NOT NULL DEFAULT '' COMMENT '落地页图片',
    `create_time`       bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='affpay offer';


CREATE TABLE IF NOT EXISTS `offervault_offer`
(
    `id`                bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`               varchar(1024)             NOT NULL COMMENT 'offer自身网址',
    `title`             varchar(600)              NOT NULL DEFAULT '' COMMENT 'offer标题',
    `payout`            varchar(32)               NOT NULL DEFAULT '' COMMENT '酬金',
    `offer_create_time` varchar(32)               NOT NULL DEFAULT 0 COMMENT 'offer创建时间',
    `offer_update_time` varchar(32)               NOT NULL DEFAULT '' COMMENT 'offer更新时间',
    `category`          varchar(256)              NOT NULL DEFAULT '' COMMENT 'offer类别',
    `geo`               VARCHAR(2048)             NOT NULL DEFAULT '' COMMENT '国家地区',
    `network`           VARCHAR(256)              NOT NULL DEFAULT '' COMMENT '营销网络',
    `description`       VARCHAR(10000)            NOT NULL DEFAULT '' COMMENT 'offer描述',
    `land_page`         VARCHAR(1024)             NOT NULL DEFAULT '' COMMENT '落地页链接',
    `land_page_img`     VARCHAR(256)              NOT NULL DEFAULT '' COMMENT '落地页图片',
    `create_time`       bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='offervault offer';


CREATE TABLE IF NOT EXISTS `odigger_offer`
(
    `id`                bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`               varchar(1024)             NOT NULL COMMENT 'offer自身网址',
    `title`             varchar(600)              NOT NULL DEFAULT '' COMMENT 'offer标题',
    `status`            varchar(24)               NOT NULL DEFAULT '' COMMENT 'offer状态',
    `payout`            varchar(32)               NOT NULL DEFAULT '' COMMENT '酬金',
    `offer_create_time` varchar(32)               NOT NULL DEFAULT 0 COMMENT 'offer创建时间',
    `offer_update_time` varchar(32)               NOT NULL DEFAULT '' COMMENT 'offer更新时间',
    `category`          varchar(256)              NOT NULL DEFAULT '' COMMENT 'offer类别',
    `geo`               VARCHAR(2048)             NOT NULL DEFAULT '' COMMENT '国家地区',
    `network`           VARCHAR(256)              NOT NULL DEFAULT '' COMMENT '营销网络',
    `description`       VARCHAR(10000)            NOT NULL DEFAULT '' COMMENT 'offer描述',
    `land_page`         VARCHAR(1024)             NOT NULL DEFAULT '' COMMENT '落地页链接',
    `land_page_img`     VARCHAR(256)              NOT NULL DEFAULT '' COMMENT '落地页图片',
    `create_time`       bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='odigger offer';


CREATE TABLE IF NOT EXISTS `google_search_result`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `query`       varchar(512)              NOT NULL COMMENT '查询内容',
    `url`         varchar(2048)             NOT NULL COMMENT '查询结果链接',
    `title`       varchar(1024)             NOT NULL COMMENT '查询结果标题',
    `snippet`     varchar(2048)             NOT NULL COMMENT '查询结果snippet',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='Google Custom Search Result';


CREATE TABLE IF NOT EXISTS `virustotal_url`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`         varchar(2048)             NOT NULL DEFAULT '' COMMENT '链接',
    `ratio`       varchar(16)               NOT NULL DEFAULT '' COMMENT '异常/总数',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal url';


CREATE TABLE IF NOT EXISTS `virustotal_url_detection`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url_id`      bigint(20)                NOT NULL COMMENT 'url在virustotal_url表中的id',
    `url`         varchar(2048)             NOT NULL DEFAULT '' COMMENT '链接',
    `vendor`      varchar(64)               NOT NULL DEFAULT '' COMMENT '安全厂家',
    `analysis`    varchar(64)               NOT NULL DEFAULT '' COMMENT '分析结果',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal url detection result';


CREATE TABLE IF NOT EXISTS `virustotal_url_details`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url_id`      bigint(20)                NOT NULL COMMENT 'url在virustotal_url表中的id',
    `url`         varchar(2048)             NOT NULL DEFAULT '' COMMENT '链接',
    `engine`      varchar(64)               NOT NULL DEFAULT '' COMMENT '安全引擎',
    `category`    varchar(64)               NOT NULL DEFAULT '' COMMENT '分类结果',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal url details';


CREATE TABLE IF NOT EXISTS `virustotal_domain`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `domain`      varchar(512)              NOT NULL DEFAULT '' COMMENT 'domain',
    `ratio`       varchar(16)               NOT NULL DEFAULT '' COMMENT '异常/总数',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal domain';


CREATE TABLE IF NOT EXISTS `virustotal_domain_detection`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `domain`      varchar(512)              NOT NULL DEFAULT '' COMMENT 'domain',
    `subdomain`   varchar(1024)             NOT NULL DEFAULT '' COMMENT 'subdomain',
    `vendor`      varchar(64)               NOT NULL DEFAULT '' COMMENT '安全厂家',
    `analysis`    varchar(64)               NOT NULL DEFAULT '' COMMENT '分析结果',
    `type`        varchar(16)               NOT NULL DEFAULT '' COMMENT 'domain/subdomain',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal domain detection result';


CREATE TABLE IF NOT EXISTS `virustotal_domain_details`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `domain`      varchar(512)              NOT NULL DEFAULT '' COMMENT 'domain',
    `subdomain`   varchar(1024)             NOT NULL DEFAULT '' COMMENT 'subdomain',
    `engine`      varchar(64)               NOT NULL DEFAULT '' COMMENT '安全引擎',
    `category`    varchar(64)               NOT NULL DEFAULT '' COMMENT '分类结果',
    `type`        varchar(16)               NOT NULL DEFAULT '' COMMENT 'domain/subdomain',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='virustotal domain details';

CREATE TABLE IF NOT EXISTS `virustotal_subdomain`
(
    `id`          bigint(20) auto_increment NOT NULL COMMENT 'id',
    `domain`      varchar(512)              NOT NULL DEFAULT '' COMMENT 'domain',
    `subdomain`   varchar(1024)             NOT NULL DEFAULT '' COMMENT 'subdomain',
    `ratio`       varchar(16)               NOT NULL DEFAULT '' COMMENT '异常/总数',
    `create_time` bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',

    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='subdomain';

CREATE TABLE IF NOT EXISTS `round_1`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(4000)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page`     varchar(4000)             NOT NULL DEFAULT '' COMMENT 'landing page url',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page url',
    `status_code`      varchar(3)                NOT NULL DEFAULT '' COMMENT '响应状态码',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_1';

CREATE TABLE IF NOT EXISTS `round_2`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(4000)             NOT NULL DEFAULT '' COMMENT 'url in round_1',
    `landing_page`     varchar(4000)             NOT NULL DEFAULT '' COMMENT 'landing page url',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page url',
    `status_code`      varchar(3)                NOT NULL DEFAULT '' COMMENT '响应状态码',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_2';

CREATE TABLE IF NOT EXISTS `final_page`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(4000)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page`     varchar(4000)             NOT NULL DEFAULT '' COMMENT 'landing page url',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page url',
    `domain`           varchar(50)               NOT NULL DEFAULT '' COMMENT 'domain',
    `type`             varchar(100)              NOT NULL DEFAULT '' COMMENT '网站类型',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='final page';

CREATE TABLE IF NOT EXISTS `round_2_new`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page_1`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_1',
    `landing_page_2`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_2',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page 2 url',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_2_new';

CREATE TABLE IF NOT EXISTS `round_3_new`
(
    `id`               bigint(20) auto_increment NOT NULL COMMENT 'id',
    `url`              varchar(1200)             NOT NULL DEFAULT '' COMMENT 'url in comments',
    `landing_page_1`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_1',
    `landing_page_2`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_2',
    `landing_page_3`   varchar(1200)             NOT NULL DEFAULT '' COMMENT 'landing page in round_3',
    `landing_page_md5` varchar(32)               NOT NULL DEFAULT '' COMMENT 'md5 of landing page 2 url',
    `checked`          varchar(50)               NOT NULL DEFAULT '' COMMENT '人工分类结果',
    `create_time`      bigint(20)                NOT NULL DEFAULT 0 COMMENT '数据创建时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8 COMMENT ='round_2_new';

alter table round_3_new
    convert to character set utf8mb4;

alter table round_2_new
    convert to character set utf8mb4;

alter table round_2
    convert to character set utf8mb4;

alter table final_page
    convert to character set utf8mb4;

alter table round_1
    convert to character set utf8mb4;

alter table video
    convert to character set utf8mb4;
alter table comment
    convert to character set utf8mb4;
alter table user
    convert to character set utf8mb4;
alter table site
    convert to character set utf8mb4;
alter table domain
    convert to character set utf8mb4;
alter table tt_cover
    convert to character set utf8mb4;
alter table affpay_offer
    convert to character set utf8mb4;
alter table offervault_offer
    convert to character set utf8mb4;
alter table odigger_offer
    convert to character set utf8mb4;
alter table google_search_result
    convert to character set utf8mb4;

alter table virustotal_url
    convert to character set utf8mb4;
alter table virustotal_url_detection
    convert to character set utf8mb4;
alter table virustotal_url_details
    convert to character set utf8mb4;

alter table virustotal_domain
    convert to character set utf8mb4;
alter table virustotal_domain_detection
    convert to character set utf8mb4;
alter table virustotal_domain_details
    convert to character set utf8mb4;

alter table virustotal_subdomain
    convert to character set utf8mb4;