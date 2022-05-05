class AccountPayloads:
    @staticmethod
    def createAccountTokenPayload(pre_session, character_token, username_token):
        payload = {
            "username": "",
            "consents": {},
            "config": {
                "outfit": {
                    "version": "1.05",
                    "name": "New Look",
                    "gender": "female01",
                    "hidden_underwear": "False",
                    "itemdetails": [
                        {
                            "key": "feet",
                            "id": "7h4799Qyjrj7b6yZ",
                            "filename": "feet_chantelbeachshoes1f"
                        },
                        {
                            "key": "hair",
                            "id": "2MXD9WBeonHTVfoC",
                            "filename": "hair_cloudnineshinebrighthair3f"
                        },
                        {
                            "key": "hair2",
                            "colour": "63, 63, 63, 63"
                        },
                        {
                            "key": "hands",
                            "id": "F3EWP425EL8OS6P2",
                            "filename": "hands_cloudninefunkyfur10f_black"
                        },
                        {
                            "key": "legs",
                            "id": "7adfdcc43506",
                            "filename": "legs_foaljulyjeans"
                        },
                        {
                            "key": "torso",
                            "id": "eEDXOX94EQZGPCg3",
                            "filename": "torso_frontrowstopsignjacket1f"
                        },
                        {
                            "key": "makeup",
                            "id": "dfOkFUCGMCQogwm2",
                            "filename": "makeup_miakeylamakeup01"
                        },
                        {
                            "key": "neck",
                            "id": "AX9PSpG9Ngp9Tldj",
                            "filename": "neck_prysmcarnivorechoker3f"
                        },
                        {
                            "key": "contour",
                            "details": "(0.000,0.000,0.000,0.000)",
                            "id": "jOjuLptzRhi80kmZ",
                            "filename": "contour_medheavy01"
                        }
                    ]
                },
                "avakinbody": {
                    "version": "1.05",
                    "name": "Avakin",
                    "gender": "female01",
                    "itemdetails": [
                        {
                            "key": "skin",
                            "id": "wFVB2IHA1BaH101m",
                            "filename": "skin_basiccolourset_female",
                            "colour": "223, 168, 137, 255",
                            "active": "False"
                        },
                        {
                            "key": "ears",
                            "id": "TW1PB7VS1RTP",
                            "filename": "ears_001_basic"
                        },
                        {
                            "key": "eyebrows",
                            "details": "(1.047,-0.588,0.020,-8.240)",
                            "id": "d1126e26e8d",
                            "filename": "eyebrows_017",
                            "colour": "46, 45, 47, 255"
                        },
                        {
                            "key": "eyes",
                            "details": "(0.350,-0.005,0.037,-4.878)",
                            "id": "2lIbLb0SfhFnKZY4",
                            "filename": "eyes_086",
                            "colour": "83, 40, 34, 255"
                        },
                        {
                            "key": "head",
                            "details": "(0.000,0.000,1.000,0.000)",
                            "id": "8HZ9WU7DBCV4",
                            "filename": "head_002_heart"
                        },
                        {
                            "key": "mouths",
                            "details": "(0.000,0.099,-0.010,0.000)",
                            "id": "EBhzrA7H5TG2daXE",
                            "filename": "mouths_089",
                            "colour": "186, 95, 90, 255"
                        }
                    ],
                    "oldid": 0,
                    "headscale": 1,
                    "animationdetails": []
                },
                "old": ""
            },
            "pre_session": "",
            "sys_info": {
                "batteryLevel": 1,
                "batteryStatus": "Charging",
                "operatingSystem": "Android OS 7.1.2 / API-25 (N2G48H/rel.se.infra.20200730.150525)",
                "operatingSystemFamily": "Other",
                "processorType": "x86 SSE3 SSE4.1 SSE4.2 AVX AVX2",
                "processorFrequency": 2400,
                "processorCount": 4,
                "systemMemorySize": 3546,
                "deviceModel": "Asus ASUS_Z01QD",
                "supportsAccelerometer": True,
                "supportsGyroscope": True,
                "supportsLocationService": True,
                "supportsVibration": False,
                "supportsAudio": True,
                "deviceType": "Handheld",
                "graphicsMemorySize": 1024,
                "graphicsDeviceName": "Adreno (TM) 640",
                "graphicsDeviceVendor": "Qualcomm",
                "graphicsDeviceID": 0,
                "graphicsDeviceVendorID": 0,
                "graphicsDeviceType": "OpenGLES2",
                "graphicsUVStartsAtTop": False,
                "graphicsDeviceVersion": "OpenGL ES 3.0",
                "graphicsShaderLevel": 30,
                "graphicsMultiThreaded": True,
                "supportsShadows": True,
                "supportsRawShadowDepthSampling": True,
                "supportsMotionVectors": True,
                "supportsImageEffects": True,
                "supports3DTextures": False,
                "supports2DArrayTextures": False,
                "supports3DRenderTextures": False,
                "supportsCubemapArrayTextures": False,
                "copyTextureSupport": "None",
                "supportsComputeShaders": False,
                "supportsInstancing": False,
                "supportsHardwareQuadTopology": False,
                "supports32bitsIndexBuffer": True,
                "supportsSparseTextures": False,
                "supportedRenderTargetCount": 1,
                "supportsMultisampledTextures": 0,
                "supportsTextureWrapMirrorOnce": 0,
                "npotSupport": "Full",
                "maxTextureSize": 16384,
                "maxCubemapSize": 16384,
                "supportsAsyncGPUReadback": False,
                "androidAPILevel": 25,
                "androidOSVersion": "7.1.2",
                "screenWidth": 1280,
                "screenHeight": 720
            },
            "feature_versions": {
                "int-gift": 2,
                "node-chat": 1,
                "jwt-avakin": 1,
                "node-hashing": 2,
                "netactor": 63,
                "homebrew": 10,
                "shader": 1,
                "lkwd-bundle-format": 1,
                "avakin-interactions": 2,
                "furniture-format": 2,
                "badges": 1,
                "chat-reactions": 1,
                "more-avakins": 1,
                "emojis": 2,
                "avatar-actions": 3,
                "lobby": 2,
                "avatar_contour": 1,
                "admin": 1
            }
        }
        data = payload.copy()
        data['username'] = username_token
        data['pre_session'] = pre_session
        data['config']['old'] = character_token
        return data

    @staticmethod
    def createAccountPayload(email, password):
        payload = {
            'email_address': email,
            'raw_password': password
        }
        return payload.copy()

    @staticmethod
    def createLoginPayload(email, password):
        payload = {"request": {"email_address": email, "raw_password": password}, "type": "email"}
        return payload.copy()

    @staticmethod
    def createTokenLoginPayload(token):
        payload = {"request": {"token": token}, "type": "token"}
        return payload.copy()


