# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3025?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3025
- Title: Fund Farm Programs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3025
- Origin chamber: Senate
- Introduced date: 2025-10-21
- Update date: 2025-10-29T14:30:37Z
- Update date including text: 2025-10-29T14:30:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-21: Introduced in Senate
- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on Appropriations.
- Latest action: 2025-10-21: Introduced in Senate

## Actions

- 2025-10-21 - IntroReferral: Introduced in Senate
- 2025-10-21 - IntroReferral: Read twice and referred to the Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-21",
    "latestAction": {
      "actionDate": "2025-10-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3025",
    "number": "3025",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Fund Farm Programs Act of 2025",
    "type": "S",
    "updateDate": "2025-10-29T14:30:37Z",
    "updateDateIncludingText": "2025-10-29T14:30:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "ssap00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-21",
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
          "date": "2025-10-21T21:03:12Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Appropriations Committee",
      "systemCode": "ssap00",
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
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3025is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3025\nIN THE SENATE OF THE UNITED STATES\nOctober 21, 2025 Mr. Hawley introduced the following bill; which was read twice and referred to the Committee on Appropriations\nA BILL\nTo appropriate funds to ensure uninterrupted services for farmers.\n#### 1. Short title\nThis Act may be cited as the Fund Farm Programs Act of 2025 .\n#### 2. Uninterrupted services for farmers\n##### (a) In general\nIn fiscal year 2026, for any period during which interim continuing appropriations or full-year appropriations for that fiscal year have not been enacted for the Department of Agriculture, there are appropriated to the Secretary of Agriculture, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to provide uninterrupted services for farmers through, and maintain continued operation of, programs and offices of the Farm Service Agency, including with respect to farm loans.\n##### (b) Retroactive services\nThe appropriations under subsection (a) shall include any amounts necessary for the costs of any services described in that subsection that were not provided during the period beginning on September 30, 2025, and ending on the date of enactment of this Act due to a lapse in appropriations.\n##### (c) Termination\nAppropriations shall be made available pursuant to subsection (a) until the date of enactment into law of appropriations for the Department of Agriculture for fiscal year 2026 (including a continuing appropriation).",
      "versionDate": "2025-10-21",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-10-29T14:05:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-21",
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
          "measure-id": "id119s3025",
          "measure-number": "3025",
          "measure-type": "s",
          "orig-publish-date": "2025-10-21",
          "originChamber": "SENATE",
          "update-date": "2025-10-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3025v00",
            "update-date": "2025-10-29"
          },
          "action-date": "2025-10-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fund Farm Programs Act of 2025</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to continue providing services for farmers\u00a0through the Farm Service Agency (FSA)\u00a0during any period in which legislation has not been enacted to provide continuing or full-year FY2026 appropriations to USDA.\u00a0</p><p>Specifically, the bill provides appropriations to continue (1) uninterrupted services for farmers through the FSA; and (2) operations of\u00a0FSA programs and offices, including with respect to farm loans. The bill also provides appropriations for the costs of\u00a0FSA services that were not provided to farmers on or after September 30, 2025, and before this bill is enacted due to a lapse in appropriations.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted to provide FY2026 appropriations for USDA (including continuing appropriations).\u00a0</p>"
        },
        "title": "Fund Farm Programs Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3025.xml",
    "summary": {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fund Farm Programs Act of 2025</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to continue providing services for farmers\u00a0through the Farm Service Agency (FSA)\u00a0during any period in which legislation has not been enacted to provide continuing or full-year FY2026 appropriations to USDA.\u00a0</p><p>Specifically, the bill provides appropriations to continue (1) uninterrupted services for farmers through the FSA; and (2) operations of\u00a0FSA programs and offices, including with respect to farm loans. The bill also provides appropriations for the costs of\u00a0FSA services that were not provided to farmers on or after September 30, 2025, and before this bill is enacted due to a lapse in appropriations.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted to provide FY2026 appropriations for USDA (including continuing appropriations).\u00a0</p>",
      "updateDate": "2025-10-29",
      "versionCode": "id119s3025"
    },
    "title": "Fund Farm Programs Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fund Farm Programs Act of 2025</strong></p><p>This bill provides appropriations for the Department of Agriculture (USDA) to continue providing services for farmers\u00a0through the Farm Service Agency (FSA)\u00a0during any period in which legislation has not been enacted to provide continuing or full-year FY2026 appropriations to USDA.\u00a0</p><p>Specifically, the bill provides appropriations to continue (1) uninterrupted services for farmers through the FSA; and (2) operations of\u00a0FSA programs and offices, including with respect to farm loans. The bill also provides appropriations for the costs of\u00a0FSA services that were not provided to farmers on or after September 30, 2025, and before this bill is enacted due to a lapse in appropriations.\u00a0</p><p>The appropriations provided by this bill are available until legislation is enacted to provide FY2026 appropriations for USDA (including continuing appropriations).\u00a0</p>",
      "updateDate": "2025-10-29",
      "versionCode": "id119s3025"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3025is.xml"
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
      "title": "Fund Farm Programs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T07:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fund Farm Programs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-25T07:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to appropriate funds to ensure uninterrupted services for farmers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-25T07:33:20Z"
    }
  ]
}
```
