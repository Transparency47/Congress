# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/747?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/747
- Title: Improper Payments Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 747
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-05-07T14:21:19Z
- Update date including text: 2025-05-07T14:21:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/747",
    "number": "747",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Improper Payments Transparency Act",
    "type": "S",
    "updateDate": "2025-05-07T14:21:19Z",
    "updateDateIncludingText": "2025-05-07T14:21:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T18:00:29Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s747is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 747\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Ricketts (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 31, United States Code, to include information on improper payments under Federal programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improper Payments Transparency Act .\n#### 2. Including improper payment information in Presidents budget submission\nSection 1105(a) of title 31, United States Code, is amended by adding at the end the following:\n(39) information with respect to improper payment (as such term is defined in section 3351) amounts and rates for programs and activities at each executive agency required to submit improper payment reports under subchapter IV of chapter 33, including\u2014 (A) a narrative description, including a detailed explanation with respect to why any improper payment amounts and rates occurred and trends of\u2014 (i) each program and activity with improper payment amounts and rates that have increased or decreased on average over the previous 3 years; and (ii) each program and activity whose improper payment amounts and rates did not change over such years; and (B) any corrective actions, including any such action in any corrective action plan under section 3352(d), with respect to such programs and activities that are incomplete, and steps the executive agency will take to address issues relating to improper payment amounts and rates. .",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on the Budget."
      },
      "number": "1771",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improper Payments Transparency Act",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-06T15:33:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s747",
          "measure-number": "747",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s747v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>"
        },
        "title": "Improper Payments Transparency Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s747.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s747"
    },
    "title": "Improper Payments Transparency Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Improper Payments Transparency Act</strong></p><p>This bill requires the President's annual budget to include specified information regarding improper payment amounts and rates for programs and activities at certain federal agencies. (An <em>improper payment</em>\u00a0is any payment that should not have been made or that was made in an incorrect amount, including an overpayment or underpayment, under a statutory, contractual, administrative, or other legally applicable requirement.)</p><p>Specifically, the President's budget must include (1) a narrative description, including a detailed explanation of why any improper payment amounts and\u00a0rates occurred and related trends for programs and activities; and (2) corrective actions and steps the agencies will take to address improper payment amount and rate issues.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s747"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s747is.xml"
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
      "title": "Improper Payments Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improper Payments Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 31, United States Code, to include information on improper payments under Federal programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:51Z"
    }
  ]
}
```
