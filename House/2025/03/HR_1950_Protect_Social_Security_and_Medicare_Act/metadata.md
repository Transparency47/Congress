# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1950?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1950
- Title: Protect Social Security and Medicare Act
- Congress: 119
- Bill type: HR
- Bill number: 1950
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-06-11T15:39:20Z
- Update date including text: 2025-06-11T15:39:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Rules.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Rules.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1950",
    "number": "1950",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "P000607",
        "district": "2",
        "firstName": "Mark",
        "fullName": "Rep. Pocan, Mark [D-WI-2]",
        "lastName": "Pocan",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Protect Social Security and Medicare Act",
    "type": "HR",
    "updateDate": "2025-06-11T15:39:20Z",
    "updateDateIncludingText": "2025-06-11T15:39:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:00:20Z",
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
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "MI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MN"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1950ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1950\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Pocan (for himself, Mr. Doggett , and Mr. Frost ) introduced the following bill; which was referred to the Committee on Rules\nA BILL\nTo protect benefits provided under Social Security, Medicare, and any other program of benefits administered by the Social Security Administration or the Centers for Medicare and Medicaid Services.\n#### 1. Short title\nThis Act may be cited as the Protect Social Security and Medicare Act .\n#### 2. Supermajority vote required to cut benefits administered by Social Security Administration or Centers for Medicare and Medicaid Services\n##### (a) Supermajority vote requirement\nA bill or joint resolution, or any amendment offered to a bill or joint resolution, which contains any provision which, if enacted, would result in the reduction of any existing benefit provided or administered by the Social Security Administration or the Centers for Medicare and Medicaid Services may not be considered in the House of Representatives or the Senate unless two-thirds of the Members present and voting agree to a motion to consider the bill, joint resolution, or amendment with the provision included.\n##### (b) Exception for payments to Medicare advantage plans\nSubsection (a) does not apply to any provision which, if enacted, would result in the reduction of any payment made to a Medicare Advantage plan under part C of title XVIII of the Social Security Act ( 42 U.S.C. 1395w\u201321 et seq. ), but only if the provision would, if enacted, result in an increase in the amount of payments made for other purposes under title XVIII of the Social Security Act in an amount equal to or greater than the amount of the reduction in payment made to the Medicare Advantage plan.\n#### 3. Determination of reduction of benefits\nDuring the consideration of a bill, joint resolution, or amendment in the House of Representatives or Senate, any determination regarding whether a provision in the bill, joint resolution, or amendment would, if enacted, result in a reduction described in section 2(a) or a reduction or increase described in section 2(b) shall be made solely on the basis of a determination made by the Office of the Chief Actuary of the Social Security Administration.",
      "versionDate": "2025-03-06",
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
        "name": "Social Welfare",
        "updateDate": "2025-03-23T11:28:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1950",
          "measure-number": "1950",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1950v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect Social Security and Medicare Act</strong></p><p>This bill requires a two-thirds vote before Congress may consider legislation that would reduce retirement, health, or other benefits administered by the Social Security Administration or the Centers for Medicare & Medicaid Services.</p><p>Specifically, such legislation may not be considered in either chamber of Congress until two-thirds of Members present and voting agree to a motion to consider the legislation. However, this restriction does not apply to legislation that reduces payments to Medicare Advantage plans so long as it also increases, in an amount equal to or greater than the reduction, payments made for other purposes under Medicare.</p>"
        },
        "title": "Protect Social Security and Medicare Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1950.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Social Security and Medicare Act</strong></p><p>This bill requires a two-thirds vote before Congress may consider legislation that would reduce retirement, health, or other benefits administered by the Social Security Administration or the Centers for Medicare & Medicaid Services.</p><p>Specifically, such legislation may not be considered in either chamber of Congress until two-thirds of Members present and voting agree to a motion to consider the legislation. However, this restriction does not apply to legislation that reduces payments to Medicare Advantage plans so long as it also increases, in an amount equal to or greater than the reduction, payments made for other purposes under Medicare.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1950"
    },
    "title": "Protect Social Security and Medicare Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Social Security and Medicare Act</strong></p><p>This bill requires a two-thirds vote before Congress may consider legislation that would reduce retirement, health, or other benefits administered by the Social Security Administration or the Centers for Medicare & Medicaid Services.</p><p>Specifically, such legislation may not be considered in either chamber of Congress until two-thirds of Members present and voting agree to a motion to consider the legislation. However, this restriction does not apply to legislation that reduces payments to Medicare Advantage plans so long as it also increases, in an amount equal to or greater than the reduction, payments made for other purposes under Medicare.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1950"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1950ih.xml"
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
      "title": "Protect Social Security and Medicare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Social Security and Medicare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect benefits provided under Social Security, Medicare, and any other program of benefits administered by the Social Security Administration or the Centers for Medicare and Medicaid Services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:37Z"
    }
  ]
}
```
