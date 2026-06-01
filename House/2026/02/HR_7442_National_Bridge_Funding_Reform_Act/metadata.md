# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7442
- Title: National Bridge Funding Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 7442
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-25T09:06:33Z
- Update date including text: 2026-02-25T09:06:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7442",
    "number": "7442",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "National Bridge Funding Reform Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:33Z",
    "updateDateIncludingText": "2026-02-25T09:06:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7442ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7442\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Nehls (for himself, Mr. Weber of Texas , Mr. Williams of Texas , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo eliminate the Carbon Reduction Program and PROTECT Program and dedicate the funding to a new bridge formula program that distributes funding based primarily on overall deck area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Bridge Funding Reform Act .\n#### 2. National bridge program and program elimination\n##### (a) Apportionment\nSection 104 of title 23, United States Code, is amended\u2014\n**(1)**\nby striking subsection (b)(7) and subsection (b)(8); and\n**(2)**\nby inserting in its place the following:\n(7) National bridge program For the national bridge program under section 175, 5.47660865256628 percent of the amount remaining after distributing amounts under paragraphs (4), (5), and (6). .\n##### (b) Carbon reduction program\nChapter 1 of title 23, United States Code, is amended by striking Section 175.\n##### (c) Promoting resilient operations for transformative, efficient, and cost-Saving transportation (PROTECT) program\nChapter 1 of title 23, United States Code, is amended by striking Section 176.\n##### (d) In general\nTitle 23, United States Code, is amended by inserting after section 175 the following:\n175. National bridge program (a) Establishment The Secretary shall establish and implement a national bridge program under this section. (b) Purposes The purpose of the national bridge program shall be to provide support for the replacement, rehabilitation, preservation, protection, and construction of bridges on Federal-aid highways and for other purposes. (c) Eligible projects (1) In general Funds apportioned to a State to carry out the national bridge program may be obligated for the replacement, rehabilitation, preservation, protection, and construction of bridges on Federal-aid highways. (2) Flexibility At the discretion of each State, funds made available for the national bridge program may be obligated for the replacement, rehabilitation, preservation, protection, and construction of bridges not on Federal-aid highways. (d) Apportionment The Secretary shall distribute the funds apportioned under section 104(b)(7) to carry out this section among States as follows\u2014 (1) 75 percent by the proportion that the total deck area of bridges on Federal-aid highways in such State bears to the sum of the total deck area of bridges on Federal-aid highways in all States; and (2) 25 percent by the proportion that the total deck area of bridges on Federal-aid highways classified as in poor condition in such State bears to the sum of the total deck area of bridges on Federal-aid highways classified as being in poor condition in all States. (e) National bridge inventory For purposes of determining the distribution of funds to States under subsection (d), the Secretary shall calculate the total deck area of bridges and the total deck area of bridges classified as being in poor condition based on the National Bridge Inventory as of December 31, 2024. .\n##### (e) Conforming amendments\n**(1)**\nSection 104 of title 23, United States Code, is amended\u2014\n**(A)**\nin subsection (b)\u2014\n**(i)**\nin the matter preceding paragraph (1), by striking the carbon reduction program under section 175, to carry out subsection (c) of the PROTECT program under section 176, ; and\n**(ii)**\nby striking paragraphs (7) and (8);\n**(B)**\nin subsection (c)(2) by striking the carbon reduction program under section 175, to carry out subsection (c) of the PROTECT program under section 176, ; and\n**(C)**\nin subsection (h) by striking the carbon reduction program under section 175, to carry out subsection (c) of the PROTECT program under section 176, .\n**(2)**\nSection 120(l)(2)(A) of title 23, United States Code, is amended by striking clauses (vi) and (vii).\n**(3)**\nSection 520(e)(3)(B) of title 23, United States Code, is amended by striking clause (ii).\n##### (f) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended\u2014\n**(1)**\nby striking the items relating to section 175 and section 176 in effect prior to enactment of this section; and\n**(2)**\nby inserting after the item relating to section 174 the following:\n175. National bridge program. .",
      "versionDate": "2026-02-09",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-19T16:47:45Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7442ih.xml"
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
      "title": "National Bridge Funding Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Bridge Funding Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To eliminate the Carbon Reduction Program and PROTECT Program and dedicate the funding to a new bridge formula program that distributes funding based primarily on overall deck area, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T04:18:23Z"
    }
  ]
}
```
