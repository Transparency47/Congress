# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4742
- Title: GIVE MILK Act
- Congress: 119
- Bill type: HR
- Bill number: 4742
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-11-05T09:05:54Z
- Update date including text: 2025-11-05T09:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4742",
    "number": "4742",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "GIVE MILK Act",
    "type": "HR",
    "updateDate": "2025-11-05T09:05:54Z",
    "updateDateIncludingText": "2025-11-05T09:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
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
      "sponsorshipDate": "2025-08-15",
      "state": "PA"
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
      "sponsorshipDate": "2025-11-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4742ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4742\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Child Nutrition Act of 1966 to allow certain participants in the special supplemental nutrition program for women, infants, and children to elect to be issued a variety of types of milk, including whole milk, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Giving Increased Variety to Ensure Milk Into the Lives of Kids Act or the GIVE MILK Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nMost Americans, including most children and adolescents, do not consume adequate levels of dairy, on average consuming only about half of the recommended amounts of dairy foods daily.\n**(2)**\nMilk is a source of many nutrients essential to health, and is the leading source of calcium, vitamin D, potassium, and phosphorus for children ages 2\u201318 and is a source of thirteen essential nutrients (calcium, phosphorus, vitamin A, vitamin D (in fortified products), riboflavin, niacin, vitamin B12, protein, potassium, zinc, choline, magnesium, and selenium) in the diets of children and adolescents, including three nutrients of public health concern: vitamin D, calcium, and potassium.\n**(3)**\nDairy foods are associated with improved bone health, a lower risk of type 2 diabetes, a beneficial or neutral effect on blood pressure, and may help reduce the risk of cardiovascular disease, coronary heart disease, and stroke.\n**(4)**\nIn a September 2019 report on beverage recommendations for early childhood, the Academy of Nutrition and Dietetics, American Academy of Pediatric Dentists, American Academy of Pediatrics, and the American Heart Association found that\u2014\n**(A)**\nmedical professionals are in agreement that whole milk is good for childhood development between ages one and two;\n**(B)**\nskim and low-fat milk are recommended for young children;\n**(C)**\nplant-based, non-dairy milks are not recommended for young children; and\n**(D)**\nan expert panel under the study recognized that there has been recent research and discussion regarding the role of dairy fat in healthy dietary patterns but in the absence of clear evidence justifying a departure from current recommendations, such expert panel chose to remain consistent with current guidance recommending whole milk for most children ages 12\u201324 months and fat-free (skim) or low-fat (1 percent) milk for children ages 2 years and older.\n**(5)**\nThe 2020 through 2025 Dietary Guidelines for Americans recommendation of the number of dairy servings for young children is\u2014\n**(A)**\n1.5 to 2 servings for 12 to 23 months; and\n**(B)**\n2 to 2.5 servings for 2 to 4 years.\n#### 3. WIC election for type of milk\n##### (a) Election for type of milk\nSection 17(f) of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786(f) ) is amended by adding at the end the following:\n(27) Election for type of milk (A) In general Notwithstanding any other provision of law, in the case of an individual participating in the program authorized by this section who is issued milk by the Secretary, such individual (or the parent or guardian of such individual) may elect to be issued nonfat milk, low-fat milk, reduced fat milk, or whole milk. (B) Election The Secretary shall issue the type of milk elected by an individual under subparagraph (A) to such individual. .\n##### (b) Revision of regulations\nThe Secretary of Agriculture shall revise regulations in accordance with the amendments made by this section, including revision of section 246.10 of title 7, Code of Federal Regulations.",
      "versionDate": "2025-07-23",
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
        "updateDate": "2025-09-16T22:07:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hr4742",
          "measure-number": "4742",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-09-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4742v00",
            "update-date": "2025-09-17"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Giving Increased Variety to Ensure Milk Into the Lives of Kids Act or the</strong> <strong>GIVE MILK Act </strong></p><p>This bill revises the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to allow WIC participants (or the parent or guardian of such participants) to elect to be issued nonfat milk, 1% low-fat milk, 2% reduced-fat milk, or whole milk.\u00a0Current WIC regulations restrict the milk choices for most women and children who are at least two years old\u00a0to nonfat or 1% milk, with exceptions.</p>"
        },
        "title": "GIVE MILK Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4742.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Giving Increased Variety to Ensure Milk Into the Lives of Kids Act or the</strong> <strong>GIVE MILK Act </strong></p><p>This bill revises the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to allow WIC participants (or the parent or guardian of such participants) to elect to be issued nonfat milk, 1% low-fat milk, 2% reduced-fat milk, or whole milk.\u00a0Current WIC regulations restrict the milk choices for most women and children who are at least two years old\u00a0to nonfat or 1% milk, with exceptions.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119hr4742"
    },
    "title": "GIVE MILK Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Giving Increased Variety to Ensure Milk Into the Lives of Kids Act or the</strong> <strong>GIVE MILK Act </strong></p><p>This bill revises the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC) to allow WIC participants (or the parent or guardian of such participants) to elect to be issued nonfat milk, 1% low-fat milk, 2% reduced-fat milk, or whole milk.\u00a0Current WIC regulations restrict the milk choices for most women and children who are at least two years old\u00a0to nonfat or 1% milk, with exceptions.</p>",
      "updateDate": "2025-09-17",
      "versionCode": "id119hr4742"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4742ih.xml"
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
      "title": "GIVE MILK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GIVE MILK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Giving Increased Variety to Ensure Milk Into the Lives of Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Child Nutrition Act of 1966 to allow certain participants in the special supplemental nutrition program for women, infants, and children to elect to be issued a variety of types of milk, including whole milk, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:29Z"
    }
  ]
}
```
