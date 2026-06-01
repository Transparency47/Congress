# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7526
- Title: Safe Skies Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7526
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-13T08:06:20Z
- Update date including text: 2026-05-13T08:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7526",
    "number": "7526",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safe Skies Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:20Z",
    "updateDateIncludingText": "2026-05-13T08:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "IN"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7526ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7526\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Carbajal (for himself, Mr. Fitzpatrick , Mr. Garamendi , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Secretary of Transportation to modify the final rule relating to flightcrew member duty and rest requirements for passenger operations of air carriers to apply to all-cargo operations of air carriers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Skies Act of 2026 .\n#### 2. Modification of final rule relating to flightcrew member duty and rest requirements for passenger operations to apply to all-cargo operations\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Transportation shall modify the final rule specified in subsection (b) so that the flightcrew member duty and rest requirements under that rule apply to flightcrew members in all-cargo operations conducted by air carriers in the same manner as those requirements apply to flightcrew members in passenger operations conducted by air carriers.\n##### (b) Final rule specified\nThe final rule specified in this subsection is the final rule of the Federal Aviation Administration\u2014\n**(1)**\npublished in the Federal Register on January 4, 2012 (77 Fed. Reg. 330); and\n**(2)**\nrelating to flightcrew member duty and rest requirements.\n##### (c) Applicability of rulemaking requirements\nThe requirements of section 553 of title 5, United States Code, shall not apply to the modification required by subsection (a).",
      "versionDate": "2026-02-12",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-27T19:53:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-12",
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
          "measure-id": "id119hr7526",
          "measure-number": "7526",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-12",
          "originChamber": "HOUSE",
          "update-date": "2026-04-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7526v00",
            "update-date": "2026-04-27"
          },
          "action-date": "2026-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Safe Skies Act of 2026</strong></p><p>This bill directs the Department of Transportation (DOT) to\u00a0expand specified duty and rest requirements to apply the requirements to all-cargo flight crew members.</p><p>Currently, a DOT final rule on flight crew member duty and rest requirements only applies to flight crew members in passenger operations conducted by air carriers. Under the bill, DOT must modify this final rule so that the requirements also apply to all-cargo flight crew members.</p>"
        },
        "title": "Safe Skies Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7526.xml",
    "summary": {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Skies Act of 2026</strong></p><p>This bill directs the Department of Transportation (DOT) to\u00a0expand specified duty and rest requirements to apply the requirements to all-cargo flight crew members.</p><p>Currently, a DOT final rule on flight crew member duty and rest requirements only applies to flight crew members in passenger operations conducted by air carriers. Under the bill, DOT must modify this final rule so that the requirements also apply to all-cargo flight crew members.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr7526"
    },
    "title": "Safe Skies Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Safe Skies Act of 2026</strong></p><p>This bill directs the Department of Transportation (DOT) to\u00a0expand specified duty and rest requirements to apply the requirements to all-cargo flight crew members.</p><p>Currently, a DOT final rule on flight crew member duty and rest requirements only applies to flight crew members in passenger operations conducted by air carriers. Under the bill, DOT must modify this final rule so that the requirements also apply to all-cargo flight crew members.</p>",
      "updateDate": "2026-04-27",
      "versionCode": "id119hr7526"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7526ih.xml"
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
      "title": "Safe Skies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:38:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Skies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T09:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Transportation to modify the final rule relating to flightcrew member duty and rest requirements for passenger operations of air carriers to apply to all-cargo operations of air carriers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:33:41Z"
    }
  ]
}
```
