# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1043?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1043
- Title: A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property.
- Congress: 119
- Bill type: S
- Bill number: 1043
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-07-17T16:30:59Z
- Update date including text: 2025-07-17T16:30:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1043",
    "number": "1043",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property.",
    "type": "S",
    "updateDate": "2025-07-17T16:30:59Z",
    "updateDateIncludingText": "2025-07-17T16:30:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
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
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T18:38:54Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "CT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1043is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1043\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Graham (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property.\n#### 1. Extension of energy credit for qualified fuel cell property\n##### (a) In general\nSection 48(c)(1)(E) of the Internal Revenue Code of 1986 is amended by striking January 1, 2025 and inserting January 1, 2033 .\n##### (b) Effective date\nThe amendments made by this section shall apply to property the construction of which begins after December 31, 2024.",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1752",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Technology for Energy Security Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-08T19:17:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1043",
          "measure-number": "1043",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-07-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1043v00",
            "update-date": "2025-07-17"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill extends the energy investment tax credit for qualified fuel cell property for eight years.</p><p>Under current law, an energy investment tax credit of up to 30% of the cost of qualified fuel cell property is available provided construction of the qualified fuel cell property begins on or before December 31, 2024. This bill extends the energy investment tax credit to include qualified fuel cell property where construction begins on or before December 31, 2032.</p>"
        },
        "title": "A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1043.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends the energy investment tax credit for qualified fuel cell property for eight years.</p><p>Under current law, an energy investment tax credit of up to 30% of the cost of qualified fuel cell property is available provided construction of the qualified fuel cell property begins on or before December 31, 2024. This bill extends the energy investment tax credit to include qualified fuel cell property where construction begins on or before December 31, 2032.</p>",
      "updateDate": "2025-07-17",
      "versionCode": "id119s1043"
    },
    "title": "A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property."
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill extends the energy investment tax credit for qualified fuel cell property for eight years.</p><p>Under current law, an energy investment tax credit of up to 30% of the cost of qualified fuel cell property is available provided construction of the qualified fuel cell property begins on or before December 31, 2024. This bill extends the energy investment tax credit to include qualified fuel cell property where construction begins on or before December 31, 2032.</p>",
      "updateDate": "2025-07-17",
      "versionCode": "id119s1043"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1043is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:18:36Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the energy credit for qualified fuel cell property.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T10:56:26Z"
    }
  ]
}
```
