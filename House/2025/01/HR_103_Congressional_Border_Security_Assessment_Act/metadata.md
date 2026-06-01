# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/103?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/103
- Title: Congressional Border Security Assessment Act
- Congress: 119
- Bill type: HR
- Bill number: 103
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-09-03T20:09:43Z
- Update date including text: 2025-09-03T20:09:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/103",
    "number": "103",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
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
    "title": "Congressional Border Security Assessment Act",
    "type": "HR",
    "updateDate": "2025-09-03T20:09:43Z",
    "updateDateIncludingText": "2025-09-03T20:09:43Z"
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
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-01-03T16:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr103ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 103\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide Members of Congress lawful access to certain Indian land to assess the security of the international boundary between the United States and Mexico located on that Indian land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Border Security Assessment Act .\n#### 2. Access to Indian reservations for border security assessment\n##### (a) In general\nA member of Congress and any Congressional staff accompanying that member shall have lawful access to any Indian reservation that includes 50 or more contiguous miles of the international boundary between the United States and Mexico for the purpose of obtaining information for assessing national security, public safety, and the security of the international boundary. Such lawful access shall extend to any roadways or easements on Indian country.\n##### (b) Definition of Indian country\nFor the purposes of this section, the term Indian country shall have the meaning given that term in section 1151 of title 18, United States Code.",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-09-03T20:00:30Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-03T20:01:17Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-09-03T20:09:43Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2025-09-03T20:00:24Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-09-03T20:01:10Z"
          },
          {
            "name": "Mexico",
            "updateDate": "2025-09-03T20:00:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T14:57:31Z"
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
          "measure-id": "id119hr103",
          "measure-number": "103",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr103v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Congressional Border Security Assessment Act</strong></p><p>This bill grants Members of Congress and their accompanying staff lawful access to Indian reservations for the purpose of assessing national security, public safety, and the security of the border. Specifically, the bill applies to an Indian reservation that includes 50 or more contiguous miles of the U.S.-Mexico border.\u00a0</p>"
        },
        "title": "Congressional Border Security Assessment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr103.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Border Security Assessment Act</strong></p><p>This bill grants Members of Congress and their accompanying staff lawful access to Indian reservations for the purpose of assessing national security, public safety, and the security of the border. Specifically, the bill applies to an Indian reservation that includes 50 or more contiguous miles of the U.S.-Mexico border.\u00a0</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr103"
    },
    "title": "Congressional Border Security Assessment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Congressional Border Security Assessment Act</strong></p><p>This bill grants Members of Congress and their accompanying staff lawful access to Indian reservations for the purpose of assessing national security, public safety, and the security of the border. Specifically, the bill applies to an Indian reservation that includes 50 or more contiguous miles of the U.S.-Mexico border.\u00a0</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr103"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr103ih.xml"
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
      "title": "Congressional Border Security Assessment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Border Security Assessment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide Members of Congress lawful access to certain Indian land to assess the security of the international boundary between the United States and Mexico located on that Indian land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T12:48:24Z"
    }
  ]
}
```
