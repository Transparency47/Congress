# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4306?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4306
- Title: Food Chemical Reassessment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4306
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-04-22T08:07:13Z
- Update date including text: 2026-04-22T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4306",
    "number": "4306",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Food Chemical Reassessment Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:13Z",
    "updateDateIncludingText": "2026-04-22T08:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:04:10Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CT"
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
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IN"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "WA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "ME"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NV"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MI"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "IL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4306ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4306\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Schakowsky (for herself, Ms. DeLauro , Ms. Adams , Mr. Carson , Ms. Jayapal , Mr. Khanna , Mr. Krishnamoorthi , Ms. Meng , Mr. Moulton , Mr. Mullin , Ms. Norton , Ms. Pingree , Ms. Titus , and Ms. Tlaib ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to require the Office of Food Chemical Safety, Dietary Supplements, and Innovation to conduct food chemical safety reassessments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Food Chemical Reassessment Act of 2025 .\n#### 2. Food safety reassessments\nSection 409 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 348 ) is amended by adding at the end the following:\n(l) Food safety reassessments (1) In general Not less frequently than once every 3 years beginning with 2026, the Office of Food Chemical Safety, Dietary Supplements, and Innovation (referred to in this section as the Office ), shall systematically and continuously reassess the safety of not less than a combination of 10 of the following substances (or classes thereof): (A) Food additives marketed pursuant to an order under subsection (c). (B) Color additives, as defined in section 201(t). (C) Substances generally recognized as safe for use in food (as defined in section 201(s)). (D) Prior-sanctioned substances, or classes thereof (as described in section 201(s)(4)). (E) Food contact substances, as defined in subsection (h)(6). (2) Public notice The Secretary shall provide public notice of the determinations made from each reassessment conducted under paragraph (1). (3) Effect of reassessment The Secretary shall\u2014 (A) in the case of a reassessment of a substance described in subparagraph (A) of paragraph (1), amend or repeal a regulation under subsection (c) issued with respect to such substance if such reassessment demonstrates that the substance is not safe; (B) in the case of a reassessment of a substance described in subparagraph (B) of paragraph (1), amend or repeal a regulation under section 721 issued with respect to such substance if such reassessment demonstrates that the substance is not safe; (C) in the case of a reassessment of a substance described in subparagraph (C) of paragraph (1), make public on the website of the Food and Drug Administration the determination that\u2014 (i) any such substance is safe for purposes of this subsection and establishing the conditions of use, if any, under which any such substance or class of substances can be used safely; or (ii) any such substance or class of substances is unsafe for purposes of this section; (D) in the case of a reassessment of a substance described in subparagraph (D) of paragraph (1), revoke the prior-sanctioned use of the substance if such reassessment demonstrates the prior-sanctioned use of such substance may be injurious to health; and (E) in the case of a reassessment of a substance described in subparagraph (E) of paragraph (1), determine that a pre-market notification under subsection (h) for the food contact substance involved is no longer effective if such reassessment demonstrates that the use of such substance is not safe. (4) Determination of substances subject to reassessment (A) In general In determining which substances or classes of substances to reassess under paragraph (1), the Secretary shall prioritize substances or classes thereof by public health need. (B) First substances subject to reassessment The Secretary may select, as the first 10 substances (or classes thereof) to be reassessed under this subsection, the following: (i) Tert-butylhydroquinone. (ii) Titanium dioxide. (iii) Red dye 40, yellow dye 5, yellow dye 6, blue dye 01, blue dye 02, and green dye 03. (iv) Perchlorate. (v) Butylated hydroxyanisole (BHA). (vi) Butylated hydroxytoluene (BHT). (vii) Trichloroethylene, methylene chloride, benzene, and ethylene chloride. (viii) Propyl gallate. (ix) Sodium benzoate. (x) Sodium nitrite. (5) Rule of construction Nothing in this subsection alters the authority or duties of the Secretary with respect to the administration and enforcement of the preceding provisions of this section. (6) Food advisory committee Not later than 180 days after the date of enactment of the Food Chemical Reassessment Act of 2025, the Secretary shall re-establish the Food Advisory Committee to advise the Secretary with respect to\u2014 (A) the standards for reassessments conducted under this section; and (B) the process and methods necessary to complete the work of the Office. (7) Class defined In this subsection, the term class , with respect to substances referred to in paragraph (1), means a group of chemicals that are chemically similar or cause similar or related pharmacological effects. .",
      "versionDate": "2025-07-10",
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
        "updateDate": "2025-07-30T13:48:50Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4306ih.xml"
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
      "title": "Food Chemical Reassessment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Food Chemical Reassessment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-22T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to require the Office of Food Chemical Safety, Dietary Supplements, and Innovation to conduct food chemical safety reassessments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-22T05:18:30Z"
    }
  ]
}
```
