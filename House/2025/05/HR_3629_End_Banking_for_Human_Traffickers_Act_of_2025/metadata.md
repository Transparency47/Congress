# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3629?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3629
- Title: End Banking for Human Traffickers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3629
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-01-12T19:44:29Z
- Update date including text: 2026-01-12T19:44:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-29 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3629",
    "number": "3629",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "End Banking for Human Traffickers Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-12T19:44:29Z",
    "updateDateIncludingText": "2026-01-12T19:44:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-29T15:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MA"
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
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3629ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3629\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Fitzpatrick (for himself and Mr. Keating ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase the role of the financial industry in combating human trafficking.\n#### 1. Short title\nThis Act may be cited as the End Banking for Human Traffickers Act of 2025 .\n#### 2. Increasing the role of the financial industry in combating human trafficking\n##### (a) Required review of procedures\nNot later than 180 days after the date of the enactment of this Act, the Financial Institutions Examination Council, in consultation with the Secretary of the Treasury, the private sector, victims of severe forms of trafficking in persons, advocates of persons at risk of becoming victims of severe forms of trafficking in persons, and appropriate law enforcement agencies, shall\u2014\n**(1)**\nreview and enhance training and examinations procedures to improve the capabilities of anti-money laundering and countering the financing of terrorism programs to detect financial transactions relating to severe forms of trafficking in persons;\n**(2)**\nreview and enhance procedures for referring potential cases relating to severe forms of trafficking in persons to the appropriate law enforcement agency; and\n**(3)**\ndetermine, as appropriate, whether requirements for financial institutions are sufficient to detect and deter money laundering relating to severe forms of trafficking in persons.\n##### (b) Interagency task force recommendations targeting money laundering related to human trafficking\n**(1) In general**\nNot later than 270 days after the date of the enactment of this Act, the Interagency Task Force To Monitor and Combat Trafficking shall submit to the Committee on Financial Services and the Committee on the Judiciary of the House of Representatives, the Committee on Banking, Housing, and Urban Affairs and the Committee on the Judiciary of the Senate, and the head of each Federal banking agency\u2014\n**(A)**\nan analysis of anti-money laundering efforts of the United States Government and United States financial institutions relating to severe forms of trafficking in persons; and\n**(B)**\nappropriate legislative, administrative, and other recommendations to strengthen efforts against money laundering relating to severe forms of trafficking in persons.\n**(2) Required recommendations**\nThe recommendations under paragraph (1) shall include\u2014\n**(A)**\nfeedback from financial institutions on best practices of successful programs to combat severe forms of trafficking in persons currently in place that may be suitable for broader adoption by similarly situated financial institutions;\n**(B)**\nfeedback from stakeholders, including victims of severe forms of trafficking in persons, advocates of persons at risk of becoming victims of severe forms of trafficking in persons, and financial institutions, on policy proposals derived from the analysis conducted by the task force referred to in paragraph (1) that would enhance the efforts and programs of financial institutions to detect and deter money laundering relating to severe forms of trafficking in persons, including any recommended changes to internal policies, procedures, and controls relating to severe forms of trafficking in persons;\n**(C)**\nany recommended changes to training programs at financial institutions to better equip employees to deter and detect money laundering relating to severe forms of trafficking in persons;\n**(D)**\nany recommended changes to expand information sharing relating to severe forms of trafficking in persons among financial institutions and between such financial institutions, appropriate law enforcement agencies, and appropriate Federal agencies; and\n**(E)**\nrecommended changes, if necessary, to existing statutory law to more effectively detect and deter money laundering relating to severe forms of trafficking in persons, where such money laundering involves the use of emerging technologies and virtual currencies.\n##### (c) Limitation\nNothing in this Act shall be construed to\u2014\n**(1)**\ngrant rulemaking authority to the Interagency Task Force To Monitor and Combat Trafficking; or\n**(2)**\nencourage financial institutions to deny services to victims of trafficking, victims of severe forms of trafficking in persons, or individuals not responsible for promoting severe forms of trafficking in persons.\n##### (d) Definitions\nAs used in this section\u2014\n**(1)**\nthe term Federal banking agency has the meaning given the term in section 3(q) of the Federal Deposit Insurance Act ( 12 U.S.C. 1813(q) );\n**(2)**\nthe term severe forms of trafficking in persons has the meaning given such term in section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 );\n**(3)**\nthe term Interagency Task Force To Monitor and Combat Trafficking means the Interagency Task Force To Monitor and Combat Trafficking established by the President pursuant to section 105 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7103 ); and\n**(4)**\nthe term law enforcement agency means an agency of the United States, a State, or a political subdivision of a State, authorized by law or by a government agency to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal or civil law.\n#### 3. Minimum standards for the elimination of trafficking\nSection 108(b) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7106(b) ) is amended by adding at the end the following new paragraph:\n(13) Whether the government of the country, consistent with the capacity of the country, has in effect a framework to prevent financial transactions involving the proceeds of severe forms of trafficking in persons, and is taking steps to implement such a framework, including by investigating, prosecuting, convicting, and sentencing individuals who attempt or conduct such transactions. .",
      "versionDate": "2025-05-29",
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
        "actionDate": "2025-10-24",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5827",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan, common sense solutions.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan priorities.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-24",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3001",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance commonsense priorities.",
      "type": "HR"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-06-03T15:37:34Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3629ih.xml"
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
      "title": "End Banking for Human Traffickers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "End Banking for Human Traffickers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the role of the financial industry in combating human trafficking.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:29Z"
    }
  ]
}
```
