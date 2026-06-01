# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/89?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/89
- Title: Prescription Freedom Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 89
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-12T20:05:46Z
- Update date including text: 2025-02-12T20:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/89",
    "number": "89",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Prescription Freedom Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-12T20:05:46Z",
    "updateDateIncludingText": "2025-02-12T20:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr89ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 89\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal the authority of the Food and Drug Administration to require that drugs be dispensed only upon prescription, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prescription Freedom Act of 2025 .\n#### 2. Repeal of FDA authority to require prescriptions\n##### (a) Repeal\nEffective as of the date that is 6 months after the date of enactment of this Act, subsection (b) of section 503 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353 ) is repealed.\n##### (b) References\nBeginning on the effective date described in subsection (a), any reference in a Federal statute, regulation, or guidance\u2014\n**(1)**\nto prescribing, a prescription, a prescription drug, or a drug subject to section 503(b) of the Federal Food, Drug, and Cosmetic Act is deemed to be a reference to prescribing, a prescription, or a prescription drug, respectively, under applicable State law; and\n**(2)**\nto any requirement or provision of section 503(b) of the Federal Food, Drug, and Cosmetic Act is deemed to be a reference to the corresponding requirement or provision, if any, in applicable State law, as determined by the Federal official or officials responsible for administering the respective Federal statute, regulation, or guidance.\n##### (c) Exception\nNotwithstanding subsections (a) and (b), the Secretary of Health and Human Services may continue to exercise the authority vested by subsection (b) of section 503 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353 ), as in effect on the day before the effective date described in subsection (a), with respect to any drug that is intended for use in terminating a pregnancy.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Abortion",
            "updateDate": "2025-02-05T20:59:51Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-02-05T20:59:51Z"
          },
          {
            "name": "Food and Drug Administration (FDA)",
            "updateDate": "2025-02-05T20:59:51Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-02-05T20:59:51Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-05T20:59:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-04T12:33:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr89",
          "measure-number": "89",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr89v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prescription Freedom Act of 2025</strong></p><p>This bill generally eliminates the authority of the Food and Drug Administration (FDA) to require that a drug be dispensed only with a prescription. However, the FDA may continue to require a prescription for any drug intended for terminating a pregnancy.</p>"
        },
        "title": "Prescription Freedom Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr89.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prescription Freedom Act of 2025</strong></p><p>This bill generally eliminates the authority of the Food and Drug Administration (FDA) to require that a drug be dispensed only with a prescription. However, the FDA may continue to require a prescription for any drug intended for terminating a pregnancy.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr89"
    },
    "title": "Prescription Freedom Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prescription Freedom Act of 2025</strong></p><p>This bill generally eliminates the authority of the Food and Drug Administration (FDA) to require that a drug be dispensed only with a prescription. However, the FDA may continue to require a prescription for any drug intended for terminating a pregnancy.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr89"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr89ih.xml"
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
      "title": "Prescription Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prescription Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the authority of the Food and Drug Administration to require that drugs be dispensed only upon prescription, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:48:42Z"
    }
  ]
}
```
