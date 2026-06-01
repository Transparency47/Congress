# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1006?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1006
- Title: Higher Education Accountability Tax Act
- Congress: 119
- Bill type: HR
- Bill number: 1006
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2026-05-06T18:20:50Z
- Update date including text: 2026-05-06T18:20:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1006",
    "number": "1006",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000295",
        "district": "14",
        "firstName": "David",
        "fullName": "Rep. Joyce, David P. [R-OH-14]",
        "lastName": "Joyce",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Higher Education Accountability Tax Act",
    "type": "HR",
    "updateDate": "2026-05-06T18:20:50Z",
    "updateDateIncludingText": "2026-05-06T18:20:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:02:50Z",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1006ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1006\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Joyce of Ohio (for himself and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify the excise tax on investment income of private colleges and universities.\n#### 1. Short title\nThis Act may be cited as the Higher Education Accountability Tax Act .\n#### 2. Modification of excise tax on investment income of private colleges and universities\n##### (a) Increase in rate of tax\nSection 4968(a) of the Internal Revenue Code of 1986 is amended by striking 1.4 percent and inserting 10 percent .\n##### (b) Additional increase in rate of tax for institutions with increases in net price\n**(1) In general**\nSection 4968(a) of such Code, as amended by subsection (a), is amended by inserting (20 percent in the case of a net-price-increase institution) after 10 percent .\n**(2) Net-price-increase institution**\nSection 4968(b) of such Code is amended by redesignating paragraph (2) as paragraph (3) and by inserting after paragraph (1) the following new paragraph:\n(2) Net-price-increase institution The term net-price-increase institution means any applicable educational institution for any taxable year if, during the 3-taxable-year period ending with the taxable year immediately preceding such taxable year, the net price of such institution increased at a rate which exceeds the rate of increase in the Consumer Price Index (as defined in section 1(f)(5)) for such period. For purposes of the preceding sentence, the term net price has the meaning given such term by section 132(a)(3) of the Higher Education Act of 1986 ( 20 U.S.C. 1015a(a)(3) ) except that such price shall be determined by taking into account all first-time, full-time undergraduate students at the institution (in addition to such students who receive student aid). .\n##### (c) Expansion of institutions subject to tax\nSection 4968(b)(1)(D) of such Code is amended by striking $500,000 and inserting $250,000 .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-02-05",
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
        "updateDate": "2025-05-05T14:59:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
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
          "measure-id": "id119hr1006",
          "measure-number": "1006",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-05",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1006v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Higher Education Accountability Tax Act </strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments and expands the number of universities and colleges that are subject to the excise tax.</p><p>Under current law,\u00a0certain private universities and colleges\u00a0with 500 or more tuition-paying students (of which more than 50% are located in the United States) and endowment assets of at least $500,000 per student (per student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments. Endowment assets that are used directly in carrying out the institution's tax-exempt educational purpose are excluded from\u00a0the tax.</p><p>The bill increases the amount of the excise tax to (1) 10% of the net investment income from a university and college endowment, or (2) 20% of the net investment income from a university and college endowment maintained by an institution that increases tuition over a three-year period (preceding the current tax year) at a rate that is higher than the inflation rate.</p><p>Under the bill, the tuition price for purposes of determining whether the 20% excise tax rate applies is the average yearly price charged to all first-time, full-time undergraduate students (including students who receive financial aid).\u00a0</p><p>Further, the bill expands the number of universities and colleges subject to the excise tax by lowering the per student threshold to $250,000.</p>"
        },
        "title": "Higher Education Accountability Tax Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1006.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Higher Education Accountability Tax Act </strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments and expands the number of universities and colleges that are subject to the excise tax.</p><p>Under current law,\u00a0certain private universities and colleges\u00a0with 500 or more tuition-paying students (of which more than 50% are located in the United States) and endowment assets of at least $500,000 per student (per student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments. Endowment assets that are used directly in carrying out the institution's tax-exempt educational purpose are excluded from\u00a0the tax.</p><p>The bill increases the amount of the excise tax to (1) 10% of the net investment income from a university and college endowment, or (2) 20% of the net investment income from a university and college endowment maintained by an institution that increases tuition over a three-year period (preceding the current tax year) at a rate that is higher than the inflation rate.</p><p>Under the bill, the tuition price for purposes of determining whether the 20% excise tax rate applies is the average yearly price charged to all first-time, full-time undergraduate students (including students who receive financial aid).\u00a0</p><p>Further, the bill expands the number of universities and colleges subject to the excise tax by lowering the per student threshold to $250,000.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1006"
    },
    "title": "Higher Education Accountability Tax Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Higher Education Accountability Tax Act </strong></p><p>This bill increases the excise tax on the net investment income of certain private university and college endowments and expands the number of universities and colleges that are subject to the excise tax.</p><p>Under current law,\u00a0certain private universities and colleges\u00a0with 500 or more tuition-paying students (of which more than 50% are located in the United States) and endowment assets of at least $500,000 per student (per student threshold) pay an excise tax in the amount of 1.4% on the net investment income from such endowments. Endowment assets that are used directly in carrying out the institution's tax-exempt educational purpose are excluded from\u00a0the tax.</p><p>The bill increases the amount of the excise tax to (1) 10% of the net investment income from a university and college endowment, or (2) 20% of the net investment income from a university and college endowment maintained by an institution that increases tuition over a three-year period (preceding the current tax year) at a rate that is higher than the inflation rate.</p><p>Under the bill, the tuition price for purposes of determining whether the 20% excise tax rate applies is the average yearly price charged to all first-time, full-time undergraduate students (including students who receive financial aid).\u00a0</p><p>Further, the bill expands the number of universities and colleges subject to the excise tax by lowering the per student threshold to $250,000.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr1006"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1006ih.xml"
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
      "title": "Higher Education Accountability Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Higher Education Accountability Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modify the excise tax on investment income of private colleges and universities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:31Z"
    }
  ]
}
```
