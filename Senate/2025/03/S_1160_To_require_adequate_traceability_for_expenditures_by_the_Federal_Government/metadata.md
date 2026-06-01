# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1160?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1160
- Title: LEDGER Act
- Congress: 119
- Bill type: S
- Bill number: 1160
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-12-05T22:55:31Z
- Update date including text: 2025-12-05T22:55:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1160",
    "number": "1160",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "LEDGER Act",
    "type": "S",
    "updateDate": "2025-12-05T22:55:31Z",
    "updateDateIncludingText": "2025-12-05T22:55:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T22:23:20Z",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1160is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1160\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Scott of Florida (for himself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require adequate traceability for expenditures by the Federal Government.\n#### 1. Short title\nThis Act may be cited as the Locating Every Disbursement in Government Expenditure Records Act or the LEDGER Act .\n#### 2. Traceability of expenditures\n##### (a) In general\nSubchapter II of chapter 35 of title 31, United States Code, is amended by adding at the end the following:\n3517. Traceability of expenditures Not later than 180 days after the date of enactment of this section, the Secretary of the Treasury shall implement a system that tracks all outlays from each appropriation, receipt, or other fund account in the Treasury by each department, agency, office, or other establishment in the executive, legislative, or judicial branch of the United States Government, including disbursements subject to the requirements under section 3325, which shall include tracking the period of availability of the amounts in the applicable appropriation, receipt, or other fund account. .\n##### (b) Conforming amendment\nThe table of sections for chapter 35 of title 31, United States Code, is amended by inserting after the item relating to section 3516 the following:\n3517. Traceability of expenditures. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-06-24",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "4091",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LEDGER Act",
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
        "updateDate": "2025-05-13T18:27:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119s1160",
          "measure-number": "1160",
          "measure-type": "s",
          "orig-publish-date": "2025-03-26",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1160v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Locating Every Disbursement in Government Expenditure Records Act or the LEDGER Act</strong></p><p>This bill requires the Department of the Treasury to implement a system that tracks all outlays from each appropriation, receipt, or other fund account in the Treasury by each department, agency, office, or other establishment in the executive, legislative, or judicial branches of the federal government. The system must also track the period of availability of the amounts in the applicable appropriation, receipt, or other fund account.</p>"
        },
        "title": "LEDGER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1160.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Locating Every Disbursement in Government Expenditure Records Act or the LEDGER Act</strong></p><p>This bill requires the Department of the Treasury to implement a system that tracks all outlays from each appropriation, receipt, or other fund account in the Treasury by each department, agency, office, or other establishment in the executive, legislative, or judicial branches of the federal government. The system must also track the period of availability of the amounts in the applicable appropriation, receipt, or other fund account.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1160"
    },
    "title": "LEDGER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Locating Every Disbursement in Government Expenditure Records Act or the LEDGER Act</strong></p><p>This bill requires the Department of the Treasury to implement a system that tracks all outlays from each appropriation, receipt, or other fund account in the Treasury by each department, agency, office, or other establishment in the executive, legislative, or judicial branches of the federal government. The system must also track the period of availability of the amounts in the applicable appropriation, receipt, or other fund account.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1160"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1160is.xml"
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
      "title": "LEDGER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LEDGER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Locating Every Disbursement in Government Expenditure Records Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require adequate traceability for expenditures by the Federal Government.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:32Z"
    }
  ]
}
```
