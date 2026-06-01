# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2352
- Title: Abolish Super PACs Act
- Congress: 119
- Bill type: HR
- Bill number: 2352
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-05-22T08:07:53Z
- Update date including text: 2026-05-22T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2352",
    "number": "2352",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000602",
        "district": "12",
        "firstName": "Summer",
        "fullName": "Rep. Lee, Summer L. [D-PA-12]",
        "lastName": "Lee",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Abolish Super PACs Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:53Z",
    "updateDateIncludingText": "2026-05-22T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "WA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "IL"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MN"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NM"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MD"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NC"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "NY"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "WA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2352ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2352\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Ms. Lee of Pennsylvania (for herself, Mr. Khanna , Mr. McGovern , Ms. Jayapal , Ms. Tlaib , Mr. Deluzio , and Mrs. Ramirez ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to place reasonable limits on contributions to Super PACs which make independent expenditures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Abolish Super PACs Act .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds as follows:\n**(1)**\nContribution limits to political action committees (PACs), including those that make independent expenditures, help secure elections by limiting both the risk of corruption and the risk that significant contributions will create the appearance of corruption.\n**(2)**\nSince contribution limits on super PACs were lifted in 2010, the number, influence, and wealth of super PACs have exploded. Obtaining millions or billions of dollars in contributions to super PACs is now critical to the success of Federal candidates\u2019 campaigns.\n**(3)**\nAs the influence of super PACs grows, so does the likelihood that they will serve as a conduit for corrupt agreements between contributor and candidate, whose communications are not subject to coordination limitations.\n**(4)**\nBetween 2008 and 2020, the amount of independent expenditures increased more than 700 percent, and in 2024, more than $4.48 billion in independent expenditures were spent on United States elections. The money for these expenditures largely came from contributions to 2,459 registered super PACs.\n**(5)**\nIn 2012, the first modern elections for Federal office held without contribution limits to super PACs, the top 1 percent of all individual super PAC contributors contributed 76.76 percent of all individual super PAC contributions, and that percentage rose to 96.94 percent in 2024. Recent elections have been influenced by individual contributors who gave more than $100 million to super PACs.\n**(6)**\nAs bribery laws have long recognized, unlawful quid pro quo exchanges can occur where the bribe is funneled into a third party, such as a super PAC. See, e.g., section 201 of title 18, United States Code; U.S. v. Menendez, 291 F. Supp. 606, 621\u201323 (D. N.J. 2018). Law enforcement in several States have prosecuted cases that involve bribes directed to super PACs. However, bribery is notoriously difficult to prosecute, and these laws do not adequately protect American voters from corruption.\n**(7)**\nWithout reasonable limitations on contributions, super PACs create an appearance of corruption. A bipartisan majority of Americans believe that large super PAC contributions are made in exchange for political favors, and that corruption is pervasive in the Federal Government. This is, as the Supreme Court recognized in Buckley v. Valeo, disastrous to confidence in the system of representative government 424 U.S. 1, 27 (1976).\n**(8)**\nPlacing limits on super PAC contributions will also lessen the risk of foreign interference in United States elections, making it more difficult for foreign entities to funnel contributions to super PACs via third-party contributors.\n**(9)**\nSpeechNow.org v. FEC, 599 F.3d 686 (D.C. Cir. 2010), the appellate court case that voided existing contribution limits to super PACs, wrongly treated contributions as expenditures and wrongly assumed that because uncoordinated independent expenditures cannot give rise to quid pro quo corruption, that contributions to independent expenditure committees similarly cannot give rise to corruption. But they can and do.\n**(10)**\nIn the 14 years since SpeechNow unleashed billions of dollars in unregulated contributions, super PACs have obtained unprecedented wealth and value to candidate campaigns and can facilitate vast, nearly untraceable corrupt transactions.\n**(11)**\nBecause Super PACs have become uniquely important to candidate campaigns and can accept millions and even hundreds of millions of dollars from single entities, candidates and contributors have reason and opportunity to guide corrupt contributions into super PACs, establishing a significant risk of corruption and creating an appearance of corruption that undermines the public\u2019s faith in their representatives and our political system.\n**(12)**\nReasonable limits on contributions to super PACs are lawful and necessary to protect American democracy and American voters.\n##### (b) Purpose\nIt is the purpose of this Act\u2014\n**(1)**\nto limit the risk of corrupt agreements between candidates and contributors by placing reasonable limits on contributions to political action committees that make independent expenditures;\n**(2)**\nto limit the appearance of corruption created by uncapped contributions to political action committees that make independent expenditures; and\n**(3)**\nto restore the public\u2019s faith in our elections.\n#### 3. Limitation on contributions to independent expenditure committees\n##### (a) Limitations\nSection 315(a)(1)(C) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30116(a)(1)(C) ) is amended by striking to any other political committee and inserting to an independent expenditure committee or any other political committee .\n##### (b) Definition\nSection 301 of such Act ( 52 U.S.C. 30101 ) is amended by adding at the end the following:\n(27) Independent expenditure committee (A) In general The term independent expenditure committee means a political committee which\u2014 (i) makes independent expenditures aggregating $5,000 or more during a calendar year; or (ii) makes contributions to other independent expenditure committees aggregating $5,000 or more during a calendar year. (B) Treatment of separate accounts The term independent expenditure committee includes an account of a political committee which is established for the purpose of making independent expenditures or contributions to other committees making independent expenditures. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to contributions and independent expenditures made during the first calendar year which begins after the date of the enactment of this Act and each succeeding calendar year.",
      "versionDate": "2025-03-26",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-09T16:11:17Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2352ih.xml"
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
      "title": "Abolish Super PACs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Abolish Super PACs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to place reasonable limits on contributions to Super PACs which make independent expenditures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:15Z"
    }
  ]
}
```
