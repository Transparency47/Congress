# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3665
- Title: Medicare Economic Security Solutions Act
- Congress: 119
- Bill type: HR
- Bill number: 3665
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-12-10T09:05:39Z
- Update date including text: 2025-12-10T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3665",
    "number": "3665",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Medicare Economic Security Solutions Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:39Z",
    "updateDateIncludingText": "2025-12-10T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-29T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "CA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "VA"
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
      "sponsorshipDate": "2025-06-09",
      "state": "DC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "TX"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3665ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3665\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Williams of Georgia (for herself and Mrs. Kim ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to limit the penalty for late enrollment under part B of the Medicare Program to 15 percent and twice the period of no enrollment, and to exclude periods of COBRA, retiree, and VA coverage from such late enrollment penalty.\n#### 1. Short title\nThis Act may be cited as the Medicare Economic Security Solutions Act .\n#### 2. Limiting Medicare part B late enrollment penalty to 15 percent and twice the period of no enrollment\n##### (a) In general\nThe first sentence of section 1839(b) of the Social Security Act ( 42 U.S.C. 1395r(b) ) is amended by striking 10 percent of the monthly premium so determined for each full 12 months and inserting 15 percent of the monthly premium so determined for premiums paid during a period equal to twice the number of months in each of the full periods of 12 months .\n##### (b) Conforming amendments\nSection 1818 of the Social Security Act ( 42 U.S.C. 1395i\u20132 ) is amended\u2014\n**(1)**\nin subsection (c)(6), by striking and shall only apply to premiums paid during a period equal to twice the number of months in the full 12-month periods described in that section and ; and\n**(2)**\nin subsection (g)(2)(B), by striking by substituting and all that follows and inserting the following: by substituting section 1818 (without any increase resulting from the application of section 1839(b) to such section 1818) for section 1839 (without any increase under subsection (b) thereof) . .\n##### (c) Effective date\n**(1) In general**\nThe amendments made by this section shall apply to premiums paid for months beginning after the end of the 90-day period beginning on the date of the enactment of this Act.\n**(2) Clarification**\nIn applying these amendments, months (before, during, or after the month in which this Act is enacted) in which an individual was or is required to pay an increased premium shall be taken into account in determining the month in which the premium will no longer be subject to an increase.\n#### 3. Exclusion of periods of COBRA, retiree, and VA coverage from Medicare part B late enrollment penalty\n##### (a) In general\nThe second sentence of section 1839(b) of the Social Security Act ( 42 U.S.C. 1395r(b) ) is amended\u2014\n**(1)**\nby striking by reason of the individual\u2019s (or the individual\u2019s spouse\u2019s) current employment ; and\n**(2)**\nby inserting or months for which the individual can demonstrate that the individual had coverage under chapter 17 of title 38, United States Code before the period at the end.\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to premiums paid for months beginning after the end of the 90-day period beginning on the date of the enactment of this Act.\n#### 4. Special enrollment period for individuals whose COBRA or retiree coverage terminates\n##### (a) In general\nSection 1837(i) of the Social Security Act ( 42 U.S.C. 1395p(i) ) is amended\u2014\n**(1)**\nin the first sentence of paragraph (1), by striking by reason of the individual's (or the individual\u2019s spouse\u2019s) current employment status in subparagraph (A);\n**(2)**\nin the first sentence of paragraph (2) by striking by reason of the individual's (or the individual\u2019s spouse\u2019s) current employment status each place it appears in subparagraphs (B) and (C); and\n**(3)**\nin paragraph (3)(A) by striking by reason of current employment status .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to terminations of coverage occurring after the end of the 90-day period beginning on the date of the enactment of this Act.",
      "versionDate": "2025-05-29",
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
        "name": "Health",
        "updateDate": "2025-06-13T12:31:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hr3665",
          "measure-number": "3665",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3665v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Medicare Economic Security Solutions Act</b></p> <p>This bill modifies provisions relating to enrollment periods for Medicare medical services. </p> <p>Among other things, the bill establishes a late enrollment penalty of 15% of monthly premiums and applies the penalty for a period equal to twice the number of months in each 12-month period during which the individual was not enrolled. Currently, the late enrollment penalty is 10% of monthly premiums for each 12-month period during which the individual was not enrolled, and the penalty continues to apply for as long as the individual is enrolled in Medicare medical services.</p> <p>The bill also expands the special enrollment periods to individuals who have health insurance coverage other than through their employer.</p>"
        },
        "title": "Medicare Economic Security Solutions Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3665.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicare Economic Security Solutions Act</b></p> <p>This bill modifies provisions relating to enrollment periods for Medicare medical services. </p> <p>Among other things, the bill establishes a late enrollment penalty of 15% of monthly premiums and applies the penalty for a period equal to twice the number of months in each 12-month period during which the individual was not enrolled. Currently, the late enrollment penalty is 10% of monthly premiums for each 12-month period during which the individual was not enrolled, and the penalty continues to apply for as long as the individual is enrolled in Medicare medical services.</p> <p>The bill also expands the special enrollment periods to individuals who have health insurance coverage other than through their employer.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr3665"
    },
    "title": "Medicare Economic Security Solutions Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Medicare Economic Security Solutions Act</b></p> <p>This bill modifies provisions relating to enrollment periods for Medicare medical services. </p> <p>Among other things, the bill establishes a late enrollment penalty of 15% of monthly premiums and applies the penalty for a period equal to twice the number of months in each 12-month period during which the individual was not enrolled. Currently, the late enrollment penalty is 10% of monthly premiums for each 12-month period during which the individual was not enrolled, and the penalty continues to apply for as long as the individual is enrolled in Medicare medical services.</p> <p>The bill also expands the special enrollment periods to individuals who have health insurance coverage other than through their employer.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr3665"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3665ih.xml"
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
      "title": "Medicare Economic Security Solutions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Medicare Economic Security Solutions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to limit the penalty for late enrollment under part B of the Medicare Program to 15 percent and twice the period of no enrollment, and to exclude periods of COBRA, retiree, and VA coverage from such late enrollment penalty.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:37Z"
    }
  ]
}
```
