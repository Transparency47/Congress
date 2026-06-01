# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/417
- Title: INFORM Act
- Congress: 119
- Bill type: S
- Bill number: 417
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-03-21T15:15:30Z
- Update date including text: 2025-03-21T15:15:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/417",
    "number": "417",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "INFORM Act",
    "type": "S",
    "updateDate": "2025-03-21T15:15:30Z",
    "updateDateIncludingText": "2025-03-21T15:15:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-05T19:57:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NH"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s417is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 417\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Sullivan (for himself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo develop a strategy for increasing access to independent information for Chinese citizens, to establish an interagency task force to carry out such strategy, and for other purposes.\n#### 1. Short titles; table of contents\n##### (a) Short titles\nThis Act may be cited as the Informing a Nation with Free, Open, and Reliable Media Act of 2025 or the INFORM Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short titles; table of contents.\nSec. 2. Definitions.\nSec. 3. Findings.\nSec. 4. Sense of Congress.\nSec. 5. Statement of policy.\nSec. 6. Strategy for increasing access to independent information for citizens of the People\u2019s Republic of China.\nSec. 7. Establishment of the Global News Service.\nSec. 8. Increasing coordination and resources for censorship circumvention, secure sharing, and content creation initiatives.\nSec. 9. Addressing the lack of reciprocity between the United States and the People\u2019s Republic of China in the information space.\n#### 2. Definitions\nIn this Act:\n**(1) CCP**\nThe term CCP means the Chinese Communist Party.\n**(2) Coordinator**\nThe term Coordinator means the coordinator of the interagency task force appointed by the President pursuant to section 8(b).\n**(3) Department**\nThe term Department means the Department of State.\n**(4) PRC**\nThe term PRC means the People's Republic of China.\n**(5) RFA**\nThe term RFA means Radio Free Asia.\n**(6) USAGM**\nThe term USAGM means the United States Agency for Global Media.\n**(7) VOA**\nThe term VOA means Voice of America.\n#### 3. Findings\nCongress finds the following:\n**(1)**\nSince the advent and proliferation of the internet, the Chinese Communist Party has viewed the global, cross-border, and open information environment the internet created as an existential threat to its legitimacy, its effective indoctrination and control of its citizens, and its authoritarian political system.\n**(2)**\nDespite brief periods of increased openness in the internet ecosystem of the People's Republic of China during the early 2000s, the CCP has since expended billions of dollars to develop a digital information control regime (commonly known as the Great Firewall of China ) that is a wholescale substitution of the global internet with compelling, nearly universally used domestic platforms with built-in censorship and surveillance features as alternatives, which has fundamentally reshaped its population\u2019s behavior.\n**(3)**\nThrough this system in the PRC, the Great Firewall blocks foreign internet search providers, independent news and media websites, circumvention and secure messaging tools, and other content deemed undesirable by the CCP.\n**(4)**\nThe PRC also engages in meta-level censorship to obscure the possibility of circumvention and surveillance evasion by criminalizing VPNs, blocking discussion of anti-censorship methods, widespread app removal from app stores, and related techniques.\n**(5)**\nChinese internet users must contend with expansive repressive digital surveillance that often results in real-world consequences and leads to significant self-censorship.\n**(6)**\nUnder the leadership of Chairman Xi Jinping, the CCP and government organs have prioritized\u2014\n**(A)**\nthe censorship and surveillance of their citizens\u2019 online behavior; and\n**(B)**\nthe indoctrination of the CCP\u2019s\u2014\n**(i)**\nauthoritarian worldview;\n**(ii)**\nanti-American and anti-West propaganda; and\n**(iii)**\nintent to undermine and redefine the United States-led global order.\n**(7)**\nThe PRC\u2019s internet censorship regime systematically\u2014\n**(A)**\namplifies the voices of nationalistic internet users;\n**(B)**\nsilences the voices of moderate or dissenting voices;\n**(C)**\nsuppresses information that threatens the credibility of the CCP, including reports of corruption and of unexplained wealth held by CCP and People\u2019s Liberation Army officials and their families; and\n**(D)**\ncreates an echo chamber on the PRC domestic internet that makes it challenging for international observers to decipher\u2014\n**(i)**\nthe prevailing beliefs, values, and perspectives of different segments of PRC society; and\n**(ii)**\ntheir views on the domestic and foreign policies of the PRC government.\n**(8)**\nConcurrent with the increased sophistication and refinement of the PRC\u2019s censored and restricted information space, the CCP has expended billions of dollars to build an asymmetric advantage by reengineering its population\u2019s online norms concurrent with\u2014\n**(A)**\nexploiting the open and uncensored online information environment in the United States and many countries globally to advance its pro-CCP and anti-United States propaganda and disinformation; and\n**(B)**\nhighly restricting the United States online and public diplomacy activities in the PRC.\n**(9)**\nThe United States Ambassador to China, Nicholas Burns, recently stated that the PRC\u2019s Ministry of State Security has interrupted and effectively cancelled 61 public in-person and online events organized by the United States mission in China since November 2023.\n**(10)**\nDespite a comprehensive censorship and surveillance regime, the relentless indoctrination by CCP and PRC government organs, and the highly coordinated, systematized, and repressive structure of the PRC censorship and propaganda apparatus, PRC citizens have begun to demonstrate\u2014\n**(A)**\na lack of confidence and satisfaction in their government\u2019s policies, conduct, and the information available to them within the PRC\u2019s censored and restrictive online information space; and\n**(B)**\na growing willingness to express dissent online, seek alternative sources of information and engagement, and call for greater economic and political freedoms.\n**(11)**\nIn a recent Stanford University study, researchers discovered that PRC university students who were exposed to foreign news and independent content changed their knowledge, beliefs, attitudes, and behaviors suggesting that demand for uncensored information can persist and may generate pressure on the PRC censorship apparatus.\n**(12)**\nIn 2021, during a period when the Clubhouse application was briefly uncensored in the People\u2019s Republic of China, downloads and engagement on Clubhouse rapidly increased and provided an opportunity for PRC internet users to openly discuss sensitive topics, including\u2014\n**(A)**\nthe reeducation camps in Xinjiang;\n**(B)**\nthe 1989 Tiananmen Square massacre; and\n**(C)**\nthe future of Taiwan.\n**(13)**\nOne Clubhouse user penned a hashtag, which was viewed more than 50,000,000 times, calling the discussions the Renaissance of China .\n**(14)**\nIn 2022, during the multi-city White Paper protests in defiance of the Government of the PRC\u2019s zero-COVID\u201319 policy, internet users in the PRC expressed solidarity and organized the protests through a variety of online platforms.\n**(15)**\nInformation technology news outlet Techopedia released a report and data indicating that, despite being largely blocked and criminalized, the usage of VPNs in the PRC doubled during 2023.\n**(16)**\nIn February 2024, after the United States Embassy in Beijing posted information on China\u2019s popular Weibo social media platform discussing scientists\u2019 use of satellite data to track and monitor the movement of giraffes, the platform was inundated with comments from PRC internet users lamenting the state of the PRC economy and recent turmoil in its stock, bond, and real estate markets, with many users expressing a desire for help from the United States.\n**(17)**\nThe demand among PRC citizens for independent and alternative sources of information is growing, while the level of United States Government funding to disseminate circumvention tools to PRC citizens so they can access independent information has remained at consistently low levels, especially compared to the billions of renminbi (Chinese yuan) the PRC is spending to censor and monitor its internet ecosystem.\n**(18)**\nPublicly-funded VPNs supported through the Open Technology Fund are used by millions of monthly active users in China and have proven to be resilient. Traditional circumvention tools, such as VPNs, are necessary but are not sufficient to address the unique challenge of China\u2019s socio-technological information control system.\n**(19)**\nIncreasing access to independent information for PRC citizens will aid broader United States efforts\u2014\n**(A)**\nto engage PRC citizens;\n**(B)**\nto provide credible and reliable alternative sources of information for PRC citizens regarding events occurring within the PRC and globally;\n**(C)**\nto promote a balanced understanding of the United States among PRC citizens; and\n**(D)**\nto support PRC citizens in their efforts to advance their individual freedoms and human rights and hold their government accountable.\n#### 4. Sense of Congress\nIt is the sense of Congress that the United States Government should\u2014\n**(1)**\nprioritize the development of a vision and strategy for engaging with PRC citizens through the development and delivery of Mandarin Chinese-language content that is timely, compelling, and pertinent to\u2014\n**(A)**\nthe issues and challenges they face in their daily lives;\n**(B)**\nthe domestic and foreign policy decisions of the PRC government; and\n**(C)**\nthe governance failures and corruption of the CCP, including unexplained wealth held by CCP and PLA officials and their families;\n**(2)**\nincrease the level of coordination among Federal agencies to develop and disseminate timely, compelling, and pertinent Mandarin Chinese-language content that is otherwise blocked by the PRC government\u2019s highly censored and restrictive internet ecosystem;\n**(3)**\ndually prioritize\u2014\n**(A)**\naccess to independent information through circumvention and other tools for PRC citizens; and\n**(B)**\nthe secure sharing of such content in the PRC\u2019s highly censored internet ecosystem;\n**(4)**\noptimize the impact of circumvention and secure content sharing tools by more effectively pairing such tools with timely, compelling, and pertinent Mandarin Chinese-language content; and\n**(5)**\nseek to counter the lack of reciprocity with the PRC in the online information and public diplomacy space.\n#### 5. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto make increasing access to independent information for and engagement with the roughly 1,400,000,000 PRC citizens a national security priority of the United States that benefits broader United States priorities to promote human rights, the rule of law, and good governance in the PRC and globally;\n**(2)**\nto prioritize the expansion and improvement of the development and dissemination of independent information to PRC citizens inside and outside the People\u2019s Republic of China, including by more effectively pairing independent information with the circumvention and other tools needed to access such content;\n**(3)**\nto prioritize and coordinate Mandarin Chinese-language content development and content dissemination, and develop technical solutions to address the PRC\u2019s digital information controls; and\n**(4)**\nto work with like-minded partners and allies\u2014\n**(A)**\nto develop coordinated and complementary strategies for increasing access to independent information for PRC citizens; and\n**(B)**\nto address the lack of reciprocity in the information and media environments between the PRC and the United States and its partners and allies.\n#### 6. Strategy for increasing access to independent information for citizens of the People\u2019s Republic of China\n##### (a) President's strategy\nNot later than 1 year after the date of the enactment of this Act, the President shall submit a strategy to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives for increasing access to independent information for citizens of the PRC who are within or outside the PRC.\n##### (b) Strategy elements\nThe strategy required under subsection (a) shall include\u2014\n**(1)**\na plan for increasing the accessibility and adoption of circumvention and secure communications tools within the PRC, which may include\u2014\n**(A)**\nan assessment of the technical challenges of the PRC\u2019s information control regime; and\n**(B)**\nan evaluation of research, technological, and other gaps that may affect strategy implementation;\n**(2)**\nan assessment of Mandarin Chinese-language content creation and distribution capabilities within the Department, across the interagency task force established pursuant to section 8, and among other Federal departments and agencies, as appropriate, including\u2014\n**(A)**\nwhether United States Government-produced, Mandarin Chinese-language content is accessible either inside or outside the PRC;\n**(B)**\nthe uptake of, and engagement with, various types of content among citizens of the PRC within or outside the PRC;\n**(C)**\nthe use of survey tools and other data sources to assess the areas of interest and concern, whether domestic or international, among different segments of PRC citizens; and\n**(D)**\nwhere gaps or duplication of effort exist in the efficacy of the Mandarin Chinese-language content developed and disseminated by the Department or the interagency task force, and how such gaps or duplication will be addressed through the strategy;\n**(3)**\na description of how the Department plans to improve coordination between components of the Department, and across the interagency task force, in\u2014\n**(A)**\ndeveloping and disseminating compelling, accessible Mandarin Chinese-language content within and outside the PRC\u2019s information control regime while avoiding duplication; and\n**(B)**\nfunding outside organizations to develop circumvention and secure content sharing tools;\n**(4)**\na description of how the Department plans to promote greater convergence and pairing between the development and dissemination of effective and high quality content and the circumvention tools used to access and share such content;\n**(5)**\na description of how the Department plans to develop networks with known and emerging Mandarin Chinese-language content developers and social media influencers through initiatives such as media and internet freedom programs based outside of the PRC;\n**(6)**\nan assessment of the current efficacy of content generated by the Department that is disseminated within the PRC, including by United States embassies and consulates within the PRC, and how Department plans to improve the efficacy and use of content disseminated within the PRC;\n**(7)**\na plan for increasing digital engagement with citizens of the PRC who are living or traveling outside of the PRC by providing them with temporary access to an uncensored internet environment; and\n**(8)**\na description of any additional resources, including additional funding or authorities, needed to further the objectives outlined in the strategy.\n##### (c) Classification\nThe strategy required under subsection (a) shall be unclassified, but may include a classified annex.\n#### 7. Establishment of the Global News Service\n##### (a) Establishment\nThe United States International Broadcasting Act of 1994 (title III of Public Law 103\u2013236 ; 22 U.S.C. 6201 et seq. ) is amended by inserting after section 309A the following:\n309B. Global News Service (a) Authority (1) In general Grants authorized under section 305(a) shall be available to award annual grants for the purpose of curating, translating, distributing, and making available content created or disseminated by the Voice of America, Radio Free Europe/Radio Liberty, Radio Free Asia, the Middle East Broadcasting Networks, the Office of Cuba Broadcasting, or any entity funded by or partnering with the United States Agency for Global Media, including news and information related to the People's Republic of China. (2) Establishment There is established a grantee entity, which\u2014 (A) shall be known as the 'Global News Service'; and (B) shall carry out the functions set forth in subsection (b). (b) Functions ln furtherance of the mission described in subsection (a)(1), the Global News Service\u2014 (1) shall seek to curate, translate, distribute, and make available content about or related to the People's Republic of China and the People's Republic of China's malign activities globally, in coordination with Voice of America's and Radio Free Asia's Mandarin Chinese language news service; (2) shall offer the content described in paragraph (1) in Mandarin Chinese and in English for the purpose of making fact-based, uncensored China-related news available to news organizations, independent journalists, and online content creators around the world; (3) should prioritize making available the content described in paragraph (1) to media outlets in countries that are influenced by Chinese Communist Party controlled media; (4) shall ensure that\u2014 (A) its Mandarin Chinese-language news service targets the Chinese diaspora abroad; and (B) its English-language news service targets foreign media outlets seeking China-related stories in English or other local languages; and (5) shall carry out any other effort consistent with the purposes of this Act if such effort is requested or approved by the United States Agency for Global Media. (c) Grant agreement (1) In general Any grant agreement with, or grants made to, the Global News Service under this section shall be subject to the limitations and restrictions set forth in paragraphs (2) through (7). (2) Headquarters The headquarters of the Global News Service and its senior administrative and managerial staff shall be in a location that ensures economy, operational effectiveness, and accountability to the United States Agency for Global Media. (3) Use of funds Grant funds may only be used for activities that are consistent with this section. Failure to comply with such requirement shall constitute a breach of contract and termination of the grant without further fiscal obligation by the United States. (4) Assumption of obligations by grantee Any contract entered into by the Global News Service shall specify that all obligations are assumed by the grantee and not by the United States Government. (5) Lease agreements Any lease agreements entered into by the Global News Service shall be, to the maximum extent possible, assignable to the United States Government. (6) Administrative costs Administrative and managerial costs for operation of the Global News Service should be kept to a minimum and, to the maximum extent feasible, should not exceed the costs that would have been incurred if the Global News Service had been operated as a Federal entity. (7) Limitation Grant funds may not be used for any activity the purpose of which is influencing the passage or defeat of legislation considered by Congress. (d) Relationship to the United States Agency for Global Media (1) In general The Global News Service shall be subject to the same oversight and governance by the United States Agency for Global Media as other grantees in accordance with section 305. (2) Assistance The United States Agency for Global Media, its broadcast entities, and the Global News Service should render assistance to each other to the extent necessary to carry out the purposes of this section or any other provision of this Act. (3) Not a federal agency or instrumentality Nothing in this section may be construed to designate the Global News Service as an agency or instrumentality of the Federal Government. (e) Audit authorities (1) In general Financial transactions of the Global News Service relating to functions carried out under this section may be audited by the Government Accountability Office in accordance with such principles and procedures, and under such rules and regulations, as may be prescribed by the Comptroller General of the United States. Any such audit shall be conducted at the place or places at which accounts of the Global News Service are normally retained. (2) Access by the government accountability office The Government Accountability Office shall have access to all books, accounts, records, reports, files, papers, and property belonging to or in use by the Global News Service pertaining to financial transactions as may be necessary to facilitate an audit. The Government Accountability Office shall be afforded full facilities for verifying transactions with any assets held by depositories, fiscal agents, and custodians. All such books, accounts, records, reports, files, papers, and property of the Global News Service shall remain in the possession and custody of the Global News Service. (3) Exercise of authorities Notwithstanding any other provision of law, the Inspector General of the Department of State and the Foreign Service is authorized to exercise the authorities set forth in chapter 4 of part I of title 5, United States Code (formerly known as the Inspector General Act of 1978 ) with respect to the Global News Service. .\n##### (b) Conforming amendments\nThe United States International Broadcasting Act of 1994 (title III of Public Law 103\u2013236 ; 22 U.S.C. 6201 et seq. ) is amended\u2014\n**(1)**\nin section 304(d) ( 22 U.S.C. 6203(d) ), by inserting the Global News Service, before the Middle East Broadcasting Networks ;\n**(2)**\nin section 305 ( 22 U.S.C. 6204 )\u2014\n**(A)**\nby moving subsection (c) so that it appears immediately after subsection (b); and\n**(B)**\nin subsection (c), by inserting the Global News Service, before or the Middle East Broadcasting Networks ; and\n**(3)**\nin section 310(d) ( 22 U.S.C. 6209(d) ), by inserting the Global News Service, before and the Middle East Broadcasting Networks .\n#### 8. Increasing coordination and resources for censorship circumvention, secure sharing, and content creation initiatives\n##### (a) Establishment of interagency task force\nThe President shall establish an interagency task force composed of representatives from the Department, National Security Council staff, and representatives from other Federal departments and agencies, as appropriate, as designated by the President.\n##### (b) Task force coordinator\n**(1) Establishment**\nThe President shall appoint a coordinator for the interagency task force established pursuant to subsection (a).\n**(2) Duties**\nThe Coordinator shall\u2014\n**(A)**\nconvene and coordinate the work of the interagency task force established pursuant to subsection (a);\n**(B)**\noversee the development and execution of the strategy described in section 6; and\n**(C)**\noversee the efforts of the Department described in subsection (d), in consultation, as appropriate, with relevant Department officials, including officials reporting to\u2014\n**(i)**\nthe Under Secretary of State for Public Diplomacy and Public Affairs;\n**(ii)**\nthe Assistant Secretary of State for Democracy, Human Rights, and Labor;\n**(iii)**\nthe Ambassador at Large for Cyberspace and Digital Policy; and\n**(iv)**\nthe Assistant Secretary of State for East Asian and Pacific Affairs.\n##### (c) Functions\nThe interagency task force shall\u2014\n**(1)**\ndevelop and execute the strategy described in section 6(a); and\n**(2)**\nincrease the coordination, within the Department and between relevant Federal departments and agencies, as appropriate, of Mandarin Chinese-language content development and dissemination, internet circumvention, and secure content-sharing tools specific to the PRC\u2019s censorship regime.\n##### (d) Department of State\n**(1) In general**\nThe Department, in consultation with relevant members of the interagency task force, shall oversee the development of compelling, timely, and relevant Mandarin Chinese-language content for a variety of audiences within the PRC and the dissemination of such content through a variety of tools and platforms within and outside the PRC.\n**(2) Internet circumvention and secure content sharing**\nThe Department, in coordination with relevant entities, other Federal departments and agencies, and external experts, as appropriate, shall seek to increase funding for programs and open source software that expand upon and develop new tools for internet circumvention and secure content sharing that are specifically tailored to evade the PRC censorship apparatus, including within the PRC, and improve immediate access to independent information for the end users of such tools.\n**(3) Media freedom, investigative journalism, and content development**\nThe Department shall seek to increase funding for media freedom, investigative journalism, and content development initiatives, including by establishing and expanding a network of individual and independent journalists or media companies and social media influencers that investigate and produce articles, reports, and other content related to real-time social, political, and economic events in the PRC\u2014\n**(A)**\nin which citizens of the PRC are directly interested; and\n**(B)**\nwhich can be accessed and amplified through a variety of tools and platforms within and outside the PRC digital ecosystem.\n**(4) Increasing Mandarin Chinese-language content within the great firewall and for citizens of the PRC living abroad**\nThe Department shall seek to increase the volume of\u2014\n**(A)**\neffective and high-quality Mandarin Chinese-language content for dissemination through Mission China\u2019s social media and other content sharing platforms;\n**(B)**\nmaterial that can be disseminated to citizens of the PRC residing outside of the PRC and the PRC censorship apparatus; and\n**(C)**\ncontent that focuses on quality of life issues in the United States that are directly relatable to issues in the PRC, including issues related to food safety, environmental sustainability, health care delivery, economic security and the jobs market, the investment climate, treatment of women, the treatment of marginalized populations, and government transparency.\n**(5) Content development and surveying**\nThe Department shall\u2014\n**(A)**\nincrease and refine Mandarin Chinese-language content directed towards citizens of the PRC residing within or outside the PRC; and\n**(B)**\nwork with external organizations, as appropriate, to regularly conduct credible, periodic surveys to gauge and assess issues of domestic and international importance to citizens of the PRC to inform the work of the interagency task force established pursuant to subsection (a) and the ongoing iteration by the Department of effective, high-quality Mandarin Chinese-language content.\n##### (e) United States Agency for Global Media\n**(1) In general**\nThe USAGM and relevant Federal and non-Federal entities shall\u2014\n**(A)**\ncarry out the actions described in paragraphs (2) through (5); and\n**(B)**\nwork with independent content creators, citizen journalists, and media organizations, as appropriate, to curate, disseminate, and amplify the highest-impact Mandarin Chinese-language content across USAGM entities to citizens of the PRC.\n**(2) Radio free asia**\n**(A) In general**\nRadio Free Asia, consistent with its congressional mandate, shall\u2014\n**(i)**\ndeliver independent, uncensored, PRC-specific news and information in local languages to audiences in the PRC and in other countries; and\n**(ii)**\nincrease coverage and digital Mandarin Chinese-language programming on political, economic, and social issues in the PRC, including by\u2014\n**(I)**\nexpanding RFA\u2019s Mandarin Chinese-language platforms;\n**(II)**\nprioritizing instances of PRC disinformation about PRC-internal topics directed towards Chinese citizens through its bilingual Asia Fact Check Lab; and\n**(III)**\nproviding insights to the interagency task force established pursuant to subsection (a) regarding\u2014\n**(aa)**\ncontent development strategies;\n**(bb)**\npriority topic areas salient to citizens of the PRC; and\n**(cc)**\ndata about access to and engagement with Mandarin Chinese-language RFA content among citizens of the PRC.\n**(B) Topics**\nTopic areas at RFA\u2019s editorial discretion referred to in subparagraph (A)(ii)(III)(bb) should include\u2014\n**(i)**\nquality of life in the PRC; and\n**(ii)**\nhuman rights, the rule of law, and good governance issues in the PRC that are relevant and important to broad segments of the population of the PRC.\n**(3) Voice of america**\nVoice of America shall, to the extent appropriate\u2014\n**(A)**\nincrease content of interest to citizens of the PRC; and\n**(B)**\nprovide insights to the interagency task force established pursuant to subsection (a) regarding\u2014\n**(i)**\ncontent development strategies;\n**(ii)**\npriority topic areas salient to citizens of the PRC; and\n**(iii)**\ndata about access to and engagement with Mandarin Chinese-language VOA content among citizens of the PRC.\n**(4) Open technology fund**\nThe Open Technology Fund shall\u2014\n**(A)**\nsupport the development and adoption of open source circumvention and secure communications tools that are tailored for use in the PRC;\n**(B)**\nincrease engagement with private sector technology companies, universities, and other relevant stakeholders to develop the next generation of internet circumvention and secure content sharing tools that\u2014\n**(i)**\nare specifically tailored to the PRC\u2019s censorship regime; and\n**(ii)**\ncan rapidly increase access to and secure sharing of independent information;\n**(C)**\nissue regular public solicitations for students and other civil society groups in the United States and in like-minded countries specializing in the cybersecurity and technology fields to research and develop the next generation of internet circumvention and secure content sharing tools that directly target the PRC censorship regime; and\n**(D)**\nregularly consult with the interagency task force established pursuant to subsection (a) regarding matters related to the development and adoption of circumvention and secure content sharing tools among citizens of the PRC, and inform about research and other technical needs related to circumvention of the PRC censorship regime and secure content sharing.\n**(5) Global news service**\nThe Global News Service shall\u2014\n**(A)**\nseek to curate, translate, distribute, and make available content about or related to the People's Republic of China and the People's Republic of China's malign activities globally, in coordination with Voice of America's and Radio Free Asia's Mandarin Chinese language news service;\n**(B)**\noffer such content in Mandarin Chinese and English for the purpose of making fact-based, uncensored China-related news available to news organizations, independent journalists, and online content creators around the world;\n**(C)**\nprioritize making available such content to media outlets in the countries that are influenced by CCP state media; and\n**(D)**\ntarget the Chinese diaspora abroad, through its Mandarin Chinese language news service.\n##### (f) Authorization of appropriations\n**(1) Department of State**\nThere is authorized to be appropriated to the Department, for each of the fiscal years 2025 through 2029, $25,000,000, which\u2014\n**(A)**\nshall be expended for ongoing and new programs in furtherance of the strategy required under section 6(a) and the functions and objectives set forth in subsections (c) and (d); and\n**(B)**\nmay be expended to contract with an external organization with expertise in surveying populations in the PRC and the broader Indo-Pacific region.\n**(2) United States Agency for Global Media**\nThere is authorized to be appropriated to the USAGM, for each of the fiscal years 2025 through 2029, $50,000,000, which shall be expended\u2014\n**(A)**\nto carry out the functions of the Global News Service, as set forth in section 309B of the United States International Broadcasting Act of 1994, as added in section 7(a); and\n**(B)**\nfor ongoing and new programs in pursuing the objectives set forth in subsection (e).\n#### 9. Addressing the lack of reciprocity between the United States and the People\u2019s Republic of China in the information space\n##### (a) Diplomatic engagement\nIn pursuing diplomatic engagement with the PRC, the Secretary of State should prioritize addressing the lack of reciprocity in access to the PRC internet and broader information space for United States Government, private sector, and nongovernmental stakeholders, particularly journalists, diplomats, researchers, academics, internet technology, and social media companies and nongovernmental organizations within the PRC.\n##### (b) Available tools\nThe President, in consultation with the Secretary of State, should consider all tools available to address the lack of reciprocity in access to the PRC internet and broader information space for United States Government, private sector, and nongovernmental stakeholders.",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-03-21T15:15:30Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s417is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "INFORM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-08T06:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INFORM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Informing a Nation with Free, Open, and Reliable Media Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-08T06:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to develop a strategy for increasing access to independent information for Chinese citizens, to establish an interagency task force to carry out such strategy, and for other purposes",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-08T06:33:40Z"
    }
  ]
}
```
