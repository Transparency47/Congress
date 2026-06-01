# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/654
- Title: TABS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 654
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-04-10T08:06:11Z
- Update date including text: 2026-04-10T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/654",
    "number": "654",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "TABS Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:11Z",
    "updateDateIncludingText": "2026-04-10T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:03:15Z",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-04",
      "state": "SC"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MO"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NE"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NY"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "WI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "WI"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "GA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MT"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr654ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 654\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo change the Bureau of Consumer Financial Protection into an independent agency named the Consumer Financial Empowerment Agency, to transition the Agency to the regular appropriations process, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taking Account of Bureaucrats\u2019 Spending Act of 2025 or the TABS Act of 2025 .\n#### 2. Consumer Financial Empowerment Agency\n##### (a) Making the Bureau an independent Consumer Financial Empowerment Agency\nThe Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5481 et seq. ) is amended\u2014\n**(1)**\nin section 1011\u2014\n**(A)**\nin the heading of such section, by striking BUREAU OF CONSUMER FINANCIAL PROTECTION and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nin subsection (a)\u2014\n**(i)**\nin the heading of such subsection, by striking Bureau and inserting Agency ;\n**(ii)**\nby striking in the Federal Reserve System, ;\n**(iii)**\nby striking independent bureau and inserting independent agency ; and\n**(iv)**\nby striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency (hereinafter in this section referred to as the Agency ) ;\n**(C)**\nin subsection (b)(5), by amending subparagraph (A) to read as follows:\n(A) shall be appointed by the President; and ;\n**(D)**\nin subsection (c), by striking paragraph (3);\n**(E)**\nin subsection (e), by striking , including in cities in which the Federal reserve banks, or branches of such banks, are located, ; and\n**(F)**\nby striking Bureau each place such term appears and inserting Agency ; and\n**(2)**\nin section 1012\u2014\n**(A)**\nin subsection (a)(10), by striking examinations, ; and\n**(B)**\nby striking subsection (c).\n##### (b) Deeming of name\nAny reference in a law, regulation, document, paper, or other record of the United States to the Bureau of Consumer Financial Protection shall be deemed a reference to the Consumer Financial Empowerment Agency.\n##### (c) Conforming amendments\n**(1) Dodd-Frank Wall Street Reform and Consumer Protection Act**\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(A)**\nin the table of contents in section 1(b)\u2014\n**(i)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ; and\n**(ii)**\nin the table of contents relating to title X, in the items relating to subtitle B, subtitle C, and section 1027, by striking Bureau each place such term appears and inserting Agency ;\n**(B)**\nin section 2, by amending paragraph (4) to read as follows:\n(4) Agency The term Agency means the Consumer Financial Empowerment Agency established under title X. ;\n**(C)**\nin section 342 by striking Bureau each place such term appears in headings and text and inserting Agency ;\n**(D)**\nin section 1400(b)\u2014\n**(i)**\nby striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ; and\n**(ii)**\nin the subsection heading, by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ;\n**(E)**\nin section 1411(a)(1), by striking Bureau and inserting Agency ; and\n**(F)**\nin section 1447, by striking Director of the Bureau each place such term appears and inserting Director of the Consumer Financial Empowerment Agency .\n**(2) Alternative Mortgage Transaction Parity Act of 1982**\nThe Alternative Mortgage Transaction Parity Act of 1982 ( 12 U.S.C. 3801 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ; and\n**(B)**\nin the subsection heading of subsection (d) of section 804 ( 12 U.S.C. 3803(d) ), by striking Bureau and inserting Agency .\n**(3) Electronic Fund Transfer Act**\nThe Electronic Fund Transfer Act ( 15 U.S.C. 1693 et seq. ) is amended\u2014\n**(A)**\nby amending the second paragraph (4) (defining the term Bureau ) to read as follows:\n(4) the term Agency means the Consumer Financial Empowerment Agency; ;\n**(B)**\nin section 916(d)(1), by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ; and\n**(C)**\nby striking Bureau each place that term appears in heading or text and inserting Agency .\n**(4) Equal Credit Opportunity Act**\nThe Equal Credit Opportunity Act ( 15 U.S.C. 1691 et seq. ) is amended\u2014\n**(A)**\nin section 702 ( 15 U.S.C. 1691a ), by amending subsection (c) to read as follows:\n(c) The term Agency means the Consumer Financial Empowerment Agency. ; and\n**(B)**\nby striking Bureau each place that term appears in heading or text and inserting Agency .\n**(5) Expedited Funds Availability Act**\nThe Expedited Funds Availability Act ( 12 U.S.C. 4001 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ; and\n**(B)**\nin the heading of section 605(f)(1), by striking board and bureau and inserting Board and Agency .\n**(6) Fair and Accurate Credit Transactions Act of 2003**\nThe Fair and Accurate Credit Transactions Act of 2003 ( Public Law 108\u2013159 ) is amended by striking Bureau each place such term appears in heading and text and inserting Agency .\n**(7) Fair Credit Reporting Act**\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended\u2014\n**(A)**\nby amending section 603(w) to read as follows:\n(w) Agency The term Agency means the Consumer Financial Empowerment Agency. ; and\n**(B)**\nby striking Bureau each place such term appears, other than in sections 626 and 603(v), and inserting Agency .\n**(8) Fair Debt Collection Practices Act**\nThe Fair Debt Collection Practices Act ( 15 U.S.C. 1692 et seq. ) is amended\u2014\n**(A)**\nby amending section 803(1) to read as follows:\n(1) The term Agency means the Consumer Financial Empowerment Agency. ; and\n**(B)**\nby striking Bureau each place such term appears in heading or text and inserting Agency .\n**(9) Federal Deposit Insurance Act**\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(A)**\nin the second paragraph (6) (with the heading Referral to bureau of consumer financial protection ) of section 8(t) ( 12 U.S.C. 1818(t) )\u2014\n**(i)**\nin the paragraph heading, by striking bureau of consumer financial protection ; and inserting Consumer Financial Empowerment Agency ; and\n**(ii)**\nby striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nby amending clause (vi) of section 11(t)(2)(A) ( 12 U.S.C. 1821(t)(2)(A)(vi) ) to read as follows:\n(vi) The Consumer Financial Empowerment Agency. ;\n**(C)**\nin section 18(x) ( 12 U.S.C. 1828(x) ), by striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(D)**\nby striking Bureau each place such term appears and inserting Agency ; and\n**(E)**\nin section 43(e) ( 12 U.S.C. 1831t(e) ), by amending paragraph (5) to read as follows:\n(5) Agency The term Agency means the Consumer Financial Empowerment Agency. .\n**(10) Federal Financial Institutions Examination Council Act of 1978**\nThe Federal Financial Institutions Examination Council Act of 1978 ( 12 U.S.C. 3301 et seq. ) is amended\u2014\n**(A)**\nin section 1004(a)(4), by striking Consumer Financial Protection Bureau and inserting Consumer Financial Empowerment Agency ; and\n**(B)**\nin section 1011, by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(11) Financial Institutions Reform, Recovery, and Enforcement Act of 1989**\nThe Financial Institutions Reform, Recovery, and Enforcement Act of 1989 ( Public Law 101\u201373 ; 103 Stat. 183) is amended\u2014\n**(A)**\nin section 1112(b) ( 12 U.S.C. 3341 ), by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nin section 1124 ( 12 U.S.C. 3353 ), by striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(C)**\nin section 1125 ( 12 U.S.C. 3354 ), by striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ; and\n**(D)**\nin section 1206(a) ( 12 U.S.C. 1833b(a) ), by striking Federal Housing Finance Board and all that follows through Farm Credit Administration and inserting Federal Housing Finance Agency, the Consumer Financial Empowerment Agency, and the Farm Credit Administration .\n**(12) Financial Literacy and Education Improvement Act**\nSection 513 of the Financial Literacy and Education Improvement Act ( 20 U.S.C. 9702 ) is amended by striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency .\n**(13) Gramm-leach-bliley Act**\nTitle V of the Gramm-Leach-Bliley Act ( 15 U.S.C. 6801 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ; and\n**(B)**\nin section 505(a)(8) ( 15 U.S.C. 6805(a)(8) ), by striking Bureau and inserting Agency .\n**(14) Home Mortgage Disclosure Act of 1975**\nThe Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nby striking Bureau each place such term appears and inserting Agency ; and\n**(C)**\nin section 303, by amending paragraph (1) to read as follows:\n(1) the term Agency means the Consumer Financial Empowerment Agency; .\n**(15) Homeowners Protection Act of 1998**\nSection 10(a)(4) of the Homeowners Protection Act of 1998 ( 12 U.S.C. 4909(a)(4) ) is amended by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(16) Home Ownership and Equity Protection Act of 1994**\nSection 158(a) of the Home Ownership and Equity Protection Act of 1994 ( 15 U.S.C. 1601 note) is amended by striking Bureau and inserting Consumer Financial Empowerment Agency .\n**(17) Interstate Land Sales Full Disclosure Act**\nThe Interstate Land Sales Full Disclosure Act ( 12 U.S.C. 1701 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Agency ;\n**(B)**\nin section 1402, by amending paragraph (12) to read as follows:\n(12) Agency means the Consumer Financial Empowerment Agency. ; and\n**(C)**\nin section 1416, by striking Bureau each place such term appears and inserting Agency .\n**(18) Real Estate Settlement Procedures Act of 1974**\nThe Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2601 et seq. ) is amended\u2014\n**(A)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nby striking Bureau each place such term appears and inserting Agency ; and\n**(C)**\nin section 3, by amending paragraph (9) to read as follows:\n(9) the term Agency means the Consumer Financial Empowerment Agency. .\n**(19) Revised Statues of the United States**\nSection 5136C(b)(3)(B) of the Revised Statutes of the United States ( 12 U.S.C. 25b(b)(3)(B) ) is amended by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(20) Right to Financial Privacy Act of 1978**\nThe Right to Financial Privacy Act of 1978 ( 12 U.S.C. 3401 et seq. ) is amended\u2014\n**(A)**\nby amending subparagraph (B) of section 1101(7) ( 12 U.S.C. 3401(7)(B) ) to read as follows:\n(B) the Consumer Financial Empowerment Agency; ; and\n**(B)**\nby striking Bureau of Consumer Financial Protection each place such term appears in heading or text and inserting Consumer Financial Empowerment Agency .\n**(21) S.A.F.E. Mortgage Licensing Act of 2008**\nThe S.A.F.E. Mortgage Licensing Act of 2008 ( 12 U.S.C. 5101 et seq. ) is amended\u2014\n**(A)**\nin section 1507, by striking Bureau, and the Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nby striking Bureau of Consumer Financial Protection each place such term appears and inserting Consumer Financial Empowerment Agency ;\n**(C)**\nby striking Bureau each place such appears, other than in sections 1505(a)(1), 1507(a)(2)(A), and 1511(b), and inserting Agency ;\n**(D)**\nin section 1503, by amending paragraph (1) to read as follows:\n(1) Agency The term Agency means the Consumer Financial Empowerment Agency. ;\n**(E)**\nin the heading of section 1508, by striking BUREAU OF CONSUMER FINANCIAL PROTECTION and inserting Consumer Financial Empowerment Agency ; and\n**(F)**\nin the heading of section 1514, by striking BUREAU and inserting AGENCY .\n**(22) Telemarketing and Consumer Fraud and Abuse Prevention Act**\nThe Telemarketing and Consumer Fraud and Abuse Prevention Act ( 15 U.S.C. 6101 et seq. ) is amended by striking Bureau of Consumer Financial Protection each place such term appears in heading or text and inserting Consumer Financial Empowerment Agency .\n**(23) Title 5, United States Code**\nTitle 5, United States Code, is amended\u2014\n**(A)**\nin section 552a(w)\u2014\n**(i)**\nin the subsection heading, by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ; and\n**(ii)**\nby striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency ;\n**(B)**\nin section 609(d)(2), by striking Consumer Financial Protection Bureau of the Federal Reserve System and inserting Consumer Financial Empowerment Agency ; and\n**(C)**\nin section 3132(a)(1)(D), by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(24) Title 10, United States Code**\n**(A) Section 987**\nSection 987(h)(3)(E) of title 10, United States Code, is amended by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(B) NDAA FY 2015**\nSection 557(a) of the Carl Levin and Howard P. Buck McKeon National Defense Authorization Act for Fiscal Year 2015 ( Public Law 113\u201329 ; 128 Stat. 3381; 10 U.S.C. 1144 note), is amended by striking Consumer Financial Protection Bureau each place such term appears and inserting Consumer Financial Empowerment Agency .\n**(25) Title 44, United States Code**\nTitle 44, United States Code, is amended\u2014\n**(A)**\nin section 3502(5), by striking the Bureau of Consumer Financial Protection, ; and\n**(B)**\nin section 3513(c), by striking Bureau of Consumer Financial Protection and inserting Consumer Financial Empowerment Agency .\n**(26) Truth in Lending Act**\nThe Truth in Lending Act ( 15 U.S.C. 1601 et seq. ) is amended\u2014\n**(A)**\nby amending section 103(b) ( 15 U.S.C. 1602(b) ) to read as follows:\n(b) Agency The term Agency means the Consumer Financial Empowerment Agency. ;\n**(B)**\nby amending section 103(c) ( 15 U.S.C. 1602(c) ) to read as follows:\n(c) Board The term Board means the Board of Governors of the Federal Reserve System. ;\n**(C)**\nin section 128(f) ( 15 U.S.C. 1638(f) ), by striking Board each place such term appears and inserting Agency ;\n**(D)**\nin sections 129B ( 15 U.S.C. 1639b ) and 129C ( 15 U.S.C. 1639c ), by striking Board each place such term appears and inserting Agency ;\n**(E)**\nin section 140A ( 15 U.S.C. 1651 ), by striking in consultation with the Bureau and inserting in consultation with the Federal Trade Commission ;\n**(F)**\nby striking Bureau each place such term appears in heading or text and inserting Agency ; and\n**(G)**\nby striking bureau and inserting Agency in the paragraph headings for\u2014\n**(i)**\nsection 122(d)(2) ( 15 U.S.C. 1632(d)(2) );\n**(ii)**\nsection 127(c)(5) ( 15 U.S.C. 1637(c)(5) );\n**(iii)**\nsection 127(r)(3) ( 15 U.S.C. 1637(r)(3) ); and\n**(iv)**\nsection 127A(a)(14) ( 15 U.S.C. 1637a(a)(14) ).\n**(27) Truth in Savings Act**\nThe Truth in Savings Act ( 12 U.S.C. 4301 et seq. ) is amended\u2014\n**(A)**\nby amending paragraph (4) of section 274 ( 12 U.S.C. 4313(4) ) to read as follows:\n(4) Agency The term Agency means the Consumer Financial Empowerment Agency. ;\n**(B)**\nby striking National Credit Union Administration Bureau each place such term appears and inserting National Credit Union Administration Board ; and\n**(C)**\nby striking Bureau each place such term appears and inserting Agency , except in section 233(b)(4)(B).\n#### 3. Bringing the Agency into the regular appropriations process\nSection 1017 of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5497 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending the heading of such subsection to read as follows: Budget, financial management, and audit.\u2014 ;\n**(B)**\nby striking paragraphs (1), (2), and (3);\n**(C)**\nby redesignating paragraphs (4) and (5) as paragraphs (1) and (2), respectively; and\n**(D)**\nby striking subparagraphs (E) and (F) of paragraph (1), as so redesignated;\n**(2)**\nby striking subsections (b) and (c);\n**(3)**\nby redesignating subsections (d) and (e) as subsections (b) and (c), respectively; and\n**(4)**\nin subsection (c), as so redesignated\u2014\n**(A)**\nby striking paragraphs (1), (2), and (3) and inserting the following:\n(1) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary to carry out this title for each of fiscal years 2026 and 2027. ; and\n**(B)**\nby redesignating paragraph (4) as paragraph (2).",
      "versionDate": "2025-01-23",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-02-24T20:49:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "House",
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
          "measure-id": "id119hr654",
          "measure-number": "654",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr654v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Taking Account of Bureaucrats' Spending Act of 2025 or the TABS Act of 2025 </strong></p><p>This bill restructures the Consumer Financial Protection Bureau and renames it as the Consumer Financial Empowerment Agency. The new agency is established as an independent agency outside of the Federal Reserve System.</p><p>The bill also changes the funding structure of the agency by prohibiting the transfer of funds to the agency from the Federal Reserve System and by authorizing congressional appropriations for FY2026-FY2027.</p>"
        },
        "title": "TABS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr654.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Taking Account of Bureaucrats' Spending Act of 2025 or the TABS Act of 2025 </strong></p><p>This bill restructures the Consumer Financial Protection Bureau and renames it as the Consumer Financial Empowerment Agency. The new agency is established as an independent agency outside of the Federal Reserve System.</p><p>The bill also changes the funding structure of the agency by prohibiting the transfer of funds to the agency from the Federal Reserve System and by authorizing congressional appropriations for FY2026-FY2027.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr654"
    },
    "title": "TABS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Taking Account of Bureaucrats' Spending Act of 2025 or the TABS Act of 2025 </strong></p><p>This bill restructures the Consumer Financial Protection Bureau and renames it as the Consumer Financial Empowerment Agency. The new agency is established as an independent agency outside of the Federal Reserve System.</p><p>The bill also changes the funding structure of the agency by prohibiting the transfer of funds to the agency from the Federal Reserve System and by authorizing congressional appropriations for FY2026-FY2027.</p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr654"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr654ih.xml"
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
      "title": "TABS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TABS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taking Account of Bureaucrats\u2019 Spending Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To change the Bureau of Consumer Financial Protection into an independent agency named the Consumer Financial Empowerment Agency, to transition the Agency to the regular appropriations process, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:33:47Z"
    }
  ]
}
```
