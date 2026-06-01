# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6487?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6487
- Title: SECURE STEM Act
- Congress: 119
- Bill type: HR
- Bill number: 6487
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2025-12-18T16:58:00Z
- Update date including text: 2025-12-18T16:58:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-05 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6487",
    "number": "6487",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "SECURE STEM Act",
    "type": "HR",
    "updateDate": "2025-12-18T16:58:00Z",
    "updateDateIncludingText": "2025-12-18T16:58:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-05T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "MI"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
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
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6487ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6487\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mr. Harrigan (for himself and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the issuance of certain visas to nationals of the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing Education and Critical U.S. Research and Employment in STEM Act of 2025 or the SECURE STEM Act .\n#### 2. Prohibition on certain visa issuances\n##### (a) Visa Ineligibility\nNotwithstanding any other provision of law and except as provided in subsection (c), the Secretary of State may not issue a visa to, and the Secretary of Homeland Security may not admit to the United States, a covered foreign national who is seeking admission to the United States under a covered visa category.\n##### (b) Employment Prohibition at National Laboratories\nBeginning on the date of enactment of this Act, a national research laboratory may not employ a covered foreign national who is present in the United States under a covered visa category on the date of enactment of this Act.\n##### (c) National Interest Waiver\nThe Secretary of State and the Secretary of Homeland Security may jointly waive the application of subsections (a) and (b) with respect to a specific individual if the Secretaries determine that such a waiver is in the National interest of the United States.\n#### 3. Reporting Requirements\nThe Secretary of State, in consultation with the Secretary of Homeland Security, shall submit to the Committee on the Judiciary and the Committee on Foreign Affairs of the House of Representatives, and the Committee on the Judiciary and the Committee on Foreign Relations of the Senate, a biannual report, including, for the previous 180-day period\u2014\n**(1)**\nthe total number of waivers granted under section 2(c);\n**(2)**\na summary of the justification for each waiver; and\n**(3)**\nbiographical information about each recipient of such a waiver, including any prior affiliation with foreign state-sponsored institutions.\n#### 4. Definitions\nFor purposes of this Act:\n**(1)**\nThe term covered visa category means a nonimmigrant visa issued under any of the following:\n**(A)**\nSection 101(a)(15)(H)(i)(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(H)(i)(b) ).\n**(B)**\nSection 101(a)(15)(O)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(O)(i) ).\n**(C)**\nSection 101(a)(15)(J) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(J) ).\n**(D)**\nSection 101(a)(15)(F), (J), or (M) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(F) , (J), or (M)) (student visas).\n**(2)**\nThe term covered foreign national means an alien who is a national of any of the following:\n**(A)**\nThe People\u2019s Republic of China.\n**(B)**\nThe Russian Federation.\n**(C)**\nThe Islamic Republic of Iran.\n**(D)**\nThe Democratic People\u2019s Republic of Korea.\n**(E)**\nThe Republic of Cuba.\n**(3)**\nThe term national research laboratory means a Federal laboratory as such term is defined in section 4 of the Stevenson\u2013Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 ).\n#### 5. Rules\nNot later than 90 days after the date of enactment of this Act, the Secretary of State, in consultation with the Secretary of Homeland Security, shall make such rules as may be necessary to carry out this Act.",
      "versionDate": "2025-12-05",
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
        "name": "Immigration",
        "updateDate": "2025-12-18T16:58:00Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6487ih.xml"
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
      "title": "SECURE STEM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T07:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SECURE STEM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securing Education and Critical U.S. Research and Employment in STEM Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T07:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the issuance of certain visas to nationals of the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T07:33:35Z"
    }
  ]
}
```
