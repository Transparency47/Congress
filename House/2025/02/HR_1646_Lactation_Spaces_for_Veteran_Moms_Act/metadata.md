# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1646
- Title: Lactation Spaces for Veteran Moms Act
- Congress: 119
- Bill type: HR
- Bill number: 1646
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-01-07T09:05:45Z
- Update date including text: 2026-01-07T09:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1646",
    "number": "1646",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "U000040",
        "district": "14",
        "firstName": "Lauren",
        "fullName": "Rep. Underwood, Lauren [D-IL-14]",
        "lastName": "Underwood",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Lactation Spaces for Veteran Moms Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:45Z",
    "updateDateIncludingText": "2026-01-07T09:05:45Z"
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
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:02:27Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1646ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1646\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Underwood introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require a lactation space in each medical center of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Lactation Spaces for Veteran Moms Act .\n#### 2. Lactation spaces in medical centers of the Department of Veterans Affairs\n##### (a) In general\nSubchapter II of chapter 17 of title 38, United States Code, is amended by adding at the end the following new section:\n1720M. Lactation spaces in medical centers of the Department (a) Lactation space required The Secretary shall ensure that each medical center of the Department contains a lactation space. (b) No unauthorized entry Nothing in this section shall be construed to authorize an individual to enter a medical center of the Department or portion thereof that the individual is not otherwise authorized to enter. (c) Lactation space defined In this section, the term lactation space means a hygienic place, other than a bathroom, that\u2014 (1) is shielded from view; (2) is free from intrusion; (3) is accessible to disabled individuals (including such individuals who use wheelchairs); (4) contains a chair and a working surface; (5) is easy to locate; (6) is clearly identified with signage; and (7) is available for use by women veterans and members of the public to express breast milk. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item related to section 1720L the following new item:\n1720M. Lactation spaces in medical centers of the Department. .\n##### (c) Effective date\nThe Secretary of Veterans Affairs shall carry out section 1720M of title 38, United States Code, as added by this section, not later than two years after the date of the enactment of this Act.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:46",
        "text": "Held at the desk."
      },
      "number": "778",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lactation Spaces for Veteran Moms Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child health",
            "updateDate": "2025-06-03T16:00:45Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-06-03T16:00:45Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-03T16:00:45Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-06-03T16:00:45Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-03T16:00:45Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-06-03T16:00:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:58:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1646",
          "measure-number": "1646",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1646v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Lactation Spaces for Veteran Moms Act</strong></p> <p>This bill requires the Department of Veterans Affairs to ensure that each of its medical centers contains a hygienic lactation space that is not a bathroom and meets other specifications (e.g., must be easy to locate). </p>"
        },
        "title": "Lactation Spaces for Veteran Moms Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1646.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lactation Spaces for Veteran Moms Act</strong></p> <p>This bill requires the Department of Veterans Affairs to ensure that each of its medical centers contains a hygienic lactation space that is not a bathroom and meets other specifications (e.g., must be easy to locate). </p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1646"
    },
    "title": "Lactation Spaces for Veteran Moms Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lactation Spaces for Veteran Moms Act</strong></p> <p>This bill requires the Department of Veterans Affairs to ensure that each of its medical centers contains a hygienic lactation space that is not a bathroom and meets other specifications (e.g., must be easy to locate). </p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr1646"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1646ih.xml"
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
      "title": "Lactation Spaces for Veteran Moms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lactation Spaces for Veteran Moms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require a lactation space in each medical center of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:26Z"
    }
  ]
}
```
