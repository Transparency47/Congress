# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1659
- Title: Bankruptcy Administration Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1659
- Origin chamber: Senate
- Introduced date: 2025-05-07
- Update date: 2026-03-12T15:08:26Z
- Update date including text: 2026-03-12T15:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, amendments, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in Senate
- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-08-01 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S5475-5476)
- 2025-08-01 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)
- 2025-08-01 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)
- 2025-08-01 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-01 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-08 - Floor: Message on Senate action sent to the House.
- 2025-08-08 11:33:35 - Floor: Received in the House.
- 2025-08-08 11:45:01 - Floor: Held at the desk.
- Latest action: 2025-05-07: Introduced in Senate

## Actions

- 2025-05-07 - IntroReferral: Introduced in Senate
- 2025-05-07 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-08-01 - Floor: Measure laid before Senate by unanimous consent. (consideration: CR S5475-5476)
- 2025-08-01 - Floor: Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)
- 2025-08-01 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)
- 2025-08-01 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-01 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-08-08 - Floor: Message on Senate action sent to the House.
- 2025-08-08 11:33:35 - Floor: Received in the House.
- 2025-08-08 11:45:01 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1659",
    "number": "1659",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Bankruptcy Administration Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-03-12T15:08:26Z",
    "updateDateIncludingText": "2026-03-12T15:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-08-08",
      "actionTime": "11:45:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-08-08",
      "actionTime": "11:33:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent. (text: CR S5475-5476)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Measure laid before Senate by unanimous consent. (consideration: CR S5475-5476)",
      "type": "Floor"
    },
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
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

## API Data: amendments

