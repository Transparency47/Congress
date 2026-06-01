# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3867?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3867
- Title: Bankruptcy Administration Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3867
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-02-09T21:17:25Z
- Update date including text: 2026-02-09T21:17:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3867",
    "number": "3867",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Bankruptcy Administration Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-09T21:17:25Z",
    "updateDateIncludingText": "2026-02-09T21:17:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T14:05:50Z",
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
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "MD"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "WI"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "FL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NC"
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
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "NY"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3867ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3867\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Mr. Cline (for himself and Mr. Ivey ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend titles 11 and 28, United States Code, to modify the compensation payable to trustees serving in cases under chapter 7 of title 11, United States Code, to extend the term of certain temporary offices of bankruptcy judges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Administration Improvement Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress has amended the laws governing bankruptcy fees as necessary to ensure that the bankruptcy system remains self-supporting, while also fairly allocating the costs of the system among those who use the system.\n**(2)**\nBecause of the importance for the bankruptcy system to be self-funded, at no cost to taxpayers, Congress has closely monitored the funding needs of the bankruptcy system, including by requiring periodic reporting by the Attorney General regarding the United States Trustee System Fund.\n**(3)**\nBecause the system governing bankruptcies of various types is interconnected, Congress has established fees, including filing fees, quarterly fees in chapter 11 cases, and other fees, that together fund the courts, judges, United States trustees, and trustees serving in bankruptcy cases under chapter 7 of title 11, United States Code.\n**(4)**\nTrustees serving in bankruptcy cases under chapter 7 of title 11, United States Code, are vital to the functioning of the bankruptcy system, as they provide services at the front lines of the bankruptcy process, administering thousands of cases.\n**(5)**\nChapter 7 bankruptcy trustees provide valuable returns of assets to government creditors, including the Internal Revenue Service, the Department of Agriculture, the Small Business Administration, and other Federal, State, and municipal governments.\n**(6)**\nDue to the work of the chapter 7 bankruptcy trustees, millions of dollars are also disbursed annually to private creditors of all types, including medical providers, unsecured creditors, small businesses, and micro-enterprises such as domestic support providers.\n**(7)**\nDespite the essential role of chapter 7 bankruptcy trustees, since 1994 the amount of compensation paid to these trustees has not been increased. As in 1994, bankruptcy trustees receive only $60 per case (composed of $45 from subsection 330(b)(1), and $15 from subsection 330(b)(2), of title 11, United States Code) in nearly 90 percent of chapter 7 cases, and bankruptcy trustees receive no compensation at all for cases in which the filing fee is waived by the bankruptcy court.\n**(8)**\nSince 1994, there have been significant increases in salaries, attorney fees, budget appropriations, filing fees, and court-related fees associated with chapter 7 bankruptcies. In contrast, the $60 paid to chapter 7 trustees has remained the same and has not even been increased for inflation. In 2021, Congress attempted to implement a mechanism that would give chapter 7 trustees a raise, but the trustees only received increased compensation for 1 fiscal year. Based on Consumer Price Index estimates, the $60 paid to trustees in 1994 would be the equivalent of over $125 today.\n**(9)**\nThis Act and the amendments made by this Act\u2014\n**(A)**\nincrease the compensation of chapter 7 bankruptcy trustees to the level that is appropriate, overdue, and proportionate with the level that was intended in 1994, by increasing the total compensation of trustees to $120 per case;\n**(B)**\nensure adequate funding of the United States trustee system through the increase of certain fees, which will also apply to districts that are not part of a United States trustee region as required by existing law; and\n**(C)**\nsupport the preservation of existing bankruptcy judgeships that are urgently needed to handle existing and anticipated increases in business and consumer caseloads.\n**(10)**\nThis Act will not alter the filing fee under chapter 7 of title 11, United States Code, and will not modify, impair, or supersede the current authority of the district courts of the United States, or of bankruptcy courts, to waive the payment of filing fees by indigent individuals.\n#### 3. Trustee compensation\n##### (a) Compensation of officers\nSection 330 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(1) by striking $45 and inserting $105 ; and\n**(2)**\nby striking subsection (e).\n##### (b) Remainder of fees\nNotwithstanding any other provision of law, the remainder of fees collected under section 1930(a)(1)(A) of title 28, United States Code, after compensating trustees under section 330(b)(1) of title 11, United States Code, shall be deposited as follows:\n**(1)**\n$63.51 in the special fund of the Treasury established under section 1931 of title 28, United States Code.\n**(2)**\n$25.00 in the special fund established in accordance with section 10101(b) of the Deficit Reduction Act of 2005 ( 28 U.S.C. 1931 note).\n**(3)**\n$51.49 in the United States Trustee System Fund established under section 589a of title 28, United States Code.\n##### (c) United States Trustee System Fund\nSection 589a of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by striking paragraph (1) and inserting the following:\n(1) 28.33 percent of the fees collected under section 1930(a)(1)(B); ; and\n**(2)**\nin subsection (f)(1)\u2014\n**(A)**\nin subparagraph (D) by striking Fourth and inserting Second ;\n**(B)**\nby striking subparagraphs (B) and (C); and\n**(C)**\nby redesignating subparagraph (D) as subparagraph (B).\n#### 4. Bankruptcy fees\n##### (a) Quarterly fees\nSection 1930(a)(6)(B) of title 28, United States Code, is amended\u2014\n**(1)**\nin clause (i), by striking 5-year and inserting 10-year ; and\n**(2)**\nin clause (ii)(II), by striking 0.8 and inserting 1.1 .\n##### (b) Period for deposits\nSection 589a(f) of title 28, United States Code, as amended by section 3(c)(2), is amended by striking 2026 each place it appears and inserting 2031 .\n##### (c) Deposits of certain fees for fiscal years 2026 through 2031\nNotwithstanding section 589a(b) of title 28, United States Code, for each of fiscal years 2026 through 2031\u2014\n**(1)**\nthe fees collected under section 1930(a)(6) of title 28, United States Code, less the amount specified in subparagraph (2) of this subsection, shall be deposited as specified in section 589a(f) of title 28, United States Code, as amended by this Act; and\n**(2)**\n$5,400,000 of the fees collected under section 1930(a)(6) of title 28, United States Code, shall be deposited in the general fund of the Treasury.\n#### 5. Extension of term of certain temporary offices of bankruptcy judge\n##### (a) Bankruptcy Administration Improvement Act of 2020\nSection 4 of the Bankruptcy Administration Improvement Act of 2020 ( 28 U.S.C. 152 note) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ;\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(C)**\nin subparagraph (C)(i), by striking 5 years and inserting 10 years ;\n**(D)**\nin subparagraph (D)(i), by striking 5 years and inserting 10 years ;\n**(E)**\nin subparagraph (E)(i), by striking 5 years and inserting 10 years ; and\n**(F)**\nin subparagraph (F)(i), by striking 5 years and inserting 10 years ;\n**(3)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(4)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(5)**\nin subsection (e)(2)(A), by striking 5 years and inserting 10 years ; and\n**(6)**\nin subsection (f)(2)(A), by striking 5 years and inserting 10 years .\n##### (b) Bankruptcy Judgeship Act of 2017\nSection 1003(b)(2)(A) of the Bankruptcy Judgeship Act of 2017 ( 28 U.S.C. 152 note) is amended by striking \u2018 \u20185 years\u2019 \u2019 and inserting \u2018 \u201810 years\u2019 \u2019.\n#### 6. Effective date; application of amendments\n##### (a) In general\nExcept as provided in paragraph (2), the amendments made by this Act shall take effect on October 1 that first occurs after the date of enactment of this Act.\n##### (b) Exceptions\n**(1) Compensation of officers**\nSection 3 and the amendments made by section 3 shall apply to any case under title 11, United States Code, commenced on or after October 1 that first occurs after the date of enactment of this Act\u2014\n**(A)**\nunder chapter 7 of title 11, United States Code; or\n**(B)**\nunder chapter 11, 12, or 13 of title 11, United States Code, that is converted to a case under chapter 7 of title 7, United States Code.\n**(2) Bankruptcy fees**\nSection 4 and the amendments made by section 4 shall apply to\u2014\n**(A)**\nany case pending under chapter 11 of title 11, United States Code, on or after October 1 that first occurs after the date of enactment of this Act; and\n**(B)**\nquarterly fees payable under section 1930(a)(6) of title 28, United States Code, for disbursements made in any calendar quarter that begins on or after October 1 that first occurs after the date of enactment of this Act.",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-08-08",
        "actionTime": "11:45:01",
        "text": "Held at the desk."
      },
      "number": "1659",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-06",
        "text": "Became Public Law No: 119-76."
      },
      "number": "3424",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bankruptcy Administration Improvement Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Bankruptcy",
            "updateDate": "2025-08-06T17:03:23Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-08-06T17:03:23Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-08-06T17:03:23Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-08-06T17:03:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-02T13:30:54Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3867ih.xml"
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
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T08:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 11 and 28, United States Code, to modify the compensation payable to trustees serving in cases under chapter 7 of title 11, United States Code, to extend the term of certain temporary offices of bankruptcy judges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T08:03:34Z"
    }
  ]
}
```
