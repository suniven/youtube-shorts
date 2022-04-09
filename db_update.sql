alter table comment
    add column type tinyint not null default 0 comment '0-不含色情链接 1-含色情链接';

alter table comment
    add column land_page varchar(1024) not null default '' comment '色情链接跳转之后的网址'