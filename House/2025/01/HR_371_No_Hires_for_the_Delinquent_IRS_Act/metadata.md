# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/371
- Title: No Hires for the Delinquent IRS Act
- Congress: 119
- Bill type: HR
- Bill number: 371
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-04-03T12:41:01Z
- Update date including text: 2025-04-03T12:41:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/371",
    "number": "371",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "No Hires for the Delinquent IRS Act",
    "type": "HR",
    "updateDate": "2025-04-03T12:41:01Z",
    "updateDateIncludingText": "2025-04-03T12:41:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-13T17:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr371ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 371\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Rouzer introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo prohibit the hiring of additional Internal Revenue Service employees until the Secretary of the Treasury certifies that no employee of the Internal Revenue Service has a seriously delinquent tax debt.\n#### 1. Short title\nThis Act may be cited as the No Hires for the Delinquent IRS Act .\n#### 2. Prohibition on IRS hiring of new employees until certification that no IRS employee has a seriously delinquent tax debt\n##### (a) In general\nNo officer or employee of the United States may extend an offer of employment in the Internal Revenue Service to any individual until after the date on which the Secretary of the Treasury publicly issues a written certification that the Internal Revenue Service does not employ any individual who has a seriously delinquent tax debt.\n##### (b) Seriously delinquent tax debt\nFor purposes of this section, the term seriously delinquent tax debt means an outstanding debt under the Internal Revenue Code of 1986 for which a notice of lien has been filed in public records pursuant to section 6323 of such Code, except that such term does not include\u2014\n**(1)**\na debt that is being paid in a timely manner pursuant to an agreement under section 6159 or section 7122 of such Code;\n**(2)**\na debt with respect to which a collection due process hearing under section 6330 of such Code, or relief under subsection (a), (b), or (f) of section 6015 of such Code, is requested or pending;\n**(3)**\na debt with respect to which a levy has been issued under section 6331 of such Code (or a debt with respect to which the applicant for employment agrees to be subject to a levy issued under such section); and\n**(4)**\na debt with respect to which relief under section 6343(a)(1)(D) of such Code is granted.",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-02-14T18:42:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
    "originChamber": "House",
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
          "measure-id": "id119hr371",
          "measure-number": "371",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr371v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Hires for the Delinquent IRS Act </strong></p><p>This bill prohibits the hiring of additional Internal Revenue Service (IRS) employees until the Department of the Treasury publicly certifies in writing that the IRS does not employ any individual who has a seriously delinquent tax debt.</p><p>The bill defines <em>seriously delinquent tax debt</em> as\u00a0an outstanding tax debt for which a notice of lien is filed in public records, but excluding tax debts</p><ul><li>being paid pursuant to an installment agreement or offer-in-compromise,</li><li>for which collection action is suspended because a due process hearing or innocent spouse relief is requested,</li><li>subject to levy, or</li><li>released from levy due to economic hardship.</li></ul>"
        },
        "title": "No Hires for the Delinquent IRS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr371.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Hires for the Delinquent IRS Act </strong></p><p>This bill prohibits the hiring of additional Internal Revenue Service (IRS) employees until the Department of the Treasury publicly certifies in writing that the IRS does not employ any individual who has a seriously delinquent tax debt.</p><p>The bill defines <em>seriously delinquent tax debt</em> as\u00a0an outstanding tax debt for which a notice of lien is filed in public records, but excluding tax debts</p><ul><li>being paid pursuant to an installment agreement or offer-in-compromise,</li><li>for which collection action is suspended because a due process hearing or innocent spouse relief is requested,</li><li>subject to levy, or</li><li>released from levy due to economic hardship.</li></ul>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr371"
    },
    "title": "No Hires for the Delinquent IRS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Hires for the Delinquent IRS Act </strong></p><p>This bill prohibits the hiring of additional Internal Revenue Service (IRS) employees until the Department of the Treasury publicly certifies in writing that the IRS does not employ any individual who has a seriously delinquent tax debt.</p><p>The bill defines <em>seriously delinquent tax debt</em> as\u00a0an outstanding tax debt for which a notice of lien is filed in public records, but excluding tax debts</p><ul><li>being paid pursuant to an installment agreement or offer-in-compromise,</li><li>for which collection action is suspended because a due process hearing or innocent spouse relief is requested,</li><li>subject to levy, or</li><li>released from levy due to economic hardship.</li></ul>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr371"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr371ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No Hires for the Delinquent IRS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Hires for the Delinquent IRS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the hiring of additional Internal Revenue Service employees until the Secretary of the Treasury certifies that no employee of the Internal Revenue Service has a seriously delinquent tax debt.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:20Z"
    }
  ]
}
```
