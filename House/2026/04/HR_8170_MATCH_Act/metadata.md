# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8170?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8170
- Title: MATCH Act
- Congress: 119
- Bill type: HR
- Bill number: 8170
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-05-20T08:08:11Z
- Update date including text: 2026-05-20T08:08:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 36 - 8.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 36 - 8.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8170",
    "number": "8170",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "MATCH Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:11Z",
    "updateDateIncludingText": "2026-05-20T08:08:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by the Yeas and Nays: 36 - 8.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
        "item": [
          {
            "date": "2026-04-22T20:40:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-02T12:32:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "GA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "ME"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MI"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "NH"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "VA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "ID"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "TX"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "NJ"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AR"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "MT"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "IN"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8170ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8170\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Baumgartner (for himself, Mr. Moolenaar , Mr. McCormick , Mr. Mannion , Mr. Golden of Maine , Mr. Huizenga , Mr. Shreve , Mr. Lawler , Mr. Riley of New York , Ms. Goodlander , and Mr. Subramanyam ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for export restrictions on certain semiconductor manufacturing equipment and components therefor, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Multilateral Alignment of Technology Controls on Hardware Act or the MATCH Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nexport controls on semiconductor manufacturing equipment and components represent one of the United States most effective defenses of this foundational technology;\n**(2)**\nadvanced computing applications like artificial intelligence are transforming military affairs and the balance of power;\n**(3)**\nthe United States and its allies have an advantage in the foundational technologies that underpin advanced computing applications, including advanced-node integrated circuits and production, and the equipment and software required to design and produce advanced-node integrated circuits;\n**(4)**\nrobust controls on semiconductor manufacturing equipment and components have been a bipartisan priority across multiple administrations, reflecting a shared recognition that protecting America\u2019s semiconductor advantage is essential to national security;\n**(5)**\nthe adversaries of the United States are exploiting gaps in the current export control regime;\n**(6)**\ncertain entities, including ChangXin Memory Technologies (CXMT), Hua Hong, Semiconductor Ltd. (Hua Hong), Huawei, Technologies Co. Ltd. (Huawei), Semiconductor Manufacturing International Corporation (SMIC), Yangtze Memory Technologies Corp. (YMTC), Advanced Micro-Fabrication Equipment Inc. China (AMEC), Beijing E-Town Semiconductor Technology Co., Ltd. (E-Town Semiconductor), NAURA Technology Group Co., Ltd. (NAURA), Piotech Semiconductor Equipment Co., Ltd. (Piotech), ACM Research, Inc. (ACM Research), PNC Process Systems Co., Ltd. (PNC Process Systems), Skyverse Technology Co. (Skyverse), Shanghai Micro Electronics Equipment (Group) (SMEE), Kingsemi Co., Ltd. (Kingsemi), and Hwatsing Technology Co. Ltd. (Hwatsing) are engaged in efforts to produce advanced-node integrated circuits and especially crucial for the Military-Civil Fusion efforts of the People\u2019s Republic of China and warrant comprehensive export controls to prevent those companies from accessing items made with United States technologies;\n**(7)**\ncompanies located in adversary countries that produce semiconductor manufacturing equipment are critical to adversaries\u2019 efforts to develop advanced-node integrated circuit production capabilities and overcome export controls, and should not be permitted to utilize or benefit from United States or allied technology or components; and\n**(8)**\nthe United States Government should work closely with allies and partners of the United States to align export controls on semiconductor manufacturing equipment and components to prevent gaps in controls, reduce the risk of circumvention, and ensure a level global playing field.\n#### 3. Report and application of controls\n##### (a) Identifying chokepoints\nNot later than 60 days after the date of the enactment of this Act, and annually thereafter, the covered agency heads shall\u2014\n**(1)**\njointly conduct a review to identify all covered semiconductor manufacturing equipment and all covered facilities; and\n**(2)**\nsubmit to the appropriate congressional committees a list of all such equipment and covered facilities.\n##### (b) Diplomatic engagement\n**(1) In general**\nThe covered agency heads shall prioritize and upon enactment of this Act immediately engage diplomatically to seek for the governments of allied supplier countries to adopt\u2014\n**(A)**\ncountrywide controls on covered semiconductor manufacturing equipment subject to the allied supplier country\u2019s jurisdiction, or other controls and licensing policies having the same practical effect; and\n**(B)**\nlicense requirements for the export of all applicable items to any covered facility, and the servicing of all applicable items at any covered facilities, with a licensing policy of denial.\n**(2) Briefing on diplomatic efforts**\nNot later than 90 days after the date of the enactment of this Act, the covered agency heads shall provide a briefing to members of the appropriate congressional committees that\u2014\n**(A)**\ndescribes the status of diplomatic efforts to secure the adoption by allied supplier countries of the controls described in paragraph (1);\n**(B)**\noutlines and assesses incentives to encourage adoption of these controls; and\n**(C)**\nidentifies\u2014\n**(i)**\nallied supplier countries that have not adopted the controls described in paragraph (1)(A);\n**(ii)**\nallied supplier countries that have not adopted the controls described in paragraph (1)(B); and\n**(iii)**\nmeasures that the United States has taken or plans to take to implement the controls described in paragraph (1).\n##### (c) Exhaustion of diplomatic recourse and application of controls\n**(1) Application of controls**\nNot later than 150 days after the enactment of this Act, and annually thereafter, the covered agency heads shall publish regulations that\u2014\n**(A)**\nensure all U.S. countrywide controls include all U.S.-origin covered semiconductor manufacturing equipment; and\n**(B)**\nensure all covered facilities in countries of concern are subject to comprehensive U.S. restrictions.\n**(2) Exhaustion of diplomatic recourse**\nBy the date that is 150 days after the date of the enactment of this Act, the covered agency heads shall jointly either\u2014\n**(A)**\ncertify to the appropriate congressional committees that all allied supplier countries have implemented\u2014\n**(i)**\ncountrywide controls over all covered semiconductor manufacturing equipment subject to the allied supplier country\u2019s jurisdiction, or other controls and licensing policies having the same practical effect; and\n**(ii)**\nlicense requirements for all applicable items, with a licensing policy of denial, or other controls and licensing policies having the same practical effect; or\n**(B)**\nprovide a list to the appropriate congressional committees of any allied supplier countries that have not implemented all controls described in subparagraph (A)(i) or (ii).\n**(3) Extension of controls**\nUnless the covered agency heads provide the certification in subparagraph (A), the covered agency heads shall issue regulations that\u2014\n**(A)**\nestablish U.S. jurisdiction over and apply countrywide controls to all covered semiconductor manufacturing equipment and components therefor exported from countries identified by the covered agency heads under subsection (c)(2)(B), whether by establishing jurisdiction over such items and applying controls directly, or by restricting the end-uses of essential components of such equipment that are already subject to U.S. jurisdiction, or both;\n**(B)**\nrequire a license for all servicing of any applicable item located in any covered facility, and implement a policy of denial for such servicing; and\n**(C)**\nestablish jurisdiction over, and apply end-user or end-use controls prohibiting, the export from countries identified by the covered agency heads under subsection (c)(2)(B) of all applicable items to any covered facility.\n##### (d) National security waiver\nThe covered agency heads may jointly grant a one-time waiver to extend the 150-day deadline under subsection (c) by not more than 90 days, if the covered agency heads, with concurrence from the Secretary of Defense and the Secretary of Energy, jointly\u2014\n**(1)**\ndetermine and certify to the appropriate congressional committees that\u2014\n**(A)**\nthe extension is in the national security interest of the United States, despite the risk that countries of concern may take advantage of the delay to further stockpile covered semiconductor manufacturing equipment; and\n**(B)**\nthe governments of an allied supplier country or countries are taking concrete, verifiable steps, pursuant to their domestic laws and regulations and as expeditiously as possible, to adopt and implement controls that are fully aligned with, or more stringent than, the controls that would otherwise be imposed under subsection (c)(3); and\n**(2)**\nsubmit a report to the appropriate congressional committees describing\u2014\n**(A)**\nthe details justifying the national security interest determination and progress that is intended to be achieved by the extension; and\n**(B)**\nthe concrete and verifiable interim steps the covered agency heads have taken to prevent stockpiling of covered semiconductor manufacturing equipment by countries of concern.\n##### (e) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the covered agency heads shall provide to the appropriate congressional committees a report that includes\u2014\n**(1)**\na list of all covered semiconductor manufacturing equipment;\n**(2)**\na list of all covered facilities and all entities that own or operate any covered facility;\n**(3)**\nthe scope of the controls described in subsection (b)(1) imposed by the United States and allied supplier countries for all covered semiconductor manufacturing equipment identified pursuant to paragraph (1);\n**(4)**\na summary of diplomatic engagements and unilateral actions undertaken in the 12-month period prior to the submission of the report to close any gap in the controls described in subsection (b)(1) among allied supplier countries; and\n**(5)**\na certification that the export of all covered semiconductor manufacturing equipment to a country of concern, and the export, reexport, or transfer, or servicing of all applicable items to any covered facility, requires a United States or allied license and applications for such licenses will be reviewed under a policy of denial.\n##### (f) Termination and reimposition of controls upon allied action\n**(1) Termination or modification**\nIf the covered agency heads determine that an allied supplier country has implemented all the controls in (c)(2)(A)(i) and (ii), the covered agency heads may, upon notifying the appropriate congressional committees of such determination, terminate or modify any control imposed under subsection (c)(3) for items exported from that allied supplier country.\n**(2) Reimposition**\nIf, after terminating or modifying a control under paragraph (1), the covered agency heads determine that the allied supplier country has materially weakened, suspended, or revoked the control or licensing policy of denial that justified the termination or modification under paragraph (1), the covered agency heads shall, not later than 60 days after making such determination\u2014\n**(A)**\nnotify the appropriate congressional committees of such determination; and\n**(B)**\nreimpose the control under subsection (c)(2) that was terminated or modified under paragraph (1).\n##### (g) Administrative procedure act rulemaking and judicial review\nThe provisions of section 1762 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4821 ) shall apply to this Act in the same manner and to the same extent as such provisions apply to the Export Control Reform Act of 2018.\n##### (h) Sunset\n**(1) Expiration**\nThis Act shall cease to have effect on the date that is 5 years after the date of the enactment of this Act.\n**(2) Continuation of prior obligations**\nThe expiration of this Act under subsection (a) shall not affect any action, proceeding, or obligation that was commenced or incurred prior to such expiration.\n##### (i) Definitions\nIn this section:\n**(1) Advanced-node integrated circuits**\nThe term advanced-node integrated circuits has the meaning given that term in section 772.1 of the Export Administration Regulations.\n**(2) Allied supplier country**\nThe term allied supplier country means any country that\u2014\n**(A)**\nis not a country of concern; and\n**(B)**\nis engaged in the production of covered semiconductor manufacturing equipment.\n**(3) Applicable item**\nThe term applicable item means any item that is or can be made subject to the Export Administration Regulations, including\u2014\n**(A)**\na foreign-produced item that is the direct product of, or produced by plants or major components that are themselves the direct product of software or technology subject to the Export Administration Regulations;\n**(B)**\na foreign-produced item with more than zero percent de minimis controlled United States-origin content; and\n**(C)**\na foreign-produced item that contain United States-origin or foreign-produced integrated circuits that are presumptively designed or produced, directly or indirectly, with technology, software, or equipment that is subject to the Export Administration Regulations.\n**(4) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(5) Country of concern**\nThe term country of concern means\u2014\n**(A)**\nthe People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions;\n**(B)**\nthe Republic of Cuba;\n**(C)**\nthe Islamic Republic of Iran;\n**(D)**\nthe Democratic People\u2019s Republic of Korea;\n**(E)**\nthe Russian Federation; and\n**(F)**\nany other foreign country listed in the Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations, as published on January 1, 2026, that is designated by the Secretary of State as a country of concern for purposes of this section and for which notice of such designation has been published in the Federal Register.\n**(6) Countrywide controls**\nThe term countrywide controls means licensing requirements and a policy of denial for the export, reexport, transfer or servicing of all specified items to any destination within any country of concern, excluding exports where the destination is a fabrication facility that existed as of the date of the enactment of this Act and remains owned and operated by a company headquartered, and having an ultimate parent headquartered, outside of any country of concern.\n**(7) Covered agency heads**\nThe term covered agency heads means the Under Secretary of Commerce for Industry and Security and the Secretary of State, in coordination with the Secretary of Energy and the Secretary of Defense, or their designees.\n**(8) Covered facility**\nThe term covered facility means any facility\u2014\n**(A)**\nwhich is\u2014\n**(i)**\nlocated in a country of concern;\n**(ii)**\nengaged in the production of advanced-node integrated circuits; and\n**(iii)**\nnot a fabrication facility that\u2014\n**(I)**\nexisted as of the date of the enactment of this Act; and\n**(II)**\nremains owned and operated by a company which is headquartered and has an ultimate parent headquartered outside of any country of concern; or\n**(B)**\nwhich is or ever has been owned or controlled by, under common ownership or control with, or manufacturing at the direction of\u2014\n**(i)**\nany entity described in section 5949(j)(3)(A) or (B);\n**(ii)**\nHuawei or Hua Hong;\n**(iii)**\nany producer, manufacturer, or developer of semiconductor manufacturing equipment that is headquartered in, or has an ultimate parent headquartered in, a country of concern; or\n**(iv)**\nany entity that is a subsidiary, affiliate, or successor to, or has a joint venture, teaming agreement, joint development or research agreement, technology transfer or collaboration agreement, or other similar type of arrangement with an entity described in paragraph (10)(B)(i), (ii), or (iii).\n**(9) Covered semiconductor manufacturing equipment**\nThe term covered semiconductor manufacturing equipment \u2014\n**(A)**\nmeans semiconductor manufacturing equipment or a component therefor that\u2014\n**(i)**\nis an applicable item; and\n**(ii)**\nthe covered agency heads determine no country of concern produces in high volume and with capabilities comparable to those of the product sold by the global market leader, as of the date of the enactment of this Act; and\n**(B)**\nincludes, at a minimum\u2014\n**(i)**\nall semiconductor manufacturing equipment, materials, and software that at the date of passage of this Act require a license for export, re-export, or in-country transfer to any destination in a country of concern;\n**(ii)**\nall deep ultraviolet immersion photolithography machines, through silicon via deposition and etch tools, cryogenic etch equipment, and cobalt deposition equipment, regardless of overlay or other performance characteristics; and\n**(iii)**\npresumptively, all semiconductor manufacturing equipment or components specified in Export Control Classification Number 3B001, 3B002, or 3B993 as of the date of the enactment of this Act, except any items the covered agency heads determine are not covered semiconductor manufacturing equipment.\n**(10) Export; in-country transfer; reexport; export administration regulation**\nThe terms export , in-country transfer , reexport , and Export Administration Regulations have the meanings given such terms in section 1742 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 ).\n**(11) Servicing**\nThe term servicing means any servicing of equipment or components, whether in-person or remote, including installation, calibration, repair, overhauling, refurbishing, testing, diagnosing, updating software or firmware, training, field services, application support engineering, customization, technical assistance, process adjustments, troubleshooting, and transfer of industry best practices for maintenance.",
      "versionDate": "2026-04-02",
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
        "updateDate": "2026-04-20T23:19:44Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8170ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MATCH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-15T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Multilateral Alignment of Technology Controls on Hardware Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-15T07:53:22Z"
    },
    {
      "title": "MATCH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for export restrictions on certain semiconductor manufacturing equipment and components therefor, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T07:48:39Z"
    }
  ]
}
```
