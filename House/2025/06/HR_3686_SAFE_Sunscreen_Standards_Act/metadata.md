# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3686
- Title: SAFE Sunscreen Standards Act
- Congress: 119
- Bill type: HR
- Bill number: 3686
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2026-02-24T23:06:17Z
- Update date including text: 2026-02-24T23:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3686",
    "number": "3686",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "J000302",
        "district": "13",
        "firstName": "John",
        "fullName": "Rep. Joyce, John [R-PA-13]",
        "lastName": "Joyce",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "SAFE Sunscreen Standards Act",
    "type": "HR",
    "updateDate": "2026-02-24T23:06:17Z",
    "updateDateIncludingText": "2026-02-24T23:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:03:40Z",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MI"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "OH"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "MA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MI"
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
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3686ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3686\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Joyce of Pennsylvania (for himself, Mrs. Dingell , Mr. Joyce of Ohio , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to improve the regulatory review process to determine the safety and effectiveness of nonprescription sunscreen active ingredients, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Accessible, Flexible, and Effective Sunscreen Standards or the SAFE Sunscreen Standards Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSkin cancer is the most common cancer in the United States.\n**(2)**\nMore people are diagnosed with skin cancer each year in the United States than all other cancers combined.\n**(3)**\nThe United States Surgeon General issued a Call to Action to Prevent Skin Cancer in 2014 based on finding that nearly 5,000,000 Americans are treated for skin cancer each year at a cost that exceeds $8,100,000,000.\n**(4)**\nIt is estimated that the number of new melanoma cases diagnosed in 2024 will increase by 7.3 percent, with an estimated 200,340 cases of melanoma diagnosed.\n**(5)**\nSkin cancer is a deadly disease, and it is expected that there will be 8,290 deaths from melanoma in 2024.\n**(6)**\nSkin cancer affects individuals of all ages, and melanoma is one of the most common cancers in young adults.\n**(7)**\nIn the United States, more than 9,500 people are diagnosed with skin cancer every day and more than 2 people die of the disease every hour.\n**(8)**\nAccording to the World Health Organization ( WHO ), 4 out of 5 cases of skin cancer can be prevented by adopting sun-safe practices.\n**(9)**\nAccording to the Environmental Protection Agency ( EPA ), the Ultraviolet (UV) Index in the United States continues to rise, increasing the risk of melanoma and other skin cancers for Americans.\n**(10)**\nThe EPA recommends Americans Use a broad spectrum sunscreen with a Sun Protection Factor ( SPF ) of at least 30 to protect against the risks of a rising UV Index.\n**(11)**\nCongress unanimously passed the Sunscreen Innovation Act in 2014 to streamline the approval process for sunscreen active ingredients to improve access to new sunscreens, but no new sunscreen active ingredients have been approved through the Food and Drug Administration\u2019s over-the-counter approval process since 1999.\n#### 3. Regulations establishing requirements for sunscreen active ingredients\nSection 505G of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355h ) is amended by adding at the end the following:\n(r) Regulations establishing requirements for sunscreen active ingredients (1) Evidence and testing standards for sunscreen active ingredients The Secretary shall establish, through guidance or regulation, standards for evaluating the safety and efficacy of sunscreen active ingredients, provided that such standards\u2014 (A) ensure the safety of consumers based on a comprehensive evaluation of scientific evidence; (B) allow for the use of real-world evidence (as defined in section 505F(b)), observational studies, and other scientifically valid approaches in place of, or to supplement, traditional clinical tests to demonstrate safety and effectiveness; and (C) apply subsection (b)(6)(C) to the regulation of sunscreen active ingredients in demonstrating a prima facie safe nonprescription marketing and use. (2) Non-animal testing methods for sunscreen active ingredients (A) In general The Secretary shall consider the types of nonclinical tests described in paragraphs (1) through (4) of the first subsection (z) of section 505 (as inserted by section 3209(a)(2) of the Health Extenders, Improving Access to Medicare, Medicaid, and CHIP, and Strengthening Public Health Act of 2022 (division FF of Public Law 117\u2013328 )), or any other alternative to animal testing that the Secretary deems appropriate, in the consideration of sunscreen active ingredients. (B) Guidance Not later than 180 days after the date of enactment of this subsection, the Secretary shall issue new guidance on how sponsors can use nonclinical testing alternatives to animal testing to meet safety and efficacy standards for sunscreen active ingredients. .\n#### 4. Sunscreen final administrative order\nThe final administrative order on pending over-the-counter sunscreen active ingredient submissions issued under section 3854 of the Coronavirus Aid, Relief, and Economic Security Act ( Public Law 116\u2013136 ; 21 U.S.C. 360fff\u20133 note) shall\u2014\n**(1)**\naccount for historical data demonstrating safe use of sunscreen active ingredients that have previously been accepted for marketing in the United States;\n**(2)**\nemphasize that sunscreen is an effective skin cancer prevention tool; and\n**(3)**\nincorporate the evidence and testing standards for sunscreen active ingredients detailed in section 505G(r) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355h ) (as added by section 3).\n#### 5. Reporting and transparency\n##### (a) To Congress\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall, beginning not later than 1 year after the date of enactment of this Act, annually submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Health, Education, Labor, and Pensions of the Senate a report describing\u2014\n**(1)**\nthe status of implementation of evidence and testing standards for sunscreen active ingredients, including\u2014\n**(A)**\nany adjustments to evidence or testing standards made under section 505G(r) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355h ) (as added by section 3); and\n**(B)**\nthe number and types of sunscreen active ingredient applications reviewed using the standards under such section 505G(r); and\n**(2)**\nthe progress of the Food and Drug Administration in allowing nonclinical testing alternatives to animal testing for the consideration of sunscreen active ingredients.\n##### (b) Publication\nNot later than 7 days after the date on which the Secretary submits a report under subsection (a), the Secretary shall publish such report on the website of the Food and Drug Administration.",
      "versionDate": "2025-06-03",
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
        "updateDate": "2025-06-23T14:03:43Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3686ih.xml"
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
      "title": "SAFE Sunscreen Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE Sunscreen Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Accessible, Flexible, and Effective Sunscreen Standards",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to improve the regulatory review process to determine the safety and effectiveness of nonprescription sunscreen active ingredients, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:22Z"
    }
  ]
}
```
