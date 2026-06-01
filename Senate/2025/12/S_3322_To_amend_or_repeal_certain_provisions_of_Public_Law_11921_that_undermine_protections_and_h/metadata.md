# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3322
- Title: Upholding Protections for Unaccompanied Children Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3322
- Origin chamber: Senate
- Introduced date: 2025-12-03
- Update date: 2026-02-26T14:56:52Z
- Update date including text: 2026-02-26T14:56:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in Senate
- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Star Print ordered on the bill.
- Latest action: 2025-12-03: Introduced in Senate

## Actions

- 2025-12-03 - IntroReferral: Introduced in Senate
- 2025-12-03 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-01-07 - Floor: Star Print ordered on the bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3322",
    "number": "3322",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Upholding Protections for Unaccompanied Children Act of 2025",
    "type": "S",
    "updateDate": "2026-02-26T14:56:52Z",
    "updateDateIncludingText": "2026-02-26T14:56:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-03",
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
        "item": [
          {
            "date": "2025-12-03T17:57:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-03T17:57:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NV"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-12-03",
      "state": "ME"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MN"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-03",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3322is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3322\nIN THE SENATE OF THE UNITED STATES\nDecember 3, 2025 Ms. Cortez Masto (for herself, Mr. Blumenthal , Mr. Wyden , Ms. Rosen , Mr. Merkley , Mr. Luj\u00e1n , Mr. King , Mr. Hickenlooper , Mr. Kim , Mr. Welch , Ms. Hirono , Mr. Schiff , Ms. Duckworth , Mr. Kelly , Ms. Smith , Mr. Bennet , Mrs. Murray , Mr. Heinrich , Mr. Markey , Mr. Sanders , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend or repeal certain provisions of Public Law 119\u201321 that undermine protections and heighten dangers for unaccompanied alien children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upholding Protections for Unaccompanied Children Act of 2025 .\n#### 2. Fees\n##### (a) Asylum fee\nSection 100002 of Public Law 119\u201321 is amended by adding at the end the following:\n(f) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n##### (b) Employment authorization document fee\nSection 100003 of Public Law 119\u201321 is amended by adding at the end the following:\n(d) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n##### (c) Special immigrant juvenile fee\n**(1) Repeal**\nSection 100005 of Public Law 119\u201321 is repealed.\n**(2) Clarification**\nThe Secretary of Homeland Security may not impose a fee in connection with any alien, parent, or legal guardian of an alien applying for special immigrant juvenile status under section 101(a)(27)(J) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(27)(J) ).\n##### (d) Annual asylum fee\nSection 100009 of Public Law 119\u201321 is amended by adding at the end the following:\n(e) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n##### (e) Employment authorization renewal fees\n**(1) Employment authorization for parolees**\nSection 100010 of Public Law 119\u201321 is amended by adding at the end the following:\n(e) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n**(2) Employment authorization for asylum applicants**\nSection 100011 of Public Law 119\u201321 is amended by adding at the end the following:\n(e) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n**(3) Employment authorization for aliens granted temporary protected status**\nSection 100012 of Public Law 119\u201321 is amended by adding at the end the following:\n(e) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n##### (f) Immigration court fees\nSection 100013 of Public Law 119\u201321 is amended by adding at the end the following:\n(l) Exception The fees otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n##### (g) In absentia removal fee\nSection 100016(c) of Public Law 119\u201321 is amended by inserting before the period at the end the following: , or to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )) .\n##### (h) Border apprehension fee\nSection 100017 of Public Law 119\u201321 is amended by inserting at the end the following:\n(e) Exception The fee otherwise required under this section shall not apply to any individual who is, or was previously determined to be, an unaccompanied alien child (as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) )). .\n#### 3. Upholding protection screenings and a fair legal process\nSection 100051 of Public Law 119\u201321 is amended by striking paragraph (8).\n#### 4. Limitations on body examinations\n##### (a) Body examinations conducted by the Office of Refugee Resettlement\nSection 87001(b) of Public Law 119\u201321 is amended\u2014\n**(1)**\nby striking paragraph (3); and\n**(2)**\nby redesignating paragraphs (4) and (5) as paragraphs (3) and (4), respectively.\n##### (b) Body examinations conducted by the Department of Homeland Security\nSection 100051 of Public Law 119\u201321 is amended\u2014\n**(1)**\nby striking paragraph (11); and\n**(2)**\nby redesignating paragraphs (9), (10), and (12) as paragraphs (8), (9), and (10), respectively.\n#### 5. Sponsor information sharing\nSection 87001 of Public Law 119\u201321 , as amended by section 4(a), is further amended by adding at the end the following:\n(d) Limitation on information sharing The Secretary of Health and Human Services shall ensure that information obtained under this section is not shared with Department of Homeland Security or any other Federal agency for the purpose of enforcing the immigration laws (as defined in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) )). .\n#### 6. Refund of fees\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Homeland Security or the Attorney General shall refund each fee paid by, or on behalf of, any individual under a provision of law that is repealed or amended under this Act to exempt such individual from such payment to the individual or entity who paid such fee.",
      "versionDate": "2025-12-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2026-02-26T14:55:23Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2026-02-26T14:56:15Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2026-02-26T14:56:52Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2026-02-26T14:55:18Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2026-02-26T14:56:07Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2026-02-26T14:55:55Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2026-02-26T14:55:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-01-07T17:37:06Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3322is.xml"
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
      "title": "Upholding Protections for Unaccompanied Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T12:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Upholding Protections for Unaccompanied Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend or repeal certain provisions of Public Law 119-21 that undermine protections and heighten dangers for unaccompanied alien children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:18Z"
    }
  ]
}
```
