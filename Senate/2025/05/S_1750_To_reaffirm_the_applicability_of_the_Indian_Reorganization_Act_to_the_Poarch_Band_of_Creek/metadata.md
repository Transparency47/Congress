# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1750?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1750
- Title: Poarch Band of Creek Indians Parity Act
- Congress: 119
- Bill type: S
- Bill number: 1750
- Origin chamber: Senate
- Introduced date: 2025-05-14
- Update date: 2025-12-05T22:52:03Z
- Update date including text: 2025-12-05T22:52:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-14: Introduced in Senate
- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- Latest action: 2025-05-14: Introduced in Senate

## Actions

- 2025-05-14 - IntroReferral: Introduced in Senate
- 2025-05-14 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1750",
    "number": "1750",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Poarch Band of Creek Indians Parity Act",
    "type": "S",
    "updateDate": "2025-12-05T22:52:03Z",
    "updateDateIncludingText": "2025-12-05T22:52:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T15:50:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1750is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1750\nIN THE SENATE OF THE UNITED STATES\nMay 14, 2025 Mrs. Britt (for herself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo reaffirm the applicability of the Indian Reorganization Act to the Poarch Band of Creek Indians, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Poarch Band of Creek Indians Parity Act .\n#### 2. Applicability of Indian Reorganization Act to the Poarch Band of Creek Indians\n##### (a) In general\nThe Poarch Band of Creek Indians shall be considered now under Federal jurisdiction as of June 18, 1934, for purposes of the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 984, chapter 576; 25 U.S.C. 5101 et seq. ).\n##### (b) Lands taken into trust\nAll lands taken into trust by the United States for the benefit of the Poarch Band of Creek Indians before the date of enactment of this Act are reaffirmed as trust land, and the actions of the Secretary of the Interior in taking those lands into trust under the Act of June 18, 1934 (commonly known as the Indian Reorganization Act ) (48 Stat. 984, chapter 576; 25 U.S.C. 5101 et seq. ), are ratified and confirmed.",
      "versionDate": "2025-05-14",
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
        "actionDate": "2025-06-25",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "4147",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Poarch Band of Creek Indians Parity Act",
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
        "name": "Native Americans",
        "updateDate": "2025-06-03T18:28:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-14",
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
          "measure-id": "id119s1750",
          "measure-number": "1750",
          "measure-type": "s",
          "orig-publish-date": "2025-05-14",
          "originChamber": "SENATE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1750v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-05-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Poarch Band of Creek Indians Parity Act</strong></p><p>This bill applies the Indian Reorganization Act (IRA) to the Poarch Band of Creek Indians. Additionally, the bill reaffirms previous decisions by the Department of the Interior to take land into trust for the tribe under the IRA.</p><p>A 2009 Supreme Court case,\u00a0<em>Carcieri v. Salazar,</em> decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Poarch Band of Creek Indians, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) reaffirms prior decisions by Interior to take land into trust for the benefit of the tribe.</p>"
        },
        "title": "Poarch Band of Creek Indians Parity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1750.xml",
    "summary": {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Poarch Band of Creek Indians Parity Act</strong></p><p>This bill applies the Indian Reorganization Act (IRA) to the Poarch Band of Creek Indians. Additionally, the bill reaffirms previous decisions by the Department of the Interior to take land into trust for the tribe under the IRA.</p><p>A 2009 Supreme Court case,\u00a0<em>Carcieri v. Salazar,</em> decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Poarch Band of Creek Indians, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) reaffirms prior decisions by Interior to take land into trust for the benefit of the tribe.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1750"
    },
    "title": "Poarch Band of Creek Indians Parity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Poarch Band of Creek Indians Parity Act</strong></p><p>This bill applies the Indian Reorganization Act (IRA) to the Poarch Band of Creek Indians. Additionally, the bill reaffirms previous decisions by the Department of the Interior to take land into trust for the tribe under the IRA.</p><p>A 2009 Supreme Court case,\u00a0<em>Carcieri v. Salazar,</em> decided that Interior could not take land into trust for a specified tribe because that tribe had not been under federal jurisdiction when the IRA was enacted in 1934. This bill (1) affirms the applicability of the IRA to the Poarch Band of Creek Indians, thereby deeming the tribe to be under federal jurisdiction as of June 18, 1934, for purposes of the IRA; and (2) reaffirms prior decisions by Interior to take land into trust for the benefit of the tribe.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1750"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1750is.xml"
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
      "title": "Poarch Band of Creek Indians Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-30T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Poarch Band of Creek Indians Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reaffirm the applicability of the Indian Reorganization Act to the Poarch Band of Creek Indians, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:23Z"
    }
  ]
}
```
