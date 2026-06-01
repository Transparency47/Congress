# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5832?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5832
- Title: REAL Meats Act
- Congress: 119
- Bill type: HR
- Bill number: 5832
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2025-12-09T22:16:56Z
- Update date including text: 2025-12-09T22:16:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5832",
    "number": "5832",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "REAL Meats Act",
    "type": "HR",
    "updateDate": "2025-12-09T22:16:56Z",
    "updateDateIncludingText": "2025-12-09T22:16:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:00:25Z",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5832ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5832\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Williams of Texas (for himself, Mr. Babin , Mr. Carter of Texas , Mr. Nehls , Mr. Weber of Texas , and Mr. Ellzey ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish consumer certainty regarding fake meat and milk products, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Requiring Ethical and Accurate Labeling of Lab-grown Meats Act or the REAL Meats Act .\n#### 2. Amendment to the Federal Food, Drug, and Cosmetic Act regarding fake meat\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) (1) If it is a cell-cultured product or an analogue product and its label does not bear immediately before the name of the product a qualifying term or disclaimer that clearly communicates to a consumer the contents and nature of the product, such as the terms cell-cultured , lab-grown , analogue , meatless , plant-based , made from plants , or other similar terms. (2) If it is a cell-cultured product or an analogue product that uses in the product name the term chicken , turkey , beef , or pork or that of another species or kind of animal processed for food subject to the Federal Meat Inspection Act or the Poultry Products Inspection Act, and its label does not bear immediately before the name of the product the term cell-cultured , lab-grown , analogue , or imitation . (3) For purposes of this paragraph: (A) The term \u2018analogue product\u2019 means any food product derived by combining processed plants, insects, or fungus with additives to approximate the texture, flavor, appearance, or other aesthetic qualities or the chemical characteristics of any specific type of meat, meat food product, poultry, or poultry product and that does not contain meat or poultry at levels that would trigger inspection under the Federal Meat Inspection Act and Poultry Products Inspection Act. (B) The term cell-cultured product means food product derived by harvesting animal cells and artificially replicating those cells in a growth medium in a laboratory to produce tissue. (C) The term \u2018meat\u2019 has the meaning given the term in section 301.2 of title 9, Code of Federal Regulations (or successor regulations). (D) The term meat food product has the meaning given the term in section 1(j) of the Federal Meat Inspection Act. (E) The term poultry and poultry product have the meanings given the terms in section 4 of the Poultry Products Inspection Act, except that such terms do not include a product that is exempted from the definition of poultry product under section 381.15 of title 9 Code of Federal Regulations (or successor regulations). .",
      "versionDate": "2025-10-24",
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
        "name": "Commerce",
        "updateDate": "2025-12-09T22:16:56Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5832ih.xml"
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
      "title": "REAL Meats Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REAL Meats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Requiring Ethical and Accurate Labeling of Lab-grown Meats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish consumer certainty regarding fake meat and milk products, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T05:18:16Z"
    }
  ]
}
```
