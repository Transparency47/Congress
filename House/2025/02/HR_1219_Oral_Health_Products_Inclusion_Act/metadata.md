# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1219?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1219
- Title: Oral Health Products Inclusion Act
- Congress: 119
- Bill type: HR
- Bill number: 1219
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-09-16T08:05:36Z
- Update date including text: 2025-09-16T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1219",
    "number": "1219",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Oral Health Products Inclusion Act",
    "type": "HR",
    "updateDate": "2025-09-16T08:05:36Z",
    "updateDateIncludingText": "2025-09-16T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:03:10Z",
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
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "IL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1219ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1219\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Van Drew (for himself, Mr. Schneider , Ms. Malliotakis , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to include over-the-counter oral healthcare products as qualified medical expenses which can be purchased with HSA and FSA funds.\n#### 1. Short title\nThis Act may be cited as the Oral Health Products Inclusion Act .\n#### 2. Inclusion of certain over-the-counter medical products as qualified medical expenses\n##### (a) HSAs\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (A), by inserting , toothbrushes (manual or electric), water flossers, or oral healthcare products after amounts paid for menstrual care products , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Oral healthcare product For purposes of this paragraph, the term oral healthcare product means an over-the-counter anticaries drug product or antiplaque or antigingivitis over-the-counter drug product suitable for topical administration to the teeth or gums that is generally recognized as safe and effective under section 505G of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355f ). .\n##### (b) Archer MSAs\nSection 220(d)(2)(A) of such Code is amended by inserting , toothbrushes (manual or electric), water flossers, or oral healthcare products (as defined in section 223(d)(2)(E)) after amounts paid for menstrual care products (as defined in section 223(d)(2)(D)) .\n##### (c) Health flexible spending arrangements and health reimbursement arrangements\nSection 106 of such Code is amended by adding at the end the following new subsection:\n(h) Reimbursement for toothbrushes, water flossers, and oral healthcare products For purposes of this section and section 105, expenses incurred for toothbrushes (manual or electric), water flossers, and oral healthcare products (as defined in section 223(d)(2)(E)) shall be treated as incurred for medical care. .\n##### (d) Effective date\nThe amendments made by this section shall apply to expenses incurred after the date of the enactment of this Act.",
      "versionDate": "2025-02-11",
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
        "updateDate": "2025-04-03T14:33:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1219",
          "measure-number": "1219",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1219v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Oral Health Products Inclusion Act</strong></p><p>This bill allows individuals to use funds in a flexible spending arrangement (FSA), health reimbursement arrangement (HRA), health savings account (HSA), or Archer medical savings account (Archer MSA) to pay for toothbrushes (manual or electric), water flossers, and oral health products.</p><p>Under current law, reimbursements from an FSA or HRA and tax-free distributions from an HSA or Archer MSA may be used to pay for the qualified medical expenses. Reimbursements from an FSA or HRA for nonmedical expenses generally are not allowed and distributions from an HSA or Archer MSA for nonmedical expenses generally are taxed as income and may be subject to an additional penalty.</p><p>Under the bill, the definition of qualified medical expenses is expanded to include toothbrushes (manual or electric), water flossers, and oral health products.</p><p>The bill defines an <em>oral health product</em> as an over-the-counter product that is (1) used for preventing or treating dental cavities, plaque, or gingivitis;\u00a0(2) suitable for topical administration to the teeth or gums; and (3) generally recognized as safe and effective.\u00a0</p>"
        },
        "title": "Oral Health Products Inclusion Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1219.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Oral Health Products Inclusion Act</strong></p><p>This bill allows individuals to use funds in a flexible spending arrangement (FSA), health reimbursement arrangement (HRA), health savings account (HSA), or Archer medical savings account (Archer MSA) to pay for toothbrushes (manual or electric), water flossers, and oral health products.</p><p>Under current law, reimbursements from an FSA or HRA and tax-free distributions from an HSA or Archer MSA may be used to pay for the qualified medical expenses. Reimbursements from an FSA or HRA for nonmedical expenses generally are not allowed and distributions from an HSA or Archer MSA for nonmedical expenses generally are taxed as income and may be subject to an additional penalty.</p><p>Under the bill, the definition of qualified medical expenses is expanded to include toothbrushes (manual or electric), water flossers, and oral health products.</p><p>The bill defines an <em>oral health product</em> as an over-the-counter product that is (1) used for preventing or treating dental cavities, plaque, or gingivitis;\u00a0(2) suitable for topical administration to the teeth or gums; and (3) generally recognized as safe and effective.\u00a0</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr1219"
    },
    "title": "Oral Health Products Inclusion Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Oral Health Products Inclusion Act</strong></p><p>This bill allows individuals to use funds in a flexible spending arrangement (FSA), health reimbursement arrangement (HRA), health savings account (HSA), or Archer medical savings account (Archer MSA) to pay for toothbrushes (manual or electric), water flossers, and oral health products.</p><p>Under current law, reimbursements from an FSA or HRA and tax-free distributions from an HSA or Archer MSA may be used to pay for the qualified medical expenses. Reimbursements from an FSA or HRA for nonmedical expenses generally are not allowed and distributions from an HSA or Archer MSA for nonmedical expenses generally are taxed as income and may be subject to an additional penalty.</p><p>Under the bill, the definition of qualified medical expenses is expanded to include toothbrushes (manual or electric), water flossers, and oral health products.</p><p>The bill defines an <em>oral health product</em> as an over-the-counter product that is (1) used for preventing or treating dental cavities, plaque, or gingivitis;\u00a0(2) suitable for topical administration to the teeth or gums; and (3) generally recognized as safe and effective.\u00a0</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr1219"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1219ih.xml"
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
      "title": "Oral Health Products Inclusion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Oral Health Products Inclusion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to include over-the-counter oral healthcare products as qualified medical expenses which can be purchased with HSA and FSA funds.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:27Z"
    }
  ]
}
```
