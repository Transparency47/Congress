# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3891?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3891
- Title: Northern Border Security and Staffing Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 3891
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-05-16T08:07:59Z
- Update date including text: 2026-05-16T08:07:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-11 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-06-11 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3891",
    "number": "3891",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Northern Border Security and Staffing Reform Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:59Z",
    "updateDateIncludingText": "2026-05-16T08:07:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-11T20:28:25Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "MI"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "WI"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "NY"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "IA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MN"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "ID"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3891ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3891\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Stauber (for himself, Mr. Langworthy , Mr. Bergman , Mr. Tiffany , Ms. Tenney , Ms. Stefanik , and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Northern Border Security Review Act to require an annual report and update the northern border threat analysis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Northern Border Security and Staffing Reform Act .\n#### 2. Findings and sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nBetween 2002 and 2011, U.S. Customs and Border Protection (CBP) roughly doubled their staffing levels, and according to the U.S. Customs and Border Protection Office Workload Staffing Model that calculates the number of CBP officers estimated to carry out the CBP mission at each air, sea, and land port of entry in the United States, states that the current staffing gap between the model results and the current staffing levels indicates a nationwide staffing shortage of 5,800 CBP officers.\n**(2)**\nThe Consolidated Appropriations Act, 2008 ( Public Law 110\u2013161 ) made Customs and Border Protection Officers eligible for the 1.7 percent enhanced law enforcement officer (LEO) retirement system, which allows law enforcement officers to retire at age 50 with 20 years of service, or at any age with 25 years of service.\n**(3)**\nOn April 30, 2024, then-Senior Official Performing the Duties of the Commissioner Troy A. Miller testified before the Committee on Appropriations of the House of Representatives that ports of entry face a 400 percent increase in retirements in 2028.\n**(4)**\nThis retirement surge would disproportionately affect ports of entry along the northern border.\n**(5)**\nA 400 percent retirement surge would leave ports of entry along the northern border understaffed and unable to protect the American people from threats.\n**(6)**\nPorts of entry along the northern border face unique staffing challenges due to their harsh winters, isolated locations, limited economic opportunities, and scarce housing markets. These factors make it difficult for northern ports of entry to recruit and retain officers who are not from its region.\n##### (b) Sense of Congress\nIt is the sense of Congress that U.S. Customs and Border Protection must begin a hiring surge of qualified recruits at ports of entry along the northern border to avoid the disastrous effects of the impending retirement surge, future retirement surges, and current staffing shortage.\n#### 3. Northern Border threat analysis update\n##### (a) In general\nThe Northern Border Security Review Act ( Public Law 114\u2013267 ) is amended\u2014\n**(1)**\nin subsection (a), in the matter preceding paragraph (1), by striking 180 days after the date of enactment of this Act and inserting not later than 180 days after the date of the enactment of the Northern Border Security and Staffing Reform Act and every five years thereafter ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (3) through (6) as paragraphs (7) through (10), respectively; and\n**(B)**\nby inserting after paragraph (2) the following new paragraphs:\n(3) the current number of U.S. Customs and Border Protection officers and agents deployed along the northern border compared with the projected demand over the following years for such officers and agents; (4) the future retirement surges of such officers and agents, associated risks, and plans for mitigation of such risks; (5) any housing challenges along the northern border for such officers and agents; (6) the development of local recruiting plans to promote the hiring of new U.S. Customs and Border Protection officers and agents local to areas close to northern ports of entry; ;\n**(3)**\nby redesignating subsection (c) as subsection (d);\n**(4)**\nby inserting after subsection (b) the following new subsection:\n(c) Additional elements The Secretary of Homeland Security shall also include in each threat analysis required under subsection (a) the following: (1) A plan, and any updates thereto, to address future retirement surges, staffing challenges, and staffing shortages along the northern border. (2) An assessment of the feasibility of the use of various recruitment and retention tools, including direct hire authority, recruitment, retention, and relocation bonuses, additional pay authorities, and student loan repayment programs to address staffing shortages along the northern border. ; and\n**(5)**\nby adding at the end the following new subsection:\n(e) Definition In this section, the term local recruiting plans means plans designed to motivate, recruit, hire, assist, and mentor local qualified candidates to apply for and have a career in U.S. Customs and Border Protection at nearby ports of entry. .",
      "versionDate": "2025-06-10",
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
        "name": "Immigration",
        "updateDate": "2025-07-23T13:35:00Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3891ih.xml"
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
      "title": "Northern Border Security and Staffing Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Northern Border Security and Staffing Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Northern Border Security Review Act to require an annual report and update the northern border threat analysis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:24Z"
    }
  ]
}
```
