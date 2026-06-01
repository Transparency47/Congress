# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5646
- Title: Restoring Safeguards for Dangerous Abortion Drugs Act
- Congress: 119
- Bill type: HR
- Bill number: 5646
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-12-05T22:54:01Z
- Update date including text: 2025-12-05T22:54:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5646",
    "number": "5646",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Restoring Safeguards for Dangerous Abortion Drugs Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:01Z",
    "updateDateIncludingText": "2025-12-05T22:54:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-30T16:03:30Z",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "SC"
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
      "sponsorshipDate": "2025-09-30",
      "state": "TX"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NC"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "TN"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MS"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5646ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5646\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mrs. Miller of Illinois (for herself, Mr. Moore of Alabama , Mrs. Biggs of South Carolina , Mr. Weber of Texas , Mr. Harrigan , Mr. Burchett , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Health and Human Services to approve a risk evaluation and mitigation strategy for mifepristone that is identical to the strategy previously approved, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Safeguards for Dangerous Abortion Drugs Act .\n#### 2. Definition\nIn this Act, the term covered medication means mifepristone, also known by the brand names, Mifeprex and Korlym, and the developmental code name, RU\u2013486.\n#### 3. Mifepristone REMS\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Secretary of Health and Human Services shall\u2014\n**(1)**\nwithdraw approval of the risk evaluation and mitigation strategy pursuant to section 505\u20131 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355\u20131 ) for the covered medication that is in effect on the date of enactment of this Act; and\n**(2)**\napprove a risk evaluation and mitigation strategy for the covered medication that is identical to the risk evaluation and mitigation strategy for such covered medication that was approved by such Secretary in June 2011.\n##### (b) Restriction\nNotwithstanding any provision of section 505\u20131 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355\u20131 ), the Secretary of Health and Human Services\u2014\n**(1)**\nshall require a risk evaluation and mitigation strategy pursuant to such section 505\u20131 for the covered medication; and\n**(2)**\nmay not approve a risk evaluation and mitigation strategy pursuant to such section for the covered medication that is different from the strategy described in subsection (a)(2).\n#### 4. Federal tort for harm to women caused by abortion drugs\n##### (a) Definition\nIn this section, the term covered entity means a telehealth provider, pharmacy, or any other person who knowingly imports or transports a covered medication in interstate or foreign commerce in violation of section 1462 of title 18, United States Code.\n##### (b) Liability\nA covered entity shall be liable in accordance with this section to any individual who suffers bodily injury or harm to mental health (including any physical, psychological, emotional, or physiological harm) that is attributable, in whole or in part, to the individual\u2019s use of a covered medication imported or transported as described in subsection (a).\n##### (c) Private right of action\nAn individual who suffers bodily injury or harm to mental health that is attributable, in whole or in part, to the individual\u2019s use of a covered medication as described in subsection (b) may bring a civil action against the covered entity in an appropriate district court of the United States or a State court of competent jurisdiction for\u2014\n**(1)**\ncompensatory damages;\n**(2)**\npunitive damages; and\n**(3)**\nattorney\u2019s fees and costs.\n##### (d) Rules of construction\nNothing in this section shall be construed to preempt any State law that makes available any other remedy to an individual described in subsection (b).\n##### (e) Effective date\nThis section shall take effect on the date that is 90 days after the date of enactment of this Act.\n#### 5. Ban on importation\nSection 801 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 381 ) is amended\u2014\n**(1)**\nin the third sentence of subsection (a), by inserting or is mifepristone, after under section 569D, ; and\n**(2)**\nin subsection (d)(1), by adding at the end the following:\n(C) Notwithstanding any other provision of law, no person may import the drug mifepristone into the United States, including by mailing such drug to individuals. .",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1631",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Restoring Safeguards for Dangerous Abortion Drugs Act",
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
        "name": "Health",
        "updateDate": "2025-11-18T16:40:13Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5646ih.xml"
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
      "title": "Restoring Safeguards for Dangerous Abortion Drugs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Safeguards for Dangerous Abortion Drugs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Health and Human Services to approve a risk evaluation and mitigation strategy for mifepristone that is identical to the strategy previously approved, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:18:25Z"
    }
  ]
}
```
