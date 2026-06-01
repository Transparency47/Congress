# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1858
- Title: A bill to require that national cemeteries be open to visitors on legal public holidays.
- Congress: 119
- Bill type: S
- Bill number: 1858
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-09T21:00:58Z
- Update date including text: 2026-04-09T21:00:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1858",
    "number": "1858",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "A bill to require that national cemeteries be open to visitors on legal public holidays.",
    "type": "S",
    "updateDate": "2026-04-09T21:00:58Z",
    "updateDateIncludingText": "2026-04-09T21:00:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T15:05:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1858is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1858\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Daines introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo require that national cemeteries be open to visitors on legal public holidays.\n#### 1. National cemeteries open on legal public holidays\nEach national cemetery administered by the Department of Defense, the Department of Veterans Affairs, or the National Park Service shall be open to visitors on the legal public holidays described in section 6103(a) of title 5, United States Code.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-11-17",
        "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs."
      },
      "number": "5942",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Cemetery Access Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-05T18:46:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
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
          "measure-id": "id119s1858",
          "measure-number": "1858",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2025-08-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1858v00",
            "update-date": "2025-08-15"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires that national cemeteries administered by the Department of Defense, Department of Veterans Affairs, or the National Park Service must be open to visitors on the 11 legal public holidays (e.g., Memorial Day).</p>"
        },
        "title": "A bill to require that national cemeteries be open to visitors on legal public holidays."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1858.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires that national cemeteries administered by the Department of Defense, Department of Veterans Affairs, or the National Park Service must be open to visitors on the 11 legal public holidays (e.g., Memorial Day).</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1858"
    },
    "title": "A bill to require that national cemeteries be open to visitors on legal public holidays."
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires that national cemeteries administered by the Department of Defense, Department of Veterans Affairs, or the National Park Service must be open to visitors on the 11 legal public holidays (e.g., Memorial Day).</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1858"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1858is.xml"
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
      "title": "A bill to require that national cemeteries be open to visitors on legal public holidays.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:29Z"
    },
    {
      "title": "A bill to require that national cemeteries be open to visitors on legal public holidays.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:56:23Z"
    }
  ]
}
```
