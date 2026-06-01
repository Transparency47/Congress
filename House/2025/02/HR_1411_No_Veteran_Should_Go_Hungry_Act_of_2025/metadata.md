# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1411?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1411
- Title: No Veteran Should Go Hungry Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1411
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-03-26T08:06:28Z
- Update date including text: 2026-03-26T08:06:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1411",
    "number": "1411",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "No Veteran Should Go Hungry Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:28Z",
    "updateDateIncludingText": "2026-03-26T08:06:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "ME"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1411ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1411\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Gottheimer introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require the provision of information and counseling regarding Federal food assistance programs as part of the Transition Assistance Program.\n#### 1. Short title\nThis Act may be cited as the No Veteran Should Go Hungry Act of 2025 .\n#### 2. Provision of food assistance program information as part of Transition Assistance Program\nSection 1142(b) of title 10, United States Code, is amended by adding at the end the following new paragraph:\n(20) Information and counseling developed and provided in consultation with the Secretary of Agriculture, regarding Federal food and nutrition assistance programs, including the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ) and the special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ). .",
      "versionDate": "2025-02-18",
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
            "name": "Food assistance and relief",
            "updateDate": "2025-06-13T19:15:31Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-06-13T19:15:27Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-06-13T19:15:35Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-13T19:15:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-13T18:45:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1411",
          "measure-number": "1411",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1411v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Veteran Should Go Hungry Act of 2025</strong></p><p>This bill requires that preseparation counseling provided to members of the Armed Forces under the Transition Assistance Program include information regarding federal food and nutrition assistance programs (e.g., the Supplemental Nutrition Assistance Program, commonly referred to as SNAP).</p>"
        },
        "title": "No Veteran Should Go Hungry Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1411.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Veteran Should Go Hungry Act of 2025</strong></p><p>This bill requires that preseparation counseling provided to members of the Armed Forces under the Transition Assistance Program include information regarding federal food and nutrition assistance programs (e.g., the Supplemental Nutrition Assistance Program, commonly referred to as SNAP).</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1411"
    },
    "title": "No Veteran Should Go Hungry Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Veteran Should Go Hungry Act of 2025</strong></p><p>This bill requires that preseparation counseling provided to members of the Armed Forces under the Transition Assistance Program include information regarding federal food and nutrition assistance programs (e.g., the Supplemental Nutrition Assistance Program, commonly referred to as SNAP).</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr1411"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1411ih.xml"
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
      "title": "No Veteran Should Go Hungry Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Veteran Should Go Hungry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the provision of information and counseling regarding Federal food assistance programs as part of the Transition Assistance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:25Z"
    }
  ]
}
```
