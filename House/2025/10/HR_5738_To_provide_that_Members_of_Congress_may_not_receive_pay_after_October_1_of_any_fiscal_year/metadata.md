# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5738
- Title: No Budget, No Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 5738
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-12-05T21:36:05Z
- Update date including text: 2025-12-05T21:36:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5738",
    "number": "5738",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001236",
        "district": "14",
        "firstName": "Tim",
        "fullName": "Rep. Moore, Tim [R-NC-14]",
        "lastName": "Moore",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Budget, No Pay Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:36:05Z",
    "updateDateIncludingText": "2025-12-05T21:36:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:30:05Z",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "MO"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "IA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "WI"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5738ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5738\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mr. Moore of North Carolina (for himself, Ms. Malliotakis , Mr. Onder , and Mrs. Miller-Meeks ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.\n#### 1. Short title\nThis Act may be cited as the No Budget, No Pay Act .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term Budget and Appropriations Chairs means the House Budget and Appropriations Chairs and the Senate Budget and Appropriations Chairs;\n**(2)**\nthe term House Budget and Appropriations Chairs means the Chair of the Committee on the Budget of the House of Representatives and the Chair of the Committee on Appropriations of the House of Representatives;\n**(3)**\nthe term Member of Congress \u2014\n**(A)**\nhas the meaning given that term under section 2106 of title 5, United States Code; and\n**(B)**\ndoes not include the Vice President; and\n**(4)**\nthe term Senate Budget and Appropriations Chairs means the Chairman of the Committee on the Budget of the Senate and the Chairman of the Committee on Appropriations of the Senate.\n#### 3. Timely approval of concurrent resolution on the budget and the appropriations bills\nNot later than October 1 of each fiscal year, both Houses of Congress shall\u2014\n**(1)**\napprove a concurrent resolution on the budget as described under section 301 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 632 ) for that fiscal year; and\n**(2)**\npass all the regular appropriations bills for that fiscal year.\n#### 4. No pay without concurrent resolution on the budget and the appropriations bills\n##### (a) In general\nNotwithstanding any other provision of law, no funds may be appropriated or otherwise be made available from the Treasury of the United States for the pay of any Member of Congress with respect to any period during which Congress is not in compliance with section 3, as determined by the Budget and Appropriations Chairs under section 5.\n##### (b) No retroactive pay\nA Member of Congress may not receive pay with respect to any period during which Congress was not in compliance with section 3, as determined by the Budget and Appropriations Chairs under section 5, at any time after the end of that period.\n#### 5. Determinations\n##### (a) Senate\n**(1) Request for certifications**\nOn October 1 of each year, the Secretary of the Senate shall submit to the Senate Budget and Appropriations Chairs a request for certification of determinations made under subparagraphs (A) and (B) of paragraph (2).\n**(2) Determinations**\nThe Senate Budget and Appropriations Chairs shall\u2014\n**(A)**\non October 1 of each fiscal year, make a determination of whether Congress is in compliance with section 3 with respect to that fiscal year and whether Senators may not be paid under section 4;\n**(B)**\ndetermine the period of days following each October 1 that Senators may not be paid under section 4; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Secretary of the Senate.\n##### (b) House of Representatives\n**(1) Request for certifications**\nOn October 1 of each fiscal year, the Chief Administrative Officer of the House of Representatives shall submit to the House Budget and Appropriations Chairs a request for certification of determinations made under subparagraphs (A) and (B) of paragraph (2).\n**(2) Determinations**\nThe House Budget and Appropriations Chairs shall\u2014\n**(A)**\non October 1 of each fiscal year, make a determination of whether Congress is in compliance with section 3 with respect to that fiscal year and whether Members of the House of Representatives may not be paid under section 4;\n**(B)**\ndetermine the period of days following each October 1 that Members of the House of Representatives may not be paid under section 4; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Chief Administrative Officer of the House of Representatives.\n#### 6. Effective date\nThis Act shall take effect on September 29, 2027.",
      "versionDate": "2025-10-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-14",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "88",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Budget, No Pay Act",
      "type": "S"
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
        "name": "Congress",
        "updateDate": "2025-10-21T12:41:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-10",
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
          "measure-id": "id119hr5738",
          "measure-number": "5738",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-10",
          "originChamber": "HOUSE",
          "update-date": "2025-10-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5738v00",
            "update-date": "2025-10-21"
          },
          "action-date": "2025-10-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>"
        },
        "title": "No Budget, No Pay Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5738.xml",
    "summary": {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5738"
    },
    "title": "No Budget, No Pay Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>",
      "updateDate": "2025-10-21",
      "versionCode": "id119hr5738"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5738ih.xml"
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
      "title": "No Budget, No Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Budget, No Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:12Z"
    }
  ]
}
```
