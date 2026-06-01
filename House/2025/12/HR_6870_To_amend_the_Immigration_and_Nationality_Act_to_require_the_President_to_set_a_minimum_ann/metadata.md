# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6870?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6870
- Title: GRACE Act
- Congress: 119
- Bill type: HR
- Bill number: 6870
- Origin chamber: House
- Introduced date: 2025-12-18
- Update date: 2026-01-28T09:05:43Z
- Update date including text: 2026-01-28T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-18: Introduced in House

## Actions

- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Introduced in House
- 2025-12-18 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6870",
    "number": "6870",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "L000397",
        "district": "18",
        "firstName": "Zoe",
        "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
        "lastName": "Lofgren",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "GRACE Act",
    "type": "HR",
    "updateDate": "2026-01-28T09:05:43Z",
    "updateDateIncludingText": "2026-01-28T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-18",
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
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-18",
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
          "date": "2025-12-18T14:07:25Z",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "AZ"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "DC"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6870ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6870\nIN THE HOUSE OF REPRESENTATIVES\nDecember 18, 2025 Ms. Lofgren (for herself, Mr. Moulton , Ms. Ansari , Ms. Tlaib , Ms. Norton , Ms. Barrag\u00e1n , Mr. Johnson of Georgia , Ms. DeGette , Mr. Lieu , Mr. Khanna , Mr. Davis of Illinois , and Ms. Clarke of New York ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to require the President to set a minimum annual goal for the number of refugees to be admitted, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guaranteed Refugee Admission Ceiling Enhancement Act or the GRACE Act .\n#### 2. Admission of refugees\nSection 207 of the Immigration and Nationality Act ( 8 U.S.C. 1157 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) In general Except as provided in subsection (b), the number of refugees who may be admitted under this section in any fiscal year shall be the sum of\u2014 (A) such number as the President determines is justified by humanitarian concerns or otherwise in the national interest, which shall be not fewer than 125,000; and (B) such number as the President determines shall be admitted to the United States through community or private sponsorship, by which community groups and private sponsors provide to a refugee and the immediate relatives or beneficiaries of the refugee initial reception and placement services similar to services provided by domestic resettlement agencies and local affiliates, in lieu of services typically provided by domestic resettlement agencies and local affiliates. (2) Absence of determination If the President does not issue a determination under paragraph (1) before the beginning of a fiscal year, the number of refugees who may be admitted in that fiscal year under this section shall be 125,000. ;\n**(B)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (7), respectively;\n**(C)**\nby inserting after paragraph (2) the following:\n(3) Numerical goals Each officer of the Federal Government responsible for refugee admissions or refugee resettlement shall treat as the numerical goals for refugee admissions under this section for the applicable fiscal year\u2014 (A) (i) a determination under paragraph (1); or (ii) in the absence of a determination under paragraph (1), the number under paragraph (2); and (B) a determination under subsection (b). ; and\n**(D)**\nby inserting after paragraph (4), as redesignated, the following:\n(5) Consideration of resettlement needs In making a determination under paragraph (1), the President shall consider the number of refugees who are in need of resettlement in a third country, as determined by the United Nations High Commissioner for Refugees in the most recently published projected global resettlement needs report. (6) Regional allocations The President shall determine regional allocations for admissions under this subsection, which shall\u2014 (A) (i) reflect the projected needs identified by the United Nations High Commissioner for Refugees in the projected global resettlement needs report for the calendar year beginning immediately after the beginning of the applicable fiscal year; or (ii) include an assessment by the Secretary of State detailing the humanitarian and national interest justifications for prioritizing refugee admissions from 1 or more regions; and (B) include an unallocated reserve that the Secretary of State, after notifying the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives , may use for 1 or more regions in which the need for additional refugee admissions arises. ; and\n**(2)**\nby adding at the end the following:\n(g) Quarterly public reports on admissions Not later than 15 days after the last day of each quarter, the President shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives, and publish on a publicly accessible website, a report that includes the following: (1) The number of refugees admitted to the United States during the preceding quarter. (2) The number of refugees admitted to the United States during the preceding quarter, expressed as a percentage of the number of refugees authorized to be admitted in accordance with the determinations under subsections (a) and (b) for the applicable fiscal year. (3) The cumulative number of refugees admitted to the United States during the applicable fiscal year, as of the last day of the preceding quarter. (4) The number of refugees to be admitted to the United States during the remainder of the applicable fiscal year so as to achieve the numerical goals set forth in the determinations under subsections (a) and (b) for such fiscal year. (5) The number of refugees from each region admitted to the United States during the preceding quarter, expressed as a percentage of the allocation for each region under subsection (a)(6) for the applicable fiscal year. (h) Quarterly reports on processing Not later than 15 days after the last day of each quarter, the President shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes the following: (1) Aliens with enhanced security checks (A) The number of aliens, by nationality, for whom an enhanced security check has been requested who were security-cleared during the preceding quarter, expressed as a percentage of all cases successfully adjudicated, approved, and security-cleared by the Director of U.S. Citizenship and Immigration Services in the applicable fiscal year. (B) The number of aliens, by nationality, for whom an enhanced security check has been requested who were admitted to the United States during the preceding quarter. (2) Circuit rides (A) For the preceding quarter\u2014 (i) the number of Refugee Corps officers deployed on circuit rides, expressed as a percentage of the overall number of Refugee Corps officers; (ii) the number of individuals interviewed\u2014 (I) on each circuit ride; and (II) at each circuit ride location; (iii) the number of circuit rides; (iv) for each circuit ride\u2014 (I) the duration of the circuit ride; (II) the average number of interviews conducted daily on the circuit ride; and (III) the percentages of interviews conducted for\u2014 (aa) individuals who require an enhanced security check; and (bb) individuals who do not require an enhanced security check; and (v) the number of interviews completed by video teleconferencing. (B) For the subsequent quarter\u2014 (i) the number of circuit rides scheduled; and (ii) the number of circuit rides planned. (3) Processing For the preceding quarter\u2014 (A) the average number of days between\u2014 (i) the date on which an individual is identified by the United States Government as a refugee; and (ii) the date on which such individual is interviewed by the Secretary of Homeland Security; (B) the average number of days between\u2014 (i) the date on which an individual identified by the United States Government as a refugee is interviewed by the Secretary of Homeland Security; and (ii) the date on which such individual is admitted to the United States; and (C) with respect to individuals identified by the United States Government as refugees who have been interviewed by the Secretary of Homeland Security, the approval, denial, and hold rates for the applications for admission of such individuals, by nationality. (4) Plan and additional information If the number of refugees admitted during the preceding quarter is less than 25 percent of the number of refugees authorized to be admitted in accordance with the determinations under subsections (a) and (b) for the applicable fiscal year, the President shall submit\u2014 (A) an assessment of country conditions and emergency humanitarian circumstances that contributed to the number of refugees admitted; (B) a plan that describes the procedural or personnel changes necessary to ensure the admission of the number of refugees authorized to be admitted to the United States in accordance with determinations under subsections (a) and (b), including a projection of the number of refugees to be admitted to the United States each month so as to achieve the numerical goals set forth in such determinations; and (C) any additional information relating to the pace of refugee admissions, as determined by the President. (5) Enhanced security check defined In this subsection, the term enhanced security check means any evaluation process to investigate national security concerns, including terrorism, espionage, sabotage, or the illegal transfer of goods, technology, or sensitive information, including\u2014 (A) any process within U.S. Citizenship and Immigration Services for handling cases with national security concerns; (B) any interagency check requested by U.S. Citizenship and Immigration Services during the adjudication process to investigate national security concerns; (C) any additional vetting or review of applicants from a country that is a state sponsor of terrorism or a country with full or partial suspension of entry into the United States under this Act; and (D) any process to screen applicant data against publicly available social media for national security purposes. (i) Rule of construction Nothing in this section may be construed\u2014 (1) to inhibit the expeditious processing of refugee and asylum applications; or (2) to restrict the authority of the Secretary of Homeland Security to admit aliens to the United States under any other Act. .",
      "versionDate": "2025-12-18",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3535",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GRACE Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2026-01-22T15:15:34Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6870ih.xml"
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
      "title": "GRACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guaranteed Refugee Admission Ceiling Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to require the President to set a minimum annual goal for the number of refugees to be admitted, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:37Z"
    }
  ]
}
```
