alter table comment
    add column type tinyint not null default 0 comment '0-不含色情链接 1-含色情链接';