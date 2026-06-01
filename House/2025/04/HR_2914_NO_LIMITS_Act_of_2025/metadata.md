# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2914?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2914
- Title: NO LIMITS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2914
- Origin chamber: House
- Introduced date: 2025-04-14
- Update date: 2025-05-27T15:53:07Z
- Update date including text: 2025-05-27T15:53:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-14: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-04-14: Introduced in House

## Actions

- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Introduced in House
- 2025-04-14 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-14",
    "latestAction": {
      "actionDate": "2025-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2914",
    "number": "2914",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "NO LIMITS Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-27T15:53:07Z",
    "updateDateIncludingText": "2025-05-27T15:53:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-14",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-04-14T13:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2914ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2914\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2025 Mr. Moolenaar (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for the imposition of sanctions relating to the People\u2019s Republic of China and support for Russian invasion of Ukraine, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the NO LIMITS Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOn September 30, 2022, the Office of Foreign Assets Control of the Department of the Treasury designated People\u2019s Republic of China entity Sinno Electronics Co. Limited (Sinno) for providing material support to the defense industrial base of the Russian Federation.\n**(2)**\nOn January 26, 2023, the Office of Foreign Assets Control of the Department of the Treasury sanctioned People\u2019s Republic of China entity Changsha Tianyi Space Science and Technology Research Institute Co. LTD (Spacety China) for providing material support to entities of the Russian Federation involved in combat operations in Ukraine.\n**(3)**\nThere is clear and increasing evidence that People\u2019s Republic of China entities continue to evade United States sanctions to provide material support to the defense and military industrial base of the Russian Federation.\n**(4)**\nUnder Executive Order 13959 (85 Fed. Reg. 73185; related to addressing the threat from securities investments that finance Communist Chinese military companies), the President found that the People\u2019s Republic of China increases the size of the country\u2019s military-industrial complex by compelling civilian Chinese companies to support its military and intelligence activities. Those companies, though remaining ostensibly private and civilian, directly support the PRC\u2019s military, intelligence, and security apparatuses and aid in their development and modernization. .\n**(5)**\nEvidence of industrial support for the Russian Federation by the People\u2019s Republic of China, combined with inherent blurred lines between the civilian versus governmental defense apparatus in the People\u2019s Republic of China, requires new authorities to protect the national security of the United States.\n##### (b) Sense of Congress\nIt is the sense of Congress that the Russian Federation\u2019s continued invasion of Ukraine is directly enabled by the People\u2019s Republic of China. It is therefore time for the President to\u2014\n**(1)**\nmore fully cut off financing avenues for People\u2019s Republic of China entities providing materiel support to the defense and related materiel sector of the economy of the Russian Federation;\n**(2)**\nmore fully cut off financing avenues for People\u2019s Republic of China entities involved in military modernization activities;\n**(3)**\nimpose country-wide export control restrictions on dual-use technology exported to the PRC over concerns of diversion to the Russian Federation; and\n**(4)**\nimpose sanctions on PRC entities involved in the export of weapons and dual-use technology to the Russian Federation, including microelectronics, aerospace, automobiles, among others.\n#### 3. Imposition of sanctions relating to the People\u2019s Republic of China and support for Russian invasion of Ukraine\n##### (a) In general\nOn and after the date that is 90 days after the date of the enactment of this Act, the President\u2014\n**(1)**\nmay impose the sanction described in subsection (c) with respect to a foreign person the President determines\u2014\n**(A)**\nis located or headquartered within, or is organized under the laws of, the People\u2019s Republic of China; and\n**(B)**\noperates in the technology sector of the economy of the Russian Federation, the defense and related materiel sector of such economy, or any other sector of such economy as may be determined by the Secretary of the Treasury or the Secretary of State, as the case may be; and\n**(2)**\nmay impose the sanction described in subsection (c) with respect to a foreign person the President determines that, in acting for or on behalf of, or for the benefit of, directly or indirectly, the armed forces or intelligence services of the People\u2019s Republic of China, is responsible for or engages in\u2014\n**(A)**\nmalicious cyber-enabled activities; or\n**(B)**\nthe production, or research and development, of dual-use technology or defense or related materials; or\n**(C)**\nfacilitating the evasion, circumvention, or direct violation of United States export controls or sanctions.\n##### (b) People\u2019s Republic of China Military Companies Operating in Russian Federation\nOn and after the date that is 180 days after the date of the enactment of this Act, the President may impose the sanctions described in subsection (c) with respect to a foreign person that\u2014\n**(1)**\nhas business operations in the Russian Federation; and\n**(2)**\nis a known Chinese military company.\n##### (c) Sanction described\n**(1) In general**\nThe sanction described in this paragraph is the exercise all of the powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of a foreign person if such property or interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Implementation**\nThe President may exercise the authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to the extent necessary to carry out this section.\n**(3) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person who violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in subsection section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n**(4) Exceptions**\n**(A) Exception for intelligence and law enforcement actions**\nSanctions under this section shall not apply with respect to\u2014\n**(i)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(ii)**\nany authorized intelligence or law enforcement activities of the United States.\n**(B) Exception relating to importation of goods**\n**(i) In general**\nThe authorities and requirements to impose sanctions authorized under this section shall not include the authority or requirement to impose sanctions on the importation of goods.\n**(ii) Good defined**\nIn this subparagraph, the term good means any article, natural or manmade substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (d) Waivers\nThe President may waive the application of sanctions under this section with respect to a foreign person for renewable periods of not more than 90 days each if the President determines and reports to Congress that such a waiver is vital to the national interests of the United States.\n##### (e) Definitions\nIn this section:\n**(1) Business operations**\nThe term business operations means any participation by any person in a commercial enterprise or venture, or participation in any association, institution, organization, or entity, whether of a commercial nature or otherwise. This includes the production, distribution, exportation, sale of goods, or provision of services, regardless of whether a pecuniary benefit or other assets are derived from such participation.\n**(2) Foreign person**\nThe term foreign person means any person that is not a United States person.\n**(3) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result (as the case may be).\n**(4) Person**\nThe term person means an individual or entity.\n**(5) United States person**\nThe term United States person means any United States citizen, permanent resident alien, an entity organized under the laws of the United States or any jurisdiction within the United States (including a foreign branch of such an entity), or any person in the United States.\n**(6) Known Chinese military company**\nThe term known Chinese military company means any of the following persons:\n**(A)**\nAviation Industry Corporation of China Ltd (AVIC).\n**(B)**\n360 Security Technology Inc. (Qihoo 360).\n**(C)**\nAdvanced Micro-Fabrication Equipment Inc. China (AMEC).\n**(D)**\nAerospace CH UAV Co., Ltd (S\u2013SEA).\n**(E)**\nBeijing Megvii Technology Co., Ltd. (Megvii).\n**(F)**\nBGI Genomics Co. Ltd. (BGI).\n**(G)**\nMGI Co. Ltd. (MGI).\n**(H)**\nChina Aerospace Science and Industry Corporation Limited (CASIC).\n**(I)**\nChina Electronics Corporation (CEC).\n**(J)**\nChina Construction Technology Co. Ltd (CCTC).\n**(K)**\nChina Communications Construction Group (CCCG).\n**(L)**\nChina Construction Technology Co. Ltd (CCTC).\n**(M)**\nChina Electronics Technology Group Corporation (CETC).\n**(N)**\nHangzhou Hikvision Digital Technology Co. Ltd (Hikvision).\n**(O)**\nChina General Nuclear Power Corporation (CGN).\n**(P)**\nChina Mobile Communications Group Co. Ltd. (China Mobile Comm).\n**(Q)**\nChina National Chemical Corporation (ChemChina).\n**(R)**\nChina National Offshore Oil Corporation (CNOOC).\n**(S)**\nChina National Nuclear Corporation (CNNC).\n**(T)**\nChina Railway Construction Corporation Limited (CRCC).\n**(U)**\nChina South Industries Group Corporation (CRCC).\n**(V)**\nChina State Construction Engineering Corporation Limited (CSCEC).\n**(W)**\nChina State Shipbuilding Corporation Limited (CSSC).\n**(X)**\nChina Telecom Group Co, Ltd. (China Telecom).\n**(Y)**\nChina Three Gorges Corporation (CTG).\n**(Z)**\nChina United Network Communications Group Co. Ltd (China Unicom).\n**(AA)**\nCloudWalk Technology Co. Ltd (CloudWalk).\n**(BB)**\nDawning Information Industry Co. Ltd (Sugon).\n**(CC)**\nHesai Technology Co. Ltd (Hesai).\n**(DD)**\nHuawei Technologies Co. Ltd (Huawei).\n**(EE)**\nInspur Group Partners Co. Ltd (IDG Capital).\n**(FF)**\nSemiconductor Manufacturing International Corporation (SMIC).\n**(GG)**\nShenzhen DJI Innovation Technology Co. Ltd (DJI).\n**(HH)**\nYangtze Memory Technologies Co., Ltd. (YMTC).\n**(II)**\nZhejiang Dahua Technology Co., Ltd (Dahua).\n**(JJ)**\nAVIC Shenyang Aircraft Co., Ltd.\n**(KK)**\nAutel Robotics Co. Ltd (Autel).\n**(LL)**\nAVIC Heavy Machinery Company Limited.\n**(MM)**\nAVIC Xi\u2019An Aircraft Industry Group Company Ltd.\n**(NN)**\nChangXin Memory Technologies (CXMT).\n**(OO)**\nDahua Technology.\n**(PP)**\nZhejiang Uniview Technologies.\n**(QQ)**\nGuizhou Guihang Automotive Components Co., Ltd.\n**(RR)**\nChangying Xinzhi Technology Co., Ltd.\n**(SS)**\nSichuan Northern Nitrocellulose Co., Ltd.\n**(TT)**\nNorthern Chemistry Industry Co., Ltd.\n**(UU)**\nAny subsidiary, affiliate, or successor of entities in subparagraphs (A) through (RR).\n##### (f) Rules of construction\nNothing in this section may be construed to limit the authority of the President to designate or sanction persons pursuant to an applicable Executive order or otherwise pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n#### 4. Determination of sanctions on arms manufacturers of the People\u2019s Republic of China engaged in overseas weapons sales\n##### (a) Determination\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury, in consultation with the Secretary of State, and the Secretary of Defense, shall submit to the appropriate congressional committees a determination of whether, for each covered person, that covered person meets the criteria for the imposition of the sanction described in section 3(c).\n##### (b) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs, the Permanent Select Committee on Intelligence, and the Select Committee on the Strategic Competition Between the United States and the Chinese Communist Party of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations, the Committee on Banking, Housing, and Urban Affairs, and the Select Committee on Intelligence of the Senate.\n**(2) Covered person**\nThe term covered person means any of the following persons:\n**(A)**\nChina North Industries Group Corporation.\n**(B)**\nAviation Industry Corporation of China.\n**(C)**\nChina Electronics Technology Group Corporation.\n**(D)**\nChina South Industries Group Corporation.\n**(E)**\nChina Aerospace Science and Industry Corporation.\n**(F)**\nChina General Nuclear Power Group.\n**(G)**\nChina National Nuclear Corporation.\n**(H)**\nChina State Shipbuilding Corporation.\n#### 5. Expanding subsidiary controls for PRC and Russian entities to prevent diversion to Russia\u2019s war effort\nAny licensing requirement applied to a PRC or Russian entity by reason of the entity being included on the entity list shall also apply to any subsidiary or other entity over which the listed entity has control.\n#### 6. Definitions\nIn this Act the term control has the meaning given that term in\u2014\n**(1)**\nsection 800.208 of title 31, Code of Federal Regulations; or\n**(2)**\nany successor regulations.\n#### 7. Regulations\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Commerce, the Secretary of Defense, and the Secretary of State, shall issue such regulations as may be necessary to carry out this Act and the amendments made by this Act.",
      "versionDate": "2025-04-14",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-27T15:53:07Z"
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
      "date": "2025-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2914ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NO LIMITS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NO LIMITS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the imposition of sanctions relating to the People's Republic of China and support for Russian invasion of Ukraine, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T03:03:21Z"
    }
  ]
}
```
