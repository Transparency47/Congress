# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2903
- Title: Safe Step Act
- Congress: 119
- Bill type: S
- Bill number: 2903
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2903",
    "number": "2903",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Safe Step Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
            "date": "2026-03-19T14:01:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-18T21:57:11Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-18T21:57:11Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NH"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "AK"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MS"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NV"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "KS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ND"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "VA"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NC"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NH"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
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
      "sponsorshipDate": "2025-09-18",
      "state": "DE"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "CT"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "AR"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "NY"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "NC"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "NM"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-07",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "CA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "AZ"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "NE"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "IL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MN"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "ME"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "WA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "HI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "WA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "WV"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2903is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2903\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Ms. Murkowski (for herself, Ms. Hassan , Mr. Marshall , Ms. Rosen , Mr. Padilla , Mr. Hickenlooper , Mr. Merkley , Mr. Sullivan , Mr. Warnock , Mrs. Hyde-Smith , Ms. Cortez Masto , Mr. Moran , Mr. Cramer , Mr. Kaine , Mr. Budd , Mrs. Shaheen , Mr. Booker , Mr. Wyden , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to require a group health plan or health insurance coverage offered in connection with such a plan to provide an exceptions process for any medication step therapy protocol, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Step Act .\n#### 2. Required exceptions process for medication step therapy protocols\n##### (a) Required exceptions process for medication step therapy protocols\nThe Employee Retirement Income Security Act of 1974 is amended by inserting after section 713 of such Act ( 29 U.S.C. 1185b ) the following new section:\n713A. Required exceptions process for medication step therapy protocols (a) In general In the case of a group health plan or health insurance issuer offering coverage offered in connection with such a plan that provides coverage of a prescription drug pursuant to a medication step therapy protocol, the plan or issuer shall\u2014 (1) implement a clear, prompt, and transparent process for a participant or beneficiary (or the prescribing health care provider (referred to in this section as the prescriber ) on behalf of the participant or beneficiary) to request an exception to such medication step therapy protocol, pursuant to subsection (b); and (2) where the participant or beneficiary or prescriber's request for an exception to the medication step therapy protocols satisfies the criteria and requirements of subsection (b), cover the requested drug in accordance with the terms established by the plan or coverage for patient cost-sharing rates or amounts at the beginning of the plan year. (b) Circumstances for exception approval The circumstances requiring an exception to a medication step therapy protocol, pursuant to a request under subsection (a), are any of the following: (1) Any treatments otherwise required under the protocol, or treatments in the same pharmacological class or having the same mechanism of action, including treatments provided prior to the effective date of the participant's or beneficiary's coverage under the plan or coverage, have been ineffective in the treatment of the disease or condition of the participant or beneficiary, when prescribed consistent with clinical indications, clinical guidelines, or other peer-reviewed evidence, based on the prescribing health care professional\u2019s judgement or relevant information provided by the participant or beneficiary (including the medical records of the participant or beneficiary). (2) Delay of effective treatment would lead to severe or irreversible consequences, or worsen disease progression or a comorbidity and the treatment otherwise required under the protocol is reasonably expected by the prescriber to be ineffective based upon the documented physical or mental characteristics of the participant or beneficiary and the known characteristics of such treatment. (3) Any treatments otherwise required under the protocol are contraindicated for the participant or beneficiary or have caused, or are likely to cause, based on clinical, peer-reviewed evidence, an adverse reaction or other physical or mental harm to the participant or beneficiary. (4) Any treatment otherwise required under the protocol has prevented, will prevent, or is likely to prevent a participant or beneficiary from achieving or maintaining reasonable and safe functional ability in performing occupational responsibilities or activities of daily living (as defined in section 441.505 of title 42, Code of Federal Regulations (or successor regulations)). (5) The participant or beneficiary is stable for his or her disease or condition on the prescription drug or drugs selected by the prescriber and has previously received approval for coverage of the relevant drug or drugs for the disease or condition by any public or private health plan. (6) Other circumstances, as determined by the Secretary. (c) Requirement of a clear process (1) In general The process required by subsection (a) shall\u2014 (A) provide the prescriber or participant or beneficiary an opportunity to present such prescriber\u2019s clinical rationale and relevant medical information for the group health plan or health insurance issuer to evaluate such request for exception; (B) develop and use a standard form and instructions for the request of an exception under subsection (b), available in paper and electronic forms, and allow for submission of such form by paper and electronic means; (C) provide both paper and electronic means for the submission of requests for additional information; (D) clearly set forth all required information and the specific criteria that will be used to determine whether an exception is warranted, which may require disclosure of\u2014 (i) the medical history or other health records of the participant or beneficiary demonstrating that the participant or beneficiary seeking an exception\u2014 (I) has tried other drugs included in the drug therapy class without success; or (II) has taken the requested drug for a clinically appropriate amount of time to establish stability, in relation to the condition being treated and prescription guidelines given by the prescribing physician; or (ii) other clinical information that may be relevant to conducting the exception review; (E) not require the submission of any information or supporting documentation beyond what is strictly necessary (as determined by the Secretary) to determine whether a circumstance listed in subsection (b) exists; (F) clearly outline conditions under which an exception request warrants expedited resolution from the group health plan or health insurance issuer, pursuant to subsection (d)(2); and (G) allow a representative of a participant or beneficiary, which may include a designated third-party advocate, to act on behalf of the participant or beneficiary. (2) Availability of process information The group health plan or health insurance issuer shall make information regarding the process required under subsection (a) readily available in the relevant plan materials, including the summary of benefits and, if available, on the website of the group health plan or health insurance issuer. Such information shall include\u2014 (A) the requirements for requesting an exception to a medication step therapy protocol pursuant to this section; and (B) any forms, supporting information, and contact information, as appropriate. (d) Timing for determination of exception The process required under subsection (a)(1) shall provide for the disposition of requests received under such paragraph in accordance with the following: (1) Subject to paragraph (2), not later than 72 hours after receiving an initial exception request, the plan or issuer shall respond to the participant or beneficiary and, if applicable, the requesting prescriber with either a determination of exception eligibility or a request for additional required information strictly necessary to make a determination of whether the conditions specified in subsection (b) are met. The plan or issuer shall respond to the participant or beneficiary and, if applicable, the requesting prescriber, with a determination of exception eligibility no later than 72 hours after receipt of the additional required information. (2) In the case of a request under circumstances in which the applicable medication step therapy protocol may seriously jeopardize the life or health of the participant or beneficiary, may jeopardize the ability of the participant or beneficiary to regain maximum function, or may subject the participant or beneficiary to severe pain that cannot be adequately managed without the treatment that is the subject of the request, the plan or issuer shall conduct a review of the request and respond to the participant or beneficiary and, if applicable, the requesting prescriber, with either a determination of exception eligibility or a request for additional required information strictly necessary to make a determination of whether the conditions specified in subsection (b) are met, in accordance with the following: (A) If the plan or issuer can make a determination of exception eligibility without additional information, such determination shall be made on an expedited basis, and no later than 24 hours after receipt of such request. (B) If the plan or issuer requires additional information before making a determination of exception eligibility, the plan or issuer shall respond to the participant or beneficiary and, if applicable, the requesting prescriber, with a request for such information within 24 hours of the request for a determination, and shall respond with a determination of exception eligibility as quickly as the condition or disease requires, and no later than 24 hours after receipt of the additional required information. (e) Duration of a grant If an exception to a medication step therapy protocol is granted under this section to a participant or beneficiary, coverage for the requested drug shall remain in effect with respect to such participant or beneficiary for not less than one year. (f) Medication step therapy protocol In this section, the term medication step therapy protocol means a drug therapy utilization management protocol or program under which a group health plan or health insurance issuer offering group health insurance coverage of prescription drugs requires a participant or beneficiary to try an alternative preferred prescription drug or drugs before the plan or health insurance issuer approves coverage for the non-preferred drug therapy prescribed. (g) Clarification This section shall apply with respect to any group health plan or health insurance coverage offered in connection with such a plan that provides coverage of a prescription drug pursuant to a policy that meets the definition of the term medication step therapy protocol in subsection (f), regardless of whether such policy is described by such group health plan or health insurance coverage as a step therapy protocol. (h) Reporting (1) Reporting to the Secretary Not later than 3 years after the date of enactment of the Safe Step Act and not later than October 1 of each year thereafter, each group health plan and health insurance issuer offering group health insurance coverage shall report to the Secretary, in such manner as the Secretary shall require, the following: (A) The number of step therapy exception requests received for each exception circumstance described in paragraphs (1) through (6) of subsection (b), and the numbers of such requests for each such circumstance that were\u2014 (i) approved; (ii) denied, and the reasons for the denials; (iii) initially denied and appealed; and (iv) initially denied and then subsequently reversed by internal appeals or external reviews. (B) The number of times a plan or issuer requested additional information in response to a step therapy exception request, by exception circumstance described in paragraphs (1) through (6) of subsection (b). (C) The number of exception requests submitted by participants or beneficiaries, and the number of exception requests submitted by prescribers, by medical specialty. (D) The medical conditions for which participants and beneficiaries were granted exceptions due to the likelihood that switching from a prescription drug will likely cause an adverse reaction by, or physical or mental harm to, the participant or beneficiary, as described in subsection (b)(3). (E) The entities responsible for providing pharmacy benefit management services for the group health plan or health insurance coverage. (2) Information A group health plan or health insurance issuer offering group health insurance coverage shall not enter into a contract with a third-party administrator or an entity providing pharmacy benefit management services on behalf of the plan or coverage that prevents the plan or issuer from obtaining from the third-party administrator or the entity providing pharmacy benefit management services any information needed for the plan or issuer to comply with the reporting requirements under paragraph (1). (3) Reports to Congress Not later than 3 years after the date of enactment of the Safe Step Act , and not later than October 1 of each year thereafter, the Secretary shall submit to Congress, and make publicly available, a report that contains a summary and analysis of the information reported under paragraph (1), including an analysis of, with respect to requests for exceptions under this section, approvals, and denials, including the reasons for denials; appeals and external reviews; and trends, if any, in exception requests by medical specialty or medical condition. .\n##### (b) Clerical amendment\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 713 the following new item:\nSec. 713A. Required exceptions process for medication step therapy protocols. .\n##### (c) Effective date\n**(1) In general**\nThe amendment made by subsection (a) applies with respect to plan years beginning with the first plan year that begins at least 6 months after the date of the enactment of this Act.\n**(2) Regulations**\nNot later than 6 months after the date of the enactment of this Act, the Secretary of Labor shall issue final regulations, through notice and comment rulemaking, to implement the provisions of section 713A of the Employee Retirement Income Security Act of 1974, as added by subsection (a).",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-19",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5509",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safe Step Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T19:17:02Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2026-04-16T19:16:47Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-16T19:16:57Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-04-16T19:16:43Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2026-04-16T19:16:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-12-16T16:56:07Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2903is.xml"
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
      "title": "Safe Step Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Step Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Employee Retirement Income Security Act of 1974 to require a group health plan or health insurance coverage offered in connection with such a plan to provide an exceptions process for any medication step therapy protocol, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T05:48:14Z"
    }
  ]
}
```
