# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/237
- Title: Paws Off Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 237
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-02-20T21:15:55Z
- Update date including text: 2025-02-20T21:15:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/237",
    "number": "237",
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
    "title": "Paws Off Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-20T21:15:55Z",
    "updateDateIncludingText": "2025-02-20T21:15:55Z"
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
          "date": "2025-01-07T16:02:40Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr237ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 237\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Mr. Schweikert introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to deem foods containing xylitol as misbranded unless the label or labeling of such foods contains a warning specifying the toxic effects of xylitol for dogs if ingested, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Paws Off Act of 2025 .\n#### 2. Xylitol label and labeling requirements\n##### (a) In general\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If it is a food that contains xylitol, unless the label or labeling of such food contains a warning specifying the toxic effects of xylitol for dogs if ingested. .\n##### (b) Rulemaking\n**(1) Interim rule**\nNot later than 6 months after the date of enactment of this Act, the Secretary shall issue an interim final rule to carry out the amendment made by subsection (a).\n**(2) Final rule**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall issue a final rule to carry out the amendment made by subsection (a).\n##### (c) Secretary defined\nIn this section, the term Secretary means the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs.",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-02-10T20:41:06Z"
          },
          {
            "name": "Animal protection and human-animal relationships",
            "updateDate": "2025-02-10T20:40:55Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-02-10T20:41:01Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2025-02-10T20:40:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-06T16:55:04Z"
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
          "measure-id": "id119hr237",
          "measure-number": "237",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr237v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Paws Off Act of 2025 </strong></p><p>This bill forbids the sale of food that contains xylitol unless the food's label contains a warning about the toxic effects of xylitol for dogs if ingested.</p>"
        },
        "title": "Paws Off Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr237.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Paws Off Act of 2025 </strong></p><p>This bill forbids the sale of food that contains xylitol unless the food's label contains a warning about the toxic effects of xylitol for dogs if ingested.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr237"
    },
    "title": "Paws Off Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Paws Off Act of 2025 </strong></p><p>This bill forbids the sale of food that contains xylitol unless the food's label contains a warning about the toxic effects of xylitol for dogs if ingested.</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119hr237"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr237ih.xml"
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
      "title": "Paws Off Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Paws Off Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to deem foods containing xylitol as misbranded unless the label or labeling of such foods contains a warning specifying the toxic effects of xylitol for dogs if ingested, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:18:27Z"
    }
  ]
}
```
