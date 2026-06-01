# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1342?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1342
- Title: Stopping Political Discrimination in Disaster Assistance Act
- Congress: 119
- Bill type: HR
- Bill number: 1342
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-12-05T22:02:22Z
- Update date including text: 2025-12-05T22:02:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1342",
    "number": "1342",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "P000605",
        "district": "10",
        "firstName": "Scott",
        "fullName": "Rep. Perry, Scott [R-PA-10]",
        "lastName": "Perry",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Stopping Political Discrimination in Disaster Assistance Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:02:22Z",
    "updateDateIncludingText": "2025-12-05T22:02:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-13T22:19:33Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1342ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1342\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Perry introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prohibit discrimination based on political affiliation in granting disaster assistance.\n#### 1. Short title\nThis Act may be cited as the Stopping Political Discrimination in Disaster Assistance Act .\n#### 2. Nondiscrimination in disaster assistance\nSection 308(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5151(a) ) is amended by striking or economic status and inserting economic status, or political affiliation .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-03",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "373",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stopping Political Discrimination in Disaster Assistance Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-13T18:49:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1342",
          "measure-number": "1342",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-06-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1342v00",
            "update-date": "2025-06-10"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stopping Political Discrimination in Disaster Assistance Act</strong></p><p>This bill prohibits discrimination on the basis of political affiliation by the Federal Emergency Management Agency (FEMA) and other participating entities (i.e., public or private entities providing or receiving assistance) in carrying out federal major disaster or emergency relief and assistance activities.</p><p>Current law requires\u00a0FEMA and other participating entities to provide federal major disaster or emergency relief and assistance without discrimination on the basis of race, color, religion, nationality, sex, age, disability, English proficiency, or economic status. The bill adds political affiliation to the classes protected under this requirement.\u00a0</p>"
        },
        "title": "Stopping Political Discrimination in Disaster Assistance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1342.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Political Discrimination in Disaster Assistance Act</strong></p><p>This bill prohibits discrimination on the basis of political affiliation by the Federal Emergency Management Agency (FEMA) and other participating entities (i.e., public or private entities providing or receiving assistance) in carrying out federal major disaster or emergency relief and assistance activities.</p><p>Current law requires\u00a0FEMA and other participating entities to provide federal major disaster or emergency relief and assistance without discrimination on the basis of race, color, religion, nationality, sex, age, disability, English proficiency, or economic status. The bill adds political affiliation to the classes protected under this requirement.\u00a0</p>",
      "updateDate": "2025-06-10",
      "versionCode": "id119hr1342"
    },
    "title": "Stopping Political Discrimination in Disaster Assistance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stopping Political Discrimination in Disaster Assistance Act</strong></p><p>This bill prohibits discrimination on the basis of political affiliation by the Federal Emergency Management Agency (FEMA) and other participating entities (i.e., public or private entities providing or receiving assistance) in carrying out federal major disaster or emergency relief and assistance activities.</p><p>Current law requires\u00a0FEMA and other participating entities to provide federal major disaster or emergency relief and assistance without discrimination on the basis of race, color, religion, nationality, sex, age, disability, English proficiency, or economic status. The bill adds political affiliation to the classes protected under this requirement.\u00a0</p>",
      "updateDate": "2025-06-10",
      "versionCode": "id119hr1342"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1342ih.xml"
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
      "title": "Stopping Political Discrimination in Disaster Assistance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Political Discrimination in Disaster Assistance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit discrimination based on political affiliation in granting disaster assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:51Z"
    }
  ]
}
```