```json
{
  "amendments": [
    {
      "amendment": {
        "actions": {
          "actions": {
            "item": [
              {
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3680 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "0",
                  "name": "Senate"
                },
                "text": "Amendment SA 3680 proposed by Senator Thune for Senator Coons. (consideration: CR S5475-5476) To make a technical correction.",
                "type": "Floor"
              },
              {
                "actionCode": "Intro-S",
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "type": "IntroReferral"
              },
              {
                "actionCode": "93000",
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment proposed (on the floor): Amendment SA 3680 proposed by Senator Thune for Senator Coons.",
                "type": "Floor"
              },
              {
                "actionCode": "94000",
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment agreed to: Amendment SA 3680 agreed to in Senate by Unanimous Consent.",
                "type": "Floor"
              },
              {
                "actionCode": "91000",
                "actionDate": "2025-08-01",
                "sourceSystem": {
                  "code": "9",
                  "name": "Library of Congress"
                },
                "text": "Senate amendment submitted",
                "type": "Floor"
              }
            ]
          },
          "count": "6"
        },
        "amendedBill": {
          "congress": "119",
          "number": "1659",
          "originChamber": "Senate",
          "originChamberCode": "S",
          "title": "Bankruptcy Administration Improvement Act of 2025",
          "type": "S",
          "updateDateIncludingText": "2026-03-12"
        },
        "chamber": "Senate",
        "congress": "119",
        "latestAction": {
          "actionDate": "2025-08-01",
          "links": {
            "link": {
              "name": "SA 3680",
              "url": "https://www.congress.gov/amendment/119th-congress/senate-amendment/3680"
            }
          },
          "text": "Amendment SA 3680 agreed to in Senate by Unanimous Consent."
        },
        "number": "3680",
        "onBehalfOfSponsor": {
          "item": [
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Submitted on behalf of"
            },
            {
              "bioguideId": "T000250",
              "firstName": "John",
              "fullName": "Sen. Thune, John [R-SD]",
              "lastName": "Thune",
              "party": "R",
              "state": "SD",
              "type": "Proposed on behalf of"
            }
          ]
        },
        "proposedDate": "2025-08-01T04:00:00Z",
        "purpose": "To make a technical correction.",
        "sponsors": {
          "item": {
            "bioguideId": "C001088",
            "firstName": "Christopher",
            "fullName": "Sen. Coons, Christopher A. [D-DE]",
            "lastName": "Coons",
            "middleName": "A.",
            "party": "D",
            "state": "DE"
          }
        },
        "submittedDate": "2025-08-01T04:00:00Z",
        "textVersions": {
          "count": "1"
        },
        "type": "SAMDT",
        "updateDate": "2026-03-12T15:08:26Z"
      }
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
            "date": "2025-08-02T01:59:00Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-05-07T21:14:04Z",
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
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "SC"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "MI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NC"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "VA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1659is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1659\nIN THE SENATE OF THE UNITED STATES\nMay 7, 2025 Mr. Coons (for himself, Mr. Graham , Mr. Booker , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend titles 11 and 28, United States Code, to modify the compensation payable to trustees serving in cases under chapter 7 of title 11, United States Code, to extend the term of certain temporary offices of bankruptcy judges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Administration Improvement Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress has amended the laws governing bankruptcy fees as necessary to ensure that the bankruptcy system remains self-supporting, while also fairly allocating the costs of the system among those who use the system.\n**(2)**\nBecause of the importance for the bankruptcy system to be self-funded, at no cost to taxpayers, Congress has closely monitored the funding needs of the bankruptcy system, including by requiring periodic reporting by the Attorney General regarding the United States Trustee System Fund.\n**(3)**\nBecause the system governing bankruptcies of various types is interconnected, Congress has established fees, including filing fees, quarterly fees in chapter 11 cases, and other fees, that together fund the courts, judges, United States trustees, and trustees serving in bankruptcy cases under chapter 7 of title 11, United States Code.\n**(4)**\nTrustees serving in bankruptcy cases under chapter 7 of title 11, United States Code, are vital to the functioning of the bankruptcy system, as they provide services at the front lines of the bankruptcy process, administering thousands of cases.\n**(5)**\nChapter 7 bankruptcy trustees provide valuable returns of assets to government creditors, including the Internal Revenue Service, the Department of Agriculture, the Small Business Administration, and other Federal, State, and municipal governments.\n**(6)**\nDue to the work of the chapter 7 bankruptcy trustees, millions of dollars are also disbursed annually to private creditors of all types, including medical providers, unsecured creditors, small businesses, and micro-enterprises such as domestic support providers.\n**(7)**\nDespite the essential role of chapter 7 bankruptcy trustees, since 1994 the amount of compensation paid to these trustees has not been increased. As in 1994, bankruptcy trustees receive only $60 per case (composed of $45 from subsection 330(b)(1), and $15 from subsection 330(b)(2), of title 11, United States Code) in nearly 90 percent of chapter 7 cases, and bankruptcy trustees receive no compensation at all for cases in which the filing fee is waived by the bankruptcy court.\n**(8)**\nSince 1994, there have been significant increases in salaries, attorney fees, budget appropriations, filing fees, and court-related fees associated with chapter 7 bankruptcies. In contrast, the $60 paid to chapter 7 trustees has remained the same and has not even been increased for inflation. In 2021, Congress attempted to implement a mechanism that would give chapter 7 trustees a raise, but the trustees only received increased compensation for 1 fiscal year. Based on Consumer Price Index estimates, the $60 paid to trustees in 1994 would be the equivalent of over $125 today.\n**(9)**\nThis Act and the amendments made by this Act\u2014\n**(A)**\nincrease the compensation of chapter 7 bankruptcy trustees to the level that is appropriate, overdue, and proportionate with the level that was intended in 1994, by increasing the total compensation of trustees to $120 per case;\n**(B)**\nensure adequate funding of the United States trustee system through the increase of certain fees, which will also apply to districts that are not part of a United States trustee region as required by existing law; and\n**(C)**\nsupport the preservation of existing bankruptcy judgeships that are urgently needed to handle existing and anticipated increases in business and consumer caseloads.\n**(10)**\nThis Act will not alter the filing fee under chapter 7 of title 11, United States Code, and will not modify, impair, or supersede the current authority of the district courts of the United States, or of bankruptcy courts, to waive the payment of filing fees by indigent individuals.\n#### 3. Trustee compensation\n##### (a) Compensation of officers\nSection 330 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(1) by striking $45 and inserting $105 ; and\n**(2)**\nby striking subsection (e).\n##### (b) Remainder of fees\nNotwithstanding any other provision of law, the remainder of fees collected under section 1930(a)(1)(A) of title 28, United States Code, after compensating trustees under section 330(b)(1) of title 11, United States Code, shall be deposited as follows:\n**(1)**\n$63.51 in the special fund of the Treasury established under section 1931 of title 28, United States Code.\n**(2)**\n$25.00 in the special fund established in accordance with section 10101(b) of the Deficit Reduction Act of 2005 ( 28 U.S.C. 1931 note).\n**(3)**\n$51.49 in the United States Trustee System Fund established under section 589a of title 28, United States Code.\n##### (c) United States Trustee System Fund\nSection 589a of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by striking paragraph (1) and inserting the following:\n(1) 28.33 percent of the fees collected under section 1930(a)(1)(B); ; and\n**(2)**\nin subsection (f)(1)\u2014\n**(A)**\nin subparagraph (D) by striking Fourth and inserting Second ;\n**(B)**\nby striking subparagraphs (B) and (C); and\n**(C)**\nby redesignating subparagraph (D) as subparagraph (B).\n#### 4. Bankruptcy fees\n##### (a) Quarterly fees\nSection 1930(a)(6)(B) of title 28, United States Code, is amended\u2014\n**(1)**\nin clause (i), by striking 5-year and inserting 10-year ; and\n**(2)**\nin clause (ii)(II), by striking 0.8 and inserting 1.1 .\n##### (b) Period for deposits\nSection 589a(f) of title 28, United States Code, as amended by section 3(c)(2), is amended by striking 2026 each place it appears and inserting 2031 .\n##### (c) Deposits of certain fees for fiscal years 2026 through 2031\nNotwithstanding section 589a(b) of title 28, United States Code, for each of fiscal years 2026 through 2031\u2014\n**(1)**\nthe fees collected under section 1930(a)(6) of title 28, United States Code, less the amount specified in subparagraph (2) of this subsection, shall be deposited as specified in section 589a(f) of title 28, United States Code, as amended by this Act; and\n**(2)**\n$5,400,000 of the fees collected under section 1930(a)(6) of title 28, United States Code, shall be deposited in the general fund of the Treasury.\n#### 5. Extension of term of certain temporary offices of bankruptcy judge\n##### (a) Bankruptcy Administration Improvement Act of 2020\nSection 4 of the Bankruptcy Administration Improvement Act of 2020 ( 28 U.S.C. 152 note) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ;\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(C)**\nin subparagraph (C)(i), by striking 5 years and inserting 10 years ;\n**(D)**\nin subparagraph (D)(i), by striking 5 years and inserting 10 years ;\n**(E)**\nin subparagraph (E)(i), by striking 5 years and inserting 10 years ; and\n**(F)**\nin subparagraph (F)(i), by striking 5 years and inserting 10 years ;\n**(3)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(4)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(5)**\nin subsection (e)(2)(A), by striking 5 years and inserting 10 years ; and\n**(6)**\nin subsection (f)(2)(A), by striking 5 years and inserting 10 years .\n##### (b) Bankruptcy Judgeship Act of 2017\nSection 1003(b)(2)(A) of the Bankruptcy Judgeship Act of 2017 ( 28 U.S.C. 152 note) is amended by striking \u2018\u20185 years\u2019\u2019 and inserting \u2018\u201810 years\u2019\u2019.\n#### 6. Effective date; application of amendments\n##### (a) In general\nExcept as provided in paragraph (2), the amendments made by this Act shall take effect on October 1 that first occurs after the date of enactment of this Act.\n##### (b) Exceptions\n**(1) Compensation of officers**\nSection 3 and the amendments made by section 3 shall apply to any case under title 11, United States Code, commenced on or after October 1 that first occurs after the date of enactment of this Act\u2014\n**(A)**\nunder chapter 7 of title 11, United States Code; or\n**(B)**\nunder chapter 11, 12, or 13 of title 11, United States Code, that is converted to a case under chapter 7 of title 7, United States Code.\n**(2) Bankruptcy fees**\nSection 4 and the amendments made by section 4 shall apply to\u2014\n**(A)**\nany case pending under chapter 11 of title 11, United States Code, on or after October 1 that first occurs after October 1 that first occurs after the date of enactment of this Act; and\n**(B)**\nquarterly fees payable under section 1930(a)(6) of title 28, United States Code, for disbursements made in any calendar quarter that begins on or after October 1 that first occurs after the date of enactment of this Act.",
      "versionDate": "2025-05-07",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1659es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1659\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend titles 11 and 28, United States Code, to modify the compensation payable to trustees serving in cases under chapter 7 of title 11, United States Code, to extend the term of certain temporary offices of bankruptcy judges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bankruptcy Administration Improvement Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCongress has amended the laws governing bankruptcy fees as necessary to ensure that the bankruptcy system remains self-supporting, while also fairly allocating the costs of the system among those who use the system.\n**(2)**\nBecause of the importance for the bankruptcy system to be self-funded, at no cost to taxpayers, Congress has closely monitored the funding needs of the bankruptcy system, including by requiring periodic reporting by the Attorney General regarding the United States Trustee System Fund.\n**(3)**\nBecause the system governing bankruptcies of various types is interconnected, Congress has established fees, including filing fees, quarterly fees in chapter 11 cases, and other fees, that together fund the courts, judges, United States trustees, and trustees serving in bankruptcy cases under chapter 7 of title 11, United States Code.\n**(4)**\nTrustees serving in bankruptcy cases under chapter 7 of title 11, United States Code, are vital to the functioning of the bankruptcy system, as they provide services at the front lines of the bankruptcy process, administering thousands of cases.\n**(5)**\nChapter 7 bankruptcy trustees provide valuable returns of assets to government creditors, including the Internal Revenue Service, the Department of Agriculture, the Small Business Administration, and other Federal, State, and municipal governments.\n**(6)**\nDue to the work of the chapter 7 bankruptcy trustees, millions of dollars are also disbursed annually to private creditors of all types, including medical providers, unsecured creditors, small businesses, and micro-enterprises such as domestic support providers.\n**(7)**\nDespite the essential role of chapter 7 bankruptcy trustees, since 1994 the amount of compensation paid to these trustees has not been increased. As in 1994, bankruptcy trustees receive only $60 per case (composed of $45 from subsection 330(b)(1), and $15 from subsection 330(b)(2), of title 11, United States Code) in nearly 90 percent of chapter 7 cases, and bankruptcy trustees receive no compensation at all for cases in which the filing fee is waived by the bankruptcy court.\n**(8)**\nSince 1994, there have been significant increases in salaries, attorney fees, budget appropriations, filing fees, and court-related fees associated with chapter 7 bankruptcies. In contrast, the $60 paid to chapter 7 trustees has remained the same and has not even been increased for inflation. In 2021, Congress attempted to implement a mechanism that would give chapter 7 trustees a raise, but the trustees only received increased compensation for 1 fiscal year. Based on Consumer Price Index estimates, the $60 paid to trustees in 1994 would be the equivalent of over $125 today.\n**(9)**\nThis Act and the amendments made by this Act\u2014\n**(A)**\nincrease the compensation of chapter 7 bankruptcy trustees to the level that is appropriate, overdue, and proportionate with the level that was intended in 1994, by increasing the total compensation of trustees to $120 per case;\n**(B)**\nensure adequate funding of the United States trustee system through the increase of certain fees, which will also apply to districts that are not part of a United States trustee region as required by existing law; and\n**(C)**\nsupport the preservation of existing bankruptcy judgeships that are urgently needed to handle existing and anticipated increases in business and consumer caseloads.\n**(10)**\nThis Act will not alter the filing fee under chapter 7 of title 11, United States Code, and will not modify, impair, or supersede the current authority of the district courts of the United States, or of bankruptcy courts, to waive the payment of filing fees by indigent individuals.\n#### 3. Trustee compensation\n##### (a) Compensation of officers\nSection 330 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(1) by striking $45 and inserting $105 ; and\n**(2)**\nby striking subsection (e).\n##### (b) Remainder of fees\nNotwithstanding any other provision of law, the remainder of fees collected under section 1930(a)(1)(A) of title 28, United States Code, after compensating trustees under section 330(b)(1) of title 11, United States Code, shall be deposited as follows:\n**(1)**\n$63.51 in the special fund of the Treasury established under section 1931 of title 28, United States Code.\n**(2)**\n$25.00 in the special fund established in accordance with section 10101(b) of the Deficit Reduction Act of 2005 ( 28 U.S.C. 1931 note).\n**(3)**\n$51.49 in the United States Trustee System Fund established under section 589a of title 28, United States Code.\n##### (c) United States Trustee System Fund\nSection 589a of title 28, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by striking paragraph (1) and inserting the following:\n(1) 28.33 percent of the fees collected under section 1930(a)(1)(B); ; and\n**(2)**\nin subsection (f)(1)\u2014\n**(A)**\nin subparagraph (D) by striking Fourth and inserting Second ;\n**(B)**\nby striking subparagraphs (B) and (C); and\n**(C)**\nby redesignating subparagraph (D) as subparagraph (B).\n#### 4. Bankruptcy fees\n##### (a) Quarterly fees\nSection 1930(a)(6)(B) of title 28, United States Code, is amended\u2014\n**(1)**\nin clause (i), by striking 5-year and inserting 10-year ; and\n**(2)**\nin clause (ii)(II), by striking 0.8 and inserting 1.1 .\n##### (b) Period for deposits\nSection 589a(f) of title 28, United States Code, as amended by section 3(c)(2), is amended by striking 2026 each place it appears and inserting 2031 .\n##### (c) Deposits of certain fees for fiscal years 2026 through 2031\nNotwithstanding section 589a(b) of title 28, United States Code, for each of fiscal years 2026 through 2031\u2014\n**(1)**\nthe fees collected under section 1930(a)(6) of title 28, United States Code, less the amount specified in subparagraph (2) of this subsection, shall be deposited as specified in section 589a(f) of title 28, United States Code, as amended by this Act; and\n**(2)**\n$5,400,000 of the fees collected under section 1930(a)(6) of title 28, United States Code, shall be deposited in the general fund of the Treasury.\n#### 5. Extension of term of certain temporary offices of bankruptcy judge\n##### (a) Bankruptcy Administration Improvement Act of 2020\nSection 4 of the Bankruptcy Administration Improvement Act of 2020 ( 28 U.S.C. 152 note) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(2)**\nin subsection (b)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ;\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(C)**\nin subparagraph (C)(i), by striking 5 years and inserting 10 years ;\n**(D)**\nin subparagraph (D)(i), by striking 5 years and inserting 10 years ;\n**(E)**\nin subparagraph (E)(i), by striking 5 years and inserting 10 years ; and\n**(F)**\nin subparagraph (F)(i), by striking 5 years and inserting 10 years ;\n**(3)**\nin subsection (c)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(4)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A)(i), by striking 5 years and inserting 10 years ; and\n**(B)**\nin subparagraph (B)(i), by striking 5 years and inserting 10 years ;\n**(5)**\nin subsection (e)(2)(A), by striking 5 years and inserting 10 years ; and\n**(6)**\nin subsection (f)(2)(A), by striking 5 years and inserting 10 years .\n##### (b) Bankruptcy Judgeship Act of 2017\nSection 1003(b)(2)(A) of the Bankruptcy Judgeship Act of 2017 ( 28 U.S.C. 152 note) is amended by striking \u2018\u20185 years\u2019\u2019 and inserting \u2018\u201810 years\u2019\u2019.\n#### 6. Effective date; application of amendments\n##### (a) In general\nExcept as provided in paragraph (2), the amendments made by this Act shall take effect on October 1 that first occurs after the date of enactment of this Act.\n##### (b) Exceptions\n**(1) Compensation of officers**\nSection 3 and the amendments made by section 3 shall apply to any case under title 11, United States Code, commenced on or after October 1 that first occurs after the date of enactment of this Act\u2014\n**(A)**\nunder chapter 7 of title 11, United States Code; or\n**(B)**\nunder chapter 11, 12, or 13 of title 11, United States Code, that is converted to a case under chapter 7 of title 7, United States Code.\n**(2) Bankruptcy fees**\nSection 4 and the amendments made by section 4 shall apply to\u2014\n**(A)**\nany case pending under chapter 11 of title 11, United States Code, on or after October 1 that first occurs after the date of enactment of this Act; and\n**(B)**\nquarterly fees payable under section 1930(a)(6) of title 28, United States Code, for disbursements made in any calendar quarter that begins on or after October 1 that first occurs after the date of enactment of this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-06-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3867",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "type": "HR"
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
            "updateDate": "2025-08-06T15:44:35Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-08-06T15:44:44Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-08-06T15:46:42Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-08-06T15:44:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-28T13:28:56Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-01",
    "originChamber": "Senate",
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
          "measure-id": "id119s1659",
          "measure-number": "1659",
          "measure-type": "s",
          "orig-publish-date": "2025-08-01",
          "originChamber": "SENATE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1659v55",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-08-01",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Bankruptcy Administration Improvement Act of 2025</strong></p><p>This bill makes several changes to the administration of bankruptcy cases, particularly by increasing certain fees, extending the sunset date of various fees, and extending the term of specified bankruptcy judgeships.</p><p>The bill increases the fees paid to the trustee in Chapter 7 (liquidation) cases.</p><p>The bill extends for an additional five years the fees paid quarterly to the U.S. trustee in Chapter 11 (reorganization) cases. The bill also increases the fee percentage for cases with large disbursements, subject to limitations.\u00a0</p><p>Finally, temporary bankruptcy judgeships in various districts are extended for an additional five years.</p><p><strong></strong></p>"
        },
        "title": "Bankruptcy Administration Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1659.xml",
    "summary": {
      "actionDate": "2025-08-01",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Bankruptcy Administration Improvement Act of 2025</strong></p><p>This bill makes several changes to the administration of bankruptcy cases, particularly by increasing certain fees, extending the sunset date of various fees, and extending the term of specified bankruptcy judgeships.</p><p>The bill increases the fees paid to the trustee in Chapter 7 (liquidation) cases.</p><p>The bill extends for an additional five years the fees paid quarterly to the U.S. trustee in Chapter 11 (reorganization) cases. The bill also increases the fee percentage for cases with large disbursements, subject to limitations.\u00a0</p><p>Finally, temporary bankruptcy judgeships in various districts are extended for an additional five years.</p><p><strong></strong></p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s1659"
    },
    "title": "Bankruptcy Administration Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-08-01",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Bankruptcy Administration Improvement Act of 2025</strong></p><p>This bill makes several changes to the administration of bankruptcy cases, particularly by increasing certain fees, extending the sunset date of various fees, and extending the term of specified bankruptcy judgeships.</p><p>The bill increases the fees paid to the trustee in Chapter 7 (liquidation) cases.</p><p>The bill extends for an additional five years the fees paid quarterly to the U.S. trustee in Chapter 11 (reorganization) cases. The bill also increases the fee percentage for cases with large disbursements, subject to limitations.\u00a0</p><p>Finally, temporary bankruptcy judgeships in various districts are extended for an additional five years.</p><p><strong></strong></p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119s1659"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1659is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1659es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "updateDate": "2025-08-09T11:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-08-02T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bankruptcy Administration Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-23T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend titles 11 and 28, United States Code, to modify the compensation payable to trustees serving in cases under chapter 7 of title 11, United States Code, to extend the term of certain temporary offices of bankruptcy judges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-23T02:48:20Z"
    }
  ]
}
```
