# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/4?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/4
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to "Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters".
- Congress: 119
- Bill type: SJRES
- Bill number: 4
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:52:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-02-12 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 12.
- 2025-02-12 - Discharge: Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2025-02-12 - Committee: Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-02-12 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 12.
- 2025-02-12 - Discharge: Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2025-02-12 - Committee: Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/4",
    "number": "4",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\".",
    "type": "SJRES",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:52:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 12.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Energy and Natural Resources discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
            "date": "2025-02-12T20:30:08Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-23T16:03:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "LA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "LA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SC"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "IN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AK"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-30",
      "state": "UT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres4is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 4\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cruz (for himself, Mr. Scott of Florida , Mr. Cassidy , Mr. Kennedy , Mr. Sheehy , Mrs. Hyde-Smith , Mr. Risch , Mr. Crapo , Mr. Scott of South Carolina , Mr. Wicker , Mr. Banks , and Mr. Sullivan ) introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters .\nThat Congress disapproves the rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters (89 Fed. Reg. 105188 (December 26, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-01-23",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres4pcs.xml",
      "text": "IIA\nCalendar No. 12\n119th CONGRESS\n1st Session\nS. J. RES. 4\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cruz (for himself, Mr. Scott of Florida , Mr. Cassidy , Mr. Kennedy , Mr. Sheehy , Mrs. Hyde-Smith , Mr. Risch , Mr. Crapo , Mr. Scott of South Carolina , Mr. Wicker , Mr. Banks , Mr. Sullivan , Mr. Lee , Mr. Justice , and Mrs. Capito ) introduced the following joint resolution; which was read twice and referred to the Committee on Energy and Natural Resources\nFebruary 12, 2025 Committee discharged, by petition, pursuant to 5 U.S.C. 802(c) , and placed on the calendar\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters .\nThat Congress disapproves the rule submitted by the Department of Energy relating to Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters (89 Fed. Reg. 105188 (December 26, 2024)), and such rule shall have no force or effect.",
      "versionDate": "2025-02-12",
      "versionType": "PCS"
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
        "actionDate": "2025-05-09",
        "text": "Became Public Law No: 119-6."
      },
      "number": "20",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\".",
      "type": "HJRES"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-26T20:31:25Z"
          },
          {
            "name": "Department of Energy",
            "updateDate": "2025-02-26T20:31:25Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-02-26T20:31:25Z"
          },
          {
            "name": "Lighting, heating, cooling",
            "updateDate": "2025-02-26T20:31:25Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-02-26T20:31:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-01-27T14:02:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119sjres4",
          "measure-number": "4",
          "measure-type": "sjres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-01-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sjres4v00",
            "update-date": "2025-01-27"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This joint resolution nullifies the rule titled <em>Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters </em>and submitted by the Department of Energy (DOE) on December 26, 2024. Under the rule, DOE adopted amended energy conservation standards for gas-fired instantaneous water heaters to achieve the maximum improvement in energy efficiency that DOE determined was technologically feasible and economically justified.</p>"
        },
        "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sjres/BILLSUM-119sjres4.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the rule titled <em>Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters </em>and submitted by the Department of Energy (DOE) on December 26, 2024. Under the rule, DOE adopted amended energy conservation standards for gas-fired instantaneous water heaters to achieve the maximum improvement in energy efficiency that DOE determined was technologically feasible and economically justified.</p>",
      "updateDate": "2025-01-27",
      "versionCode": "id119sjres4"
    },
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This joint resolution nullifies the rule titled <em>Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters </em>and submitted by the Department of Energy (DOE) on December 26, 2024. Under the rule, DOE adopted amended energy conservation standards for gas-fired instantaneous water heaters to achieve the maximum improvement in energy efficiency that DOE determined was technologically feasible and economically justified.</p>",
      "updateDate": "2025-01-27",
      "versionCode": "id119sjres4"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres4is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres4pcs.xml"
        }
      ],
      "type": "PCS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-25T05:03:29Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Energy relating to \"Energy Conservation Program: Energy Conservation Standards for Consumer Gas-fired Instantaneous Water Heaters\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T11:56:31Z"
    }
  ]
}
```
