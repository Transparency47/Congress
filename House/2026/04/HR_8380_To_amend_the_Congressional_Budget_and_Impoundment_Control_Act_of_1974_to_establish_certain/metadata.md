# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8380
- Title: To amend the Congressional Budget and Impoundment Control Act of 1974 to establish certain procedures for consideration of annual appropriation bills, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 8380
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-20T08:08:19Z
- Update date including text: 2026-05-20T08:08:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-20 - IntroReferral: Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8380",
    "number": "8380",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to establish certain procedures for consideration of annual appropriation bills, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:19Z",
    "updateDateIncludingText": "2026-05-20T08:08:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Rules, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-20T16:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "OK"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "UT"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8380ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8380\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Mr. McClintock (for himself, Mr. Cole , Mrs. Bice , and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Rules , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to establish certain procedures for consideration of annual appropriation bills, and for other purposes.\n#### 1. Procedures for consideration of annual appropriation bills\n##### (a) In general\nSection 309 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 640 ) is amended to read as follows:\n309. Approval of regular appropriation bills (a) In the Senate (1) Except as provided in paragraph (2), the provisions of section 305 for the consideration in the Senate of concurrent resolutions on the budget and conference reports thereon shall apply to the consideration in the Senate of annual appropriation bills. (2) Debate in the Senate on any annual appropriation bill, and all amendments thereto and debatable motions and appeals in connection therewith, shall be limited to not more than 20 hours. (3) Paragraphs (1) and (2) shall not apply to any measure providing continuing appropriations. (b) In the House of Representatives It shall not be in order in the House of Representatives to consider any resolution providing for an adjournment period of more than three calendar days during the month of July until the House of Representatives has approved annual appropriation bills providing new budget authority under the jurisdiction of all the subcommittees of the Committee on Appropriations for the fiscal year beginning on October 1 of such year. For purposes of this section, the chairman of the Committee on Appropriations of the House of Representatives shall periodically advise the Speaker as to changes in jurisdiction among its various subcommittees. .\n##### (b) Conforming amendment\nIn the table of contents in section 1(b) of such Act ( 2 U.S.C. 621 note), the item relating to section 309 is amended to read as follows:\nSec. 309. Approval of regular appropriation bills. .",
      "versionDate": "2026-04-20",
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
        "name": "Economics and Public Finance",
        "updateDate": "2026-04-28T13:08:57Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8380ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to establish certain procedures for consideration of annual appropriation bills, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:18:21Z"
    },
    {
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to establish certain procedures for consideration of annual appropriation bills, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T08:06:15Z"
    }
  ]
}
```
