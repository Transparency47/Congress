# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1100?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1100
- Title: Nutritious SNAP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1100
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-08-19T13:38:51Z
- Update date including text: 2025-08-19T13:38:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1100",
    "number": "1100",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000603",
        "district": "",
        "firstName": "Rand",
        "fullName": "Sen. Paul, Rand [R-KY]",
        "lastName": "Paul",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Nutritious SNAP Act of 2025",
    "type": "S",
    "updateDate": "2025-08-19T13:38:51Z",
    "updateDateIncludingText": "2025-08-19T13:38:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:51:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1100is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1100\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Paul introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act to modify the definition of food under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nutritious SNAP Act of 2025 .\n#### 2. Definition of food; waiver of eligibility of certain food\n##### (a) Definition of food\nSection 3(k) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2012(k) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking home consumption and inserting home consumption, subject to section 11(y), ; and\n**(2)**\nby inserting , any nonalcoholic beverage that is not water, cow's milk, a milk-substitute beverage (such as almond milk, soy milk, and coconut milk), or 100 percent juice, snack and dessert food items (as described in the supplemental guidance document of the Food and Nutrition Service, effective as of March 5, 2018, entitled Accessory Foods List ), before tobacco .\n##### (b) Waiver of eligibility of certain food\nSection 11 of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020 ) is amended by adding at the end the following:\n(y) Waiver of eligibility of certain food The Secretary shall permit a State agency, on request of the State agency, to prohibit the use of benefits to purchase food that the applicable State nutrition agency determines to be unhealthy food. .",
      "versionDate": "2025-03-25",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T14:52:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1100",
          "measure-number": "1100",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-08-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1100v00",
            "update-date": "2025-08-19"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Nutritious SNAP Act of 2025</strong></p><p>This bill prohibits Supplemental Nutrition Assistance Program (SNAP) benefits from being used to purchase certain beverages (e.g., soda) and snack foods.</p><p>Specifically, SNAP benefits may only be used to purchase a beverage that is nonalcoholic and is\u00a0(1) water, (2) cow's milk, (3) a milk-substitute beverage (e.g., almond milk, soy milk, and coconut milk), or (4) 100% juice.</p><p>Further, the bill prohibits the use of benefits to purchase\u00a0snack and dessert food items which are included on the Food and Nutrition Service's Accessory Foods List that went into effect on March 5, 2018.\u00a0Examples of snack and dessert foods on the list include potato and tortilla chips, ice cream, candy, snack cakes and pastries, and packaged baking mixes for cakes, brownies, and muffins.</p><p>In addition, on the request of a state agency, the Department of Agriculture must allow the state agency to prohibit the use of SNAP benefits to purchase food that the applicable\u00a0state nutrition\u00a0agency determines to be<em> </em>unhealthy food.</p>"
        },
        "title": "Nutritious SNAP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1100.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nutritious SNAP Act of 2025</strong></p><p>This bill prohibits Supplemental Nutrition Assistance Program (SNAP) benefits from being used to purchase certain beverages (e.g., soda) and snack foods.</p><p>Specifically, SNAP benefits may only be used to purchase a beverage that is nonalcoholic and is\u00a0(1) water, (2) cow's milk, (3) a milk-substitute beverage (e.g., almond milk, soy milk, and coconut milk), or (4) 100% juice.</p><p>Further, the bill prohibits the use of benefits to purchase\u00a0snack and dessert food items which are included on the Food and Nutrition Service's Accessory Foods List that went into effect on March 5, 2018.\u00a0Examples of snack and dessert foods on the list include potato and tortilla chips, ice cream, candy, snack cakes and pastries, and packaged baking mixes for cakes, brownies, and muffins.</p><p>In addition, on the request of a state agency, the Department of Agriculture must allow the state agency to prohibit the use of SNAP benefits to purchase food that the applicable\u00a0state nutrition\u00a0agency determines to be<em> </em>unhealthy food.</p>",
      "updateDate": "2025-08-19",
      "versionCode": "id119s1100"
    },
    "title": "Nutritious SNAP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nutritious SNAP Act of 2025</strong></p><p>This bill prohibits Supplemental Nutrition Assistance Program (SNAP) benefits from being used to purchase certain beverages (e.g., soda) and snack foods.</p><p>Specifically, SNAP benefits may only be used to purchase a beverage that is nonalcoholic and is\u00a0(1) water, (2) cow's milk, (3) a milk-substitute beverage (e.g., almond milk, soy milk, and coconut milk), or (4) 100% juice.</p><p>Further, the bill prohibits the use of benefits to purchase\u00a0snack and dessert food items which are included on the Food and Nutrition Service's Accessory Foods List that went into effect on March 5, 2018.\u00a0Examples of snack and dessert foods on the list include potato and tortilla chips, ice cream, candy, snack cakes and pastries, and packaged baking mixes for cakes, brownies, and muffins.</p><p>In addition, on the request of a state agency, the Department of Agriculture must allow the state agency to prohibit the use of SNAP benefits to purchase food that the applicable\u00a0state nutrition\u00a0agency determines to be<em> </em>unhealthy food.</p>",
      "updateDate": "2025-08-19",
      "versionCode": "id119s1100"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1100is.xml"
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
      "title": "Nutritious SNAP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nutritious SNAP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act to modify the definition of food under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T04:18:17Z"
    }
  ]
}
```
