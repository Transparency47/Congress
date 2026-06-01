# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/387
- Title: Texas Agricultural Producers Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 387
- Origin chamber: House
- Introduced date: 2025-01-14
- Update date: 2026-02-17T21:50:25Z
- Update date including text: 2026-02-17T21:50:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-14: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-01-14: Introduced in House

## Actions

- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Introduced in House
- 2025-01-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-14",
    "latestAction": {
      "actionDate": "2025-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/387",
    "number": "387",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Texas Agricultural Producers Assistance Act",
    "type": "HR",
    "updateDate": "2026-02-17T21:50:25Z",
    "updateDateIncludingText": "2026-02-17T21:50:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-14",
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
          "date": "2025-01-14T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:03:57Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr387ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 387\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2025 Ms. De La Cruz (for herself, Ms. Crockett , Mr. Ellzey , Mr. Fallon , and Mr. Arrington ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to submit to Congress a report on available assistance to agricultural producers in the State of Texas that have suffered economic losses due to the failure of Mexico to deliver water.\n#### 1. Short title\nThis Act may be cited as the Texas Agricultural Producers Assistance Act .\n#### 2. Report on available assistance to agricultural producers in the State of Texas that have suffered economic losses due to the failure of Mexico to deliver water\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Agriculture shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that lists all existing authorities of the Secretary and programs within the Department of Agriculture that are or could be made available to provide assistance to agricultural producers in the State of Texas that have suffered economic losses due to the failure of Mexico to deliver water to the United States in accordance with the Treaty Relating to the Utilization of Waters of the Colorado and Tijuana Rivers and of the Rio Grande signed at Washington on February 3, 1944, and the Supplementary Protocol signed at Washington on November 14, 1944.",
      "versionDate": "2025-01-14",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-21T12:12:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-14",
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
          "measure-id": "id119hr387",
          "measure-number": "387",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-14",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr387v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Texas Agricultural Producers Assistance Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to submit a report to Congress on USDA assistance available for agricultural producers in Texas related to Mexico's non-compliance with a 1944 treaty with the United States\u00a0concerning water utilization. </p><p>Specifically, the USDA report must list all of the existing USDA authorities and programs that are or could be made available to provide assistance to agricultural producers in Texas that have suffered economic losses due to Mexico not delivering water to the United States in accordance with the Treaty on Utilization of Waters of the Colorado and Tijuana Rivers and of the Rio Grande, including the Supplementary Protocol.</p>"
        },
        "title": "Texas Agricultural Producers Assistance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr387.xml",
    "summary": {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Texas Agricultural Producers Assistance Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to submit a report to Congress on USDA assistance available for agricultural producers in Texas related to Mexico's non-compliance with a 1944 treaty with the United States\u00a0concerning water utilization. </p><p>Specifically, the USDA report must list all of the existing USDA authorities and programs that are or could be made available to provide assistance to agricultural producers in Texas that have suffered economic losses due to Mexico not delivering water to the United States in accordance with the Treaty on Utilization of Waters of the Colorado and Tijuana Rivers and of the Rio Grande, including the Supplementary Protocol.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr387"
    },
    "title": "Texas Agricultural Producers Assistance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Texas Agricultural Producers Assistance Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to submit a report to Congress on USDA assistance available for agricultural producers in Texas related to Mexico's non-compliance with a 1944 treaty with the United States\u00a0concerning water utilization. </p><p>Specifically, the USDA report must list all of the existing USDA authorities and programs that are or could be made available to provide assistance to agricultural producers in Texas that have suffered economic losses due to Mexico not delivering water to the United States in accordance with the Treaty on Utilization of Waters of the Colorado and Tijuana Rivers and of the Rio Grande, including the Supplementary Protocol.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr387"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr387ih.xml"
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
      "title": "Texas Agricultural Producers Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Texas Agricultural Producers Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to submit to Congress a report on available assistance to agricultural producers in the State of Texas that have suffered economic losses due to the failure of Mexico to deliver water.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:30Z"
    }
  ]
}
```
