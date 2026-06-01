# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4460?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4460
- Title: Rural Community Hospital Demonstration Program Reauthorization
- Congress: 119
- Bill type: S
- Bill number: 4460
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-27T11:21:00Z
- Update date including text: 2026-05-27T11:21:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2428; text: CR S2428)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-05-21 - Floor: Message on Senate action sent to the House.
- 2026-05-21 15:18:43 - Floor: Received in the House.
- 2026-05-21 15:30:43 - Floor: Held at the desk.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-05-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S2428; text: CR S2428)
- 2026-05-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-05-20 - Discharge: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-05-20 - Committee: Senate Committee on Finance discharged by Unanimous Consent.
- 2026-05-21 - Floor: Message on Senate action sent to the House.
- 2026-05-21 15:18:43 - Floor: Received in the House.
- 2026-05-21 15:30:43 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4460",
    "number": "4460",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Rural Community Hospital Demonstration Program Reauthorization",
    "type": "S",
    "updateDate": "2026-05-27T11:21:00Z",
    "updateDateIncludingText": "2026-05-27T11:21:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-21",
      "actionTime": "15:30:43",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-21",
      "actionTime": "15:18:43",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-21",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S2428; text: CR S2428)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Finance discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
        "item": [
          {
            "date": "2026-05-20T22:04:53Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-30T17:54:32Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CO"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "ID"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AK"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NM"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MS"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VT"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "KS"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-30",
      "state": "ME"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AK"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OR"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NM"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "OK"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "CO"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4460is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4460\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Grassley (for himself, Mr. Bennet , Mr. Crapo , Mr. Wyden , Mr. Sullivan , Mr. Luj\u00e1n , Mrs. Hyde-Smith , Mr. Welch , Mr. Moran , Mr. King , Ms. Murkowski , Mr. Merkley , Mr. Ricketts , Mr. Heinrich , Mr. Lankford , and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for an extension of the rural community hospital demonstration program.\n#### 1. Short title\nThis Act may be cited as the Rural Community Hospital Demonstration Program Reauthorization .\n#### 2. Five-year extension of the rural community hospital demonstration program\n##### (a) In general\nSubsection (a)(5) of section 410A of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( Public Law 108\u2013173 ; 42 U.S.C. 1395ww note), is amended by striking 15-year extension period and inserting 20-year extension period .\n##### (b) Conforming amendments for extension\n**(1) Extension of demonstration period**\nSubsection (g) of such section 410A is amended\u2014\n**(A)**\nin the subsection heading, by striking Fifteen-Year and inserting Twenty-Year ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking additional 15-year and inserting additional 20-year ; and\n**(ii)**\nby striking 15-year extension period and inserting 20-year extension period ;\n**(C)**\nin paragraph (2), by striking 15-year extension period and inserting 20-year extension period ;\n**(D)**\nin paragraph (3), by striking 15-year extension period and inserting 20-year extension period ;\n**(E)**\nin paragraph (4), by striking 15-year extension period each place it appears and inserting 20-year extension period ;\n**(F)**\nin paragraph (5), by striking 15-year extension period each place it appears and inserting 20-year extension period ; and\n**(G)**\nin subparagraph (A) of paragraph (6), by striking 15-year extension period and inserting 20-year extension period .\n**(2) Rule for hospitals that are not original participants in the demonstration**\nParagraph (5) of subsection (g) of such section 410A is amended\u2014\n**(A)**\nin subparagraph (B), by striking Additional extension and inserting CAA, 2021 extension ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(C) Additional extension During the fourth 5 years of the 20-year extension period, the Secretary shall apply the provisions of paragraph (4) to rural community hospitals that are not described in paragraph (4) but are participating in the demonstration program under this section at any time during the period beginning on December 30, 2024, and ending on January 1, 2027, in a similar manner as such provisions apply to rural community hospitals described in paragraph (4). .",
      "versionDate": "2026-04-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4460es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 4460\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo provide for an extension of the rural community hospital demonstration program.\n#### 1. Short title\nThis Act may be cited as the Rural Community Hospital Demonstration Program Reauthorization .\n#### 2. Five-year extension of the rural community hospital demonstration program\n##### (a) In general\nSubsection (a)(5) of section 410A of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( Public Law 108\u2013173 ; 42 U.S.C. 1395ww note), is amended by striking 15-year extension period and inserting 20-year extension period .\n##### (b) Conforming amendments for extension\n**(1) Extension of demonstration period**\nSubsection (g) of such section 410A is amended\u2014\n**(A)**\nin the subsection heading, by striking Fifteen-Year and inserting Twenty-Year ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking additional 15-year and inserting additional 20-year ; and\n**(ii)**\nby striking 15-year extension period and inserting 20-year extension period ;\n**(C)**\nin paragraph (2), by striking 15-year extension period and inserting 20-year extension period ;\n**(D)**\nin paragraph (3), by striking 15-year extension period and inserting 20-year extension period ;\n**(E)**\nin paragraph (4), by striking 15-year extension period each place it appears and inserting 20-year extension period ;\n**(F)**\nin paragraph (5), by striking 15-year extension period each place it appears and inserting 20-year extension period ; and\n**(G)**\nin subparagraph (A) of paragraph (6), by striking 15-year extension period and inserting 20-year extension period .\n**(2) Rule for hospitals that are not original participants in the demonstration**\nParagraph (5) of subsection (g) of such section 410A is amended\u2014\n**(A)**\nin subparagraph (B), by striking Additional extension and inserting CAA, 2021 extension ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(C) Additional extension During the fourth 5 years of the 20-year extension period, the Secretary shall apply the provisions of paragraph (4) to rural community hospitals that are not described in paragraph (4) but are participating in the demonstration program under this section at any time during the period beginning on December 30, 2024, and ending on January 1, 2027, in a similar manner as such provisions apply to rural community hospitals described in paragraph (4). .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Health care costs and insurance",
            "updateDate": "2026-05-22T19:15:26Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-05-22T19:15:31Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2026-05-22T19:15:14Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2026-05-22T19:15:36Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2026-05-22T19:15:22Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-05-22T19:15:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-21T15:06:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-30",
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
          "measure-id": "id119s4460",
          "measure-number": "4460",
          "measure-type": "s",
          "orig-publish-date": "2026-04-30",
          "originChamber": "SENATE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4460v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2026-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Community Hospital Demonstration Program Reauthorization</strong></p><p>This bill extends the Rural Community Hospital Demonstration Program for an additional five years. The\u00a0program tests the feasibility of cost-based reimbursement under Medicare for small rural hospitals that are too large to qualify for special payment as critical access hospitals.</p><p>The bill specifies that hospitals that participate in the program between December 30, 2024, and January 1, 2027, may continue to participate during the five-year extension period.</p>"
        },
        "title": "Rural Community Hospital Demonstration Program Reauthorization"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4460.xml",
    "summary": {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Community Hospital Demonstration Program Reauthorization</strong></p><p>This bill extends the Rural Community Hospital Demonstration Program for an additional five years. The\u00a0program tests the feasibility of cost-based reimbursement under Medicare for small rural hospitals that are too large to qualify for special payment as critical access hospitals.</p><p>The bill specifies that hospitals that participate in the program between December 30, 2024, and January 1, 2027, may continue to participate during the five-year extension period.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s4460"
    },
    "title": "Rural Community Hospital Demonstration Program Reauthorization"
  },
  "summaries": [
    {
      "actionDate": "2026-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Community Hospital Demonstration Program Reauthorization</strong></p><p>This bill extends the Rural Community Hospital Demonstration Program for an additional five years. The\u00a0program tests the feasibility of cost-based reimbursement under Medicare for small rural hospitals that are too large to qualify for special payment as critical access hospitals.</p><p>The bill specifies that hospitals that participate in the program between December 30, 2024, and January 1, 2027, may continue to participate during the five-year extension period.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119s4460"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4460is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4460es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Rural Community Hospital Demonstration Program Reauthorization",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Rural Community Hospital Demonstration Program Reauthorization",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-22T02:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Community Hospital Demonstration Program Reauthorization",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for an extension of the rural community hospital demonstration program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:38Z"
    }
  ]
}
```
