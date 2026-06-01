# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2665?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2665
- Title: Drug Shortage Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2665
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T19:59:54Z
- Update date including text: 2025-09-18T19:59:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2665",
    "number": "2665",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Drug Shortage Prevention Act of 2025",
    "type": "S",
    "updateDate": "2025-09-18T19:59:54Z",
    "updateDateIncludingText": "2025-09-18T19:59:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T22:24:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "ME"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "AK"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2665is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2665\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Ms. Klobuchar (for herself, Ms. Collins , Ms. Warren , Ms. Murkowski , Ms. Smith , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to provide for notification by manufacturers of critical drugs of increased demand, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Shortage Prevention Act of 2025 .\n#### 2. Improving notification procedures in case of increased demand for critical drugs\n##### (a) In general\nSection 506C of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c ) is amended\u2014\n**(1)**\nin the section heading, by striking Discontinuance or interruption in the production of life-saving drugs and inserting Notification of issues affecting domestic supply of critical drugs ;\n**(2)**\nby striking subsections (a), (b), and (c), and inserting the following:\n(a) Notification required (1) In general A manufacturer of a covered drug shall notify the Secretary, in accordance with subsection (b), of\u2014 (A) (i) a permanent discontinuance in the manufacture of the drug or an interruption of the manufacture of the drug that is likely to lead to a meaningful disruption in the supply of such drug in the United States; (ii) a permanent discontinuance in the manufacture of an active pharmaceutical ingredient of such drug, or an interruption in the manufacture of an active pharmaceutical ingredient of such drug that is likely to lead to a meaningful disruption in the supply of the active pharmaceutical ingredient of such drug; or (iii) any other circumstance, such as an increase in demand or export restriction, that is likely to leave the manufacturer unable to meet demand for the drug without a meaningful shortfall or delay; and (B) the reasons for such discontinuance, interruption, or other circumstance, if known. (2) Contents Notification under this subsection with respect to a covered drug shall include\u2014 (A) with respect to the reasons for the discontinuation, interruption, or other circumstance described in paragraph (1)(A)(iii), if an active pharmaceutical ingredient is a reason for, or risk factor in, such discontinuation, interruption, or other circumstance, the source of the active pharmaceutical ingredient and any alternative sources for the active pharmaceutical ingredient known to the manufacturer; (B) whether any associated device used for preparation or administration included in the drug is a reason for, or a risk factor in, such discontinuation, interruption, or other circumstance described in paragraph (1)(A)(iii); (C) the expected duration of the interruption; and (D) such other information as the Secretary may require. (b) Timing A notice required under subsection (a) shall be submitted to the Secretary\u2014 (1) at least 6 months prior to the date of the discontinuance or interruption; (2) in the case of such a notice with respect to a circumstance described in subsection (a)(1)(A)(iii), as soon as practicable, or not later than 10 business days after the onset of the circumstance; or (3) if compliance with paragraph (1) or (2) is not possible, as soon as practicable. (c) Distribution To the maximum extent practicable, the Secretary shall distribute, through such means as the Secretary determines appropriate, information on the discontinuance or interruption of the manufacture of, or other circumstance described in subsection (a)(1)(A)(iii) that is likely to lead to a shortage or meaningful disruption in the supply of, covered drugs to appropriate organizations, including physician, health provider, and patient organizations, as described in section 506E. ;\n**(3)**\nin subsection (g), in the matter preceding paragraph (1), by striking drug described in subsection (a) and inserting covered drug ; and\n**(4)**\nin subsection (j), by striking drug described in subsection (a) and inserting covered drug .\n##### (b) Definitions\nParagraph (1) of section 506C(h) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 356c(h) ) is amended to read as follows:\n(1) the term covered drug means a drug that is intended for human use and that\u2014 (A) is\u2014 (i) life-supporting; (ii) life-sustaining; or (iii) intended for use in the prevention or treatment of a debilitating disease or condition, including any such drug used in emergency medical care or during surgery or any such drug that is critical to the public health during a public health emergency declared by the Secretary under section 319 of the Public Health Service Act; (B) is not a radio pharmaceutical drug product or any other product as designated by the Secretary; and (C) is not a biological product (as defined in section 351(i) of the Public Health Service Act), unless otherwise provided by the Secretary in the regulations promulgated under subsection (i); .\n#### 3. Reporting on supply chains\nSection 510(j)(3)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(j)(3)(A) ) is amended\u2014\n**(1)**\nby striking annually to the Secretary in the first sentence and inserting to the Secretary, once during the month of March each year and once during the month of September each year, ;\n**(2)**\nby inserting , and the legal names of, and any additional information the Secretary may require, regarding suppliers of active pharmaceutical ingredients and intermediate and in-process materials such person used for the manufacture, preparation, propagation, compounding, or processing of such drug, and the amount of such drug manufactured, prepared, propagated, compounded, or processed using each such active pharmaceutical ingredient or intermediate or in-process material sourced from each such supplier before the period at the end of the first sentence; and\n**(3)**\nby inserting after the first sentence the following: In addition to the reporting required under the preceding sentence, each person who registers with the Secretary under this section with regard to a drug may voluntarily report on the information described in the preceding sentence, at such other times as the Secretary may specify. .",
      "versionDate": "2025-08-01",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-18T19:59:54Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2665is.xml"
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
      "title": "Drug Shortage Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Drug Shortage Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to provide for notification by manufacturers of critical drugs of increased demand, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:19Z"
    }
  ]
}
```
