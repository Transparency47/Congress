# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3829?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3829
- Title: FinCEN–SBA Coordination on Beneficial Ownership Registration Act
- Congress: 119
- Bill type: HR
- Bill number: 3829
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2025-12-05T22:55:01Z
- Update date including text: 2025-12-05T22:55:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3829",
    "number": "3829",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "FinCEN\u2013SBA Coordination on Beneficial Ownership Registration Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:01Z",
    "updateDateIncludingText": "2025-12-05T22:55:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-06T13:05:10Z",
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
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "GA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OH"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "LA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3829ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3829\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Ms. Vel\u00e1zquez (for herself and Ms. Waters ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Small Business , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Director of the Financial Crimes Enforcement Network and the Administrator of the Small Business Administration to enter into a memorandum of understanding to ensure the dissemination of covered information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FinCEN\u2013SBA Coordination on Beneficial Ownership Registration Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nmalign actors seek to conceal their ownership of corporations, limited liability companies, or other similar entities in the United States to facilitate illicit activity, including money laundering, the financing of terrorism, proliferation financing, serious tax fraud, human and drug trafficking, counterfeiting, piracy, securities fraud, financial fraud, and acts of foreign corruption, harming the national security interests of the United States and allies of the United States;\n**(2)**\nFederal legislation providing for the collection of beneficial ownership information for corporations, limited liability companies, or other similar entities formed under the laws of the States is needed to\u2014\n**(A)**\nset a clear, Federal standard for incorporation practices;\n**(B)**\nprotect vital Unites States national security interests;\n**(C)**\nprotect interstate and foreign commerce;\n**(D)**\nbetter enable critical national security, intelligence, and law enforcement efforts to counter money laundering, the financing of terrorism, and other illicit activity; and\n**(E)**\nbring the United States into compliance with international anti-money laundering and countering the financing of terrorism standards;\n**(3)**\nFederal legislation providing for the collection of beneficial ownership information is needed to protect critical law enforcement and national security efforts;\n**(4)**\nthe Secretary of the Treasury and the Administrator of the Small Business Administration should work with small business concerns and other reporting companies to provide clarity and minimize burdens on them while still generating a highly useful database;\n**(5)**\nan overwhelming bipartisan majority of Congress codified the provisions of paragraphs (1) through (4) in the enactment of the Corporate Transparency Act (title LXIV of division F of Public Law 116\u2013283 ); and\n**(6)**\nfull implementation of the Corporate Transparency Act is critical to further the provisions of paragraphs (1) through (4).\n#### 3. Definitions\nIn this Act:\n**(1) Administration; Administrator**\nThe terms Administration and Administrator mean the Small Business Administration and the Administrator thereof, respectively.\n**(2) Beneficial ownership requirements**\nThe term beneficial ownership requirements means the requirements under section 5336 of title 31, United States Code.\n**(3) Covered agencies**\nThe term covered agencies means FinCEN and the Administration.\n**(4) Covered information**\nThe term covered information means information developed by FinCEN regarding the beneficial ownership information reporting requirements under section 5336 of title 31, United States Code.\n**(5) Director**\nThe term Director means the Director of FinCEN.\n**(6) FinCEN**\nThe term FinCEN means the Financial Crimes Enforcement Network described in section 310 of title 31, United States Code.\n**(7) Reporting company**\nThe term reporting company has the meaning given in section 5336 of title 31, United States Code.\n**(8) Resource partner**\nThe term resource partner means\u2014\n**(A)**\na small business development center (as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 ));\n**(B)**\na women\u2019s business center described in section 29 of the Small Business Act ( 15 U.S.C. 656 ); and\n**(C)**\nVeteran Business Outreach Centers described in section 32 of the Small Business Act ( 15 U.S.C. 657b ).\n**(9) Small business concern**\nThe term small business concern has the meaning given under section 3 of the Small Business Act ( 15 U.S.C. 632 ).\n#### 4. Memorandum of understanding to ensure the dissemination of covered information\n##### (a) Meeting\nNot later than 30 days after the date of the enactment of this Act, the Administrator and the Director shall meet to discuss the contents of the memorandum of understanding required by subsection (b).\n##### (b) Memorandum of understanding\nNot later than 90 days after the date of the enactment of this Act, the Administrator and the Director shall enter into a written memorandum of understanding to jointly carry out the following activities:\n**(1)**\nDisseminating covered information to reporting companies and trade associations and other entities that represent small business concerns, including dissemination through resource partners of the Administration.\n**(2)**\nEnsuring covered information is made available in English, Spanish, and any additional languages as jointly determined by the Director and the Administrator.\n**(3)**\nEnsuring that the homepage of the website of the Administration includes a link to the relevant webpages of FinCEN relating to beneficial ownership requirements and registration for reporting companies.\n**(4)**\nImplementing a plan to identify and counter scams or other fraudulent schemes related to, or purporting to be, beneficial ownership reporting, and to educate reporting companies and trade associations and other entities that represent small business concerns about such scams or fraudulent schemes.\n**(5)**\nHosting in-person town halls and webinars\u2014\n**(A)**\norganized by the Administrator, acting through national or regional offices of the Administration;\n**(B)**\nthat feature presentations by FinCEN staff on compliance with beneficial ownership requirements; and\n**(C)**\nthat are advertised to reporting companies and trade associations and other entities that represent small business concerns.\n**(6)**\nImplementing a plan to use field offices of the Administration and Domestic Liaisons of FinCEN for the in-person town halls and webinars described in paragraph (5).\n**(7)**\nAny other activities the Director and the Administrator determine necessary to increase the number of reporting companies in compliance with beneficial ownership requirements.\n##### (c) Public availability of memorandum of understanding\nNot later than 7 days after the date on which the Director and Administrator enter into a memorandum of understanding under subsection (b), the Director and the Administrator shall each make the memorandum publicly available on a website of FinCEN and the Administration, respectively.\n##### (d) Meetings\nNot later than 6 months after the date on which the Director and Administrator enter into a memorandum of understanding under subsection (b), and every 6 months thereafter, the Director (or a designee) and the Administrator (or a designee) shall review the following:\n**(1)**\nIssues related to, and continued coordination on, the requirements of the memorandum.\n**(2)**\nChallenges associated with increasing the number of reporting companies in compliance with beneficial ownership requirements.\n**(3)**\nReasons provided by reporting companies to covered agencies for failing to comply with beneficial ownership requirements.\n**(4)**\nStrategies for collaboration to address the reasons described in paragraph (3).\n**(5)**\nAny other topics the Director and the Administrator determine necessary.\n##### (e) Compensation\nThe Director (or a designee) and the Administrator (or a designee) may not receive compensation for attending a meeting required by subsection (d).\n#### 5. Reports\nNot later than 30 days after the date on which the Director and Administrator enter into a memorandum of understanding under section 3(b), and every 30 days thereafter, the Director and the Administrator shall jointly submit to the Committees on Small Business and Entrepreneurship and Banking, Housing, and Urban Affairs of the Senate and the Committees on Small Business and Financial Services of the House of Representatives a report that includes the following:\n**(1)**\nFor the 30-day period preceding the date of the report\u2014\n**(A)**\na description of the actions taken under the memorandum of understanding to provide outreach to reporting companies that are required to, but have failed to, comply with beneficial ownership requirements;\n**(B)**\nthe estimated number of reporting companies that have received covered information or other assistance relating to beneficial ownership requirements from the Administration or FinCEN as a result of actions taken pursuant to the memorandum of understanding; and\n**(C)**\nthe number of reporting companies in compliance with beneficial ownership requirements.\n**(2)**\nA description of the actions the Director and the Administrator plan to take under the memorandum of understanding during the 30-day period following the date of the report to provide covered information to reporting companies that have failed to comply with beneficial ownership requirements.",
      "versionDate": "2025-06-06",
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
        "actionDate": "2025-06-09",
        "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "1995",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FinCEN\u2013SBA Coordination on Beneficial Ownership Registration Act",
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
        "name": "Commerce",
        "updateDate": "2025-07-01T13:26:00Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3829ih.xml"
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
      "title": "FinCEN\u2013SBA Coordination on Beneficial Ownership Registration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FinCEN\u2013SBA Coordination on Beneficial Ownership Registration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the Financial Crimes Enforcement Network and the Administrator of the Small Business Administration to enter into a memorandum of understanding to ensure the dissemination of covered information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:21Z"
    }
  ]
}
```
