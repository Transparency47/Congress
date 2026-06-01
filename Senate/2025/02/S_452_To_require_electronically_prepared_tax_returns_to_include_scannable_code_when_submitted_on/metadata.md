# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/452?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/452
- Title: BARCODE Efficiency Act
- Congress: 119
- Bill type: S
- Bill number: 452
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-01-16T14:02:51Z
- Update date including text: 2026-01-16T14:02:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/452",
    "number": "452",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "BARCODE Efficiency Act",
    "type": "S",
    "updateDate": "2026-01-16T14:02:51Z",
    "updateDateIncludingText": "2026-01-16T14:02:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T18:00:44Z",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s452is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 452\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Young (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require electronically prepared tax returns to include scannable code when submitted on paper, and to require the use of optical character recognition technology for paper documents received by the Internal Revenue Service.\n#### 1. Short title\nThis Act may be cited as the Barcode Automation for Revenue Collection to Organize Disbursement and Enhance Efficiency Act or the BARCODE Efficiency Act .\n#### 2. Scanning and digitization of tax returns and correspondence\n##### (a) Returns prepared electronically and submitted on paper\nWith respect to any Federal tax return which is prepared electronically, but is printed and filed on paper\u2014\n**(1)**\nsuch return shall bear a code which, when scanned, converts the data included in such return to electronic format, and\n**(2)**\nsubject to subsection (b)(1)(B), the Internal Revenue Service shall use barcode scanning technology to convert the data included in such returns to electronic format.\n##### (b) Optical character recognition software\nWith respect to\u2014\n**(1)**\nany Federal tax return which\u2014\n**(A)**\nis not prepared electronically and is printed and filed on paper, or\n**(B)**\nis described in subsection (a)(1) but, for any reason, the data included in such return cannot be accurately converted into electronic format, or\n**(2)**\nany correspondence which is received by the Internal Revenue Service in a paper form (with the exception of any such correspondence which has been received by the Internal Revenue Service in electronic format),\nthe Internal Revenue Service shall use optical character recognition technology (or any functionally similar technology) to transcribe such return or correspondence.\n##### (c) Exception\n**(1) In general**\nSubsection (a) or (b) shall not apply to the extent that the Secretary of the Treasury or the Secretary\u2019s delegate determines that the technology described in such subsection is slower or less reliable than\u2014\n**(A)**\nthe process of manually transcribing returns or correspondence received in a paper form, or\n**(B)**\nany other process that the Internal Revenue Service is using or would otherwise use.\n**(2) Report to congress**\nAny exception to the application of subsection (a) or (b) pursuant to paragraph (1) shall not take effect unless the Secretary provides a report to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate regarding the determination made by the Secretary under such paragraph within 30 days of such determination.\n##### (d) Effective date\nThis section shall apply to\u2014\n**(1)**\nany individual income tax return (as defined in section 6011(e)(3)(C) of the Internal Revenue Code of 1986) received on or after January 1 of the first calendar year beginning more than 180 days after the date of enactment of this Act,\n**(2)**\nany estate tax return (as described in section 6018 of such Code) or gift tax return (as described in section 6019 of such Code) received on or after January 1 of the first calendar year beginning more than 24 months after the date of enactment of this Act, and\n**(3)**\nany other return or correspondence received on or after January 1 of the first calendar year beginning more than 12 months after the date of enactment of this Act.",
      "versionDate": "2025-02-06",
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
        "actionDate": "2026-01-14",
        "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 0."
      },
      "number": "6956",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "BARCODE Efficiency Act",
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
        "updateDate": "2025-05-05T17:04:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s452",
          "measure-number": "452",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s452v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Barcode Automation for Revenue Collection to Organize Disbursement and Enhance Efficiency Act or the BARCODE Efficiency Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to use barcodes, barcode scanning technology, and optical character recognition (or similar) technology to digitize certain federal tax return information and correspondence, unless the technology is\u00a0slower or less reliable than other IRS processes (subject to conditions).\u00a0</p><p>Specifically, the bill requires a scannable barcode on electronically-prepared federal tax returns that are printed and filed in paper format with the IRS. The bill also requires the IRS to use barcode scanning technology to convert data included on such returns into an electronic format.</p><p>Further, the bill requires the IRS to use optical character recognition (or similar) technology to transcribe federal tax returns and correspondence received by the IRS that are not prepared electronically and are received in paper format.</p><p>However, under the bill, the use of barcodes, barcode scanning technology, and optical character recognition (or similar) technology is not required if (1) such technology is slower or less reliable than manual transcription or any other IRS process, and (2) the IRS provides a report to Congress regarding the determination to not use such technology.</p>"
        },
        "title": "BARCODE Efficiency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s452.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Barcode Automation for Revenue Collection to Organize Disbursement and Enhance Efficiency Act or the BARCODE Efficiency Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to use barcodes, barcode scanning technology, and optical character recognition (or similar) technology to digitize certain federal tax return information and correspondence, unless the technology is\u00a0slower or less reliable than other IRS processes (subject to conditions).\u00a0</p><p>Specifically, the bill requires a scannable barcode on electronically-prepared federal tax returns that are printed and filed in paper format with the IRS. The bill also requires the IRS to use barcode scanning technology to convert data included on such returns into an electronic format.</p><p>Further, the bill requires the IRS to use optical character recognition (or similar) technology to transcribe federal tax returns and correspondence received by the IRS that are not prepared electronically and are received in paper format.</p><p>However, under the bill, the use of barcodes, barcode scanning technology, and optical character recognition (or similar) technology is not required if (1) such technology is slower or less reliable than manual transcription or any other IRS process, and (2) the IRS provides a report to Congress regarding the determination to not use such technology.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s452"
    },
    "title": "BARCODE Efficiency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Barcode Automation for Revenue Collection to Organize Disbursement and Enhance Efficiency Act or the BARCODE Efficiency Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to use barcodes, barcode scanning technology, and optical character recognition (or similar) technology to digitize certain federal tax return information and correspondence, unless the technology is\u00a0slower or less reliable than other IRS processes (subject to conditions).\u00a0</p><p>Specifically, the bill requires a scannable barcode on electronically-prepared federal tax returns that are printed and filed in paper format with the IRS. The bill also requires the IRS to use barcode scanning technology to convert data included on such returns into an electronic format.</p><p>Further, the bill requires the IRS to use optical character recognition (or similar) technology to transcribe federal tax returns and correspondence received by the IRS that are not prepared electronically and are received in paper format.</p><p>However, under the bill, the use of barcodes, barcode scanning technology, and optical character recognition (or similar) technology is not required if (1) such technology is slower or less reliable than manual transcription or any other IRS process, and (2) the IRS provides a report to Congress regarding the determination to not use such technology.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s452"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s452is.xml"
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
      "title": "BARCODE Efficiency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BARCODE Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Barcode Automation for Revenue Collection to Organize Disbursement and Enhance Efficiency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require electronically prepared tax returns to include scannable code when submitted on paper, and to require the use of optical character recognition technology for paper documents received by the Internal Revenue Service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:28Z"
    }
  ]
}
```
