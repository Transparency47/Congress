# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7153
- Title: Agriculture and National Security Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7153
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-17T08:07:28Z
- Update date including text: 2026-04-17T08:07:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7153",
    "number": "7153",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Agriculture and National Security Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:28Z",
    "updateDateIncludingText": "2026-04-17T08:07:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
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
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:02:00Z",
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
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "KS"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NJ"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MD"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "PA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IN"
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
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7153ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7153\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mrs. Bice (for herself, Mr. Khanna , Mr. Schmidt , Mr. Edwards , Mr. Nunn of Iowa , Mr. Smith of New Jersey , and Mr. Shreve ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo improve connections between the Department of Agriculture and national and homeland security agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Agriculture and National Security Act of 2026 .\n#### 2. Sense of Congress relating to agriculture and national security\nIt is the sense of Congress that there are increasingly robust Federal activities to address homeland security vulnerabilities across the food and agriculture sector, including with regard to agriculture and food defense, critical infrastructure, emergency management, and catastrophic events, but additional efforts are needed to identify national security vulnerabilities related to food and agriculture, particularly with regard to emerging technologies.\n#### 3. National security\n##### (a) In general\nIn recognition that food and agriculture are critical to the national security of the United States, the Secretary of Agriculture (referred to in this Act as the Secretary ) shall prioritize national security in addition to homeland security in the Department of Agriculture (referred to in this Act as the Department ), including by increasing the number of staff at the Department with security clearances and access to classified systems and networks.\n##### (b) Senior Advisor for National Security\n**(1) Appointment**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall\u2014\n**(A)**\nestablish within the Office of the Secretary the position of Senior Advisor for National Security (referred to in this Act as the Senior Advisor ); and\n**(B)**\nappoint an individual to the position of Senior Advisor.\n**(2) Duties**\nThe Senior Advisor shall, in coordination with and complementary to the duties of the Office of Homeland Security of the Department\u2014\n**(A)**\nserve as the principal advisor to the Secretary on national security;\n**(B)**\nact as the primary liaison on behalf of the Department with the National Security Council and other Federal departments and agencies in activities relating to national security;\n**(C)**\ncoordinate national security activities across the Department, including to ensure that national security concerns are integrated into the homeland security activities of the Department wherever appropriate; and\n**(D)**\ncommunicate with stakeholders to identify national security vulnerabilities and risk mitigation strategies relevant to food and agriculture.\n##### (c) Interagency coordination\nSection 221(e) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6922(e) ) is amended by adding at the end the following:\n(3) Detailees authorized The Secretary may provide detailees to, and accept and employ personnel detailed from, defense, national and homeland security, law enforcement, and intelligence agencies, with or without reimbursement, to improve information sharing, vulnerability identification, and risk mitigation related to food and agriculture. .\n##### (d) Biennial reports\nSection 221 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6922 ) is amended by adding at the end the following:\n(f) Biennial reports Not later than 180 days after the date of enactment of this Act, and not less frequently than once every 2 years thereafter, the Secretary shall submit to Congress and the National Security Council a report that includes\u2014 (1) from the perspective of the Department, an assessment of any gaps or limitations in national security efforts related to food and agriculture in the United States, including\u2014 (A) influence of foreign state-owned enterprise; (B) control of and access to agricultural data; (C) foreign acquisition of intellectual property, agricultural assets, and land; (D) agricultural input shortages and dependence on foreign-sourced inputs; (E) supply chain and trade disruptions; (F) science and technology cooperation; (G) cybersecurity and artificial intelligence; (H) unequal investments in research, development, and scale-up; (I) incongruent regulatory policies; and (J) other vulnerabilities throughout the food and agriculture sector, particularly with regard to emerging technologies; (2) the actions taken by the Secretary to address any gaps or limitations identified under paragraph (1), including through interagency coordination, threat information sharing, and stakeholder outreach; (3) policy recommendations, including recommendations for executive actions and legislative proposals\u2014 (A) to reduce any gaps or limitations identified under paragraph (1); and (B) to address any identified vulnerabilities with respect to the gaps or limitations identified under paragraph (1); and (4) resources the Department requires to address current and future national security vulnerabilities related to food and agriculture. .",
      "versionDate": "2026-01-20",
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
        "updateDate": "2026-02-18T19:51:20Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7153ih.xml"
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
      "title": "Agriculture and National Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agriculture and National Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve connections between the Department of Agriculture and national and homeland security agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:24Z"
    }
  ]
}
```
