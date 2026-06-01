# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1469?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1469
- Title: Protecting Children with Food Allergies Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1469
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-03-13T19:21:53Z
- Update date including text: 2026-03-13T19:21:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1469",
    "number": "1469",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Protecting Children with Food Allergies Act of 2025",
    "type": "S",
    "updateDate": "2026-03-13T19:21:53Z",
    "updateDateIncludingText": "2026-03-13T19:21:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T20:42:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1469is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1469\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Durbin (for himself and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Child Nutrition Act of 1966 to include food allergy information in existing training modules for local food service personnel.\n#### 1. Short title\nThis Act may be cited as the Protecting Children with Food Allergies Act of 2025 .\n#### 2. Including food allergy information in existing training modules for local food service personnel\n##### (a) Food allergy training module\nSection 7(g)(2)(B)(iii) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1776(g)(2)(B)(iii) ) is amended\u2014\n**(1)**\nby redesignating subclauses (II) and (III) as subclauses (III) and (IV), respectively; and\n**(2)**\nby inserting after subclause (I) the following:\n(II) food allergies, including information on the best practices to prevent, recognize, and respond to food-related allergic reactions; .\n##### (b) Certification\nSection 7(g)(2)(B)(ii)(II) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1776(g)(B)(ii)(II) ) is amended by striking clause (i) and inserting clauses (i) and (iii) .",
      "versionDate": "2025-04-10",
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
        "text": "Became Public Law No: 119-69."
      },
      "number": "222",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Whole Milk for Healthy Kids Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-22T13:17:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1469",
          "measure-number": "1469",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-03-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1469v00",
            "update-date": "2026-03-13"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Children with Food Allergies Act of 2025</strong></p><p>This bill requires that local school food service personnel receive annual training and certification on food allergies as part of the training provided by the National School Lunch Program of the Department of Agriculture.</p><p>Under current law, the mandatory training and certification for school food service personnel must include modules on (1) nutrition, and (2) health and food safety standards and methodologies.</p><p>Under the bill, the training and\u00a0certification\u00a0must also include a module on food allergies, including information on the best practices to prevent, recognize, and respond to food-related allergic reactions.</p><p>As part of the certification, the bill also requires that food service personnel\u00a0demonstrate competence in the training provided.</p>"
        },
        "title": "Protecting Children with Food Allergies Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1469.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Children with Food Allergies Act of 2025</strong></p><p>This bill requires that local school food service personnel receive annual training and certification on food allergies as part of the training provided by the National School Lunch Program of the Department of Agriculture.</p><p>Under current law, the mandatory training and certification for school food service personnel must include modules on (1) nutrition, and (2) health and food safety standards and methodologies.</p><p>Under the bill, the training and\u00a0certification\u00a0must also include a module on food allergies, including information on the best practices to prevent, recognize, and respond to food-related allergic reactions.</p><p>As part of the certification, the bill also requires that food service personnel\u00a0demonstrate competence in the training provided.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s1469"
    },
    "title": "Protecting Children with Food Allergies Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Children with Food Allergies Act of 2025</strong></p><p>This bill requires that local school food service personnel receive annual training and certification on food allergies as part of the training provided by the National School Lunch Program of the Department of Agriculture.</p><p>Under current law, the mandatory training and certification for school food service personnel must include modules on (1) nutrition, and (2) health and food safety standards and methodologies.</p><p>Under the bill, the training and\u00a0certification\u00a0must also include a module on food allergies, including information on the best practices to prevent, recognize, and respond to food-related allergic reactions.</p><p>As part of the certification, the bill also requires that food service personnel\u00a0demonstrate competence in the training provided.</p>",
      "updateDate": "2026-03-13",
      "versionCode": "id119s1469"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1469is.xml"
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
      "title": "Protecting Children with Food Allergies Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Children with Food Allergies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Child Nutrition Act of 1966 to include food allergy information in existing training modules for local food service personnel.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:23Z"
    }
  ]
}
```
