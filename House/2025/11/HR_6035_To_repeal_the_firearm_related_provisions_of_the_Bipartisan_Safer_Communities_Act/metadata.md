# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6035?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6035
- Title: Second Amendment Restoration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6035
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-03-26T08:06:27Z
- Update date including text: 2026-03-26T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-12 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6035",
    "number": "6035",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001095",
        "district": "38",
        "firstName": "Wesley",
        "fullName": "Rep. Hunt, Wesley [R-TX-38]",
        "lastName": "Hunt",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Second Amendment Restoration Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:27Z",
    "updateDateIncludingText": "2026-03-26T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-12T17:00:20Z",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AZ"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "TN"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "FL"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "AL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "SC"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "CO"
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
      "sponsorshipDate": "2025-12-01",
      "state": "IN"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "LA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6035ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6035\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Hunt (for himself, Mr. Nehls , Mr. Clyde , Mr. Gill of Texas , Mr. Roy , Mr. Gosar , Mr. Rose , Mr. Donalds , Mr. Moore of Alabama , and Mr. Collins ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo repeal the firearm-related provisions of the Bipartisan Safer Communities Act.\n#### 1. Short title\nThis Act may be cited as the Second Amendment Restoration Act of 2025 .\n#### 2. Findings\nThe Congress finds as follows:\n**(1)**\nThe Second Amendment to the United States Constitution guarantees the right of law-abiding citizens to keep and bear arms.\n**(2)**\nThe firearm-related provisions of the Bipartisan Safer Communities Act ( Public Law 117\u2013159 ) impose unnecessary burdens on that right without demonstrable benefit to public safety.\n**(3)**\nThe purpose of this Act is to restore constitutional protections and refocus Federal efforts on addressing the root causes of violence.\n#### 3. Repeal of firearm-related provisions of the Bipartisan Safer Communities Act\n##### (a) Repeals\n**(1) Firearms**\nTitle II of division A of the Bipartisan Safer Communities Act ( Public Law 117\u2013159 ) is hereby repealed.\n**(2) ESEA amendment**\nSubtitle D of title III of division A of the Bipartisan Safer Communities Act ( Public Law 117\u2013159 ) is hereby repealed.\n##### (b) Restoration of prior law\n**(1) Title 18 , United States Code**\n**(A) Conforming amendments**\nEach provision of sections 921, 922, 924, 1956, 1961, and 2516 of title 18, United States Code, amended by such title II is amended to be the provision in effect immediately before the enactment of such title II.\n**(B) Clerical amendments**\nThe table of sections for chapter 44 of such title is amended by striking the items relating to sections 932, 933, and 934.\n**(2) Brady Handgun Violence Prevention Act**\nEach provision of section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) amended by such title II is amended be the provision in effect immediately before the enactment of such title II.\n**(3) Title I of the Omnibus Crime Control and Safe Streets Act of 1968**\nEach provision of section 501 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152 ) amended by such title II is amended to be the provision in effect immediately before the enactment of such title II.\n**(4) Title 28 , United States Code**\nEach provision of section 534 of title 28, United States Code, amended by such title II is amended to be the provision in effect immediately before the enactment of such title II.\n**(5) ESEA**\nEach provision of section 8526 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7906 ) amended by such subtitle D is amended to be the provision in effect immediately before the enactment of such subtitle D.\n##### (c) Elimination of funding for NICS expansion of juvenile records\nParagraph (3) under the heading State and Local Law Enforcement Activities\u2014Office of Justice Programs\u2014state and local law enforcement assistance of title I of division B of the Bipartisan Safer Communities Supplemental Appropriations Act ( Public Law 117\u2013159 ) is amended by striking , including grants to assist States in providing disqualifying juvenile records under subsection (g) or (n) of section 922 of title 18, United States Code .",
      "versionDate": "2025-11-12",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-19T13:23:43Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6035ih.xml"
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
      "title": "Second Amendment Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Amendment Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-18T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the firearm-related provisions of the Bipartisan Safer Communities Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-18T09:18:20Z"
    }
  ]
}
```
