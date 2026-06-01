# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/289
- Title: Youth Poisoning Protection Act
- Congress: 119
- Bill type: S
- Bill number: 289
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-02-04T04:11:38Z
- Update date including text: 2026-02-04T04:11:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 132.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.
- 2025-07-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.
- 2025-07-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 132.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/289",
    "number": "289",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000622",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Duckworth, Tammy [D-IL]",
        "lastName": "Duckworth",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Youth Poisoning Protection Act",
    "type": "S",
    "updateDate": "2026-02-04T04:11:38Z",
    "updateDateIncludingText": "2026-02-04T04:11:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 132.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-49.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2025-07-29T20:56:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T17:36:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "UT"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "OH"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s289is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 289\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Duckworth (for herself, Mr. Curtis , and Mr. Moreno ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo ban the sale of products with a high concentration of sodium nitrite to individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Youth Poisoning Protection Act .\n#### 2. Banning of products containing a high concentration of sodium nitrite\n##### (a) In general\nAny consumer product containing a high concentration of sodium nitrite shall be considered to be a banned hazardous product under section 8 of the Consumer Product Safety Act ( 15 U.S.C. 2057 ).\n##### (b) Rule of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nprohibit any commercial or industrial purpose in which high concentration sodium nitrite is not customarily produced or distributed for sale to, or use or consumption by, or enjoyment of, a consumer; and\n**(2)**\napply to high concentration sodium nitrite that meets the definition of a drug , device , or cosmetic (as such terms are defined in sections 201(g), (h), and (i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) , (h), and (i))), or food (as defined in section 201(f) of such Act ( 21 U.S.C. 321(f) )), including poultry and poultry products (as such terms are defined in sections 4(e) and (f) of the Poultry Products Inspection Act ( 21 U.S.C. 453(e) and (f))), meat and meat food products (as such terms are defined in section 1(j) of the Federal Meat Inspection Act ( 21 U.S.C. 601(j) )), and eggs and egg products (as such terms are defined in section 4 of the Egg Products Inspection Act ( 21 U.S.C. 1033 )).\n##### (c) Definitions\nFor purposes of this section:\n**(1) Consumer product**\nThe term consumer product has the meaning given that term under section 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ).\n**(2) High concentration of sodium nitrite**\nThe term high concentration of sodium nitrite means a concentration of 10 or more percent by weight of sodium nitrite.\n##### (d) Effective date\nThis section shall take effect 90 days after the date of enactment of this Act.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s289rs.xml",
      "text": "II\nCalendar No. 132\n119th CONGRESS\n1st Session\nS. 289\n[Report No. 119\u201349]\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Duckworth (for herself, Mr. Curtis , Mr. Moreno , and Ms. Baldwin ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nJuly 29, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo ban the sale of products with a high concentration of sodium nitrite to individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Youth Poisoning Protection Act .\n#### 2. Banning of products containing a high concentration of sodium nitrite\n##### (a) In general\nAny consumer product containing a high concentration of sodium nitrite shall be considered to be a banned hazardous product under section 8 of the Consumer Product Safety Act ( 15 U.S.C. 2057 ).\n##### (b) Rule of construction\nNothing in this section shall be construed to\u2014\n**(1)**\nprohibit any commercial or industrial purpose in which high concentration sodium nitrite is not customarily produced or distributed for sale to, or use or consumption by, or enjoyment of, a consumer; and\n**(2)**\napply to high concentration sodium nitrite that meets the definition of a drug , device , or cosmetic (as such terms are defined in sections 201(g), (h), and (i) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) , (h), and (i))), or food (as defined in section 201(f) of such Act ( 21 U.S.C. 321(f) )), including poultry and poultry products (as such terms are defined in sections 4(e) and (f) of the Poultry Products Inspection Act ( 21 U.S.C. 453(e) and (f))), meat and meat food products (as such terms are defined in section 1(j) of the Federal Meat Inspection Act ( 21 U.S.C. 601(j) )), and eggs and egg products (as such terms are defined in section 4 of the Egg Products Inspection Act ( 21 U.S.C. 1033 )).\n##### (c) Definitions\nFor purposes of this section:\n**(1) Consumer product**\nThe term consumer product has the meaning given that term under section 3(a)(5) of the Consumer Product Safety Act ( 15 U.S.C. 2052(a)(5) ).\n**(2) High concentration of sodium nitrite**\nThe term high concentration of sodium nitrite means a concentration of 10 or more percent by weight of sodium nitrite.\n##### (d) Effective date\nThis section shall take effect 90 days after the date of enactment of this Act.",
      "versionDate": "2025-07-29",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-16",
        "text": "Read twice. Placed on Senate Legislative Calendar under General Orders. Calendar No. 116."
      },
      "number": "1442",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Youth Poisoning Protection Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-05-12T18:05:19Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-05-12T18:05:19Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-05-12T18:05:19Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2025-05-12T18:05:19Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-05-12T18:05:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-02T16:04:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s289",
          "measure-number": "289",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s289v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Youth Poisoning Protection Act</strong></p><p>This bill makes a consumer product with a concentration of sodium nitrite of 10% or greater a banned hazardous product.</p><p>The restriction does not apply to specified drugs, medical devices, cosmetics, or food products.</p>"
        },
        "title": "Youth Poisoning Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s289.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Youth Poisoning Protection Act</strong></p><p>This bill makes a consumer product with a concentration of sodium nitrite of 10% or greater a banned hazardous product.</p><p>The restriction does not apply to specified drugs, medical devices, cosmetics, or food products.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s289"
    },
    "title": "Youth Poisoning Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Youth Poisoning Protection Act</strong></p><p>This bill makes a consumer product with a concentration of sodium nitrite of 10% or greater a banned hazardous product.</p><p>The restriction does not apply to specified drugs, medical devices, cosmetics, or food products.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s289"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s289is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s289rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Youth Poisoning Protection Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-07-31T04:23:19Z"
    },
    {
      "title": "Youth Poisoning Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Youth Poisoning Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ban the sale of products with a high concentration of sodium nitrate to individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:22Z"
    }
  ]
}
```
