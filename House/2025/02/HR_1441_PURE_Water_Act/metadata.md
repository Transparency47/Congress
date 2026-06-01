# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1441
- Title: PURE Water Act
- Congress: 119
- Bill type: HR
- Bill number: 1441
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-11-14T15:16:13Z
- Update date including text: 2025-11-14T15:16:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1441",
    "number": "1441",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "PURE Water Act",
    "type": "HR",
    "updateDate": "2025-11-14T15:16:13Z",
    "updateDateIncludingText": "2025-11-14T15:16:13Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-02-18T18:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "MD"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1441ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1441\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Torres of New York (for himself, Mr. Lawler , Mr. Nadler , Mr. Latimer , Mr. Riley of New York , and Mr. Olszewski ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax credit for the purchase and installation of certain water filtration systems in homes.\n#### 1. Short title\nThis Act may be cited as the Providing Useful Relief for Enhanced Water Act or the PURE Water Act .\n#### 2. Water filtration credit\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Water filtration credit (a) Allowance of credit In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the sum of\u2014 (1) 20 percent of qualified primary residence filtration expenditures, and (2) 10 percent of qualified non-primary residence filtration expenditures. (b) Maximum credit The credit allowed under subsection (a) for any taxable year shall not exceed $2,500. (c) Carryforward of unused credit If the credit allowable under subsection (a) exceeds the limitation imposed by subsection (b), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such succeeding taxable year. (d) Definitions For purposes of this section\u2014 (1) Qualified primary residence filtration expenditure The term qualified primary residence filtration expenditure means an expenditure for a qualified water filter for use in a dwelling unit located in the United States and used as a the primary residence of the taxpayer. (2) Qualified non-primary residence filtration expenditure The term qualified non-primary residence filtration expenditure means an expenditure for a qualified water filter for use in a dwelling unit located in the United States and used as a secondary residence of the taxpayer. (3) Qualified water filter For purposes of this section, the term qualified water filter \u2014 (A) means a home water filtration system the purpose of which is to remove at least 90 percent of lead, PFAS, and PFOAS from drinking water, and (B) does not include maintenance costs or replacement parts for such filtration system. (4) PFAS The term PFAS means per- and polyfluoroalkyl substances that contain at least one fully fluorinated carbon atom. (5) PFOA The term PFOA means perfluorooctanoic acid. (e) Basis adjustment For purposes of this subtitle, if a credit is allowed under this section for any expenditure with respect to any property, the increase in the basis of such property which would (but for this subsection) result from such expenditure shall be reduced by the amount of the credit so allowed. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Water filtration credit.\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-07T12:46:36Z"
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
          "measure-id": "id119hr1441",
          "measure-number": "1441",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-11-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1441v00",
            "update-date": "2025-11-14"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Providing Useful Relief for Enhanced Water Act or the PURE Water Act</strong></p><p>This bill establishes a new nonrefundable federal tax credit for 20% of the cost of a water filter used in a primary residence located in the United States (or 10% of the cost for a water filter used in a non-primary U.S. residence). (Limitations apply.)</p><p>Under the bill, the tax credit is limited to $2,500 in a tax year. However, the bill allows the amount of the tax credit in excess of the annual maximum amount to be carried forward to the succeeding tax year.</p><p>To qualify for the tax credit, the water filter must be a home water filtration system\u00a0with the purpose of\u00a0removing from drinking water at least 90% of (1) lead, (2) per- and polyfluoroalkyl substances that contain at least one fully fluorinated carbon atom (PFAS), and (3) perfluorooctanoic acid (PFOA).</p><p>Finally, under the bill, the increase in the basis of the residence (the value of the residence for federal tax purposes) due to the water filter excludes the amount of the allowed tax credit.</p>"
        },
        "title": "PURE Water Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1441.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Useful Relief for Enhanced Water Act or the PURE Water Act</strong></p><p>This bill establishes a new nonrefundable federal tax credit for 20% of the cost of a water filter used in a primary residence located in the United States (or 10% of the cost for a water filter used in a non-primary U.S. residence). (Limitations apply.)</p><p>Under the bill, the tax credit is limited to $2,500 in a tax year. However, the bill allows the amount of the tax credit in excess of the annual maximum amount to be carried forward to the succeeding tax year.</p><p>To qualify for the tax credit, the water filter must be a home water filtration system\u00a0with the purpose of\u00a0removing from drinking water at least 90% of (1) lead, (2) per- and polyfluoroalkyl substances that contain at least one fully fluorinated carbon atom (PFAS), and (3) perfluorooctanoic acid (PFOA).</p><p>Finally, under the bill, the increase in the basis of the residence (the value of the residence for federal tax purposes) due to the water filter excludes the amount of the allowed tax credit.</p>",
      "updateDate": "2025-11-14",
      "versionCode": "id119hr1441"
    },
    "title": "PURE Water Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Providing Useful Relief for Enhanced Water Act or the PURE Water Act</strong></p><p>This bill establishes a new nonrefundable federal tax credit for 20% of the cost of a water filter used in a primary residence located in the United States (or 10% of the cost for a water filter used in a non-primary U.S. residence). (Limitations apply.)</p><p>Under the bill, the tax credit is limited to $2,500 in a tax year. However, the bill allows the amount of the tax credit in excess of the annual maximum amount to be carried forward to the succeeding tax year.</p><p>To qualify for the tax credit, the water filter must be a home water filtration system\u00a0with the purpose of\u00a0removing from drinking water at least 90% of (1) lead, (2) per- and polyfluoroalkyl substances that contain at least one fully fluorinated carbon atom (PFAS), and (3) perfluorooctanoic acid (PFOA).</p><p>Finally, under the bill, the increase in the basis of the residence (the value of the residence for federal tax purposes) due to the water filter excludes the amount of the allowed tax credit.</p>",
      "updateDate": "2025-11-14",
      "versionCode": "id119hr1441"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1441ih.xml"
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
      "title": "PURE Water Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PURE Water Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Useful Relief for Enhanced Water Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a tax credit for the purchase and installation of certain water filtration systems in homes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:23Z"
    }
  ]
}
```
