# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7464
- Title: TEMP Act
- Congress: 119
- Bill type: HR
- Bill number: 7464
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-05-05T12:26:43Z
- Update date including text: 2026-05-05T12:26:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7464",
    "number": "7464",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000472",
        "district": "18",
        "firstName": "Scott",
        "fullName": "Rep. Franklin, Scott [R-FL-18]",
        "lastName": "Franklin",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TEMP Act",
    "type": "HR",
    "updateDate": "2026-05-05T12:26:43Z",
    "updateDateIncludingText": "2026-05-05T12:26:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:03:25Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "FL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7464ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7464\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Scott Franklin of Florida (for himself, Mr. Carbajal , Mr. Soto , Mr. Carter of Georgia , Ms. Lee of Florida , Mr. Steube , Mr. Patronis , Mr. Mills , Mr. Fine , Ms. Wilson of Florida , Mr. Rutherford , Mrs. Cammack , Mr. Subramanyam , and Mr. Buchanan ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to direct the Federal Crop Insurance Corporation to conduct research and development on frost or cold weather insurance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Temperature Event Mitigation Policy Act or the TEMP Act .\n#### 2. Research and development on frost or cold weather insurance\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Frost or cold weather insurance (A) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding an index-based policy to insure crops (including tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, blueberries, and any other crop) on a nationally-available basis against losses due to a frost or cold weather event. (B) Research and development Research and development under subparagraph (A) shall\u2014 (i) evaluate the effectiveness of risk management tools, such as the use of an index, with respect to low frequency and catastrophic loss weather events; and (ii) result in a policy that provides protection for at least 1 of the following: (I) Production loss. (II) Revenue loss. (C) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that describes\u2014 (i) the results of the research and development carried out under this paragraph; and (ii) any recommendations with respect to those results. .",
      "versionDate": "2026-02-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-01",
        "text": "Placed on the Union Calendar, Calendar No. 548."
      },
      "number": "8646",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Agriculture, Rural Development, Food and Drug Administration, and Related Agency Appropriations Act, 2027",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-30",
        "actionTime": "11:15:02",
        "text": "The Clerk was authorized to correct section numbers, punctuation, and cross references, and to make other necessary technical and conforming corrections in the engrossment of H.R. 7567."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-11",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3843",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TEMP Act",
      "type": "S"
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
        "updateDate": "2026-02-17T17:46:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-10",
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
          "measure-id": "id119hr7464",
          "measure-number": "7464",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7464v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-02-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>"
        },
        "title": "TEMP Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7464.xml",
    "summary": {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7464"
    },
    "title": "TEMP Act"
  },
  "summaries": [
    {
      "actionDate": "2026-02-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Temperature Event Mitigation Policy Act or the</strong> <strong>TEMP Act </strong></p><p>This bill directs the federal crop insurance program to provide for research and development regarding a temperature-based index policy to insure crops (including\u00a0tomatoes, peppers, sugarcane, strawberries, melons, citrus, peaches, and blueberries) on a nationally-available basis against losses due to a frost or cold weather event.</p><p>The research and development must (1) evaluate the effectiveness of risk management tools with respect to low frequency and catastrophic loss weather events, and (2) result in a policy that provides protection for production loss or revenue loss.\u00a0</p><p>The term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.\u00a0Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., temperature level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr7464"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7464ih.xml"
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
      "title": "TEMP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TEMP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Temperature Event Mitigation Policy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-12T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to direct the Federal Crop Insurance Corporation to conduct research and development on frost or cold weather insurance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-12T04:03:36Z"
    }
  ]
}
```
