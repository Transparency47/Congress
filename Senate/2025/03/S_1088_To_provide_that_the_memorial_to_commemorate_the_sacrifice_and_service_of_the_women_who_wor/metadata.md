# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1088?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1088
- Title: World War II Women's Memorial Location Act
- Congress: 119
- Bill type: S
- Bill number: 1088
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-04-23T19:42:35Z
- Update date including text: 2026-04-23T19:42:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1088",
    "number": "1088",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "World War II Women's Memorial Location Act",
    "type": "S",
    "updateDate": "2026-04-23T19:42:35Z",
    "updateDateIncludingText": "2026-04-23T19:42:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T20:19:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-09T18:12:53Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-09T18:12:53Z",
                "name": "Hearings By (subcommittee)"
              }
            ]
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "TN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MD"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "FL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-23",
      "state": "PA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1088is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1088\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mrs. Shaheen (for herself, Mrs. Blackburn , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide that the memorial to commemorate the sacrifice and service of the women who worked on the home front to support the efforts of the United States military during World War II may be located on the National Mall, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the World War II Women's Memorial Location Act .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nduring World War II, more than 18,000,000 women answered the call during a global crisis to hold down the home front by working as pilots, engineers, mechanics, code breakers, and more, building planes, tanks, munitions, and other equipment needed by United States troops, and serving as the backbone of the war effort;\n**(2)**\nsection 702 of division DD of the Consolidated Appropriations Act, 2023 ( 40 U.S.C. 8903 note; Public Law 117\u2013328 ), authorized the World War II Women\u2019s Memorial Foundation (formerly known as the Women Who Worked on the Home Front Foundation ) to establish a commemorative work on Federal land in the District of Columbia and its environs to commemorate the service and sacrifice to the United States of the women who worked on the home front during World War II; and\n**(3)**\nlocating the commemorative work described in paragraph (2) on the National Mall would be a respectful extension of the enduring legacy of the women who worked on the home front during World War II.\n#### 3. Location of commemorative work\nNotwithstanding section 8908 of title 40, United States Code, the commemorative work to commemorate the commitment and service of the women who worked on the home front during World War II authorized by section 702 of division DD of the Consolidated Appropriations Act, 2023 ( 40 U.S.C. 8903 note; Public Law 117\u2013328 ), may be located within\u2014\n**(1)**\nArea I, as depicted on the map entitled Commemorative Areas Washington, DC and Environs , numbered 869/86501 B, and dated June 24, 2003; or\n**(2)**\nthe Reserve (as defined in section 8902(a) of title 40, United States Code).",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-10",
        "text": "Received in the Senate and Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "2290",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "World War II Women's Memorial Location Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "District of Columbia",
            "updateDate": "2025-07-24T14:00:52Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-07-24T14:00:52Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-07-24T14:00:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-02T15:45:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
    "originChamber": "Senate",
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
          "measure-id": "id119s1088",
          "measure-number": "1088",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2026-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1088v00",
            "update-date": "2026-04-23"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>World War II Women's Memorial Location Act</strong></p><p>This bill allows the commemorative work for women who worked on the home front during World War II to be located in either (1) the Reserve, an area that generally extends from the United States Capitol to the Lincoln Memorial, and from the White House to the Jefferson Memorial; or (2) the area just outside the Reserve, known as Area I. (This <a href=\"https://www.ncpc.gov/maps/the-reserve/\">map</a> shows the Reserve in red and Area I in yellow.)</p>"
        },
        "title": "World War II Women's Memorial Location Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1088.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>World War II Women's Memorial Location Act</strong></p><p>This bill allows the commemorative work for women who worked on the home front during World War II to be located in either (1) the Reserve, an area that generally extends from the United States Capitol to the Lincoln Memorial, and from the White House to the Jefferson Memorial; or (2) the area just outside the Reserve, known as Area I. (This <a href=\"https://www.ncpc.gov/maps/the-reserve/\">map</a> shows the Reserve in red and Area I in yellow.)</p>",
      "updateDate": "2026-04-23",
      "versionCode": "id119s1088"
    },
    "title": "World War II Women's Memorial Location Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>World War II Women's Memorial Location Act</strong></p><p>This bill allows the commemorative work for women who worked on the home front during World War II to be located in either (1) the Reserve, an area that generally extends from the United States Capitol to the Lincoln Memorial, and from the White House to the Jefferson Memorial; or (2) the area just outside the Reserve, known as Area I. (This <a href=\"https://www.ncpc.gov/maps/the-reserve/\">map</a> shows the Reserve in red and Area I in yellow.)</p>",
      "updateDate": "2026-04-23",
      "versionCode": "id119s1088"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1088is.xml"
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
      "title": "World War II Women's Memorial Location Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "World War II Women's Memorial Location Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that the memorial to commemorate the sacrifice and service of the women who worked on the home front to support the efforts of the United States military during World War II may be located on the National Mall, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:17Z"
    }
  ]
}
```
