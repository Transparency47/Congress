# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1168?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1168
- Title: Portable Ultrasound Reimbursement Equity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1168
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2026-05-12T20:06:35Z
- Update date including text: 2026-05-12T20:06:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1168",
    "number": "1168",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Portable Ultrasound Reimbursement Equity Act of 2025",
    "type": "S",
    "updateDate": "2026-05-12T20:06:35Z",
    "updateDateIncludingText": "2026-05-12T20:06:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T15:28:58Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NH"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1168is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1168\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Cornyn (for himself and Ms. Hassan ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide coverage of portable ultrasound transportation and set up services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Portable Ultrasound Reimbursement Equity Act of 2025 .\n#### 2. Coverage of portable ultrasound transportation and set up services under the Medicare program\n##### (a) In general\nSection 1861(s)(3) of the Social Security Act ( 42 U.S.C. 1395x(s)(3) ) is amended by striking diagnostic X-ray tests and inserting diagnostic X-ray and ultrasound tests .\n##### (b) Ensuring equitable payment for portable ultrasound transportation services\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsection:\n(aa) Ensuring equitable payment for portable ultrasound transportation and set Up services (1) In general The Secretary shall provide a separate payment under this part for portable ultrasound transportation and set up services in the same manner and to the same extent that separate payments are provided for portable X-ray transportation and set up services. (2) Payment requirements The Secretary shall specify requirements applicable to suppliers of portable ultrasound transportation and set up services under this part. Such requirements shall be substantially similar to the requirements applicable to suppliers of portable X-ray services under subpart C of part 486 of title 42, Code of Federal Regulations (or a successor regulation). .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to services furnished on or after January 1, 2027.",
      "versionDate": "2025-03-27",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2477",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Portable Ultrasound Reimbursement Equity Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-05-01T13:27:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119s1168",
          "measure-number": "1168",
          "measure-type": "s",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2026-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1168v00",
            "update-date": "2026-05-12"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Portable Ultrasound Reimbursement Equity Act of 2025</strong></p><p>This bill provides for Medicare coverage of ultrasound tests performed\u00a0at a beneficiary's home. The Centers for Medicare & Medicaid Services must provide for separate payments for portable ultrasound services in the same manner and to the same extent as for portable X-ray services.</p>"
        },
        "title": "Portable Ultrasound Reimbursement Equity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1168.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Portable Ultrasound Reimbursement Equity Act of 2025</strong></p><p>This bill provides for Medicare coverage of ultrasound tests performed\u00a0at a beneficiary's home. The Centers for Medicare & Medicaid Services must provide for separate payments for portable ultrasound services in the same manner and to the same extent as for portable X-ray services.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119s1168"
    },
    "title": "Portable Ultrasound Reimbursement Equity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Portable Ultrasound Reimbursement Equity Act of 2025</strong></p><p>This bill provides for Medicare coverage of ultrasound tests performed\u00a0at a beneficiary's home. The Centers for Medicare & Medicaid Services must provide for separate payments for portable ultrasound services in the same manner and to the same extent as for portable X-ray services.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119s1168"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1168is.xml"
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
      "title": "Portable Ultrasound Reimbursement Equity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Portable Ultrasound Reimbursement Equity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage of portable ultrasound transportation and set up services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T03:03:25Z"
    }
  ]
}
```
