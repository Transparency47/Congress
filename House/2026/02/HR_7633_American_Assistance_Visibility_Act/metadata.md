# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7633
- Title: American Assistance Visibility Act
- Congress: 119
- Bill type: HR
- Bill number: 7633
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-04-09T19:05:27Z
- Update date including text: 2026-04-09T19:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 1.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7633",
    "number": "7633",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "American Assistance Visibility Act",
    "type": "HR",
    "updateDate": "2026-04-09T19:05:27Z",
    "updateDateIncludingText": "2026-04-09T19:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 44 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
        "item": [
          {
            "date": "2026-03-26T16:06:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-20T16:32:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7633ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7633\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Shreve introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the United States flag to be displayed on United States foreign assistance.\n#### 1. Short title\nThis Act may be cited as the American Assistance Visibility Act .\n#### 2. Requirement to display United States flag on foreign assistance\nThe Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) is amended\u2014\n**(1)**\nin section 641, by striking the second sentence; and\n**(2)**\nby adding after such section the following:\n641A. Requirement to display United States flag on foreign assistance (a) In general The United States flag shall be distinctively displayed on foreign assistance and, except as provided under subsection (b), be the sole visual-branding element displayed on foreign assistance. (b) Exception In addition to the United State flag, the Secretary of State may authorize on a case-by-case basis any other visual-branding element to be displayed on foreign assistance under the following: (1) When required by an international agreement or partnership where co-branding is a formal condition of such agreement or partnership. (2) When necessary for the clear identification of implementing partners, provided that the United States flag remains the most prominent visual-branding element. (3) Any other basis the Secretary of State determines necessary. (c) Waiver The Secretary of State may waive any requirement of this section as such Secretary determines necessary to ensure the safety or security of personnel or beneficiaries in high-risk locations. (d) Directed rulemaking The Secretary of State shall issue such regulations as are necessary to implement this section, including specifications, with respect to the United States flag, regarding\u2014 (1) minimum size requirements; (2) color accuracy; (3) placement location; and (4) any other requirement the Secretary determines necessary to ensure the United States flag is clearly and prominently displayed on foreign assistance. (e) Foreign assistance defined In this section, the term foreign assistance means each tangible item provided by the United States Government to a foreign country or international organization under this or any other Act, including\u2014 (1) buildings, equipment, vehicles, project or construction site signage, and any other physical asset or infrastructure; (2) food aid, medical supplies, and other commodities; and (3) banners, posters, websites, social media accounts or posts, and other public outreach or report publications. .\n#### 3. Applicability\nThis Act, and the amendments made by this Act, shall apply with respect to foreign assistance (as defined section 641A of the Foreign Assistance Act of 1961) provided after the date of the enactment of this Act.",
      "versionDate": "2026-02-20",
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
        "name": "International Affairs",
        "updateDate": "2026-02-25T18:35:12Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7633ih.xml"
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
      "title": "American Assistance Visibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Assistance Visibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the United States flag to be displayed on United States foreign assistance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:48:33Z"
    }
  ]
}
```