class RewardsPayloads:
    @staticmethod
    def createRewardsPayload():
        return [{"global": True, "reward": "avakin_new_user_register_coin"},
                {"global": True, "reward": "avakin_new_user_register"},
                {"global": True, "reward": "Hub_RateFive"},
                {"global": True, "reward": "Hub_SendGiftFri"},
                {"global": True, "reward": "Hub_Send5FriRequest"},
                {"global": True, "reward": "Hub_LogFirstTime"},
                {"global": True, "reward": "Hub_View10PeepsNotFri"},
                {"global": True, "reward": "Hub_FunWithFlags"},
                {"global": True, "reward": "Hub_ViewCredits"},
                {"global": True, "reward": "Hub_AcceptFriReq"},
                {"global": True, "reward": "Hub_ReadWelcMess"},
                {"global": True, "reward": "Hub_Ratepeeps"},
                {"global": True, "reward": "Hub_BeenRated"},
                {"global": True, "reward": "Hub_ChangeTop3"},
                {"global": True, "reward": "Hub_SendAnyFriReq"},
                {"global": True, "reward": "Hub_ChangeMood"},
                {"global": True, "reward": "Hub_SendMessToFri"},
                {"global": True, "reward": "Hub_LogIn3daysInRow"},
                {"global": True, "reward": "Hub_Add5fris"},
                {"global": True, "reward": "Hub_GetRatedby10peeps"},
                {"global": True, "reward": "Hub_ChangeAvakin"},
                {"global": False, "reward": "Life_IRated"},
                {"global": False, "reward": "Life_Socialite"},
                {"global": False, "reward": "Life_Gatecrashing"},
                {"global": False, "reward": "Life_GossipGuru"},
                {"global": False, "reward": "Life_RSVP"},
                {"global": False, "reward": "Life_WorldTravelled"},
                {"global": False, "reward": "Life_InteriorDesigner"},
                {"global": False, "reward": "Life_Shopaholic"},
                {"global": False, "reward": "Life_FullyLoaded"},
                {"global": False, "reward": "Life_Chatterbox"},
                {"global": False, "reward": "Life_LongHaul"},
                {"global": False, "reward": "Life_Conversationalist"},
                {"global": False, "reward": "Life_Fidgety"},
                {"global": False, "reward": "Life_500Miles"},
                {"global": False, "reward": "Life_KnockKnock"},
                {"global": False, "reward": "Life_AtHome"},
                {"global": False, "reward": "Life_Squatter"},
                {"global": False, "reward": "Life_CreamOfTheCrop"},
                {"global": True, "reward": "Hub_CompAllProInfo"},
                {"global": True, "reward": "Global_Milestone0"},
                {"global": True, "reward": "Hub_FriendReferral01"},
                {"global": True, "reward": "Hub_FriendReferral03"},
                {"global": True, "reward": "Global_Milestone1"},
                {"global": True, "reward": "Hub_FriendReferral05"},
                {"global": True, "reward": "Global_Milestone2"},
                {"global": True, "reward": "Hub_FriendReferral10"},
                {"global": True, "reward": "Hub_FriendReferral20"},
                ]

    @staticmethod
    def createBypassGiftingLimitPayload():
        payload = {"stats": {"prof_coinspacks": 114, "prof_coinspacks_coins": 1001000, "prof_coinspacks_coins2": 50000}}
        return payload.copy()

    @staticmethod
    def createDailyRewardPayload(current_day):
        payload = {'current_day': current_day}
        return payload.copy()

    @staticmethod
    def createDailyXpBoostingPayload():
        return [
            (12, {"global": True, "reward": "avakinlife_xp_reward_visitor"}),
            (20, {"global": True, "reward": "avakinlife_xp_reward_mbox"}),
            (25, {"global": True, "reward": "avakinlife_xp_reward_talking"}),
            (70, {"global": True, "reward": "avakinlife_xp_reward_daily_gems"}),
            (2, {"global": True, "reward": "avakinlife_xp_reward_dive"}),
            (1, {"global": True, "reward": "avakinlife_xp_reward_daily_visit"}),
            (1, {"global": True, "reward": "avakinlife_xp_reward_photo"}),
        ]

    @staticmethod
    def createSpinRewardsPayload():
        return {
            'context': "Login"
        }

    @staticmethod
    def createGemsCollectPayload():
        return [
            {"reward": "avakinlife_dailyreward_a_water_mill"},
            {"reward": "avakinlife_dailyreward_a_weddingmaze"},
            {"reward": "avakinlife_dailyreward_a_riohouse"},
            {"reward": "avakinlife_dailyreward_a_tropicalislandapartment_night"},
            {"reward": "avakinlife_dailyreward_a_greekvilla"},
            {"reward": "avakinlife_dailyreward_a_balconyapartment"},
            {"reward": "avakinlife_dailyreward_a_circlehouse"},
            {"reward": "avakinlife_dailyreward_a_scandinavianhouse"},
            {"reward": "avakinlife_dailyreward_a_greenapartment"},
            {"reward": "avakinlife_dailyreward_a_hospitalward"},
            {"reward": "avakinlife_dailyreward_a_nightclub_ibiza"},
            {"reward": "avakinlife_dailyreward_newyorkcelebapartment"},
            {"reward": "avakinlife_dailyreward_a_parisapartment"},
            {"reward": "avakinlife_dailyreward_r_hauntedhouse"},
            {"reward": "avakinlife_dailyreward_dreamisland"},
            {"reward": "avakinlife_dailyreward_a_japanesehouse_night"},
            {"reward": "avakinlife_dailyreward_island_apartment"},
            {"reward": "avakinlife_dailyreward_a_parisapartment_night"},
            {"reward": "avakinlife_dailyreward_hauntedhouse_private"},
            {"reward": "avakinlife_dailyreward_a_artgallery"},
            {"reward": "avakinlife_dailyreward_a_lagarageapartment_night"},
            {"reward": "avakinlife_dailyreward_yacht_scene"},
            {"reward": "avakinlife_dailyreward_serenitylake"},
            {"reward": "avakinlife_dailyreward_r_privatejet"},
            {"reward": "avakinlife_dailyreward_a_weddinggarden_night"},
            {"reward": "avakinlife_dailyreward_customshop"},
            {"reward": "avakinlife_dailyreward_a_superjet"},
            {"reward": "avakinlife_dailyreward_a_whitemezzanine"},
            {"reward": "avakinlife_dailyreward_a_balivilla"},
            {"reward": "avakinlife_dailyreward_la_villa"},
            {"reward": "avakinlife_dailyreward_a_moroccandesert"},
            {"reward": "avakinlife_dailyreward_a_dallasfarmhouse_night"},
            {"reward": "avakinlife_dailyreward_splitfloorapartment"},
            {"reward": "avakinlife_dailyreward_sodiumbar_private"},
            {"reward": "avakinlife_dailyreward_a_maldivesgetaway"},
            {"reward": "avakinlife_dailyreward_a_basementpool"},
            {"reward": "avakinlife_dailyreward_a_belairapartment_pink"},
            {"reward": "avakinlife_dailyreward_ajagaraspeak"},
            {"reward": "avakinlife_dailyreward_a_tattoostudio"},
            {"reward": "avakinlife_dailyreward_a_lochnesscottage"},
            {"reward": "avakinlife_dailyreward_photostudio"},
            {"reward": "avakinlife_dailyreward_a_phinisiyacht"},
            {"reward": "avakinlife_dailyreward_a_greekvilla_night"},
            {"reward": "avakinlife_dailyreward_newyorkpenthouse_day"},
            {"reward": "avakinlife_dailyreward_a_lagarageapartment"},
            {"reward": "avakinlife_dailyreward_a_japanesehouse"},
            {"reward": "avakinlife_dailyreward_a_centralparkapartment"},
            {"reward": "avakinlife_dailyreward_arcaciadrive"},
            {"reward": "avakinlife_dailyreward_sportsboat"},
            {"reward": "avakinlife_dailyreward_a_beachhouse_night"},
            {"reward": "avakinlife_dailyreward_a_woodcurve"},
            {"reward": "avakinlife_dailyreward_classicapartment"},
            {"reward": "avakinlife_dailyreward_underwaterscene"},
            {"reward": "avakinlife_dailyreward_a_halloweencastle"},
            {"reward": "avakinlife_dailyreward_a_threestoryapartment"},
            {"reward": "avakinlife_dailyreward_a_superyacht"},
            {"reward": "avakinlife_dailyreward_a_woodcurve_winter"},
            {"reward": "avakinlife_dailyreward_a_hawaii_island"},
            {"reward": "avakinlife_dailyreward_larooftopbar"},
            {"reward": "avakinlife_dailyreward_abbyhillcottage"},
            {"reward": "avakinlife_dailyreward_a_turkishvilla"},
            {"reward": "avakinlife_dailyreward_bayviewexpanded"},
            {"reward": "avakinlife_dailyreward_a_suburbanhouse_night"},
            {"reward": "avakinlife_dailyreward_a_castleapartment"},
            {"reward": "avakinlife_dailyreward_a_dallasfarmhouse"},
            {"reward": "avakinlife_dailyreward_a_norwegianlakehouse"},
            {"reward": "avakinlife_dailyreward_a_kiev_loft_apartment"},
            {"reward": "avakinlife_dailyreward_a_wintertriangle_house"},
            {"reward": "avakinlife_dailyreward_starterapartment"},
            {"reward": "avakinlife_dailyreward_a_moroccandesert_day"},
            {"reward": "avakinlife_dailyreward_a_mossflat"},
            {"reward": "avakinlife_dailyreward_a_scandinavianhouselux"},
            {"reward": "avakinlife_dailyreward_newyorkcelebapartmentdeluxe"},
            {"reward": "avakinlife_dailyreward_a_windowcurve_night"},
            {"reward": "avakinlife_dailyreward_a_suburbanhouse"},
            {"reward": "avakinlife_dailyreward_a_nottinghill"},
            {"reward": "avakinlife_dailyreward_a_weddinggarden"},
            {"reward": "avakinlife_dailyreward_sailyacht"},
            {"reward": "avakinlife_dailyreward_a_weddingvenue"},
            {"reward": "avakinlife_dailyreward_a_nyoffice"},
            {"reward": "avakinlife_dailyreward_a_collegeclassroom"},
            {"reward": "avakinlife_dailyreward_private_jet"},
            {"reward": "avakinlife_dailyreward_a_dancestudio"},
            {"reward": "avakinlife_dailyreward_a_beachhouse"},
            {"reward": "avakinlife_dailyreward_custombar"},
            {"reward": "avakinlife_dailyreward_a_mexicohouse"},
            {"reward": "avakinlife_dailyreward_newyorkapartment"},
            {"reward": "avakinlife_dailyreward_a_dubaivilla"},
            {"reward": "avakinlife_dailyreward_a_balivilla_night"},
            {"reward": "avakinlife_dailyreward_a_balconyapartment_2_night"},
            {"reward": "avakinlife_dailyreward_a_halloweenship2017"},
            {"reward": "avakinlife_dailyreward_a_mengwivilla"},
            {"reward": "avakinlife_dailyreward_a_cityskyline_rain"},
            {"reward": "avakinlife_dailyreward_a_belairapartment"},
            {"reward": "avakinlife_dailyreward_a_balconyapartment_2"},
            {"reward": "avakinlife_dailyreward_a_wintercabin"},
            {"reward": "avakinlife_dailyreward_a_orlandohouse"},
            {"reward": "avakinlife_dailyreward_a_luxurytrain"},
            {"reward": "avakinlife_dailyreward_a_comohouse"},
            {"reward": "avakinlife_dailyreward_arcaciadrive_night"},
            {"reward": "avakinlife_dailyreward_a_venetianballroom"},
            {"reward": "avakinlife_dailyreward_a_modernwoodland"},
            {"reward": "avakinlife_dailyreward_newyorkpenthouse"},
            {"reward": "avakinlife_dailyreward_a_londonfishtank"},
            {"reward": "avakinlife_dailyreward_a_norwegianlakehouse_summer"},
            {"reward": "avakinlife_dailyreward_a_russiaapartment"},
            {"reward": "avakinlife_dailyreward_a_maltesevilla"},
            {"reward": "avakinlife_dailyreward_a_floridahouse"},
            {"reward": "avakinlife_dailyreward_a_algrave_villa"},
            {"reward": "avakinlife_dailyreward_a_tropicalislandapartment"},
            {"reward": "avakinlife_dailyreward_a_windmill"},
            {"reward": "avakinlife_dailyreward_a_cityskyline"},
            {"reward": "avakinlife_dailyreward_a_wintercabin_summer"},
            {"reward": "avakinlife_dailyreward_a_superyacht_night"},
            {"reward": "avakinlife_dailyreward_a_basementpool_night"},
            {"reward": "avakinlife_dailyreward_a_windowcurve"},
            {"reward": "avakinlife_dailyreward_a_windowcurve"},
            {"reward": "avakinlife_dailyreward_a_moroccan_villa"},
            {"reward": "avakinlife_dailyreward_a_balconyapartment_night"}
        ]
