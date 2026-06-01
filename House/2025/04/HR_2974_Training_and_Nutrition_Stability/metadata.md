# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2974?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2974
- Title: Training and Nutrition Stability
- Congress: 119
- Bill type: HR
- Bill number: 2974
- Origin chamber: House
- Introduced date: 2025-04-21
- Update date: 2025-10-29T08:06:18Z
- Update date including text: 2025-10-29T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-21: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-04-21: Introduced in House

## Actions

- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-21",
    "latestAction": {
      "actionDate": "2025-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2974",
    "number": "2974",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "E000297",
        "district": "13",
        "firstName": "Adriano",
        "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
        "lastName": "Espaillat",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Training and Nutrition Stability",
    "type": "HR",
    "updateDate": "2025-10-29T08:06:18Z",
    "updateDateIncludingText": "2025-10-29T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-21",
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
          "date": "2025-04-21T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NC"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "OH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MO"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2974ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2974\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2025 Mr. Espaillat (for himself, Mr. Bresnahan , Ms. Adams , Mr. Miller of Ohio , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to exempt workforce training dollars as income for supplemental nutrition assistance program beneficiaries.\n#### 1. Short title\nThis Act may be cited as the Training and Nutrition Stability Act .\n#### 2. Amendment to the supplemental nutrition assistance program\nSection 5 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014 ) is amended by striking subsection (l).\n#### 3. Exclusion for income from employment and training program\nSection 5(d) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(d) ) is amended\u2014\n**(1)**\nin paragraph (18) by striking and at the end,\n**(2)**\nin paragraph (19) by striking the period at the end and inserting ; and , and\n**(3)**\nby adding at the end the following:\n(20) Income a household member receives from allowances, earning, and payments to household members participating in any program defined in section 6(o)(1), any program established under section 6(d)(4), any vocational rehabilitation program established and defined under the Rehabilitation Act of 1973, and any refugee employment program established and defined under section 412(c) of the Immigration and Nationality Act. .",
      "versionDate": "2025-04-21",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-18T14:23:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-21",
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
          "measure-id": "id119hr2974",
          "measure-number": "2974",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2974v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-04-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Training and Nutrition Stability Act</strong></p><p>This bill excludes specific employment and training program funds from income when determining eligibility for the Supplemental Nutrition Assistance Program (SNAP).</p><p>As background, a\u00a0household must have an income below a certain level to qualify for SNAP program benefits.\u00a0Certain allowances, earnings, and payments do not count towards a household's income.</p><p>Under this bill, examples\u00a0of programs excluded from income\u00a0include Workforce Innovation and Opportunity Act (WIOA) programs, vocational rehabilitation programs, and refugee employment programs.</p><p>This bill also removes the requirement that earnings from on-the-job training be considered earned income for purposes of determining SNAP eligibility.</p>"
        },
        "title": "Training and Nutrition Stability"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2974.xml",
    "summary": {
      "actionDate": "2025-04-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Training and Nutrition Stability Act</strong></p><p>This bill excludes specific employment and training program funds from income when determining eligibility for the Supplemental Nutrition Assistance Program (SNAP).</p><p>As background, a\u00a0household must have an income below a certain level to qualify for SNAP program benefits.\u00a0Certain allowances, earnings, and payments do not count towards a household's income.</p><p>Under this bill, examples\u00a0of programs excluded from income\u00a0include Workforce Innovation and Opportunity Act (WIOA) programs, vocational rehabilitation programs, and refugee employment programs.</p><p>This bill also removes the requirement that earnings from on-the-job training be considered earned income for purposes of determining SNAP eligibility.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr2974"
    },
    "title": "Training and Nutrition Stability"
  },
  "summaries": [
    {
      "actionDate": "2025-04-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Training and Nutrition Stability Act</strong></p><p>This bill excludes specific employment and training program funds from income when determining eligibility for the Supplemental Nutrition Assistance Program (SNAP).</p><p>As background, a\u00a0household must have an income below a certain level to qualify for SNAP program benefits.\u00a0Certain allowances, earnings, and payments do not count towards a household's income.</p><p>Under this bill, examples\u00a0of programs excluded from income\u00a0include Workforce Innovation and Opportunity Act (WIOA) programs, vocational rehabilitation programs, and refugee employment programs.</p><p>This bill also removes the requirement that earnings from on-the-job training be considered earned income for purposes of determining SNAP eligibility.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr2974"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2974ih.xml"
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
      "title": "Training and Nutrition Stability",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-07T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Training and Nutrition Stability",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to exempt workforce training dollars as income for supplemental nutrition assistance program beneficiaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-07T04:33:28Z"
    }
  ]
}
```
