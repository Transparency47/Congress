# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2800?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2800
- Title: Pharmacy and Medically Underserved Areas Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 2800
- Origin chamber: Senate
- Introduced date: 2025-09-15
- Update date: 2025-12-02T16:57:04Z
- Update date including text: 2025-12-02T16:57:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-15: Introduced in Senate
- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-15: Introduced in Senate

## Actions

- 2025-09-15 - IntroReferral: Introduced in Senate
- 2025-09-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-15",
    "latestAction": {
      "actionDate": "2025-09-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2800",
    "number": "2800",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Pharmacy and Medically Underserved Areas Enhancement Act",
    "type": "S",
    "updateDate": "2025-12-02T16:57:04Z",
    "updateDateIncludingText": "2025-12-02T16:57:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-15",
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
      "actionDate": "2025-09-15",
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
          "date": "2025-09-15T19:40:40Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2800is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2800\nIN THE SENATE OF THE UNITED STATES\nSeptember 15, 2025 Mr. Grassley (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide for coverage under the Medicare program of pharmacist services.\n#### 1. Short title\nThis Act may be cited as the Pharmacy and Medically Underserved Areas Enhancement Act .\n#### 2. Medicare coverage of pharmacist services\n##### (a) Coverage\nSection 1861(s)(2) of the Social Security Act ( 42 U.S.C. 1395x(s)(2) ) is amended\u2014\n**(1)**\nin subparagraph (JJ), by inserting and at the end; and\n**(2)**\nby adding at the end the following new subparagraph:\n(KK) pharmacist services furnished by a pharmacist, as licensed by State law, individually or on behalf of a pharmacy provider\u2014 (i) which the pharmacist is legally authorized to perform in the State in which the individual performs such services; (ii) as would otherwise be covered under this part if furnished by a physician, or as an incident to a physician\u2019s service; and (iii) in a setting located in a health professional shortage area (as defined in section 332(a)(1)(A) of the Public Health Service Act), medically underserved area, or medically underserved population (as defined in section 330(b)(3) of such Act); .\n##### (b) Payment\nSection 1833(a)(1) of the Social Security Act ( 42 U.S.C. 1395l(a)(1) ) is amended\u2014\n**(1)**\nby striking and (HH) and inserting (HH) ; and\n**(2)**\nby inserting before the semicolon at the end the following: , and (II) with respect to pharmacist services (as defined in section 1861(s)(2)(KK)), the amounts paid shall be equal to 80 percent of the lesser of the actual charge or 85 percent of the fee schedule amount provided under section 1848 if such services had been furnished by a physician .\n##### (c) Effective date; Pharmacist specific codes\n**(1) Effective date**\nThe amendments made by subsections (a) and (b) shall apply with respect to services furnished on or after January 1, 2027.\n**(2) Pharmacist specific codes**\nThe Secretary of Health and Human Services shall develop pharmacist specific codes, as necessary, under the physician fee schedule under section 1848 of the Social Security Act ( 42 U.S.C. 1395w\u20134 ).",
      "versionDate": "2025-09-15",
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
        "name": "Health",
        "updateDate": "2025-09-29T13:44:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-15",
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
          "measure-id": "id119s2800",
          "measure-number": "2800",
          "measure-type": "s",
          "orig-publish-date": "2025-09-15",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2800v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-09-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Pharmacy and Medically Underserved Areas Enhancement Act</b></p> <p>This bill provides for Medicare coverage and payment with respect to certain\u00a0pharmacist services that (1) are furnished by a pharmacist in a health-professional shortage area, and (2) would otherwise be covered under Medicare if furnished by a physician. </p>"
        },
        "title": "Pharmacy and Medically Underserved Areas Enhancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2800.xml",
    "summary": {
      "actionDate": "2025-09-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Pharmacy and Medically Underserved Areas Enhancement Act</b></p> <p>This bill provides for Medicare coverage and payment with respect to certain\u00a0pharmacist services that (1) are furnished by a pharmacist in a health-professional shortage area, and (2) would otherwise be covered under Medicare if furnished by a physician. </p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2800"
    },
    "title": "Pharmacy and Medically Underserved Areas Enhancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Pharmacy and Medically Underserved Areas Enhancement Act</b></p> <p>This bill provides for Medicare coverage and payment with respect to certain\u00a0pharmacist services that (1) are furnished by a pharmacist in a health-professional shortage area, and (2) would otherwise be covered under Medicare if furnished by a physician. </p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2800"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2800is.xml"
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
      "title": "Pharmacy and Medically Underserved Areas Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-27T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pharmacy and Medically Underserved Areas Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-27T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide for coverage under the Medicare program of pharmacist services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T03:48:24Z"
    }
  ]
}
```
