# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8545?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8545
- Title: Access to Donor Milk Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8545
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-13T21:00:36Z
- Update date including text: 2026-05-13T21:00:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-28 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-28 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8545",
    "number": "8545",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Access to Donor Milk Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T21:00:36Z",
    "updateDateIncludingText": "2026-05-13T21:00:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-28T13:01:40Z",
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
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "OK"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8545ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8545\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Ms. Houlahan (for herself, Mrs. Bice , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo protect and expand access to pasteurized, donor human milk, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Donor Milk Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Donor human milk**\nThe term donor human milk means human milk that is collected, pasteurized, and dispensed without additives.\n**(2) Donor human milk-derived product**\nThe term donor human milk-derived product means a product made predominantly from donor human milk\u2014\n**(A)**\nfrom which one or more components has been removed in order to produce a specialty nutritional product; or\n**(B)**\nto which one or more human milk or non-human milk components has been added to produce such a product.\n**(3) Donor human milk bank**\nThe term donor human milk bank means an organization that\u2014\n**(A)**\nmeets standards established by the Food and Drug Administration for purposes of ensuring the safety of donor human milk and human milk banks, including such standards as may be prescribed pursuant to section 6; and\n**(B)**\ncollects, tests, processes, pasteurizes, and distributes, in compliance with applicable Federal and State law, donor human milk or donor human milk derived products.\n**(4) Nonprofit donor human milk bank**\nThe term nonprofit donor human milk bank means a donor human milk bank that is an organization\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ); and\n**(B)**\nexempt from taxation under section 501(a) of such Code ( 26 U.S.C. 501(a) ).\n#### 3. Support for donor human milk activities\nSection 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ) is amended\u2014\n**(1)**\nin subsection (b)(4), by inserting (including support for donor human milk (as defined in section 2 of the Access to Donor Milk Act of 2026 ) activities) after promotion ; and\n**(2)**\nin subsection (h)(1)(C)\u2014\n**(A)**\nin clause (i), by striking clause (ii) and inserting clauses (ii) and (iii) ; and\n**(B)**\nby adding at the end the following:\n(iii) Donor human milk A State agency may use amounts made available under clause (i) for\u2014 (I) collecting and storing donations of unprocessed human milk; and (II) the transfer of the milk described in subclause (I) to a nonprofit donor human milk bank (as defined in section 2 of the Access to Donor Milk Act of 2026 ). .\n#### 4. Emergency capacity funding for human milk banks\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall award competitive grants, subject to subsection (c), to eligible entities for expanding emergency capacity with respect to banking donor human milk.\n##### (b) Application\nAn eligible entity seeking a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Criteria\nThe Secretary may award grants under subsection (a) only in the event of any of the following:\n**(1)**\nThe Secretary determines that expanded capacity is necessary to respond to any major disaster declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ) or to any public health emergency declared under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ).\n**(2)**\nThe President makes a determination described in section 102(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122(1) ), or the Secretary makes such a determination.\n**(3)**\nThe Secretary determines emergency capacity is needed to ensure adequate supply is available to meet the demand for donor human milk from an eligible entity.\n##### (d) Use of funds\nExpanding emergency capacity pursuant to a grant under this section may include\u2014\n**(1)**\npublicizing the need for donor human milk, especially for high-risk infants;\n**(2)**\nraising awareness and providing resources to families, especially families of high-risk infants, about donor human milk;\n**(3)**\ncovering donor human milk collection, storage, pasteurization, transfer, and processing fees;\n**(4)**\nincreasing staffing and supplies needed at donor human milk banks;\n**(5)**\npurchasing consumable products needed for donor human milk processing; and\n**(6)**\nacquiring equipment for safety and quality processing of donor human milk.\n##### (e) Eligible entity\nFor purposes of this section, the term eligible entity means an entity that\u2014\n**(1)**\nis a nonprofit donor human milk bank; and\n**(2)**\nin the application submitted under subsection (b), demonstrates, with respect to such entity\u2014\n**(A)**\na rapid increase in demand for donor human milk; or\n**(B)**\na shortage of supplies needed to operate a donor human milk bank.\n##### (f) Authorization of appropriations\nFor the purposes of carrying out this section, there are authorized to be appropriated $3,000,000 for fiscal year 2026, and such sums as may be necessary for each fiscal year thereafter.\n#### 5. Public awareness campaign with respect to donor human milk\n##### (a) In general\nThe Secretary of Health and Human Services\u2014\n**(1)**\nshall, acting through the Administrator of the Health Resources and Services Administration, develop a public awareness campaign with respect to the benefits and safety of donor human milk from donor human milk banks; and\n**(2)**\nmay work with nonprofit donor human milk banks.\n##### (b) Distribution of educational materials\nThe public awareness campaign under subsection (a) shall include the distribution of educational materials to\u2014\n**(1)**\nclinicians, such as pediatric specialists, pediatricians, obstetricians, pediatric nutritionists, midwives, and lactation consultants, including international board-certified lactation consultants;\n**(2)**\nexpectant and new parents, with a focus on expectant and new parents that are participating in the special supplemental nutrition program for women, infants, and children program under section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ); and\n**(3)**\ncommunity-based organizations.\n#### 6. Regulatory status of donor human milk\n##### (a) Public meeting\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Health and Human Services (referred to in this section as the Secretary ) shall, for purposes of assisting the Secretary in establishing minimum safety standards for donor human milk and donor human milk-derived products under subsection (c), convene a public meeting.\n##### (b) Safety standards\nIn establishing the safety standards under subsection (c), the Secretary shall take into account\u2014\n**(1)**\nthe unique factors related to donor human milk and donor human milk-derived products;\n**(2)**\nethical considerations;\n**(3)**\nthe protection of the United States donor milk supply; and\n**(4)**\nthe resources available to non-profit milk banks.\n##### (c) Guidance\nNot later than 18 months after the date of enactment of this Act, the Secretary shall issue draft guidance that\u2014\n**(1)**\nestablishes minimum appropriate safety standards for the collection and preparation, storage, handling, and processing through pasteurization, and transfer of donor human milk and donor human milk-derived products; and\n**(2)**\nconsiders the minimum appropriateness of screening, testing, and other processes, to ensure the safety of donor human milk and donor human milk-derived products, as determined by the Secretary.",
      "versionDate": "2026-04-28",
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
        "updateDate": "2026-05-13T21:00:36Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8545ih.xml"
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
      "title": "Access to Donor Milk Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:53:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Donor Milk Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect and expand access to pasteurized, donor human milk, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:48:47Z"
    }
  ]
}
```
