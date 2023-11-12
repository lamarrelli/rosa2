def count_min_edges_to_tree(n, edges):
    # Number of edges = Number of nodes - 1 (for a tree)
    num_edges = n - 1
    current_edges = len(edges)

    # The number of additional edges needed to form a tree
    return num_edges - current_edges

# Example Dataset
n = 848
adjacency_list = [
   ('728', '28'), ('23', '11'), ('157', '331'), ('44', '158'), ('683', '127'), ('315', '267'), ('54', '81'), ('129', '376'), ('434', '536'), ('52', '91'), ('100', '285'), ('162', '235'), ('4', '6'), ('541', '277'), ('143', '582'), ('228', '195'), ('79', '643'), ('29', '31'), ('482', '475'), ('4', '3'), ('429', '351'), ('499', '213'), ('30', '485'), ('833', '164'), ('765', '282'), ('67', '220'), ('614', '391'), ('201', '264'), ('173', '474'), ('11', '4'), ('590', '111'), ('26', '265'), ('669', '490'), ('198', '738'), ('54', '262'), ('680', '7'), ('217', '240'), ('539', '425'), ('666', '292'), ('733', '585'), ('530', '164'), ('759', '568'), ('244', '358'), ('401', '180'), ('69', '3'), ('387', '800'), ('382', '477'), ('361', '250'), ('272', '628'), ('121', '458'), ('34', '327'), ('383', '379'), ('117', '96'), ('751', '743'), ('249', '208'), ('154', '92'), ('781', '607'), ('277', '55'), ('828', '225'), ('167', '259'), ('269', '12'), ('329', '568'), ('296', '106'), ('343', '302'), ('90', '94'), ('43', '8'), ('711', '685'), ('119', '316'), ('401', '665'), ('31', '377'), ('594', '308'), ('150', '257'), ('621', '52'), ('112', '65'), ('129', '105'), ('178', '67'), ('245', '251'), ('640', '280'), ('473', '430'), ('647', '452'), ('2', '3'), ('485', '527'), ('758', '59'), ('114', '82'), ('16', '86'), ('227', '93'), ('517', '477'), ('3', '671'), ('137', '68'), ('710', '656'), ('71', '215'), ('732', '722'), ('313', '399'), ('654', '496'), ('67', '38'), ('107', '565'), ('111', '65'), ('279', '508'), ('15', '48'), ('148', '253'), ('187', '274'), ('88', '83'), ('426', '611'), ('481', '605'), ('338', '650'), ('595', '2'), ('3', '26'), ('685', '21'), ('261', '679'), ('697', '50'), ('639', '704'), ('98', '66'), ('493', '168'), ('449', '805'), ('88', '138'), ('101', '252'), ('825', '153'), ('56', '41'), ('293', '93'), ('77', '102'), ('228', '291'), ('160', '835'), ('88', '303'), ('51', '80'), ('729', '283'), ('6', '121'), ('81', '450'), ('177', '103'), ('396', '417'), ('779', '765'), ('569', '317'), ('45', '49'), ('755', '695'), ('116', '120'), ('175', '24'), ('827', '357'), ('731', '373'), ('696', '255'), ('600', '172'), ('136', '88'), ('97', '460'), ('357', '500'), ('534', '192'), ('27', '28'), ('658', '802'), ('604', '416'), ('28', '83'), ('268', '82'), ('126', '247'), ('675', '506'), ('561', '43'), ('40', '199'), ('724', '444'), ('591', '347'), ('422', '257'), ('231', '132'), ('632', '841'), ('305', '180'), ('361', '395'), ('588', '469'), ('55', '12'), ('74', '101'), ('742', '81'), ('206', '375'), ('5', '22'), ('400', '27'), ('151', '141'), ('778', '220'), ('99', '550'), ('368', '715'), ('418', '17'), ('239', '335'), ('193', '444'), ('171', '84'), ('108', '105'), ('493', '526'), ('117', '198'), ('29', '25'), ('354', '424'), ('551', '193'), ('465', '257'), ('287', '519'), ('2', '25'), ('137', '435'), ('60', '36'), ('547', '24'), ('334', '50'), ('157', '475'), ('100', '85'), ('507', '718'), ('19', '39'), ('786', '524'), ('797', '384'), ('240', '720'), ('310', '409'), ('617', '794'), ('210', '284'), ('358', '722'), ('589', '806'), ('341', '138'), ('662', '824'), ('108', '447'), ('842', '480'), ('85', '6'), ('77', '5'), ('65', '40'), ('579', '118'), ('713', '433'), ('267', '484'), ('124', '660'), ('430', '396'), ('30', '132'), ('481', '377'), ('82', '633'), ('476', '661'), ('93', '45'), ('259', '620'), ('162', '135'), ('742', '766'), ('134', '108'), ('692', '319'), ('13', '11'), ('5', '58'), ('299', '61'), ('62', '5'), ('374', '564'), ('283', '295'), ('179', '68'), ('440', '123'), ('467', '286'), ('402', '13'), ('225', '524'), ('297', '667'), ('69', '71'), ('125', '25'), ('270', '258'), ('11', '373'), ('354', '753'), ('480', '234'), ('613', '598'), ('796', '18'), ('295', '416'), ('15', '64'), ('211', '59'), ('90', '155'), ('2', '21'), ('139', '425'), ('351', '531'), ('236', '187'), ('130', '289'), ('294', '337'), ('701', '59'), ('598', '820'), ('443', '42'), ('466', '782'), ('252', '332'), ('27', '338'), ('254', '603'), ('272', '275'), ('700', '377'), ('189', '470'), ('345', '574'), ('23', '66'), ('43', '560'), ('139', '112'), ('27', '24'), ('75', '368'), ('66', '684'), ('238', '260'), ('279', '254'), ('276', '302'), ('537', '730'), ('657', '193'), ('4', '61'), ('413', '324'), ('87', '396'), ('292', '30'), ('548', '194'), ('122', '49'), ('750', '164'), ('186', '13'), ('318', '36'), ('45', '498'), ('798', '818'), ('793', '252'), ('20', '577'), ('490', '745'), ('202', '602'), ('147', '351'), ('102', '317'), ('682', '189'), ('251', '763'), ('129', '144'), ('576', '53'), ('98', '653'), ('126', '146'), ('165', '242'), ('15', '157'), ('380', '11'), ('123', '244'), ('475', '717'), ('387', '156'), ('608', '199'), ('142', '119'), ('782', '784'), ('761', '787'), ('207', '267'), ('128', '99'), ('302', '309'), ('549', '606'), ('759', '807'), ('672', '453'), ('355', '203'), ('329', '637'), ('709', '627'), ('320', '406'), ('16', '290'), ('203', '26'), ('130', '37'), ('811', '473'), ('71', '106'), ('312', '461'), ('799', '148'), ('363', '256'), ('135', '124'), ('727', '218'), ('188', '161'), ('272', '10'), ('404', '488'), ('24', '18'), ('51', '354'), ('723', '667'), ('170', '752'), ('810', '367'), ('72', '165'), ('213', '319'), ('51', '22'), ('195', '209'), ('218', '205'), ('77', '147'), ('286', '278'), ('124', '122'), ('641', '770'), ('384', '651'), ('689', '288'), ('721', '540'), ('276', '259'), ('719', '795'), ('8', '207'), ('166', '176'), ('44', '192'), ('50', '528'), ('174', '38'), ('128', '166'), ('712', '138'), ('66', '103'), ('346', '529'), ('165', '173'), ('789', '190'), ('52', '804'), ('26', '239'), ('30', '97'), ('346', '161'), ('656', '239'), ('90', '392'), ('721', '783'), ('188', '664'), ('37', '505'), ('532', '747'), ('287', '54'), ('315', '386'), ('89', '452'), ('366', '296'), ('567', '192'), ('557', '388'), ('157', '433'), ('29', '453'), ('206', '616'), ('79', '197'), ('168', '41'), ('414', '40'), ('120', '442'), ('57', '533'), ('429', '639'), ('270', '514'), ('8', '1'), ('19', '140'), ('7', '105'), ('494', '200'), ('42', '133'), ('788', '150'), ('762', '170'), ('73', '79'), ('534', '563'), ('54', '20'), ('212', '214'), ('598', '577'), ('584', '642'), ('17', '32'), ('504', '30'), ('39', '843'), ('263', '686'), ('204', '23'), ('241', '31'), ('24', '143'), ('232', '5'), ('488', '601'), ('610', '771'), ('213', '179'), ('35', '42'), ('660', '780'), ('540', '71'), ('233', '42'), ('289', '819'), ('359', '77'), ('294', '706'), ('432', '459'), ('347', '340'), ('320', '74'), ('129', '159'), ('222', '397'), ('280', '8'), ('29', '304'), ('96', '156'), ('188', '503'), ('586', '584'), ('35', '256'), ('124', '148'), ('170', '382'), ('5', '3'), ('592', '399'), ('95', '91'), ('138', '255'), ('813', '742'), ('234', '72'), ('584', '641'), ('75', '845'), ('537', '182'), ('224', '587'), ('190', '16'), ('415', '94'), ('355', '741'), ('276', '389'), ('274', '486'), ('44', '627'), ('729', '822'), ('275', '764'), ('152', '791'), ('211', '449'), ('75', '127'), ('369', '812'), ('532', '270'), ('583', '330'), ('362', '369'), ('395', '507'), ('535', '102'), ('716', '102'), ('36', '370'), ('12', '831'), ('100', '543'), ('156', '205'), ('130', '439'), ('30', '431'), ('191', '201'), ('206', '101'), ('83', '515'), ('645', '345'), ('33', '46'), ('90', '24'), ('283', '186'), ('740', '481'), ('281', '62'), ('19', '2'), ('361', '739'), ('823', '510'), ('365', '644'), ('59', '809'), ('261', '572'), ('115', '70'), ('790', '576'), ('170', '455'), ('367', '166'), ('123', '104'), ('652', '604'), ('54', '388'), ('531', '549'), ('441', '162'), ('25', '161'), ('2', '1'), ('18', '59'), ('663', '174'), ('691', '359'), ('239', '254'), ('838', '141'), ('184', '815'), ('89', '615'), ('830', '148'), ('42', '89'), ('7', '14'), ('116', '558'), ('222', '169'), ('195', '43'), ('55', '153'), ('384', '407'), ('217', '73'), ('350', '636'), ('74', '365'), ('33', '116'), ('128', '427'), ('26', '33'), ('44', '432'), ('307', '248'), ('746', '501'), ('834', '168'), ('761', '377'), ('393', '177'), ('398', '352'), ('41', '39'), ('18', '273'), ('91', '478'), ('72', '13'), ('645', '719'), ('180', '155'), ('38', '18'), ('183', '23'), ('322', '256'), ('785', '595'), ('191', '17'), ('16', '5'), ('222', '313'), ('408', '106'), ('620', '726'), ('34', '22'), ('494', '512'), ('371', '454'), ('152', '212'), ('405', '305'), ('222', '348'), ('222', '687'), ('352', '176'), ('238', '1'), ('314', '26'), ('297', '226'), ('206', '437'), ('209', '553'), ('705', '297'), ('394', '737'), ('520', '28'), ('152', '94'), ('14', '40'), ('607', '343'), ('216', '53'), ('15', '3'), ('37', '22'), ('104', '471'), ('757', '1'), ('650', '816'), ('695', '268'), ('78', '40'), ('13', '70'), ('282', '172'), ('44', '82'), ('472', '275'), ('328', '374'), ('61', '342'), ('347', '808'), ('403', '681'), ('422', '648'), ('442', '580'), ('635', '670'), ('777', '96'), ('391', '337'), ('25', '47'), ('572', '736'), ('821', '742'), ('421', '12'), ('310', '187'), ('246', '340'), ('772', '635'), ('234', '446'), ('17', '230'), ('27', '52'), ('12', '164'), ('164', '404'), ('196', '73'), ('21', '839'), ('163', '379'), ('196', '423'), ('160', '85'), ('349', '329'), ('10', '12'), ('31', '321'), ('32', '261'), ('492', '488'), ('451', '110'), ('34', '585'), ('165', '674'), ('55', '110'), ('367', '703'), ('570', '2'), ('649', '552'), ('617', '10'), ('589', '15'), ('489', '768'), ('150', '138'), ('260', '278'), ('436', '837'), ('527', '542'), ('743', '138'), ('83', '381'), ('88', '420'), ('393', '411'), ('497', '566'), ('231', '245'), ('193', '51'), ('635', '260'), ('479', '29'), ('468', '609'), ('748', '628'), ('127', '298'), ('769', '716'), ('142', '221'), ('286', '502'), ('293', '814'), ('288', '104'), ('145', '44'), ('631', '314'), ('547', '630'), ('47', '75'), ('676', '337'), ('172', '170'), ('371', '80'), ('638', '175'), ('336', '90'), ('35', '28'), ('360', '9'), ('16', '96'), ('243', '61'), ('90', '224'), ('105', '187'), ('439', '552'), ('333', '256'), ('185', '4'), ('673', '337'), ('33', '36'), ('84', '62'), ('278', '306'), ('258', '142'), ('179', '223'), ('185', '735'), ('401', '662'), ('76', '118'), ('559', '407'), ('58', '76'), ('52', '339'), ('225', '30'), ('350', '327'), ('325', '329'), ('244', '774'), ('186', '226'), ('534', '618'), ('43', '491'), ('219', '198'), ('612', '5'), ('152', '229'), ('462', '66'), ('655', '553'), ('31', '776'), ('687', '708'), ('496', '490'), ('92', '33'), ('85', '250'), ('225', '344'), ('1', '330'), ('50', '48'), ('798', '72'), ('120', '194'), ('464', '538'), ('536', '688'), ('1', '7'), ('102', '469'), ('45', '33'), ('105', '208'), ('353', '285'), ('223', '489'), ('698', '128'), ('482', '497'), ('184', '70'), ('189', '114'), ('48', '593'), ('150', '545'), ('625', '524'), ('619', '143'), ('111', '744'), ('702', '554'), ('10', '5'), ('130', '501'), ('248', '52'), ('521', '33'), ('844', '705'), ('550', '694'), ('7', '181'), ('145', '271'), ('636', '678'), ('690', '581'), ('490', '30'), ('182', '67'), ('255', '556'), ('364', '59'), ('378', '125'), ('523', '78'), ('149', '147'), ('17', '734'), ('308', '714'), ('37', '119'), ('317', '659'), ('573', '565'), ('20', '13'), ('18', '767'), ('5', '836'), ('170', '94'), ('13', '30'), ('826', '786'), ('19', '426'), ('325', '152'), ('224', '756'), ('749', '46'), ('126', '61'), ('202', '154'), ('390', '294'), ('224', '428'), ('699', '365'), ('109', '29'), ('294', '199'), ('516', '107'), ('88', '468'), ('141', '66'), ('102', '167'), ('107', '38'), ('516', '544'), ('597', '103'), ('494', '668'), ('562', '145'), ('792', '52'), ('372', '623'), ('335', '456'), ('428', '707'), ('509', '130'), ('556', '632'), ('575', '775'), ('10', '410'), ('518', '12'), ('434', '232'), ('202', '463'), ('341', '510'), ('622', '364'), ('70', '584'), ('345', '336'), ('624', '156'), ('522', '246'), ('55', '312'), ('124', '817'), ('610', '71'), ('513', '70'), ('131', '96'), ('328', '64'), ('370', '483'), ('200', '323'), ('490', '546'), ('385', '200'), ('213', '801'), ('35', '487'), ('511', '149'), ('266', '658'), ('8', '200'), ('525', '315'), ('18', '773'), ('187', '419'), ('2', '803'), ('677', '580'), ('22', '53'), ('634', '226'), ('60', '438'), ('69', '113'), ('439', '495'), ('43', '169'), ('320', '356'), ('31', '68'), ('554', '436'), ('346', '476'), ('829', '354'), ('4', '9'), ('93', '163'), ('74', '10'), ('428', '596'), ('73', '42'), ('17', '2'), ('571', '405'), ('122', '300'), ('303', '326'), ('202', '308'), ('840', '295'), ('26', '263'), ('257', '266'), ('104', '44'), ('301', '148'), ('581', '326'), ('377', '394'), ('445', '104'), ('311', '52'), ('339', '506'), ('448', '82'), ('98', '210'), ('340', '357'), ('578', '562'), ('722', '754'), ('31', '57'), ('362', '70'), ('457', '253'), ('329', '832'), ('213', '436'), ('403', '268'), ('230', '372'), ('55', '63'), ('442', '466')
]

# Count the number of edges required to form a tree
edges_required = count_min_edges_to_tree(n, adjacency_list)
print(edges_required)
