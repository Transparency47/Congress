# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2659?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2659
- Title: 504 Credit Risk Management Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2659
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T20:08:26Z
- Update date including text: 2025-09-18T20:08:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-09-17 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-09-17 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2659",
    "number": "2659",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "504 Credit Risk Management Improvement Act of 2025",
    "type": "S",
    "updateDate": "2025-09-18T20:08:26Z",
    "updateDateIncludingText": "2025-09-18T20:08:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
            "date": "2025-09-17T18:30:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-08-01T20:40:18Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2659is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2659\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Young (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Investment Act of 1958 to enhance the Office of Credit Risk Management, to require the Administrator of the Small Business Administration to issue rules relating to environmental obligations of certified development companies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 504 Credit Risk Management Improvement Act of 2025 .\n#### 2. Enhancements to the Office of Credit Risk Management\nTitle V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ) is amended by adding at the end the following:\n511. Office of Credit Risk Management oversight (a) Definitions In this section\u2014 (1) the term Director means the Director of the Office; and (2) the term Office means the Office of Credit Risk Management established under section 47 of the Small Business Act ( 15 U.S.C. 657t ). (b) Duties relating to 504 program The Office\u2014 (1) shall be responsible for\u2014 (A) supervising any certified development company, as provided in subsection (d); and (B) conducting file reviews with respect to loan closings under the program established under this title, as provided in subsection (c); and (2) may\u2014 (A) take formal and informal enforcement actions against a certified development company, as provided in subsection (e); and (B) charge a certified development company a fee, as provided in subsection (g). (c) Loan closing file reviews With respect to a loan closing under the program established under this title, the Office shall be responsible for the following: (1) Conducting a complete file review of a random selection of all loan closings, the number, frequency, and conduct of which shall be at the discretion of the Office, to ensure program integrity, including a review of the items listed on the Checklist for Complete File Review contained in the appropriate form of the Administration. (2) Not later than 60 days after the date on which each complete file review conducted under paragraph (1) is completed, preparing a written report documenting the results of that review, which the Office shall send to\u2014 (A) the applicable certified development company; (B) the designated attorney that closed the loan for the certified development company; and (C) the Commercial Loan Service Center. (3) If a complete file review conducted under paragraph (1) reveals a deficiency that could result in a loss to the Administration, requiring the applicable certified development company or the designated attorney to promptly correct the deficiency. (d) Supervision of certified development companies With respect to the supervision of certified development companies\u2014 (1) an employee of the Office shall\u2014 (A) be present for, and supervise, the review of any such company that is conducted by a contractor of the Office on the premises of the company; and (B) supervise the review of any such company that is conducted by a contractor of the Office that is not conducted on the premises of the company; and (2) the Administrator shall\u2014 (A) develop a timeline for the review by the Office of certified development companies and the submission of reports regarding those reviews, under which the Administrator shall\u2014 (i) submit to a certified development company a written report of any review of the company not later than 90 days after the date on which the review is concluded; or (ii) if the Administrator expects to submit the report after the end of the 90-day period described in clause (i)\u2014 (I) notify the company of the expected date of submission of the report and the reason for the delay; and (II) submit to the company the report; and (B) if a response by a certified development company is requested in a report submitted under subparagraph (A), require the company to submit responses to the Administrator not later than 45 business days after the date on which the company receives the report. (e) Enforcement authority against certified development companies (1) Informal enforcement authority The Director may take an informal enforcement action against a certified development company if the Director finds that the company has violated a statutory or regulatory requirement or any requirement in a Standard Operating Procedures Manual or Policy Notice relating to a program or function of the Office of Capital Access. (2) Formal enforcement authority (A) In general With the approval of the Lender Oversight Committee established under section 48 of the Small Business Act ( 15 U.S.C. 657u ), the Director may take a formal enforcement action against any certified development company if the Director finds that the company has violated\u2014 (i) a statutory or regulatory requirement, including a requirement relating to the necessary funds for making loans when those funds are not made available to the company from private sources on reasonable terms; or (ii) any requirement described in a Standard Operating Procedures Manual or Policy Notice relating to a program or function of the Office of Capital Access. (B) Enforcement actions The decision to take an enforcement action against a certified development company under subparagraph (A) shall be based on the severity or frequency of the violation and may include assessing a civil monetary penalty against the company in an amount that is not greater than $250,000. (3) Failure to submit annual report With respect to a certified development company that, as of the date that is 60 days after the date on which the company is required to submit any report, fails to submit that report, the Director may\u2014 (A) suspend the company from participating in the program established under this title for a period that is not longer than 30 days; or (B) impose a penalty on the company in an amount to be determined by the Director, except that the amount of the penalty shall be not more than $10,000. (f) Portfolio risk analysis of 504 loans (1) In general The Director shall annually conduct a risk analysis of the portfolio of the Administration with respect to all loans guaranteed under section 504. (2) Report to Congress On December 1, 2025, and every December 1 thereafter, the Director shall submit to Congress a report containing the results of each portfolio risk analysis conducted under paragraph (1) during the fiscal year preceding the submission of the report, which shall include\u2014 (A) an analysis of the overall program risk of projects and loans approved under section 504; (B) an analysis of the program risk, set forth separately by industry concentration; (C) without identifying individual certified development companies by name, a consolidated analysis of the risk created by the individual companies responsible for not less than 1 percent of the gross project approvals set forth separately for the year covered by the report by\u2014 (i) the dollar value of the loans made by such companies; and (ii) the number of loans made by such companies; (D) steps taken by the Administrator to mitigate the risks identified in subparagraphs (A), (B), and (C); (E) the number of certified development companies, the number of projects undertaken, the number of unique third party lenders participating in the program, and the gross and net dollar amount of debentures guaranteed and approved projects; (F) the number and dollar amount of total losses, the number and dollar amount of total purchases, and the percentage and dollar amount of recoveries at the Administration; (G) the number and type of enforcement actions recommended by the Director; (H) the number and type of enforcement actions approved by the Lender Oversight Committee established under section 48 of the Small Business Act ( 15 U.S.C. 657u ); (I) the number and type of enforcement actions disapproved by the Lender Oversight Committee; and (J) the number and dollar amount of civil monetary penalties assessed. (g) Fee authority regarding certified development companies (1) In general On and after the date that is 1 year after the date of enactment of the 504 Credit Risk Management Improvement Act of 2025 , the Office may collect from each certified development company a fee as necessary to reduce to zero the cost to the Administration of examinations, reviews, rulemakings, and other lender oversight activities in this Act, the amount of which\u2014 (A) shall be determined on a graduated scale according to the size of the portfolio of the certified development company with respect to the program carried out under this title; and (B) shall not exceed the amount that is 1 basis point with respect to the value of the portfolio described in subparagraph (A). (2) Payment A certified development company on which a fee is imposed under paragraph (1) shall pay the fee from the servicing fees collected by the development company pursuant to regulation. .\n#### 3. Rules relating to obligations of certified development companies under the National Environmental Policy Act\n##### (a) Eligible certified development company defined\nIn this section, the term eligible certified development company means a certified development company, within the meaning under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ), that receives assistance pursuant to that title.\n##### (b) Requirement To issue rules\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Small Business Administration shall issue rules to clarify the procedures necessary for an eligible certified development company to comply with the applicable requirements under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n##### (c) Rule of construction\nNothing in this section shall be construed to modify the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).",
      "versionDate": "2025-08-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-09-18T20:08:26Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2659is.xml"
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
      "title": "504 Credit Risk Management Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "504 Credit Risk Management Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Investment Act of 1958 to enhance the Office of Credit Risk Management, to require the Administrator of the Small Business Administration to issue rules relating to environmental obligations of certified development companies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:24Z"
    }
  ]
}
```
