# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/238?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/238
- Title: Healthy Technology Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 238
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-02-20T21:19:39Z
- Update date including text: 2025-02-20T21:19:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/238",
    "number": "238",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Healthy Technology Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-20T21:19:39Z",
    "updateDateIncludingText": "2025-02-20T21:19:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
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
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:03:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr238ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 238\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Schweikert introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to clarify that artificial intelligence and machine learning technologies can qualify as a practitioner eligible to prescribe drugs if authorized by the State involved and approved, cleared, or authorized by the Food and Drug Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Healthy Technology Act of 2025 .\n#### 2. Prescription of drugs by artificial intelligence or machine learning technologies\nSection 503(b) of Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353(b) ) is amended by adding at the end the following:\n(6) In this subsection, the term practitioner licensed by law to administer such drug includes artificial intelligence and machine learning technology that are\u2014 (A) authorized pursuant to a statute of the State involved to prescribe the drug involved; and (B) approved, cleared, or authorized under section 510(k), 513, 515, or 564. .",
      "versionDate": "2025-01-07",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-02-10T19:03:50Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-02-10T19:03:50Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-02-10T19:03:50Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-02-10T19:03:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-06T16:56:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr238",
          "measure-number": "238",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr238v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Healthy Technology Act of 2025 </strong></p><p>This bill establishes that artificial intelligence (AI) or machine learning technology may be eligible to prescribe drugs.</p><p>Currently, certain drugs may be dispensed only upon a prescription provided by a practitioner licensed by law to administer the drug. Under this bill, an AI or machine learning technology may qualify as such a prescribing practitioner if the technology is (1) authorized by state law to prescribe the drug involved; and (2) approved, cleared, or authorized under certain federal provisions pertaining to medical devices and products.</p>"
        },
        "title": "Healthy Technology Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr238.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Technology Act of 2025 </strong></p><p>This bill establishes that artificial intelligence (AI) or machine learning technology may be eligible to prescribe drugs.</p><p>Currently, certain drugs may be dispensed only upon a prescription provided by a practitioner licensed by law to administer the drug. Under this bill, an AI or machine learning technology may qualify as such a prescribing practitioner if the technology is (1) authorized by state law to prescribe the drug involved; and (2) approved, cleared, or authorized under certain federal provisions pertaining to medical devices and products.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr238"
    },
    "title": "Healthy Technology Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Healthy Technology Act of 2025 </strong></p><p>This bill establishes that artificial intelligence (AI) or machine learning technology may be eligible to prescribe drugs.</p><p>Currently, certain drugs may be dispensed only upon a prescription provided by a practitioner licensed by law to administer the drug. Under this bill, an AI or machine learning technology may qualify as such a prescribing practitioner if the technology is (1) authorized by state law to prescribe the drug involved; and (2) approved, cleared, or authorized under certain federal provisions pertaining to medical devices and products.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr238"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr238ih.xml"
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
      "title": "Healthy Technology Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Technology Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to clarify that artificial intelligence and machine learning technologies can qualify as a practitioner eligible to prescribe drugs if authorized by the State involved and approved, cleared, or authorized by the Food and Drug Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:28Z"
    }
  ]
}
```
