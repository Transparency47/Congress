# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6556
- Title: Failing Bank Acquisition Fairness Act
- Congress: 119
- Bill type: HR
- Bill number: 6556
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 406.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.
- 2026-02-02 - Calendars: Placed on the Union Calendar, Calendar No. 406.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.
- 2026-02-02 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6556",
    "number": "6556",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000562",
        "district": "8",
        "firstName": "Stephen",
        "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
        "lastName": "Lynch",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Failing Bank Acquisition Fairness Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-02-02",
      "calendarNumber": {
        "calendar": "U00406"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 406.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-02",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-475.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 51 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
        "item": [
          {
            "date": "2026-02-02T15:19:06Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T17:46:56Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T17:46:48Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:06:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6556ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6556\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Lynch introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit the use of certain concentration limit exceptions with respect to mergers involving a failed bank unless the applicable agency determines such use is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Failing Bank Acquisition Fairness Act .\n#### 2. Concentration limit exceptions only available to avoid serious adverse economic or financial effects\n##### (a) Concentration limits with respect to deposits\n**(1) Federal Deposit Insurance Act**\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(A)**\nin section 18(c)(13)\u2014\n**(i)**\nby amending subparagraph (B) to read as follows:\n(B) Subparagraph (A) shall not apply to an interstate merger transaction if\u2014 (i) such interstate merger transaction involves 1 or more insured depository institutions in default or in danger of default and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from a company that is not subject to the prohibition in subparagraph (A); or (ii) the Corporation provides assistance under section 13 to facilitate such interstate merger transaction and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from a company that is not subject to the prohibition in subparagraph (A). ; and\n**(ii)**\nin subparagraph (C)\u2014\n**(I)**\nin clause (i), by striking and at the end;\n**(II)**\nin clause (ii), by striking the period at the end and inserting a semicolon; and\n**(III)**\nby adding at the end the following:\n(iii) the term qualified bid means an application, proposed application, or bid from a company where\u2014 (I) if applicable, the company, any affiliate insured depository institution, and any affiliate depository institution holding company is well capitalized and well managed, as of the date of the application, proposed application, or bid; and (II) upon consummation of the transaction, the resulting insured depository institution is well capitalized; (iv) the term well capitalized \u2014 (I) with respect to an insured depository institution, has the meaning given such term in section 38(b) ( 12 U.S.C. 1831o(b) ); (II) with respect to a bank holding company, has the meaning given such term in section 2(o)(1)(B) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(1)(B) ); (III) with respect to a savings and loan holding company, has the meaning given such term in section 238.2 of title 12, Code of Federal Regulations; and (IV) with respect to a company that is not an insured depository institution, bank holding company, or savings and loan holding company, means maintaining equity capital that the Corporation determines is commensurate with the capital maintained by an insured depository institution that is well capitalized; and (v) the term well managed has the meaning given such term in section 2(o)(9) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(9) ). ; and\n**(B)**\nin section 44, by amending subsection (e) to read as follows:\n(e) Exception for Banks in Default or in Danger of Default (1) General exception The responsible agency, may without regard to paragraph (1), (3), (4), or (5) of subsection (b) or paragraph (2), (4), or (5) of subsection (a), approve an application under subsection (a)(1) for approval of a merger transaction if\u2014 (A) the merger transaction involves 1 or more banks in default or in danger of default; or (B) the Corporation provides assistance under section 13(c) to facilitate such merger transaction. (2) Concentration limit exception The responsible agency may, without regard to subsection (b)(2), approve an application under subsection (a)(1) for approval of a merger transaction if\u2014 (A) the merger transaction involves 1 or more banks in default or in danger of default and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in subsection (b)(2); or (B) the Corporation provides assistance under section 13(c) to facilitate such merger transaction and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in subsection (b)(2). (3) Qualified bid defined In this subsection, the term qualified bid has the meaning given that term in section 18(c)(13)(C). .\n**(2) Bank Holding Company Act of 1956**\nThe Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) is amended\u2014\n**(A)**\nin section 3(d), by amending paragraph (5) to read as follows:\n(5) Exception for banks in default or in danger of default (A) General exception The Board may, without regard to subparagraph (B) or (D) of paragraph (1) or paragraph (3), approve an application pursuant to paragraph (1)(A) if\u2014 (i) the application is for an acquisition of 1 or more banks in default or in danger of default; or (ii) the application is for an acquisition with respect to which assistance is provided under section 13(c) of the Federal Deposit Insurance Act. (B) Concentration limit exception The Board may, without regard to paragraph (2), approve an application pursuant to paragraph (1)(A) if\u2014 (i) the application is for the acquisition of 1 or more banks in default or in danger of default and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in paragraph (2); or (ii) the application is for an acquisition with respect to which assistance is provided under section 13(c) of the Federal Deposit Insurance Act and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in paragraph (2). (C) Qualified bid defined In this paragraph, the term qualified bid has the meaning given that term in section 18(c)(13)(C) of the Federal Deposit Insurance Act. ; and\n**(B)**\nin section 4(i)(8), by amending subsection (B) to read as follows:\n(B) Exception Subparagraph (A) shall not apply to an acquisition if\u2014 (i) such acquisition involves an insured depository institution in default or in danger of default and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in paragraph (2); or (ii) the Federal Deposit Insurance Corporation provides assistance under section 13 of the Federal Deposit Insurance Act to facilitate such acquisition and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in paragraph (2). .\n##### (b) Concentration limit with respect to consolidated liabilities\nSection 14(c) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1852(c) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), and (3) as subparagraphs (A), (B), and (C), respectively;\n**(2)**\nby striking With the and inserting the following:\n(1) In general With the ; and\n**(3)**\nby adding at the end the following:\n(2) Limitation The Board may provide written consent for an acquisition described in paragraph (1)(A) or in paragraph (1)(B) only if the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in subsection (b). .\n#### 3. Congressional notification and justification for waivers\n##### (a) In general\nWhenever the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, or the Federal Deposit Insurance Corporation waives a concentration limit under section 18(c)(13)(B) or section 44(e) of the Federal Deposit Insurance Act or under section 3(d)(5), section 4(i)(8)(B), or section 14(c)(2) of the Bank Holding Company Act of 1956, in connection with the acquisition of a bank or insured depository institution in default or in danger of default, or in connection with an acquisition with respect to which the Federal Deposit Insurance Corporation provides assistance under section 13 of the Federal Deposit Insurance Act, the waiving agency and the Federal Deposit Insurance Corporation, jointly, shall, not later than 30 days after such waiver, submit a written report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs in the Senate containing\u2014\n**(1)**\na justification for the waiver, including an analysis of why it was necessary to prevent significant economic disruption or significant adverse effects on financial stability;\n**(2)**\na description of alternative bids or outcomes considered, including efforts to solicit and encourage bids from entities that would not require a waiver;\n**(3)**\nan explanation of why alternative bids were not selected, if applicable; and\n**(4)**\nany recommendations for legislative or regulatory changes to improve competition in future insured depository institution resolutions.\n##### (b) Public disclosure\nThe waiving agency submitting a report under subsection (a) and the Federal Deposit Insurance Corporation shall make the report publicly available on their respective websites, subject to redactions for confidential supervisory information and any other information described under section 552(b) of title 5, United States Code.\n#### 4. Limitation on considering bad faith bids in least cost determination\nSection 13(c)(4) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4) ) is amended by adding at the end the following:\n(I) Limitation on considering bad faith bids In making a determination under this paragraph of whether an exercise of authority is the least costly to the Deposit Insurance Fund, the Corporation may not consider any application, proposed application, or bid from a company, if such application, proposed application, or bid would result in violation of\u2014 (i) section 18(c)(13) or 44(b)(2); or (ii) section 3(d)(2), 4(i)(8), or 14 of the Bank Holding Company Act of 1956. .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6556rh.xml",
      "text": "IB\nUnion Calendar No. 406\n119th CONGRESS\n2d Session\nH. R. 6556\n[Report No. 119\u2013475]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Lynch introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 2, 2026 Additional sponsor: Mr. Gottheimer\nFebruary 2, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo prohibit the use of certain concentration limit exceptions with respect to mergers involving a failed bank unless the applicable agency determines such use is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Failing Bank Acquisition Fairness Act .\n#### 2. Concentration limit exceptions only available to avoid serious adverse economic or financial effects\n##### (a) Concentration limits with respect to deposits\n**(1) Federal Deposit Insurance Act**\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(A)**\nin section 18(c)(13)\u2014\n**(i)**\nby amending subparagraph (B) to read as follows:\n(B) Subparagraph (A) shall not apply to an interstate merger transaction if\u2014 (i) such interstate merger transaction involves 1 or more insured depository institutions in default or in danger of default and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from a company that is not subject to the prohibition in subparagraph (A); or (ii) the Corporation provides assistance under section 13 to facilitate such interstate merger transaction and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from a company that is not subject to the prohibition in subparagraph (A). ; and\n**(ii)**\nin subparagraph (C)\u2014\n**(I)**\nin clause (i), by striking and at the end;\n**(II)**\nin clause (ii), by striking the period at the end and inserting a semicolon; and\n**(III)**\nby adding at the end the following:\n(iii) the term qualified bid means an application, proposed application, or bid from a company where\u2014 (I) if applicable, the company, any affiliate insured depository institution, and any affiliate depository institution holding company is well capitalized and well managed, as of the date of the application, proposed application, or bid; and (II) upon consummation of the transaction, the resulting insured depository institution is well capitalized; (iv) the term well capitalized \u2014 (I) with respect to an insured depository institution, has the meaning given such term in section 38(b) ( 12 U.S.C. 1831o(b) ); (II) with respect to a bank holding company, has the meaning given such term in section 2(o)(1)(B) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(1)(B) ); (III) with respect to a savings and loan holding company, has the meaning given such term in section 238.2 of title 12, Code of Federal Regulations; and (IV) with respect to a company that is not an insured depository institution, bank holding company, or savings and loan holding company, means maintaining equity capital that the Corporation determines is commensurate with the capital maintained by an insured depository institution that is well capitalized; and (v) the term well managed has the meaning given such term in section 2(o)(9) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1841(o)(9) ). ; and\n**(B)**\nin section 44, by amending subsection (e) to read as follows:\n(e) Exception for Banks in Default or in Danger of Default (1) General exception The responsible agency may, without regard to paragraph (1), (3), (4), or (5) of subsection (b) or paragraph (2), (4), or (5) of subsection (a), approve an application under subsection (a)(1) for approval of a merger transaction if\u2014 (A) the merger transaction involves 1 or more banks in default or in danger of default; or (B) the Corporation provides assistance under section 13(c) to facilitate such merger transaction. (2) Concentration limit exception The responsible agency may, without regard to subsection (b)(2), approve an application under subsection (a)(1) for approval of a merger transaction if\u2014 (A) the merger transaction involves 1 or more banks in default or in danger of default and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in subsection (b)(2); or (B) the Corporation provides assistance under section 13(c) to facilitate such merger transaction and the responsible agency determines, based on clear and convincing evidence, that consummation of the proposed interstate merger transaction is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in subsection (b)(2). (3) Qualified bid defined In this subsection, the term qualified bid has the meaning given that term in section 18(c)(13)(C). .\n**(2) Bank Holding Company Act of 1956**\nThe Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) is amended\u2014\n**(A)**\nin section 3(d), by amending paragraph (5) to read as follows:\n(5) Exception for banks in default or in danger of default (A) General exception The Board may, without regard to subparagraph (B) or (D) of paragraph (1) or paragraph (3), approve an application pursuant to paragraph (1)(A) if\u2014 (i) the application is for an acquisition of 1 or more banks in default or in danger of default; or (ii) the application is for an acquisition with respect to which assistance is provided under section 13(c) of the Federal Deposit Insurance Act. (B) Concentration limit exception The Board may, without regard to paragraph (2), approve an application pursuant to paragraph (1)(A) if\u2014 (i) the application is for the acquisition of 1 or more banks in default or in danger of default and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in paragraph (2); or (ii) the application is for an acquisition with respect to which assistance is provided under section 13(c) of the Federal Deposit Insurance Act and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid from another institution that is not subject to the prohibition in paragraph (2). (C) Qualified bid defined In this paragraph, the term qualified bid has the meaning given that term in section 18(c)(13)(C) of the Federal Deposit Insurance Act. ; and\n**(B)**\nin section 4(i)(8), by amending subsection (B) to read as follows:\n(B) Exception Subparagraph (A) shall not apply to an acquisition if\u2014 (i) such acquisition involves an insured depository institution in default or in danger of default and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in paragraph (2); or (ii) the Federal Deposit Insurance Corporation provides assistance under section 13 of the Federal Deposit Insurance Act to facilitate such acquisition and the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in paragraph (2). .\n##### (b) Concentration limit with respect to consolidated liabilities\nSection 14(c) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1852(c) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), and (3) as subparagraphs (A), (B), and (C), respectively;\n**(2)**\nby striking With the and inserting the following:\n(1) In general With the ; and\n**(3)**\nby adding at the end the following:\n(2) Limitation The Board may provide written consent for an acquisition described in paragraph (1)(A) or in paragraph (1)(B) only if the Board determines, based on clear and convincing evidence, that consummation of the proposed acquisition is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and the Corporation has not received any qualified bid (as defined in section 18(c)(13)(C) of the Federal Deposit Insurance Act) from another institution that is not subject to the prohibition in subsection (b). .\n#### 3. Congressional notification and justification for waivers\n##### (a) In general\nWhenever the Board of Governors of the Federal Reserve System, the Comptroller of the Currency, or the Federal Deposit Insurance Corporation waives a concentration limit under section 18(c)(13)(B) or section 44(e) of the Federal Deposit Insurance Act or under section 3(d)(5), section 4(i)(8)(B), or section 14(c)(2) of the Bank Holding Company Act of 1956, in connection with the acquisition of a bank or insured depository institution in default or in danger of default, or in connection with an acquisition with respect to which the Federal Deposit Insurance Corporation provides assistance under section 13 of the Federal Deposit Insurance Act, the waiving agency and the Federal Deposit Insurance Corporation, jointly, shall, not later than 30 days after such waiver, submit a written report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs in the Senate containing\u2014\n**(1)**\na justification for the waiver, including an analysis of why it was necessary to prevent significant economic disruption or significant adverse effects on financial stability;\n**(2)**\na description of alternative bids or outcomes considered, including efforts to solicit and encourage bids from entities that would not require a waiver;\n**(3)**\nan explanation of why alternative bids were not selected, if applicable; and\n**(4)**\nany recommendations for legislative or regulatory changes to improve competition in future insured depository institution resolutions.\n##### (b) Public disclosure\nThe waiving agency submitting a report under subsection (a) and the Federal Deposit Insurance Corporation shall make the report publicly available on their respective websites, subject to redactions for confidential supervisory information and any other information described under section 552(b) of title 5, United States Code.\n#### 4. Limitation on considering bad faith bids in least cost determination\nSection 13(c)(4) of the Federal Deposit Insurance Act ( 12 U.S.C. 1823(c)(4) ) is amended by adding at the end the following:\n(I) Limitation on considering bad faith bids In making a determination under this paragraph of whether an exercise of authority is the least costly to the Deposit Insurance Fund, the Corporation may not consider any application, proposed application, or bid from a company, if such application, proposed application, or bid would result in violation of\u2014 (i) section 18(c)(13) or 44(b)(2); or (ii) section 3(d)(2), 4(i)(8), or 14 of the Bank Holding Company Act of 1956. .",
      "versionDate": "2026-02-02",
      "versionType": "Reported in House"
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-01-13T19:05:24Z"
          },
          {
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-13T19:02:31Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-13T19:02:17Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2026-01-13T19:03:14Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2026-01-13T19:02:01Z"
          },
          {
            "name": "Federal Deposit Insurance Corporation (FDIC)",
            "updateDate": "2026-01-13T19:05:03Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2026-01-13T19:03:25Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-13T19:03:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T19:31:49Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6556ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6556rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Failing Bank Acquisition Fairness Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-03T06:38:17Z"
    },
    {
      "title": "Failing Bank Acquisition Fairness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T10:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Failing Bank Acquisition Fairness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T10:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of certain concentration limit exceptions with respect to mergers involving a failed bank unless the applicable agency determines such use is necessary to prevent significant economic disruption or significant adverse effects on financial stability, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T10:03:26Z"
    }
  ]
}
```
