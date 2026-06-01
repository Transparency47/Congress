# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/88?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/88
- Title: No Budget, No Pay Act
- Congress: 119
- Bill type: S
- Bill number: 88
- Origin chamber: Senate
- Introduced date: 2025-01-14
- Update date: 2025-12-05T21:36:09Z
- Update date including text: 2025-12-05T21:36:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in Senate
- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-14: Introduced in Senate

## Actions

- 2025-01-14 - IntroReferral: Introduced in Senate
- 2025-01-14 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/88",
    "number": "88",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No Budget, No Pay Act",
    "type": "S",
    "updateDate": "2025-12-05T21:36:09Z",
    "updateDateIncludingText": "2025-12-05T21:36:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T19:57:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "NV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MT"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "MO"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MT"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "OH"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "WV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-15",
      "state": "FL"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s88is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 88\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2025 Mr. Scott of Florida (for himself, Ms. Rosen , Mrs. Blackburn , Mrs. Britt , Mr. Budd , Mr. Cruz , Mr. Daines , and Mr. Schmitt ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.\n#### 1. Short title\nThis Act may be cited as the No Budget, No Pay Act .\n#### 2. Definitions\nIn this Act\u2014\n**(1)**\nthe term Budget and Appropriations Chairs means the House Budget and Appropriations Chairs and the Senate Budget and Appropriations Chairs;\n**(2)**\nthe term House Budget and Appropriations Chairs means the Chair of the Committee on the Budget of the House of Representatives and the Chair of the Committee on Appropriations of the House of Representatives;\n**(3)**\nthe term Member of Congress \u2014\n**(A)**\nhas the meaning given that term under section 2106 of title 5, United States Code; and\n**(B)**\ndoes not include the Vice President; and\n**(4)**\nthe term Senate Budget and Appropriations Chairs means the Chairman of the Committee on the Budget of the Senate and the Chairman of the Committee on Appropriations of the Senate.\n#### 3. Timely approval of concurrent resolution on the budget and the appropriations bills\nNot later than October 1 of each fiscal year, both Houses of Congress shall\u2014\n**(1)**\napprove a concurrent resolution on the budget as described under section 301 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 632 ) for that the fiscal year; and\n**(2)**\npass all the regular appropriations bills for that fiscal year.\n#### 4. No pay without concurrent resolution on the budget and the appropriations bills\n##### (a) In general\nNotwithstanding any other provision of law, no funds may be appropriated or otherwise be made available from the Treasury of the United States for the pay of any Member of Congress with respect to any period during which Congress is not in compliance with section 3, as determined by the Budget and Appropriations Chairs under section 5.\n##### (b) No retroactive pay\nA Member of Congress may not receive pay with respect to any period during which Congress was not in compliance with section 3, as determined by the Budget and Appropriations Chairs under section 5, at any time after the end of that period.\n#### 5. Determinations\n##### (a) Senate\n**(1) Request for certifications**\nOn October 1 of each year, the Secretary of the Senate shall submit to the Senate Budget and Appropriations Chairs a request for certification of determinations made under subparagraphs (A) and (B) of paragraph (2).\n**(2) Determinations**\nThe Senate Budget and Appropriations Chairs shall\u2014\n**(A)**\non October 1 of each fiscal year, make a determination of whether Congress is in compliance with section 3 with respect to that fiscal year and whether Senators may not be paid under section 4;\n**(B)**\ndetermine the period of days following each October 1 that Senators may not be paid under section 4; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Secretary of the Senate.\n##### (b) House of Representatives\n**(1) Request for certifications**\nOn October 1 of each fiscal year, the Chief Administrative Officer of the House of Representatives shall submit to the House Budget and Appropriations Chairs a request for certification of determinations made under subparagraphs (A) and (B) of paragraph (2).\n**(2) Determinations**\nThe House Budget and Appropriations Chairs shall\u2014\n**(A)**\non October 1 of each fiscal year, make a determination of whether Congress is in compliance with section 3 with respect to that fiscal year and whether Members of the House of Representatives may not be paid under section 4;\n**(B)**\ndetermine the period of days following each October 1 that Members of the House of Representatives may not be paid under section 4; and\n**(C)**\nprovide timely certification of the determinations under subparagraphs (A) and (B) upon the request of the Chief Administrative Officer of the House of Representatives.\n#### 6. Effective date\nThis Act shall take effect on September 29, 2027.",
      "versionDate": "2025-01-14",
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
        "actionDate": "2025-10-10",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "5738",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Budget, No Pay Act",
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
            "name": "Appropriations",
            "updateDate": "2025-03-03T19:07:55Z"
          },
          {
            "name": "Budget process",
            "updateDate": "2025-03-03T19:07:55Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-03T19:07:55Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-03T19:07:55Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-03T19:07:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-28T15:54:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119s88",
          "measure-number": "88",
          "measure-type": "s",
          "orig-publish-date": "2025-01-14",
          "originChamber": "SENATE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s88v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>"
        },
        "title": "No Budget, No Pay Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s88.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s88"
    },
    "title": "No Budget, No Pay Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>No Budget, No Pay Act</strong></p><p>This bill prohibits Members of Congress from being paid in a fiscal year until both chambers approve the budget resolution and pass all regular appropriations bills for that fiscal year. Retroactive pay is prohibited for such a period.</p><p>This bill takes\u00a0effect on\u00a0September 29, 2027.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119s88"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s88is.xml"
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
      "title": "No Budget, No Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Budget, No Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that Members of Congress may not receive pay after October 1 of any fiscal year in which Congress has not approved a concurrent resolution on the budget and passed the regular appropriations bills.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:38Z"
    }
  ]
}
```
