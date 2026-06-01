# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5398?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5398
- Title: Pay Our Homeland Defenders Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 5398
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2025-10-25T08:05:45Z
- Update date including text: 2025-10-25T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5398",
    "number": "5398",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Pay Our Homeland Defenders Act of 2026",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:45Z",
    "updateDateIncludingText": "2025-10-25T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MN"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "OK"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MI"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "WA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "SC"
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
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IN"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MS"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
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
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MN"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5398ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5398\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Huizenga (for himself, Ms. Boebert , Ms. Tenney , Mrs. Kiggans of Virginia , Mr. Finstad , Mr. Bean of Florida , and Mrs. Bice ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide salary and expenses for Department of Homeland Security personnel during a Government shutdown during fiscal year 2026 or fiscal year 2027, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pay Our Homeland Defenders Act of 2026 .\n#### 2. Continuing appropriations for DHS employees during Government shutdown\n##### (a) In general\nThere are hereby appropriated, out of any money in the Treasury not otherwise appropriated, for any period during which interim or full-year appropriations for fiscal year 2026 or fiscal year 2027 are not in effect such sums as are necessary to provide pay and allowances to\u2014\n**(1)**\nlaw enforcement personnel of the Department of Homeland Security during such period, including any personnel within classification series 0083, 1801, 1802, 1811, 1881, 1895, 1896, or 2181 (or any successor series);\n**(2)**\nany Department of Homeland Security employees or contractors that the Secretary determines are necessary to carry out this subsection, including employees or contractors involved in the administrative, payroll, distribution, accounting, and commercial accounts functions; and\n**(3)**\nmembers, civilian personnel, and contractors of the United States Coast Guard during such period, to the extent not otherwise provided for by law.\n##### (b) Termination\nAppropriations and authority granted pursuant to this Act shall remain available until the earlier of the following:\n**(1)**\nThe enactment into law of an appropriation (including a continuing resolution) for any of the purposes described in subsection (a).\n**(2)**\nThe enactment into law of a regular appropriations bill or continuing resolution without an appropriation for those purposes.\n**(3)**\nJanuary 1, 2027.",
      "versionDate": "2025-09-16",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-09-24T15:35:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-16",
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
          "measure-id": "id119hr5398",
          "measure-number": "5398",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-16",
          "originChamber": "HOUSE",
          "update-date": "2025-10-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5398v00",
            "update-date": "2025-10-01"
          },
          "action-date": "2025-09-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Pay Our Homeland Defenders Act of 2026</strong></p><p>This bill provides continuing appropriations for the salaries of certain Department of Homeland Security (DHS) employees during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown).</p><p>If there is a government shutdown in FY2026 or FY2027, the bill provides continuing appropriations to provide pay and allowances to\u00a0</p><ul><li>DHS law enforcement personnel;</li><li>DHS employees or contractors who are necessary to carry out this bill, including employees or contractors involved in the administrative, payroll, distribution, accounting, and commercial accounts functions; and</li><li>members, civilian personnel, and contractors of the\u00a0U.S. Coast Guard.</li></ul><p>The bill provides the appropriations until the earlier of (1) the enactment of specified appropriations legislation, or (2) January 1, 2027.</p>"
        },
        "title": "Pay Our Homeland Defenders Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5398.xml",
    "summary": {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Our Homeland Defenders Act of 2026</strong></p><p>This bill provides continuing appropriations for the salaries of certain Department of Homeland Security (DHS) employees during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown).</p><p>If there is a government shutdown in FY2026 or FY2027, the bill provides continuing appropriations to provide pay and allowances to\u00a0</p><ul><li>DHS law enforcement personnel;</li><li>DHS employees or contractors who are necessary to carry out this bill, including employees or contractors involved in the administrative, payroll, distribution, accounting, and commercial accounts functions; and</li><li>members, civilian personnel, and contractors of the\u00a0U.S. Coast Guard.</li></ul><p>The bill provides the appropriations until the earlier of (1) the enactment of specified appropriations legislation, or (2) January 1, 2027.</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr5398"
    },
    "title": "Pay Our Homeland Defenders Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Pay Our Homeland Defenders Act of 2026</strong></p><p>This bill provides continuing appropriations for the salaries of certain Department of Homeland Security (DHS) employees during any period in which interim or full-year appropriations for FY2026 or FY2027 are not in effect (i.e., a government shutdown).</p><p>If there is a government shutdown in FY2026 or FY2027, the bill provides continuing appropriations to provide pay and allowances to\u00a0</p><ul><li>DHS law enforcement personnel;</li><li>DHS employees or contractors who are necessary to carry out this bill, including employees or contractors involved in the administrative, payroll, distribution, accounting, and commercial accounts functions; and</li><li>members, civilian personnel, and contractors of the\u00a0U.S. Coast Guard.</li></ul><p>The bill provides the appropriations until the earlier of (1) the enactment of specified appropriations legislation, or (2) January 1, 2027.</p>",
      "updateDate": "2025-10-01",
      "versionCode": "id119hr5398"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5398ih.xml"
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
      "title": "Pay Our Homeland Defenders Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pay Our Homeland Defenders Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide salary and expenses for Department of Homeland Security personnel during a Government shutdown during fiscal year 2026 or fiscal year 2027, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:21Z"
    }
  ]
}
```
