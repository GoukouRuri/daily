 CREATE TABLE `MEDIA_NEWS` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL COMMENT '标题',
  `url` varchar(200) NOT NULL COMMENT '链接地址',
  `publish_date` datetime NOT NULL COMMENT '发布时间',
  `del_flag` tinyint(4) DEFAULT '0' COMMENT '是否隐藏,0显示,1隐藏',
  `save_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8