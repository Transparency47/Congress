# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2162
- Title: Honey Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 2162
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-03-26T08:06:36Z
- Update date including text: 2026-03-26T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2162",
    "number": "2162",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Honey Integrity Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:36Z",
    "updateDateIncludingText": "2026-03-26T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:01:30Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MS"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "KY"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "WV"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "SD"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2162ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2162\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Steube (for himself, Mr. Panetta , and Mr. Ezell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for the protection of the integrity of honey marketed in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honey Integrity Act .\n#### 2. Standard of identity for honey\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall establish a standard of identity for honey in accordance with applicable United States Pharmacopeia standards under section 401 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 341 ).\n#### 3. Report to Congress on enforcement actions with respect to misbranded honey\nNot later than 2 years after the date of the enactment of this Act, the Secretary shall submit a report to Congress on enforcement actions taken under the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 et seq. ) with respect to\u2014\n**(1)**\nhoney that is adulterated under section 402 of such Act ( 21 U.S.C. 342 ); and\n**(2)**\nhoney that is misbranded under section 403 of such Act ( 21 U.S.C. 343 ).\n#### 4. Honey Integrity Program\n##### (a) In general\nThe Secretary shall establish a program for the purposes of detecting economically motivated adulteration and improving honey integrity for honey introduced, or delivered for introduction, into interstate commerce. Such program shall be known as the Honey Integrity Program.\n##### (b) Testing required\n**(1) In general**\nPursuant to the Honey Integrity Program, beginning 180 days after the date of the enactment of this Act, the Secretary shall require that each qualifying commercial honey packer in the United States\u2014\n**(A)**\nconduct testing on honey the packer intends to be marketed in the United States, as described in paragraph (2);\n**(B)**\ncertify to the Secretary that the packer has complied with the requirements of this section and that the packer has no reason to believe that the packer has traded in honey that has been the subject of economically motivated adulteration; and\n**(C)**\nreport the results of such testing to the Secretary at such time and in such manner as the Secretary may specify.\n**(2) Testing requirements**\nA qualifying commercial honey packer shall ensure that testing conducted pursuant to paragraph (1) shall\u2014\n**(A)**\nuse all the best available science, including nuclear DNA testing, mitochondrial DNA testing, and any other established forensic DNA identity testing methods, nuclear magnetic resonance, high-resolution mass spectrometry, and other tests in a combined protocol designed to produce the most scientifically valid outcomes with respect to detecting economically motivated adulteration;\n**(B)**\nensure that a minimum volume of honey is tested to be effective according to law enforcement protocols to be developed by the Secretary, in consultation with the Commissioner of U.S. Customs and Border Protection, and the heads of other Federal agencies, as the Secretary determines appropriate; and\n**(C)**\nbe consistent with, or superior to, the best practices of other countries with respect to conducting testing of honey for economically motivated adulteration (as defined by the Secretary).\n**(3) Packer obligations**\nThe Secretary shall require each qualifying commercial honey packer to\u2014\n**(A)**\nreport to the Secretary findings of testing conducted under this section, at such time and in such manner as the Secretary may specify; and\n**(B)**\nin the case of a packer identifying economically motivated adulteration (as defined by the Secretary) in any honey the packer intends to market in the United States\u2014\n**(i)**\nreport such information to the Secretary and such law enforcement officials as the Secretary may require, not later than 24 hours after that identification; and\n**(ii)**\nrefuse receipt of such honey.\n**(4) Effect of EMA identification**\nUpon receipt of an alert of the identification of economically motivated adulteration (as defined by the Secretary), the Secretary shall\u2014\n**(A)**\ninvestigate, test, and destroy honey determined to be so adulterated after confirming results through Federal laboratory findings;\n**(B)**\nmaintain and share data on such identification with relevant enforcement agencies at the Federal, State, and local level, including the Commissioner of U.S. Customs and Border Protection and the Secretary of Agriculture; and\n**(C)**\nmaintain and share data on such identification with stakeholders, including national domestic producer associations.\n##### (c) List of packers\nThe Secretary shall\u2014\n**(1)**\npublish, and update as necessary, a list of each qualifying commercial honey packer in the United States, including packers excluded by the Secretary from being considered a qualifying commercial honey packer; and\n**(2)**\ndistribute such list, upon initial publication, and upon each update, to relevant stakeholders, as determined by the Secretary .\n##### (d) Interagency cooperation\n**(1) Consultation**\nIn developing the testing requirements under subsection (b), the Secretary shall consult with the Commissioner of U.S. Customs and Border Protection, the Secretary of Agriculture, and the head of any other Federal agency the Secretary determines to be appropriate, and the Secretary may consult with such Commissioner, such Secretary, and the heads of such other Federal agencies in otherwise carrying out this section.\n**(2) Resources**\nIn the case that the Food and Drug Administration lacks the necessary resources and laboratories available to test honey, U.S. Customs and Border Protection and the Department of Agriculture shall make available to the Secretary laboratory and other resources required by the Secretary for purposes of carrying out this section.\n##### (e) Fees and funding\n**(1) Assessment**\nEach qualifying commercial honey packer shall be subject to a fee due at such time and in such amounts as the Secretary may specify.\n**(2) Crediting and availability of fees**\nFees authorized under paragraph (1) shall be collected and available for obligation only to the extent and in the amount provided in advance in appropriations Acts. Such fees are authorized to remain available until expended.\n**(3) Authorization of appropriations**\nThere is authorized to be appropriated for fees under this section an amount equal to the amount necessary to carry out this section.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term economically motivated adulteration means any practice, such as intentionally leaving out, taking out, substituting a valuable ingredient or part of a food, or adding a substance to a food, that is intended to increase the value of a food (as defined in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 )) that makes such food adulterated within the meaning of section 402 of such Act ( 21 U.S.C. 342 ).\n**(2)**\n**(A)**\nThe term qualifying commercial honey packer means any packer who is required to pay an assessment to the National Honey Board established pursuant to the Commodity Promotion, Research, and Information Act of 1996 ( 7 U.S.C. 7411 et seq. ).\n**(B)**\nSuch term excludes packers who meet such criteria for exclusion as the Secretary may develop.\n**(3)**\nThe term Secretary , except as otherwise specified, means the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-13",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1028",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Honey Integrity Act",
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
        "updateDate": "2025-04-01T17:39:26Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2162ih.xml"
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
      "title": "Honey Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honey Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the protection of the integrity of honey marketed in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:35Z"
    }
  ]
}
```
