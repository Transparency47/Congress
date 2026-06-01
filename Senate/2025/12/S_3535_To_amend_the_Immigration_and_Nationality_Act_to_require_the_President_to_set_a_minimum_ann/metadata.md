# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3535
- Title: GRACE Act
- Congress: 119
- Bill type: S
- Bill number: 3535
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-22T17:12:22Z
- Update date including text: 2026-01-22T17:12:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3535",
    "number": "3535",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "GRACE Act",
    "type": "S",
    "updateDate": "2026-01-22T17:12:22Z",
    "updateDateIncludingText": "2026-01-22T17:12:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T19:26:36Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MN"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "WA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NH"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "DE"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-17",
      "state": "VT"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NJ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3535is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3535\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Markey (for himself, Ms. Warren , Mr. Murphy , Ms. Smith , Mr. Kaine , Mr. Blumenthal , Mr. Welch , Mrs. Murray , Mrs. Shaheen , Ms. Hirono , Mr. Merkley , Mr. Coons , Mr. Durbin , Mr. Wyden , Mr. Sanders , Ms. Duckworth , Mr. Booker , Mr. Kim , and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to require the President to set a minimum annual goal for the number of refugees to be admitted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteed Refugee Admission Ceiling Enhancement Act or the GRACE Act .\n#### 2. Admission of refugees\nSection 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) In general Except as provided in subsection (b), the number of refugees who may be admitted under this section in any fiscal year shall be the sum of\u2014 (A) such number as the President determines is justified by humanitarian concerns or otherwise in the national interest, which shall be not fewer than 125,000; and (B) such number as the President determines shall be admitted to the United States through community or private sponsorship, by which community groups and private sponsors provide to a refugee and the immediate relatives or beneficiaries of the refugee initial reception and placement services similar to services provided by domestic resettlement agencies and local affiliates, in lieu of services typically provided by domestic resettlement agencies and local affiliates. (2) Absence of determination If the President does not issue a determination under paragraph (1) before the beginning of a fiscal year, the number of refugees who may be admitted in that fiscal year under this section shall be 125,000. ;\n**(B)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (7), respectively;\n**(C)**\nby inserting after paragraph (2) the following:\n(3) Numerical goals Each officer of the Federal Government responsible for refugee admissions or refugee resettlement shall treat as the numerical goals for refugee admissions under this section for the applicable fiscal year\u2014 (A) (i) a determination under paragraph (1); or (ii) in the absence of a determination under paragraph (1), the number under paragraph (2); and (B) a determination under subsection (b). ; and\n**(D)**\nby inserting after paragraph (4), as redesignated, the following:\n(5) Consideration of resettlement needs In making a determination under paragraph (1), the President shall consider the number of refugees who are in need of resettlement in a third country, as determined by the United Nations High Commissioner for Refugees in the most recently published projected global resettlement needs report. (6) Regional allocations The President shall determine regional allocations for admissions under this subsection, which shall\u2014 (A) (i) reflect the projected needs identified by the United Nations High Commissioner for Refugees in the projected global resettlement needs report for the calendar year beginning immediately after the beginning of the applicable fiscal year; or (ii) include an assessment by the Secretary of State detailing the humanitarian and national interest justifications for prioritizing refugee admissions from 1 or more regions; and (B) include an unallocated reserve that the Secretary of State, after notifying the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives , may use for 1 or more regions in which the need for additional refugee admissions arises. ; and\n**(2)**\nby adding at the end the following:\n(g) Quarterly public reports on admissions Not later than 15 days after the last day of each quarter, the President shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives , and publish on a publicly accessible website, a report that includes the following: (1) The number of refugees admitted to the United States during the preceding quarter. (2) The number of refugees admitted to the United States during the preceding quarter, expressed as a percentage of the number of refugees authorized to be admitted in accordance with the determinations under subsections (a) and (b) for the applicable fiscal year. (3) The cumulative number of refugees admitted to the United States during the applicable fiscal year, as of the last day of the preceding quarter. (4) The number of refugees to be admitted to the United States during the remainder of the applicable fiscal year so as to achieve the numerical goals set forth in the determinations under subsections (a) and (b) for such fiscal year. (5) The number of refugees from each region admitted to the United States during the preceding quarter, expressed as a percentage of the allocation for each region under subsection (a)(6) for the applicable fiscal year. (h) Quarterly reports on processing Not later than 15 days after the last day of each quarter, the President shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes the following: (1) Aliens with enhanced security checks (A) The number of aliens, by nationality, for whom an enhanced security check has been requested who were security-cleared during the preceding quarter, expressed as a percentage of all cases successfully adjudicated, approved, and security-cleared by the Director of the U.S. Citizenship and Immigration Services in the applicable fiscal year. (B) The number of aliens, by nationality, for whom an enhanced security check has been requested who were admitted to the United States during the preceding quarter. (2) Circuit rides (A) For the preceding quarter\u2014 (i) the number of Refugee Corps officers deployed on circuit rides, expressed as a percentage of the overall number of Refugee Corps officers; (ii) the number of individuals interviewed\u2014 (I) on each circuit ride; and (II) at each circuit ride location; (iii) the number of circuit rides; (iv) for each circuit ride\u2014 (I) the duration of the circuit ride; (II) the average number of interviews conducted daily on the circuit ride; and (III) the percentages of interviews conducted for\u2014 (aa) individuals who require an enhanced security check; and (bb) individuals who do not require an enhanced security check; and (v) the number of interviews completed by video teleconferencing. (B) For the subsequent quarter\u2014 (i) the number of circuit rides scheduled; and (ii) the number of circuit rides planned. (3) Processing For the preceding quarter\u2014 (A) the average number of days between\u2014 (i) the date on which an individual is identified by the United States Government as a refugee; and (ii) the date on which such individual is interviewed by the Secretary of Homeland Security; (B) the average number of days between\u2014 (i) the date on which an individual identified by the United States Government as a refugee is interviewed by the Secretary of Homeland Security; and (ii) the date on which such individual is admitted to the United States; and (C) with respect to individuals identified by the United States Government as refugees who have been interviewed by the Secretary of Homeland Security, the approval, denial, and hold rates for the applications for admission of such individuals, by nationality. (4) Plan and additional information If the number of refugees admitted during the preceding quarter is less than 25 percent of the number of refugees authorized to be admitted in accordance with the determinations under subsections (a) and (b) for the applicable fiscal year, the President shall submit\u2014 (A) an assessment of country conditions and emergency humanitarian circumstances that contributed to the number of refugees admitted; (B) a plan that describes the procedural or personnel changes necessary to ensure the admission of the number of refugees authorized to be admitted to the United States in accordance with determinations under subsections (a) and (b), including a projection of the number of refugees to be admitted to the United States each month so as to achieve the numerical goals set forth in such determinations; and (C) any additional information relating to the pace of refugee admissions, as determined by the President. (5) Enhanced security check defined In this subsection, the term enhanced security check means any evaluation process to investigate national security concerns, including terrorism, espionage, sabotage, or the illegal transfer of goods, technology, or sensitive information, including\u2014 (A) any process within U.S. Citizenship and Immigration Services for handling cases with national security concerns; (B) any interagency check requested by U.S. Citizenship and Immigration Services during the adjudication process to investigate national security concerns; (C) any additional vetting or review of applicants from a country that is a state sponsor of terrorism or a country with full or partial suspension of entry into the United States under this Act; and (D) any process to screen applicant data against publicly available social media for national security purposes. (i) Rule of construction Nothing in this section may be construed\u2014 (1) to inhibit the expeditious processing of refugee and asylum applications; or (2) to restrict the authority of the Secretary of Homeland Security to admit aliens to the United States under any other Act. .",
      "versionDate": "2025-12-17",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6870",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GRACE Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-20T15:09:41Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3535is.xml"
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
      "title": "GRACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Guaranteed Refugee Admission Ceiling Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Immigration and Nationality Act to require the President to set a minimum annual goal for the number of refugees to be admitted, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:27Z"
    }
  ]
}
```
