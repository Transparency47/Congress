# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/132
- Title: Filing Relief for Natural Disasters Act
- Congress: 119
- Bill type: S
- Bill number: 132
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-04-01T19:15:39Z
- Update date including text: 2026-04-01T19:15:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/132",
    "number": "132",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Filing Relief for Natural Disasters Act",
    "type": "S",
    "updateDate": "2026-04-01T19:15:39Z",
    "updateDateIncludingText": "2026-04-01T19:15:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-01-16T21:05:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MD"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s132is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 132\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Ms. Cortez Masto (for herself, Mr. Kennedy , Mrs. Blackburn , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the rules for postponing certain deadlines by reason of disaster.\n#### 1. Short title\nThis Act may be cited as the Filing Relief for Natural Disasters Act .\n#### 2. Modification of rules for postponing certain deadlines by reason of disaster\n##### (a) Authority To postpone Federal tax deadlines by reason of State-Declared disasters\nSection 7508A of the Internal Revenue Code of 1986 is amended by redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively, and by inserting after subsection (b) the following new subsection:\n(c) Special rule for State-Declared disasters (1) In general The Secretary may, upon the written request of the Governor of a State (or the Mayor, in the case of the District of Columbia), apply the rules of subsection (a) to a qualified State declared disaster in the same manner as a disaster, fire, or action otherwise described in subsection (a). (2) Qualified State declared disaster For purposes of this section, the term qualified State declared disaster means, with respect to any State, any natural catastrophe (including any hurricane, tornado, storm, high water, winddriven water, tidal wave, tsunami, earthquake, volcanic eruption, landslide, mudslide, snowstorm, or drought), or, regardless of cause, any fire, flood, or explosion, in any part of the State, which in the determination of the Governor of such State (or the Mayor, in the case of the District of Columbia) causes damage of sufficient severity and magnitude to warrant the application of the rules of this section. (3) State For purposes of this section, the term State includes the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands. .\n##### (b) Mandatory extensions extended to 120 days\nSection 7508A(e) of such Code, as redesignated by subsection (a), is amended\u2014\n**(1)**\nby striking 60 days in paragraph (1)(B) thereof and inserting 120 days ,\n**(2)**\nby striking 60-day in paragraph (6) thereof and inserting 120-day , and\n**(3)**\nby striking 60 -day in the heading and inserting 120 -day .\n##### (c) Effective date\nThe amendments made by this section shall apply to declarations made after the date of the enactment of this Act.",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-24",
        "text": "Became Public Law No: 119-29."
      },
      "number": "517",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Filing Relief for Natural Disasters Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "District of Columbia",
            "updateDate": "2025-03-05T20:56:43Z"
          },
          {
            "name": "Internal Revenue Service (IRS)",
            "updateDate": "2025-03-05T20:56:43Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-03-05T20:56:43Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-05T20:56:43Z"
          },
          {
            "name": "Tax administration and collection, taxpayers",
            "updateDate": "2025-03-05T20:56:43Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-03-05T20:56:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-25T19:49:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
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
          "measure-id": "id119s132",
          "measure-number": "132",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s132v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Filing Relief for Natural Disasters Act</strong></p><p>This bill authorizes the Internal Revenue Service (IRS) to postpone federal tax deadlines for taxpayers affected by a qualified state declared disaster, upon written request by the state governor. The bill also increases the automatic extension of federal tax deadlines for certain taxpayers.</p><p>Under current law, the IRS may postpone federal tax deadlines for taxpayers affected by a federally declared disaster, including (but not limited to) deadlines for (1) filing federal tax returns, (2) paying federal taxes, (3) making retirement plan contributions, and (4) tax assessments and collections.</p><p>The bill authorizes the IRS to postpone such federal tax deadlines for taxpayers affected by a qualified state declared disaster upon written request by the state\u2019s governor (or the District of\u00a0Columbia mayor). Under the bill, a state includes the District of Columbia, Puerto Rico, the U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.</p><p>The bill defines <em>qualified state declared disaster</em> as any natural catastrophe,\u00a0fire, flood, or explosion that causes damage of sufficient severity and magnitude to warrant a request to postpone such federal tax deadlines.</p><p>Further, under current law, an automatic 60-day extension of such federal tax deadlines applies to certain relief workers, individuals killed or injured as a result of a federally declared disaster, and taxpayers whose principal residence, business, or tax records are located in a federally declared disaster area.</p><p>The bill increases to 120 days the automatic extension of federal tax deadlines for these\u00a0taxpayers.</p>"
        },
        "title": "Filing Relief for Natural Disasters Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s132.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Filing Relief for Natural Disasters Act</strong></p><p>This bill authorizes the Internal Revenue Service (IRS) to postpone federal tax deadlines for taxpayers affected by a qualified state declared disaster, upon written request by the state governor. The bill also increases the automatic extension of federal tax deadlines for certain taxpayers.</p><p>Under current law, the IRS may postpone federal tax deadlines for taxpayers affected by a federally declared disaster, including (but not limited to) deadlines for (1) filing federal tax returns, (2) paying federal taxes, (3) making retirement plan contributions, and (4) tax assessments and collections.</p><p>The bill authorizes the IRS to postpone such federal tax deadlines for taxpayers affected by a qualified state declared disaster upon written request by the state\u2019s governor (or the District of\u00a0Columbia mayor). Under the bill, a state includes the District of Columbia, Puerto Rico, the U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.</p><p>The bill defines <em>qualified state declared disaster</em> as any natural catastrophe,\u00a0fire, flood, or explosion that causes damage of sufficient severity and magnitude to warrant a request to postpone such federal tax deadlines.</p><p>Further, under current law, an automatic 60-day extension of such federal tax deadlines applies to certain relief workers, individuals killed or injured as a result of a federally declared disaster, and taxpayers whose principal residence, business, or tax records are located in a federally declared disaster area.</p><p>The bill increases to 120 days the automatic extension of federal tax deadlines for these\u00a0taxpayers.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s132"
    },
    "title": "Filing Relief for Natural Disasters Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Filing Relief for Natural Disasters Act</strong></p><p>This bill authorizes the Internal Revenue Service (IRS) to postpone federal tax deadlines for taxpayers affected by a qualified state declared disaster, upon written request by the state governor. The bill also increases the automatic extension of federal tax deadlines for certain taxpayers.</p><p>Under current law, the IRS may postpone federal tax deadlines for taxpayers affected by a federally declared disaster, including (but not limited to) deadlines for (1) filing federal tax returns, (2) paying federal taxes, (3) making retirement plan contributions, and (4) tax assessments and collections.</p><p>The bill authorizes the IRS to postpone such federal tax deadlines for taxpayers affected by a qualified state declared disaster upon written request by the state\u2019s governor (or the District of\u00a0Columbia mayor). Under the bill, a state includes the District of Columbia, Puerto Rico, the U.S. Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.</p><p>The bill defines <em>qualified state declared disaster</em> as any natural catastrophe,\u00a0fire, flood, or explosion that causes damage of sufficient severity and magnitude to warrant a request to postpone such federal tax deadlines.</p><p>Further, under current law, an automatic 60-day extension of such federal tax deadlines applies to certain relief workers, individuals killed or injured as a result of a federally declared disaster, and taxpayers whose principal residence, business, or tax records are located in a federally declared disaster area.</p><p>The bill increases to 120 days the automatic extension of federal tax deadlines for these\u00a0taxpayers.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119s132"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s132is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Filing Relief for Natural Disasters Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:18:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Filing Relief for Natural Disasters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify the rules for postponing certain deadlines by reason of disaster.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:22Z"
    }
  ]
}
```
