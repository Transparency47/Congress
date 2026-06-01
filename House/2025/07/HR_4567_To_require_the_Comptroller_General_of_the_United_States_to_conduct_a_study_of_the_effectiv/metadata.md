# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4567?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4567
- Title: Supporting Military Voters Act
- Congress: 119
- Bill type: HR
- Bill number: 4567
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-03-31T12:29:27Z
- Update date including text: 2026-03-31T12:29:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4567",
    "number": "4567",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Supporting Military Voters Act",
    "type": "HR",
    "updateDate": "2026-03-31T12:29:27Z",
    "updateDateIncludingText": "2026-03-31T12:29:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:00:40Z",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CO"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "OK"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "OH"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4567ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4567\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Ms. Lee of Florida (for herself, Mr. Neguse , and Mrs. Bice ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require the Comptroller General of the United States to conduct a study of the effectiveness of the Federal Government in carrying out its responsibilities under the Uniformed and Overseas Citizens Absentee Voting Act to promote access to voting for absent uniformed services voters and an analysis of means for improving access to voter registration information and assistance for members of the Armed Forces and their family members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Military Voters Act .\n#### 2. Government Accountability Office report on implementation of Uniformed and Overseas Citizens Absentee Voting Act and improving access to voter registration information and assistance for absent uniformed services voters\n##### (a) In general\nThe Comptroller General of the United States shall conduct\u2014\n**(1)**\nan analysis of the effectiveness of the Federal Government in carrying out its responsibilities under the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20301 et seq. ) to promote access to voting for absent uniformed services voters; and\n**(2)**\na study on means for improving access to voter registration information and assistance for members of the Armed Forces and their family members.\n##### (b) Elements\n**(1) Analysis**\nThe analysis required by subsection (a)(1) shall include analysis of the following:\n**(A)**\nData and information pertaining to the transmission of ballots to absent uniformed services voters.\n**(B)**\nData and information pertaining to the methods of transmission of voted ballots from absent uniformed services voters, including the efficacy and security of such methods.\n**(C)**\nData and information pertaining to the treatment by election officials of voted ballots transmitted by absent uniformed services voters, including\u2014\n**(i)**\nthe rate at which such ballots are counted in elections;\n**(ii)**\nthe rate at which such ballots are rejected in elections; and\n**(iii)**\nthe reasons for such rejections.\n**(D)**\nAn analysis of the effectiveness of the assistance provided to absent uniformed services voters by Voting Assistance Officers of the Federal Voting Assistance Program of the Department of Defense.\n**(E)**\nA review of the extent of coordination between Voting Assistance Officers and State and local election officials.\n**(F)**\nInformation regarding such other issues relating to the ability of absent uniformed services voters to register to vote, vote, and have their ballots counted in elections for Federal office.\n**(G)**\nData and information pertaining to\u2014\n**(i)**\nthe awareness of members of the Armed Forces and their family members of the requirement under section 1566a of title 10, United States Code, that the Secretaries of the military departments provide voter registration information and assistance; and\n**(ii)**\nwhether members of the Armed Forces and their family members received such information and assistance at the times required by subsection (c) of that section.\n**(2) Study**\nThe study required by subsection (a)(2) shall include the following:\n**(A)**\nAn assessment of potential actions to be undertaken by the Secretary of each military department to increase access to voter registration information and assistance for members of the Armed Forces and their family members.\n**(B)**\nAn estimate of the costs and requirements to fully meet the needs of members of the Armed Forces for access to voter registration information and assistance.\n##### (c) Methods\nIn conducting the analysis and study required by subsection (a), the Comptroller General shall, in cooperation and consultation with the Secretaries of the military departments\u2014\n**(1)**\nuse existing information from available government and other public sources; and\n**(2)**\nacquire, through the Comptroller General\u2019s own investigations, interviews, and analysis, such other information as the Comptroller General requires to conduct the analysis and study.\n##### (d) Report required\nNot later than September 30, 2027, the Comptroller General shall submit to the Committee on Rules and Administration of the Senate and the Committee on House Administration of the House of Representatives a report on the analysis and study required by subsection (a).\n##### (e) Definitions\nIn this section:\n**(1) Absent uniformed services voter**\nThe term absent uniformed services voter has the meaning given that term in section 107 of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20310 ).\n**(2) Family member**\nThe term family member , with respect to a member of the Armed Forces, means a spouse and other dependent (as defined in section 1072 of title 10, United States Code) of the member.",
      "versionDate": "2025-07-21",
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
        "updateDate": "2025-08-07T16:29:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-21",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr4567",
          "measure-number": "4567",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-21",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4567v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Supporting Military Voters Act</b></p> <p>This bill requires the Government Accountability Office (GAO) to study and report on access to voting for uniformed services voters.</p> <p>Specifically, the GAO must</p> <ul> <li>analyze the effectiveness of the federal government in carrying out the Uniformed and Overseas Citizens Absentee Voting Act to promote access to voting for absent uniformed services voters, and</li> <li>study ways to improve access to voter registration information and assistance for members of the Armed Forces and their family members.</li> </ul>"
        },
        "title": "Supporting Military Voters Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4567.xml",
    "summary": {
      "actionDate": "2025-07-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Supporting Military Voters Act</b></p> <p>This bill requires the Government Accountability Office (GAO) to study and report on access to voting for uniformed services voters.</p> <p>Specifically, the GAO must</p> <ul> <li>analyze the effectiveness of the federal government in carrying out the Uniformed and Overseas Citizens Absentee Voting Act to promote access to voting for absent uniformed services voters, and</li> <li>study ways to improve access to voter registration information and assistance for members of the Armed Forces and their family members.</li> </ul>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4567"
    },
    "title": "Supporting Military Voters Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Supporting Military Voters Act</b></p> <p>This bill requires the Government Accountability Office (GAO) to study and report on access to voting for uniformed services voters.</p> <p>Specifically, the GAO must</p> <ul> <li>analyze the effectiveness of the federal government in carrying out the Uniformed and Overseas Citizens Absentee Voting Act to promote access to voting for absent uniformed services voters, and</li> <li>study ways to improve access to voter registration information and assistance for members of the Armed Forces and their family members.</li> </ul>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4567"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4567ih.xml"
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
      "title": "Supporting Military Voters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Military Voters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to conduct a study of the effectiveness of the Federal Government in carrying out its responsibilities under the Uniformed and Overseas Citizens Absentee Voting Act to promote access to voting for absent uniformed services voters and an analysis of means for improving access to voter registration information and assistance for members of the Armed Forces and their family members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:34Z"
    }
  ]
}
```
