# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4523?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4523
- Title: A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the "Sorensen-Estrada Post Office".
- Congress: 119
- Bill type: S
- Bill number: 4523
- Origin chamber: Senate
- Introduced date: 2026-05-13
- Update date: 2026-05-19T16:54:00Z
- Update date including text: 2026-05-19T16:54:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-05-13: Introduced in Senate
- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-05-13: Introduced in Senate

## Actions

- 2026-05-13 - IntroReferral: Introduced in Senate
- 2026-05-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4523",
    "number": "4523",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
    "type": "S",
    "updateDate": "2026-05-19T16:54:00Z",
    "updateDateIncludingText": "2026-05-19T16:54:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T21:57:48Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4523is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4523\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2026 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the Sorensen-Estrada Post Office .\n#### 1. Sorensen-Estrada Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, shall be known and designated as the Sorensen-Estrada Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Sorensen-Estrada Post Office .",
      "versionDate": "2026-05-13",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-05-19T16:53:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-05-13",
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
          "measure-id": "id119s4523",
          "measure-number": "4523",
          "measure-type": "s",
          "orig-publish-date": "2026-05-13",
          "originChamber": "SENATE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4523v00",
            "update-date": "2026-05-19"
          },
          "action-date": "2026-05-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
        },
        "title": "A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4523.xml",
    "summary": {
      "actionDate": "2026-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "updateDate": "2026-05-19",
      "versionCode": "id119s4523"
    },
    "title": "A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2026-05-13",
      "actionDesc": "Introduced in Senate",
      "text": "This bill designates the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "updateDate": "2026-05-19",
      "versionCode": "id119s4523"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4523is.xml"
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
      "title": "A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:42Z"
    },
    {
      "title": "A bill to designate the facility of the United States Postal Service located at 111 South Tremont Street in Tremonton, Utah, as the \"Sorensen-Estrada Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T10:56:26Z"
    }
  ]
}
```
