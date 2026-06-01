# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1873
- Title: MARSHALS Act
- Congress: 119
- Bill type: S
- Bill number: 1873
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T22:54:25Z
- Update date including text: 2025-12-05T22:54:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1873",
    "number": "1873",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "MARSHALS Act",
    "type": "S",
    "updateDate": "2025-12-05T22:54:25Z",
    "updateDateIncludingText": "2025-12-05T22:54:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
        "item": {
          "date": "2025-05-22T16:57:03Z",
          "name": "Referred To"
        }
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1873is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1873\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Booker (for himself, Mr. Schumer , Mr. Schiff , Mr. Padilla , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to transfer the United States Marshals Service to the judicial branch, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maintaining Authority and Restoring Security to Halt the Abuse of Law or the MARSHALS Act .\n#### 2. United States Marshals Service\n##### (a) Transfer\nTitle 28, United States Code, is amended\u2014\n**(1)**\nby redesignating chapter 37 as chapter 59; and\n**(2)**\nby transferring chapter 59, as so redesignated, from part II to part III so as to appear after chapter 58.\n##### (b) Court officers and employees\nChapter 59, as redesignated by subsection (a), of title 28, United States Code, is amended\u2014\n**(1)**\nin section 561\u2014\n**(A)**\nby striking subsections (a) through (d) and inserting the following:\n(a) There is hereby established a United States Marshals Service as a bureau within the judicial branch of the United States. There shall be at the head of the United States Marshals Service (hereafter in this chapter referred to as the Service ) a Director (hereafter in this chapter referred to as the Director ) who shall be appointed by the Chief Justice, in consultation with the Board established under subsection (i) (hereafter in this chapter referred to as the Board ). The Director may be removed by the Board. (b) The Chief Justice of the United States shall appoint, in consultation with the Board, a United States marshal for each judicial district of the United States and for the Superior Court of the District of Columbia, except that any marshal appointed for the Northern Mariana Islands may at the same time serve as marshal in another judicial district. Each United States marshal shall be an official of the Service and shall serve under the direction of the Director. (c) Each marshal shall be appointed for a term of four years. A marshal shall, unless that marshal has resigned or been removed by the Chief Justice of the United States, in consultation with the Board, continue to perform the duties of that office after the end of that 4-year term until a successor is appointed and qualifies. ;\n**(B)**\nby redesignating subsections (e) through (i) as subsections (d) through (h), respectively; and\n**(C)**\nby adding at the end the following:\n(i) (1) The activities of the Director shall be supervised by a Board to be composed of\u2014 (A) the Chief Justice of the United States; (B) the Judicial Conference of the United States; and (C) the Director, who shall be an ex officio, nonvoting member. (2) The Board shall establish general goals and objectives covering the major functions and operations of the Service to improve the efficiency and effectiveness of the operations of the Service. ;\n**(2)**\nin section 562, by striking subsections (a) and (b) and inserting the following:\nIn the case of a vacancy in the office of a United States marshal, the Chief Justice of the United States, shall appoint a United States marshal to serve the remainder of the 4-year term. ;\n**(3)**\nby striking section 564;\n**(4)**\nby redesignating sections 565 and 566 as sections 564 and 565, respectively;\n**(5)**\nin section 564, as so redesignated, by striking Attorney General and inserting Chief Justice of the United States, in consultation with the Board ;\n**(6)**\nin section 565, as so redesignated\u2014\n**(A)**\nby striking subsection (e) and inserting the following:\n(e) The United States Marshals Service is authorized to provide for the personal protection of Federal jurists, court officers, witnesses, and other threatened persons in the interests of justice where criminal intimidation impedes on the functioning of the judicial process or any other official proceeding. ;\n**(B)**\nin subsection (h), by striking directed by the Attorney General and inserting requested by the Attorney General, and approved by the Director ; and\n**(C)**\nin subsection (i), by striking the third sentence;\n**(7)**\nby inserting after section 565, as so redesignated, the following:\n566. Assistance in other law enforcement matters At the request of the Attorney General, and with the approval of the Director, the Service may assist the Department of Justice with the following tasks: (1) Investigating such fugitive matters, both within and outside the United States, as directed by the Attorney General. (2) Issuing administrative subpoenas in accordance with section 3486 of title 18, solely for the purpose of investigating unregistered sex offenders (as defined in section 3486). (3) Assisting State, local, and other Federal law enforcement agencies, upon the request of such an agency, in locating and recovering missing children. ; and\n**(8)**\nin section 569(b), by striking President and inserting Chief Justice, in consultation with the Board .\n##### (c) Technical and conforming amendments\n**(1)**\nThe table of chapters for part III of title 28, United States Code, is amended by adding at the end the following:\n59. United States Marshals Service 561 .\n**(2)**\nThe table of contents for chapter 59, as redesignated by subsection (a) of this section, is amended by read as follows:\nSec. 561. United States Marshals Service. 562. Vacancies. 563. Oath of office. 564. Expenses of the Service. 565. Powers and duties. 566. Assistance in other law enforcement matters. 567. Collection of fees; accounting. 568. Practice of law prohibited. 569. Reemployment rights. .\n**(3)**\nSection 3002(16) of title 28, United States Code, is amended by striking , a deputy and all that follows through the period at the end and inserting or a deputy marshal.\n**(4)**\nSection 210G(k)(3)(C) of the Homeland Security Act of 2002 ( 6 U.S.C. 124n(k)(3)(C)(ii) ) is amended\u2014\n**(A)**\nin clause (ii), by striking subclause (I) and inserting the following:\n(I) personal protection operations by the Federal Bureau of Investigation as specified in section 533 of title 28, United States Code; ;\n**(B)**\nin clause (iii)(III), by striking and at the end;\n**(C)**\nin clause (iv), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(v) missions authorized to be performed by the judicial branch, including personal protection operations by the United States Marshals Service of Federal jurists, court officers, witnesses, and other threatened persons in the interests of justice, as specified in section 565(e) of title 28, United States Code. .\n**(5)**\nSection 142(a) of the Sex Offender Registration and Notification Act ( 34 U.S.C. 20941(a) ) is amended\u2014\n**(A)**\nin the first sentence, by striking including the United States Marshals Service and inserting including at the request of the Attorney General, and with the approval of the United States Marshals Service Director, the United States Marshals Service may assist the Department of Justice ; and\n**(B)**\nby striking the second sentence.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3607",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "MARSHALS Act",
      "type": "HR"
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
        "name": "Law",
        "updateDate": "2025-06-16T13:22:27Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1873is.xml"
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
      "title": "MARSHALS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MARSHALS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maintaining Authority and Restoring Security to Halt the Abuse of Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 28, United States Code, to transfer the United States Marshals Service to the judicial branch, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:25Z"
    }
  ]
}
```
