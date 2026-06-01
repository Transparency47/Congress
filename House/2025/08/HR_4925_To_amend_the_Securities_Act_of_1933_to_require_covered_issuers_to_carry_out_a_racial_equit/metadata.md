# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4925
- Title: Original Securities and Exchange Atonement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4925
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-09-18T19:55:12Z
- Update date including text: 2025-09-18T19:55:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4925",
    "number": "4925",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Original Securities and Exchange Atonement Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-18T19:55:12Z",
    "updateDateIncludingText": "2025-09-18T19:55:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:31:10Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4925ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4925\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Green of Texas introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Act of 1933 to require covered issuers to carry out a racial equity audit every 2 years, to require atonement for the descendants of enslaved persons, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Original Securities and Exchange Atonement Act of 2025 .\n#### 2. Racial equity audit\n##### (a) In general\nThe Securities Act of 1933 is amended by inserting after section 4A ( 15 U.S.C. 77d\u20131 ) the following:\n4B. Racial equity audit (a) In general Not later than the end of the 6-month period beginning on the date of enactment of this section, and every 2 years thereafter, each covered issuer shall\u2014 (1) conduct an independent audit to assess within each line of business\u2014 (A) the issuer\u2019s policies and practices on civil rights, equity, diversity, and inclusion; (B) how such policies and practices affect the issuer\u2019s business; and (C) whether the issuer, any predecessor institution of the issuer, or any affiliate of the issuer had direct or indirect ties to or profited from the institution of slavery; (2) issue a report to the Commission containing\u2014 (A) in the case of\u2014 (i) the initial report or any subsequent report for which the covered issuer determines material changes have occurred since the previous report, all findings and determinations made in carrying out the assessments required under paragraph (1); or (ii) a subsequent report for which the covered issuer determines no material changes have occurred since the previous report, an attestation that no material changes were found under the assessments required under paragraph (1); (B) to the extent the issuer identifies ties to or profits from the institution of slavery, a disclosure of the steps the issuer has taken to reconcile such ties or profits; and (C) to the extent the issuer identifies ties to or profits from the institution of slavery and has not taken steps to reconcile such ties or profits, a disclosure of the steps to reconcile such ties or profits the issuer plans to take, which may include\u2014 (i) startup capital and funded savings programs in low to moderate income communities for low to moderate income individuals residing in such communities; (ii) grants or contributions to historically Black colleges and universities; and (iii) grants or contributions to historically black organizations exempt from taxation as described in paragraph (3) or (4) section 501(c) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Code; and (3) make the report described under paragraph (2) available to the public, including on a website of the issuer and a website of the Commission. (b) Failure To issue report (1) Enforcement by Commission (A) Covered issuer fines Any covered issuer that fails to issue a report required under subsection (a)(2), or that reports false, misleading, or inaccurate information in such a report, shall be fined by the Commission in an amount of $20,000 per day until the report is issued, or until the report is corrected to not be false, misleading, or inaccurate, as applicable. (B) Employee fines Any employee or officer of a covered issuer who intentionally fails to issue a report required under subsection (a)(2) or that reports false, misleading, or inaccurate information in such report, shall be fined by the Commission in an amount of $2,000 per day until the report is issued, or until the report is corrected to not be false, misleading, or inaccurate, as applicable. (C) Transfer of amounts The Commission shall transfer\u2014 (i) 50 percent of the fines collected pursuant to subparagraphs (A) and (B) to the Secretary of the Treasury, and the Secretary of the Treasury shall, without further appropriation, use such funds to carry out the duties of the Office of Minority Low to Moderate Income Programs; and (ii) 50 percent of the fines collected pursuant to subparagraphs (A) and (B) to the Secretary of Housing and Urban Development, and the Secretary of Housing and Urban Development shall, without further appropriation, use such funds to carry out\u2014 (I) a program to provide housing counseling and homebuyer assistance, including downpayments, closing costs, and interest rate buydowns, to first-time, first-generation minority low to moderate income homebuyers; (II) eviction and foreclosure assistance to minority low to moderate income renters and homebuyers; (III) affordable housing production under the Housing Trust Fund established under section 1338 of the Federal Housing Enterprises Financial Safety and Soundness act of 1992 ( 12 U.S.C. 4568 ), including permanent supportive housing for people experiencing homelessness; (IV) rental assistance to eligible low income households under the Housing Choice Voucher Program under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ); and (V) formula grants to participating jurisdictions to conduct Equity Plans under the rule of the Secretary of Housing and Urban Development implementing the requirement under the Fair Housing Act ( 42 U.S.C. 3601 ) to affirmatively further fair housing. (2) Private right of action A person that holds the securities of a covered issuer and suffers harm as a result of the failure of such covered issuer to issue a report required under subsection (a)(2), may bring an action against the covered issuer in the appropriate district court of the United States. (3) Whistleblower awards (A) In general The Commission shall pay an award or awards to 1 or more individuals who voluntarily provided original information to the Commission that led to the successful enforcement of the fines required under subparagraph (A) or (B) of paragraph (1) in the case of the failure of a covered issuer to issue a report required under subsection (a)(2) or that reports false, misleading, or inaccurate information in such a report. (B) Amount The amount of an award under subparagraph (A) shall\u2014 (i) be established by the Commission by rule in an amount that the Commission determines is sufficient to create incentive for individuals to voluntarily provide original information and deter noncompliance with subsection (a); and (ii) not be less than $20,000. (C) Original information defined In this paragraph, the term original information means information that\u2014 (i) is derived from the independent knowledge or analysis of an individual who voluntarily provides the information to the Commission; (ii) is not known to the Commission from any other source, unless the whistleblower is the original source of the information; and (iii) is not exclusively derived from an allegation made in a judicial or administrative hearing, in a governmental report, hearing, audit, or investigation, or from the news media, unless the whistleblower is a source of the information. (c) Definitions In this section: (1) Area median income With respect to an individual, the term area median income means the median income for the area in which the individual lives, as determined by the Secretary of Housing and Urban Development for purposes of the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ). (2) Covered issuer The term covered issuer means an issuer that\u2014 (A) makes use of the mails or any means or instrumentality of interstate commerce; and (B) has\u2014 (i) more than 100 employees; or (ii) a capitalization of greater than or equal to $300,000,000. (3) Low to moderate income With respect to an individual, the term low to moderate income means the individual has earnings of less than 80 percent of the area median income. (4) Minority The term minority means racial and ethnic populations that are underrepresented in the general population relative to the number of persons in the total population. (5) Reconcile The term reconcile means to account for and balance in an equitable manner. .\n##### (b) Office of Minority Low to Moderate Income Programs\nChapter 3 of title 31, United States Code, is amended\u2014\n**(1)**\nin subchapter I, by adding at the end the following:\n317. Office of Minority Low to Moderate Income Programs (a) Establishment There is established, within the Department of the Treasury, an Office of Minority Low to Moderate Income Programs. (b) Duties The Office of Minority Low to Moderate Income Programs shall provide grants for\u2014 (1) startup capital and funded savings programs in low to moderate income minority communities for low to moderate income minority individuals residing in such communities; and (2) such other programs determined appropriate by the Secretary in furtherance of atonement for descendants of enslaved persons. (c) Funding (1) Authorization of appropriations There is authorized to be appropriated to the Secretary of the Treasury $3,000,000,000 to carry out this section. (2) Administrative costs The Secretary of the Treasury may use 2 percent of amounts appropriated to carry out this section for administrative expenses related to carrying out the duties of the Office of Minority Low to Moderate Income Programs. (d) Definitions In this section: (1) Area median income With respect to a community, the term area median income means the median income for the area in which the community is located, as determined by the Secretary of Housing and Urban Development for purposes of the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ). (2) Low to moderate income community The term low to moderate income community means a census tract in which 51 percent or more of the households located in the census tract earn less than 80 percent of the area median income. ; and\n**(2)**\nin the table of contents for such chapter, by inserting after the item relating to section 316 the following:\n317. Office of Minority Low to Moderate Income Programs. .",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-18T19:55:12Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4925ih.xml"
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
      "title": "Original Securities and Exchange Atonement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Original Securities and Exchange Atonement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Act of 1933 to require covered issuers to carry out a racial equity audit every 2 years, to require atonement for the descendants of enslaved persons, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T04:18:37Z"
    }
  ]
}
```
